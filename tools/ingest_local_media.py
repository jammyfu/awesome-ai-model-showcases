#!/usr/bin/env python3
"""Download original case media and archive prompts/posts locally.

User asked to store third-party media in-repo with attribution.
License remains unknown; MIT still covers source code only.
"""
from __future__ import annotations

import hashlib
import json
import mimetypes
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parents[1]
X_SRC = ROOT / "playbooks/research/x-inventory.json"
WEB_SRC = ROOT / "playbooks/research/web-inventory.json"
GAME_SRC = ROOT / "playbooks/research/game-sequences.json"
IDEAS = ROOT / "docs/data/ideas.json"
CASES = ROOT / "docs/cases"
MANIFEST = ROOT / "docs/data/local-media-manifest.json"
MISSING = ROOT / "playbooks/local-media-missing.md"
POSTS = ROOT / "playbooks/research/source-posts.json"
EXTRAS = ROOT / "playbooks/research/live-media-extras.json"
DOWNLOADED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%d")
PREV = {}
if MANIFEST.exists():
    try:
        PREV = {
            f.get("source_url"): f
            for f in json.loads(MANIFEST.read_text(encoding="utf-8")).get("files") or []
            if f.get("ok") and f.get("sha256") and f.get("local_path")
        }
    except Exception:
        PREV = {}

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

REJECT_CONTENT_TYPES = (
    "text/html",
    "text/plain",
    "application/json",
    "application/xml",
    "text/xml",
    "application/javascript",
    "text/javascript",
)


def reject_download_payload(content_type: str, data: bytes) -> str:
    """Return an error if the HTTP payload is not media. Empty string if acceptable."""
    ct = (content_type or "").split(";")[0].strip().lower()
    if any(ct == bad or ct.startswith(bad + "+") for bad in REJECT_CONTENT_TYPES):
        return f"rejected content-type {ct or '(empty)'}"
    head = (data or b"")[:1024].lstrip().lower()
    if (
        head.startswith(b"<!doctype")
        or head.startswith(b"<html")
        or head.startswith(b"<head")
        or (head.startswith(b"<") and b"<html" in head)
    ):
        return "rejected HTML body (not media)"
    if ct in {"application/json", "text/json"} or (head.startswith(b"{") and b'"' in head[:80]):
        if not ct.startswith("image/") and "mp4" not in ct and "video/" not in ct:
            return "rejected JSON/text body (not media)"
    return ""


def ext_for(url: str, content_type: str) -> str:
    ct = (content_type or "").split(";")[0].strip().lower()
    mapping = {
        "video/mp4": ".mp4",
        "image/gif": ".gif",
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
    }
    if ct in mapping:
        return mapping[ct]
    path = url.split("?")[0]
    suf = Path(path).suffix.lower()
    if suf in {".mp4", ".gif", ".jpg", ".jpeg", ".png", ".webp"}:
        return ".jpg" if suf == ".jpeg" else suf
    return mimetypes.guess_extension(ct) or ".bin"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str, referer: str) -> tuple[int, str, bytes, str]:
    headers = {"User-Agent": UA, "Accept": "*/*"}
    if referer:
        headers["Referer"] = referer
    if "pbs.twimg.com/media/" in url and "name=" not in url:
        url = url + ("&" if "?" in url else "?") + "name=orig"
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
            ct = resp.headers.get("Content-Type", "")
            return resp.status, ct, data, url
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type", "") if e.headers else "", e.read() if e.fp else b"", url
    except Exception as e:
        return 0, "", str(e).encode(), url


