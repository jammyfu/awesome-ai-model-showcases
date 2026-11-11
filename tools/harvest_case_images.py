#!/usr/bin/env python3
"""Fetch one representative image per main-catalog case.

Writes data/case-images.json. Does not invent URLs. A direct image or GIF on
the case, an X post thumbnail, or a per-run still named on the source page is
kept. Shared site logos are not reused across unrelated cases.
"""
from __future__ import annotations

import json
import re
import ssl
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/data/community-cases.json"
X_SRC = ROOT / "playbooks/research/x-inventory.json"
GAME_SRC = ROOT / "playbooks/research/game-sequences.json"
MANIFEST = ROOT / "docs/data/local-media-manifest.json"
OUT = ROOT / "data/case-images.json"
THUMBS = ROOT / "assets/thumbs"
MAX_BYTES = 300 * 1024
UA = "awesome-ai-model-showcases thumbnail harvest (attribution archive)"
MAIN_KEYS = (
    "collected_x_author_claim",
    "collected_web_gif",
    "collected_already_in_repo",
    "collected_game_author_claim",
    "collected_claude",
    "collected_gemini",
    "collected_gpt_code",
    "collected_grok",
    "collected_qwen",
    "collected_deepseek",
)
FORBID = (
    "禁止转载",
    "不得转载",
    "严禁转载",
    "未经许可不得转载",
    "未经授权不得转载",
    "do not republish",
    "do not re-publish",
    "no republication",
    "not for republication",
    "not for redistribution",
)
IMAGE_EXT = (".gif", ".jpg", ".jpeg", ".png", ".webp")
CTX = ssl.create_default_context()


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: list[tuple[str, str]] = []
        self.images: list[str] = []
        self.posters: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {k.lower(): (v or "") for k, v in attrs}
        if tag == "meta":
            key = (data.get("property") or data.get("name") or "").lower()
            if key in {"og:image", "twitter:image", "og:image:url"}:
                self.meta.append((key, data.get("content") or ""))
        elif tag == "img" and data.get("src"):
            self.images.append(data["src"])
        elif tag == "video" and data.get("poster"):
            self.posters.append(data["poster"])


def fetch(url: str, timeout: int = 25) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
        body = resp.read(20_000_000)
        ctype = resp.headers.get("Content-Type") or ""
        return body, ctype


def looks_image_url(url: str) -> bool:
    path = url.split("?", 1)[0].lower()
    if path.endswith(IMAGE_EXT):
        return True
    return "/media/" in path and "pbs.twimg.com" in path and not path.endswith(".mp4")


def abs_url(base: str, ref: str) -> str:
    ref = (ref or "").strip()
    if not ref or ref.startswith("data:"):
        return ""
    return urllib.request.urljoin(base, ref)


def x_status_id(url: str) -> str:
    match = re.search(r"https?://(?:www\.)?x\.com/(?:[^/]+/status|i/article)/(\d+)", url or "")
    return match.group(1) if match else ""


def forbid_text(text: str) -> str:
    low = text.lower()
    for phrase in FORBID:
        if phrase.lower() in low:
            return phrase
    return ""


def preview_map() -> dict[str, str]:
    found: dict[str, str] = {}
    if X_SRC.is_file():
        data = json.loads(X_SRC.read_text(encoding="utf-8"))
        groups = []
        for key in ("author_claim_media_meta_checked", "pending_verification"):
            groups.extend(data.get(key) or [])
        for item in groups:
            for media in item.get("media") or []:
                url = media.get("preview_image_url") or ""
                if url and item.get("id") not in found:
                    found[item["id"]] = url
    if GAME_SRC.is_file():
        data = json.loads(GAME_SRC.read_text(encoding="utf-8"))
        rows = data.get("cases") or data.get("sequences") or []
        if isinstance(data, dict) and not rows:
            rows = [v for v in data.values() if isinstance(v, dict) and v.get("id")]
        stack = [data]
        while stack:
            cur = stack.pop()
            if isinstance(cur, dict):
                cid = cur.get("id")
                for media in cur.get("media") or []:
                    if isinstance(media, dict) and media.get("preview_image_url") and cid and cid not in found:
                        found[cid] = media["preview_image_url"]
                stack.extend(cur.values())
            elif isinstance(cur, list):
                stack.extend(cur)
    if MANIFEST.is_file():
        man = json.loads(MANIFEST.read_text(encoding="utf-8"))
        for item in man.get("files") or []:
            if item.get("role") in {"poster", "still", "gif"} and item.get("source_url") and item.get("case_id"):
                found.setdefault(item["case_id"], item["source_url"])
    return found