def download_one(item: dict) -> dict:
    url = item["url"]
    dest_dir = Path(item["dest_dir"])
    dest_dir.mkdir(parents=True, exist_ok=True)
    rec = {
        "case_id": item["case_id"],
        "role": item["role"],
        "source_url": url,
        "author": item.get("author") or "",
        "post_url": item.get("post_url") or "",
        "downloaded_at": DOWNLOADED_AT,
        "http_status": 0,
        "content_type": "",
        "bytes": 0,
        "sha256": "",
        "local_path": "",
        "ext": "",
        "ok": False,
        "error": "",
        "skipped_unchanged": False,
    }
    prev = PREV.get(url)
    if prev:
        old = ROOT / prev["local_path"]
        if old.is_file() and sha256(old.read_bytes()) == prev["sha256"]:
            dest = dest_dir / Path(prev["local_path"]).name
            if dest.resolve() != old.resolve():
                dest.write_bytes(old.read_bytes())
            rec.update(
                {
                    "ok": True,
                    "skipped_unchanged": True,
                    "http_status": 200,
                    "content_type": prev.get("content_type") or "",
                    "bytes": prev.get("bytes") or dest.stat().st_size,
                    "sha256": prev["sha256"],
                    "local_path": str(dest.relative_to(ROOT)).replace("\\", "/"),
                    "ext": prev.get("ext") or dest.suffix.lstrip("."),
                    "downloaded_at": prev.get("downloaded_at") or DOWNLOADED_AT,
                }
            )
            return rec
    status, ct, data, final = 0, "", b"", url
    last_err = ""
    for attempt in range(3):
        status, ct, data, final = fetch(url, item.get("referer") or "")
        if status == 200 and data and len(data) > 32:
            break
        last_err = data.decode("utf-8", "replace")[:180] if status != 200 else f"short body {len(data)}"
        time.sleep(1.2 * (attempt + 1))
    rec["http_status"] = status
    rec["content_type"] = ct
    rec["bytes"] = len(data) if status == 200 else 0
    if status != 200 or not data or len(data) < 32:
        rec["error"] = f"HTTP {status}: {last_err or 'empty'}"
        return rec
    reject = reject_download_payload(ct, data)
    if reject:
        rec["error"] = reject
        rec["ok"] = False
        return rec
    ext = ext_for(final, ct)
    # Never rename MP4 to GIF.
    if "mp4" in (ct or "") or final.endswith(".mp4"):
        ext = ".mp4"
    name = item["filename"] + ext
    path = dest_dir / name
    path.write_bytes(data)
    rec.update(
        {
            "ok": True,
            "sha256": sha256(data),
            "local_path": str(path.relative_to(ROOT)).replace("\\", "/"),
            "ext": ext.lstrip("."),
            "bytes": len(data),
            "content_type": ct,
        }
    )
    return rec


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def case_docs(case_id: str, meta: dict, files: list[dict]) -> None:
    d = CASES / case_id
    d.mkdir(parents=True, exist_ok=True)
    prompt = (meta.get("original_prompt") or "").strip()
    write_text(
        d / "prompt.md",
        "# Original prompt\n\n"
        + (prompt if prompt else "（原文未公开 / original prompt not published）\n"),
    )
    post_bits = [
        f"# {case_id}",
        "",
        f"- Author: {meta.get('author')}",
        f"- Source: {meta.get('source_url')}",
        f"- Model: {meta.get('model_claim')}",
        f"- Pipeline: {meta.get('pipeline')}",
        f"- Verification: {meta.get('verify')}",
        f"- Workflow: {meta.get('workflow') or ''}",
        "",
        "## Play / 玩法",
        "",
        meta.get("play") or meta.get("title") or "",
        "",
        "## Original post text",
        "",
        (meta.get("post_text") or "（清单未收录原帖全文 / original post text not in inventory）"),
        "",
        "## Notes / process",
        "",
        meta.get("notes") or "",
    ]
    write_text(d / "post.md", "\n".join(post_bits) + "\n")
    media_md = []
    for f in files:
        if not f.get("ok"):
            media_md.append(f"- MISSING `{f['role']}` {f['source_url']} — {f.get('error')}")
            continue
        rel = Path(f["local_path"]).name
        if f["ext"] in {"gif", "jpg", "jpeg", "png", "webp"}:
            media_md.append(f"![{rel}](media/{rel})")
        elif f["ext"] == "mp4":
            media_md.append(
                f'<video src="media/{rel}" controls muted loop playsinline preload="metadata" style="max-width:100%"></video>\n\n[local {rel}](media/{rel})'
            )
        else:
            media_md.append(f"- [{rel}](media/{rel})")
    write_text(
        d / "README.md",
        "\n".join(
            [
                f"# {meta.get('title') or case_id}",
                "",
                f"Author: **{meta.get('author')}** · Source: {meta.get('source_url')}",
                "",
                f"Model evidence: {meta.get('model_claim')}",
                "",
                f"Pipeline: {meta.get('pipeline')} · Verification: {meta.get('verify')}",
                "",
                "License: **unknown**. Archived locally at the user's request. MIT covers repo source code only. This is not an author grant or CC0.",
                "",
                "## Media",
                "",
                *media_md,
                "",
                "## Prompt",
                "",
                "See [prompt.md](prompt.md) for the full original text (empty if unpublished).",
                "",
                "## Post / process",
                "",
                "See [post.md](post.md).",
                "",
            ]
        ),
    )
    # Pages-readable detail
    embeds = []
    for f in files:
        if not f.get("ok"):
            continue
        rel = Path(f["local_path"]).name
        if f["ext"] in {"gif", "jpg", "jpeg", "png", "webp"}:
            embeds.append(f'<img src="media/{rel}" alt="{rel}" style="max-width:100%;height:auto">')
        elif f["ext"] == "mp4":
            embeds.append(
                f'<video src="media/{rel}" controls muted loop playsinline preload="metadata" style="max-width:100%"></video>'
            )
    write_text(
        d / "index.html",
        f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{meta.get('title') or case_id}</title>
<style>body{{font:16px/1.5 sans-serif;max-width:880px;margin:24px auto;padding:0 16px;background:#10131a;color:#eff3f8}}a{{color:#c2ff67}}video,img{{border-radius:10px;background:#1a1e27;margin:8px 0}}</style></head>
<body>
<p><a href="../../index.html">← catalog</a></p>
<h1>{meta.get('title') or case_id}</h1>
<p>Author: {meta.get('author')} · <a href="{meta.get('source_url') or '#'}">original source</a></p>
<p>{meta.get('model_claim')}<br>{meta.get('pipeline')} · {meta.get('verify')}</p>
<p>License unknown. Local archive, not an author grant. MIT covers source code only.</p>
<h2>Media</h2>
{''.join(embeds) or '<p>No local media.</p>'}
<h2>Prompt</h2>
<pre>{(meta.get('original_prompt') or '（原文未公开）').replace('<','&lt;')}</pre>
<p><a href="prompt.md">prompt.md</a> · <a href="post.md">post.md</a> · <a href="README.md">README.md</a></p>
</body></html>
""",
    )


def jobs_from_sources() -> tuple[list[dict], dict]:
    x = json.loads(X_SRC.read_text(encoding="utf-8"))
    web = json.loads(WEB_SRC.read_text(encoding="utf-8"))
    game = json.loads(GAME_SRC.read_text(encoding="utf-8"))
    ideas = {i["id"]: i for i in json.loads(IDEAS.read_text(encoding="utf-8"))}
    jobs = []
    meta = {}

    def add(case_id, role, url, filename, author, post, referer=""):
        if not url:
            return
        jobs.append(
            {
                "case_id": case_id,
                "role": role,
                "url": url,
                "filename": filename,
                "dest_dir": str(CASES / case_id / "media"),
                "author": author,
                "post_url": post,
                "referer": referer or post,
            }
        )

    for c in x["author_claim_media_meta_checked"]:
        cid = c["id"]
        author = "@" + ((c.get("author") or {}).get("username") or "unknown")
        claim = c.get("model_claim") or {}
        meta[cid] = {
            "title": c.get("play_summary") or cid,
            "author": author,
            "source_url": c.get("post_url"),
            "model_claim": "作者声明 2.6" + (f"：{claim.get('quote')}" if isinstance(claim, dict) and claim.get("quote") else ""),
            "pipeline": "作者称直出 GIF · X 附件实际 MP4",
            "verify": "作者声明 + 媒体元数据已核 · 未观看 · 未复测",
            "workflow": c.get("workflow") or "",
            "play": c.get("play_summary") or "",
            "notes": c.get("notes") or "",
            "original_prompt": c.get("original_prompt") or "",
            "group": "x",
        }
        n_dyn = n_still = n_ref = 0
        seen = set()
        for m in c.get("media") or []:
            url = m.get("url")
            if not url or url in seen:
                continue
            seen.add(url)
            kind = (m.get("content_type") or "") + (m.get("platform_media_type") or "")
            if "mp4" in kind or m.get("platform_media_type") in ("animated_gif", "video"):
                n_dyn += 1
                add(cid, "x-dynamic", url, f"{n_dyn:02d}-dynamic", author, c.get("post_url"), "https://x.com/")
            else:
                n_still += 1
                add(cid, "still", url, f"{n_still:02d}-still", author, c.get("post_url"), "https://x.com/")
            thumb = m.get("preview_image_url")
            if thumb and thumb not in seen:
                seen.add(thumb)
                add(cid, "poster", thumb, f"{n_dyn or n_still:02d}-poster", author, c.get("post_url"), "https://x.com/")
        for u in c.get("reference_image_urls") or []:
            if u in seen:
                continue
            seen.add(u)
            n_ref += 1
            add(cid, "reference", u, f"{n_ref:02d}-ref", author, c.get("post_url"), "https://x.com/")

    for e in web.get("confirmed_entries") or []:
        cid = e["id"]
        meta[cid] = {
            "title": e.get("playbook") or cid,
            "author": e.get("author"),
            "source_url": e.get("source_url"),
            "model_claim": e.get("model_claim") or "",
            "pipeline": "原生 GIF 直链（已本地归档）",
            "verify": "页面模型依据 + GIF 多帧探测 · 未复测生成",
            "workflow": "",
            "play": e.get("playbook") or "",
            "notes": e.get("vs_baseline") or "",
            "original_prompt": e.get("prompt") or "",
            "group": "web",
        }
        host = e.get("source_url") or ""
        if "atlascloud" in str(e.get("media_url") or ""):
            host = "https://www.atlascloud.ai/"
        add(cid, "gif", e.get("media_url"), "01-gif", e.get("author"), e.get("source_url"), host)
        for i, u in enumerate(e.get("reference_image_urls") or [], 1):
            add(cid, "reference", u, f"{i:02d}-ref", e.get("author"), e.get("source_url"), e.get("source_url"))

    # Krouxzz
    meta["krouxzz-wave-ref"] = {
        "title": "角色挥手循环",
        "author": "@Krouxzz",
        "source_url": "https://x.com/Krouxzz/status/2118283796181053637",
        "model_claim": "作者声明 2.6",
        "pipeline": "作者称 looping GIF · X 附件 MP4",
        "verify": "已在库 · 作者声明 · 未观看附件",
        "workflow": "",
        "play": "角色挥手循环",
        "notes": "",
        "original_prompt": (ideas.get("krouxzz-wave-ref") or {}).get("prompt") or "",
        "group": "inrepo",
    }
    krouxzz_urls = [
        (ideas.get("krouxzz-wave-ref") or {}).get("media_url")
        or "https://video.twimg.com/tweet_video/HWWnk8IXsAE0aXq.mp4",
        "https://video.twimg.com/tweet_video/HWWnk8IXsAE0aXq.mp4",
        "https://video.twimg.com/tweet_video/HWWn8n7b0AAN1xP.mp4",
    ]
    for i, u in enumerate(dict.fromkeys([u for u in krouxzz_urls if u]), 1):
        add(
            "krouxzz-wave-ref",
            "x-dynamic",
            u,
            f"{i:02d}-dynamic",
            "@Krouxzz",
            "https://x.com/Krouxzz/status/2118283796181053637",
            "https://x.com/",
        )

    # Luffy: archive prompts; try known post if ideas have no media
    luffy_prompt = []
    for iid, idea in ideas.items():
        if iid.startswith("luffy-"):
            if idea.get("prompt"):
                luffy_prompt.append(f"## {idea.get('title_zh') or iid}\n\n{idea['prompt']}\n")
    meta["luffy-x-article"] = {
        "title": "路飞 X Article：榨干 Image 2.6 的 10 个神级玩法（多玩法一组）",
        "author": "@0xluffy_eth",
        "source_url": "https://x.com/i/article/2118269816821919744",
        "model_claim": "作者声明 2.6",
        "pipeline": "社区长文 · 提示词已本地全文归档",
        "verify": "已在库 · 提示词逐字",
        "workflow": "X Article 多玩法一组",
        "play": "路飞 X Article",
        "notes": "库存无附件 URL；文章接口尝试未取得媒体，不能断言原长文绝无媒体。介绍帖库存无附件。正文提示词已归档。",
        "original_prompt": "\n".join(luffy_prompt),
        "group": "inrepo",
    }

    game_map = {
        "gs-daft-trade-gamedev-combo": "game-daft-pixel-combo",
        "gs-maker-evan-fox-ronin-game": "game-maker-evan-fox-ronin",
        "gs-xiaomovps-fighter-actions": "game-xiaomovps-fighter",
    }
    for g in game.get("stronger_candidates") or []:
        cid = game_map.get(g["id"])
        if not cid:
            continue
        idea = ideas.get(cid) or {}
        author = "@" + ((g.get("author") or {}).get("username") or "")
        meta[cid] = {
            "title": idea.get("title_zh") or g.get("play_summary") or cid,
            "author": author,
            "source_url": g.get("post_url") or idea.get("source_url"),
            "model_claim": idea.get("model") or "作者声明 2.6",
            "pipeline": idea.get("pipeline") or "",
            "verify": "作者声明 2.6 · 非官方验证 · 未观看",
            "workflow": (g.get("output_workflow") or ""),
            "play": g.get("play_summary") or "",
            "notes": idea.get("production_notes") or g.get("notes") or "",
            "original_prompt": (g.get("original_prompt") or idea.get("prompt") or ""),
            "group": "game",
        }
        n = 0
        for m in g.get("media") or []:
            url = m.get("url")
            if not url:
                continue
            n += 1
            role = "x-dynamic" if "mp4" in str(m.get("content_type")) or str(m.get("url")).endswith(".mp4") else "still"
            add(cid, role, url, f"{n:02d}-{role.split('-')[-1]}", author, g.get("post_url"), "https://x.com/")

    # varg (not in X game stronger the same way)
    v = ideas.get("game-varg-knight-run") or {}
    meta["game-varg-knight-run"] = {
        "title": v.get("title_zh") or "骑士跑循环",
        "author": v.get("source_label") or "vargHQ",
        "source_url": v.get("source_url"),
        "model_claim": v.get("model") or "",
        "pipeline": v.get("pipeline") or "sprite sheet",
        "verify": "作者声明 2.6 · 非官方验证 · 未观看",
        "workflow": "",
        "play": v.get("description_zh") or "",
        "notes": v.get("production_notes") or "",
        "original_prompt": v.get("prompt") or "",
        "group": "game",
    }
    if v.get("media_url"):
        add("game-varg-knight-run", "still", v["media_url"], "01-sheet", "vargHQ", v.get("source_url"), v.get("source_url"))
    if v.get("media_loop_url"):
        add("game-varg-knight-run", "x-dynamic", v["media_loop_url"], "02-loop", "vargHQ", v.get("source_url"), v.get("source_url"))

    if EXTRAS.exists():
        extras = json.loads(EXTRAS.read_text(encoding="utf-8"))
        for cid, items in extras.items():
            if cid not in meta:
                continue
            n = 0
            for it in items:
                n += 1
                add(
                    cid,
                    it.get("role") or "still",
                    it["url"],
                    it.get("filename") or f"{n:02d}-extra",
                    meta[cid].get("author") or "",
                    meta[cid].get("source_url") or "",
                    "https://x.com/",
                )

    if POSTS.exists():
        posts = json.loads(POSTS.read_text(encoding="utf-8"))
        for cid, m in meta.items():
            text = posts.get(cid) or posts.get(m.get("source_url") or "")
            if text:
                m["post_text"] = text

    return jobs, meta


def main() -> None:
    CASES.mkdir(parents=True, exist_ok=True)
    jobs, meta = jobs_from_sources()
    # de-dupe exact url per case+url
    uniq = []
    seen = set()
    for j in jobs:
        key = (j["case_id"], j["url"])
        if key in seen:
            continue
        seen.add(key)
        uniq.append(j)
    print(f"download jobs: {len(uniq)}")
    results = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs = {pool.submit(download_one, j): j for j in uniq}
        for fut in as_completed(futs):
            rec = fut.result()
            results.append(rec)
            flag = "OK" if rec["ok"] else "FAIL"
            print(f"{flag} {rec['case_id']} {rec['role']} {rec['bytes']} {rec.get('error','')[:80]}")

    by_case: dict[str, list] = {}
    for r in results:
        by_case.setdefault(r["case_id"], []).append(r)
    for cid, m in meta.items():
        case_docs(cid, m, by_case.get(cid, []))
        if cid == "luffy-x-article":
            write_text(
                CASES / cid / "prompt.md",
                "# Original prompts from the Luffy article\n\n" + (m.get("original_prompt") or "（原文未公开）") + "\n",
            )

    dyn_ok = sum(1 for r in results if r["ok"] and r["role"] == "x-dynamic")
    dyn_all = [r for r in results if r["role"] == "x-dynamic" and r["case_id"].startswith("x-")]
    missing = [r for r in results if not r["ok"]]
    manifest = {
        "downloaded_at": DOWNLOADED_AT,
        "license_note": "License unknown. Local archive at user request. Not an author grant or CC0. MIT covers source code only.",
        "counts": {
            "jobs": len(uniq),
            "ok": sum(1 for r in results if r["ok"]),
            "failed": len(missing),
            "x_dynamic_attempted": len(dyn_all),
            "x_dynamic_ok": sum(1 for r in dyn_all if r["ok"]),
            "bytes": sum(r["bytes"] for r in results if r["ok"]),
        },
        "files": sorted(results, key=lambda r: (r["case_id"], r["role"], r["source_url"])),
        "cases": sorted(meta.keys()),
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    miss_md = ["# Local media download gaps", "", f"Date {DOWNLOADED_AT}. Failures are listed, not skipped silently.", ""]
    if not missing:
        miss_md.append("All download jobs succeeded.")
    for r in missing:
        miss_md.append(f"- `{r['case_id']}` {r['role']} {r['source_url']} — {r['error']}")
    if "luffy-x-article" in meta and not by_case.get("luffy-x-article"):
        miss_md.append(
            "- `luffy-x-article` media — inventory has no attachment URL; the X article/post API attempt did not retrieve media (article id 2118269816821919744 returned API 404 as a post). That cannot assert the original longform has no media. Announcement 2118274913337552992 has no attachments in the inventory. Prompts archived in prompt.md. Not replaced with SVG."
        )
    miss_md.append("")
    miss_md.append("Notes:")
    miss_md.append("- Krouxzz live attachment is `HWWnk8IXsAE0aXq.mp4` (archived). `HWWn8n7b0AAN1xP.mp4` was a stale catalog URL and 404s.")
    miss_md.append("- Ravivit paper-boat GIF requires a browser User-Agent; Atlas 403s the inventory bot UA.")
    MISSING.write_text("\n".join(miss_md) + "\n", encoding="utf-8")
    print(json.dumps(manifest["counts"], ensure_ascii=False))
    print("wrote", MANIFEST, MISSING)


if __name__ == "__main__":
    main()