def date_map() -> dict[str, tuple[str, str]]:
    found: dict[str, tuple[str, str]] = {}
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    for key in MAIN_KEYS:
        for row in catalog.get(key) or []:
            if re.fullmatch(r"\d{4}-\d{2}(-\d{2})?", str(row.get("date") or "")):
                found[row["id"]] = (row["date"], "catalog date field")
    if X_SRC.is_file():
        data = json.loads(X_SRC.read_text(encoding="utf-8"))
        for item in data.get("author_claim_media_meta_checked") or []:
            raw = str(item.get("created_at_beijing") or "")
            if len(raw) >= 10 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw[:10]):
                found[item["id"]] = (raw[:10], "x-inventory created_at_beijing")
    return found


def parse_html(url: str, body: bytes) -> tuple[MetaParser, str]:
    text = body.decode("utf-8", "replace")
    parser = MetaParser()
    try:
        parser.feed(text)
    except Exception:
        pass
    return parser, text


def jamesgreene_stills(page_html: str) -> dict[str, str]:
    stills = {}
    for src in re.findall(r'src="(/media/models/runs/code-1/[^"]+\.webp)"', page_html):
        slug = src.rsplit("/", 1)[-1].removesuffix(".webp")
        stills[slug] = "https://jamesgreene.com" + src
    return stills


def fxtwitter(status_id: str) -> tuple[str, str]:
    url = f"https://api.fxtwitter.com/status/{status_id}"
    body, _ctype = fetch(url)
    data = json.loads(body.decode("utf-8"))
    tweet = data.get("tweet") or {}
    media = (tweet.get("media") or {}).get("all") or []
    image = ""
    for item in media:
        kind = (item.get("type") or "").lower()
        if kind == "photo" and item.get("url"):
            image = item["url"]
            break
        if item.get("thumbnail_url"):
            image = item["thumbnail_url"]
            break
    created = str(tweet.get("created_at") or "")
    return image, created


def utc_day(created_at: str) -> str:
    # Example: Thu Nov 05 10:06:27 +0000 2026
    match = re.search(r"(\d{4})$", (created_at or "").strip())
    months = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
        "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
    }
    parts = (created_at or "").split()
    if len(parts) >= 6 and parts[1] in months and parts[2].isdigit() and match:
        return f"{parts[5]}-{months[parts[1]]}-{int(parts[2]):02d}"
    return ""


def snowflake_day(status_id: str) -> str:
    ms = (int(status_id) >> 22) + 1288834974657
    from datetime import datetime, timezone
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).date().isoformat()


_COMMIT_DAY: dict[str, str] = {}


def github_committer_day(api_url: str) -> str:
    if api_url in _COMMIT_DAY:
        return _COMMIT_DAY[api_url]
    day = ""
    try:
        body, _ctype = fetch(api_url)
        data = json.loads(body.decode("utf-8"))
        if isinstance(data, list):
            data = data[0] if data else {}
        day = str(((data.get("commit") or {}).get("committer") or {}).get("date") or "")[:10]
    except Exception:
        day = ""
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
        _COMMIT_DAY[api_url] = day
        return day
    return ""


def published_day(page_text: str) -> str:
    match = re.search(r'datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', page_text or "")
    return match.group(1) if match else ""


def archived_bytes(case_id: str, image_url: str) -> bytes | None:
    if not MANIFEST.is_file() or not image_url:
        return None
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for item in man.get("files") or []:
        if item.get("case_id") == case_id and item.get("source_url") == image_url and item.get("local_path"):
            path = ROOT / item["local_path"]
            if path.is_file() and item.get("ext") in {"gif", "jpg", "jpeg", "png", "webp"}:
                return path.read_bytes()
    return None


def atelier_sol_gif(page_text: str) -> str:
    if "github.com/marmikshah/atelier" not in (page_text or ""):
        return ""
    api = "https://api.github.com/repos/marmikshah/atelier/contents/showcase/gifs/gpt-6.1-sol-max?ref=master"
    body, _ctype = fetch(api)
    rows = json.loads(body.decode("utf-8"))
    gifs = [row.get("download_url") or "" for row in rows if str(row.get("name") or "").endswith(".gif")]
    gifs = sorted(url for url in gifs if url)
    return gifs[0] if gifs else ""


def save_thumb(case_id: str, raw: bytes, ctype: str) -> tuple[str, int]:
    if raw[:64].lstrip().lower().startswith(b"<!doctype") or raw[:32].lstrip().lower().startswith(b"<html"):
        raise ValueError("payload is HTML")
    low = ctype.lower()
    if "text/html" in low or "json" in low:
        raise ValueError(f"not an image: {ctype}")
    THUMBS.mkdir(parents=True, exist_ok=True)
    try:
        img = Image.open(BytesIO(raw))
        img.load()
    except Exception as exc:
        raise ValueError(f"unreadable image: {exc}") from exc
    fmt = (img.format or "").upper()
    ext = { "GIF": "gif", "JPEG": "jpg", "PNG": "png", "WEBP": "webp" }.get(fmt)
    if ext is None:
        raise ValueError(f"unsupported format {img.format}")
    dest = THUMBS / f"{case_id}.{ext}"
    if fmt == "GIF" and len(raw) <= MAX_BYTES and getattr(img, "n_frames", 1) > 1:
        dest.write_bytes(raw)
        return dest.relative_to(ROOT).as_posix(), dest.stat().st_size
    frame = img.copy()
    if fmt == "GIF":
        frame.seek(0)
    if frame.mode not in {"RGB", "L"}:
        frame = frame.convert("RGB")
    else:
        frame = frame.convert("RGB")
    width = 640
    if frame.width > width:
        height = max(1, round(frame.height * width / frame.width))
        frame = frame.resize((width, height), Image.Resampling.LANCZOS)
    dest = THUMBS / f"{case_id}.jpg"
    quality = 85
    blob = b""
    while quality >= 40:
        buf = BytesIO()
        frame.save(buf, format="JPEG", quality=quality, optimize=True)
        blob = buf.getvalue()
        if len(blob) <= MAX_BYTES:
            break
        quality -= 10
        if frame.width > 320:
            frame = frame.resize((frame.width * 3 // 4, frame.height * 3 // 4), Image.Resampling.LANCZOS)
    if len(blob) > MAX_BYTES:
        raise ValueError(f"still {len(blob)} bytes after compress")
    dest.write_bytes(blob)
    return dest.relative_to(ROOT).as_posix(), len(blob)


def harvest_one(row: dict, previews: dict[str, str], dates: dict[str, tuple[str, str]], stills: dict[str, str]) -> dict:
    cid = row["id"]
    source = row.get("source_url") or ""
    media = row.get("media_url") or ""
    credit = row.get("author") or ""
    note: list[str] = []
    image = ""
    page_text = ""
    basis = ""
    if looks_image_url(media) and not media.endswith(".html"):
        image = media
        basis = "case media_url"
    status_id = x_status_id(source) or x_status_id(media)
    if not image and status_id:
        try:
            found, _created = fxtwitter(status_id)
            if found:
                image = found
                basis = "fxtwitter status media"
            else:
                note.append("fxtwitter returned no image")
        except Exception as exc:
            note.append(f"fxtwitter failed: {exc.__class__.__name__}")
    if not image and media.endswith(".html"):
        slug = media.rsplit("/", 1)[-1].removesuffix(".html")
        if slug in stills:
            image = stills[slug]
            basis = "jamesgreene.com/models per-run still"
    if not image and source and not status_id:
        try:
            body, ctype = fetch(source)
            parser, page_text = parse_html(source, body)
            if "html" in ctype or page_text.lstrip().startswith("<"):
                for _key, content in parser.meta:
                    image = abs_url(source, content)
                    if image:
                        basis = "og:image or twitter:image"
                        break
                if not image:
                    for src in parser.posters + parser.images:
                        candidate = abs_url(source, src)
                        if looks_image_url(candidate):
                            image = candidate
                            basis = "source page image"
                            break
        except Exception as exc:
            note.append(f"source page failed: {exc.__class__.__name__}")
    elif source and not status_id and not page_text:
        try:
            body, _ctype = fetch(source)
            _parser, page_text = parse_html(source, body)
        except Exception as exc:
            note.append(f"source page failed: {exc.__class__.__name__}")
    if not image and cid == "web-atelier-gpt61-sol-ten-frame-loops":
        try:
            found = atelier_sol_gif(page_text)
            if found:
                image = found
                basis = "first GIF in gpt-6.1-sol-max, linked from the Atelier page"
        except Exception as exc:
            note.append(f"atelier showcase failed: {exc.__class__.__name__}")
    if not image and previews.get(cid):
        image = previews[cid]
        basis = "inventory preview or archived poster URL"
        note.append("live page had no still; used a URL already stored from the post")
    banned = forbid_text(page_text) if page_text else ""
    date, date_basis = dates.get(cid, ("", ""))
    if not date and status_id:
        try:
            _image, created = fxtwitter(status_id)
            date = utc_day(created) or snowflake_day(status_id)
            date_basis = "fxtwitter created_at" if utc_day(created) else "status id snowflake UTC day"
        except Exception:
            try:
                date = snowflake_day(status_id)
                date_basis = "status id snowflake UTC day"
            except Exception:
                pass
    if not date:
        published = published_day(page_text)
        if published:
            date, date_basis = published, "source page datePublished"
    if not date and "a20f88b18a9abe8cd1531fb8a8e738a5a4701ce2" in source:
        day = github_committer_day(
            "https://api.github.com/repos/ailingqu/awesome-ai-gif-prompts/commits/a20f88b18a9abe8cd1531fb8a8e738a5a4701ce2"
        )
        if day:
            date, date_basis = day, "cited GitHub commit committer date"
    if not date and "github.com/vargHQ/skills" in source:
        day = github_committer_day(
            "https://api.github.com/repos/vargHQ/skills/commits?path=gpt-image-sprite-sheet/SKILL.md&per_page=1"
        )
        if day:
            date, date_basis = day, "GitHub file committer date"
    record = {
        "id": cid,
        "image_url": image,
        "image_source": source,
        "image_credit": credit,
        "image_basis": basis,
        "date": date,
        "date_basis": date_basis,
        "download": "missing",
        "thumb": "",
        "bytes": 0,
        "forbid_phrase": banned,
        "note": "; ".join(note),
    }
    if not image:
        return record
    if banned:
        record["download"] = "forbidden"
        record["note"] = (record["note"] + "; " if record["note"] else "") + f"explicit no-reprint phrase: {banned}"
        return record
    try:
        try:
            raw, ctype = fetch(image)
        except urllib.error.HTTPError as exc:
            cached = archived_bytes(cid, image) if exc.code == 404 else None
            if cached is None:
                raise
            raw, ctype = cached, "application/octet-stream"
            note.append("live image URL returned 404; thumbnail uses the archived file of that same URL")
            record["note"] = "; ".join(note)
        rel, size = save_thumb(cid, raw, ctype)
    except Exception as exc:
        record["download"] = "failed"
        record["note"] = (record["note"] + "; " if record["note"] else "") + f"download failed: {exc}"
        return record
    record["download"] = "saved"
    record["thumb"] = rel
    record["bytes"] = size
    return record


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    rows = [row for key in MAIN_KEYS for row in catalog.get(key) or []]
    previews = preview_map()
    dates = date_map()
    stills: dict[str, str] = {}
    try:
        body, _ctype = fetch("https://jamesgreene.com/models/")
        stills = jamesgreene_stills(body.decode("utf-8", "replace"))
        print(f"jamesgreene stills: {len(stills)}", flush=True)
    except Exception as exc:
        print(f"jamesgreene page failed: {exc}", flush=True)
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(harvest_one, row, previews, dates, stills) for row in rows]
        for fut in as_completed(futures):
            rec = fut.result()
            results.append(rec)
            print(f"{rec['download']:9} {rec['id']} {rec['image_basis']}", flush=True)
    order = {row["id"]: i for i, row in enumerate(rows)}
    results.sort(key=lambda rec: order[rec["id"]])
    payload = {
        "meta": {
            "harvested": "2026-11-11",
            "tool": "tools/harvest_case_images.py",
            "rule": "Representative still from the case media URL, the source post, or a per-run image named on the source page. No invented URLs.",
        },
        "cases": results,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts: dict[str, int] = {}
    for rec in results:
        counts[rec["download"]] = counts.get(rec["download"], 0) + 1
    print("counts", counts, "of", len(results), flush=True)


if __name__ == "__main__":
    main()
