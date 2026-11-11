#!/usr/bin/env python3
"""Require real local archives: format, prompts, counts, and case correspondence."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from media_format import ffprobe_bin, probe_media  # noqa: E402
UNPUBLISHED_MARK = "（原文未公开 / original prompt not published）"
MAIN_KEYS = (
    "collected_x_author_claim",
    "collected_web_gif",
    "collected_already_in_repo",
    "collected_game_author_claim",
)
REQUIRED_FILE_KEYS = (
    "case_id",
    "role",
    "source_url",
    "author",
    "post_url",
    "downloaded_at",
    "sha256",
    "local_path",
    "ext",
    "bytes",
)


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def norm_text(s: str) -> str:
    s = (s or "").replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in s.split("\n")).strip()


def prompt_archive_body(text: str) -> str:
    """Drop leading headings so a title cannot satisfy the prompt check."""
    lines = (text or "").replace("\r\n", "\n").replace("\r", "\n").split("\n")
    i = 0
    while i < len(lines) and (not lines[i].strip() or lines[i].lstrip().startswith("#")):
        i += 1
    return norm_text("\n".join(lines[i:]))


def source_prompts_for(cid: str, rec: dict, x_by: dict, web_by: dict, ideas: list) -> list[str]:
    found: list[str] = []
    if cid in x_by:
        found.append(x_by[cid].get("original_prompt") or "")
    if cid in web_by:
        found.append(web_by[cid].get("prompt") or "")
    for idea in ideas:
        iid = idea.get("id") or ""
        if iid == cid:
            found.append(idea.get("prompt") or "")
        elif cid == "luffy-x-article" and iid.startswith("luffy-"):
            found.append(idea.get("prompt") or "")
    if rec.get("original_prompt"):
        found.append(rec["original_prompt"])
    # Keep order, drop exact duplicate empties later in check.
    return found


def check_prompt_archive(cid: str, archive_text: str, sources: list[str]) -> None:
    body = prompt_archive_body(archive_text)
    nonempty = [norm_text(s) for s in sources if norm_text(s)]
    if nonempty:
        for src in nonempty:
            if src not in body:
                raise AssertionError(
                    f"{cid}: archived prompt.md is missing full source text "
                    f"({src[:60]!r}…); heading fallback is not accepted"
                )
        if body == "" or body == "Original prompt":
            raise AssertionError(f"{cid}: prompt body is empty after stripping headings")
        return
    if UNPUBLISHED_MARK not in body:
        raise AssertionError(
            f"{cid}: unpublished prompt must carry the explicit marker {UNPUBLISHED_MARK!r}"
        )


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lfs_pointer(path: Path):
    if path.stat().st_size > 1024:
        return None
    try:
        text = path.read_text("utf-8")
    except UnicodeDecodeError:
        return None
    if not text.startswith("version https://git-lfs.github.com/spec/v1"):
        return None
    fields = dict(line.split(" ", 1) for line in text.splitlines() if " " in line)
    return {"oid": fields.get("oid", "").removeprefix("sha256:"), "size": int(fields.get("size", "-1"))}


def x_dynamic_urls(x_inv: dict) -> list[str]:
    urls = []
    for c in x_inv["author_claim_media_meta_checked"]:
        for m in c.get("media") or []:
            url = m.get("url") or ""
            kind = (m.get("content_type") or "") + (m.get("platform_media_type") or "")
            if "mp4" in kind or m.get("platform_media_type") in ("animated_gif", "video") or url.endswith(".mp4"):
                urls.append(url)
    return urls


def check_manifest_file(f: dict) -> dict:
    for key in REQUIRED_FILE_KEYS:
        if f.get(key) in (None, ""):
            raise AssertionError(f"manifest missing {key}: {f.get('case_id')}")
    path = ROOT / f["local_path"]
    if not path.is_file():
        raise AssertionError(f"missing file {f['local_path']}")
    pointer = lfs_pointer(path)
    if pointer is not None:
        # Checked out without LFS content (e.g. CI): the pointer's oid is the
        # sha256 of the real file and its size is the real byte count.
        if pointer["oid"] != f["sha256"]:
            raise AssertionError(f"sha256 mismatch (lfs pointer) {f['local_path']}")
        if pointer["size"] != f["bytes"]:
            raise AssertionError(f"size mismatch (lfs pointer) {f['local_path']}")
        if pointer["size"] >= 95 * 1024 * 1024:
            raise AssertionError(f"oversized {f['local_path']}")
        return {"lfs_pointer": True}
    if sha256_file(path) != f["sha256"]:
        raise AssertionError(f"sha256 mismatch {f['local_path']}")
    if path.stat().st_size != f["bytes"]:
        raise AssertionError(f"size mismatch {f['local_path']}")
    if path.stat().st_size >= 90 * 1024 * 1024:
        raise AssertionError(f"oversized {f['local_path']}")
    if f.get("ext") == "mp4" and str(f["local_path"]).endswith(".gif"):
        raise AssertionError(f"mp4 stored as gif {f['local_path']}")
    info = probe_media(path, ext=f.get("ext") or "", role=f.get("role") or "")
    return info


def catalog_rows(catalog: dict) -> list[dict]:
    rows = []
    for key, val in catalog.items():
        if key == "meta":
            continue
        if isinstance(val, list):
            rows.extend(val)
    return rows


def main() -> int:
    manifest = load_json("docs/data/local-media-manifest.json")
    catalog = load_json("docs/data/community-cases.json")
    x_inv = load_json("playbooks/research/x-inventory.json")
    web_inv = load_json("playbooks/research/web-inventory.json")
    ideas = load_json("docs/data/ideas.json")
    missing = (ROOT / "playbooks/local-media-missing.md").read_text(encoding="utf-8")

    # Local-media completeness applies to the GPT Image archive buckets only.
    # Other model-family cases are source-link-only by default (MEDIA_RIGHTS).
    main_rows = []
    for key in MAIN_KEYS:
        main_rows.extend(catalog[key])
    counts_meta = catalog["meta"]["counts"]
    assert len(main_rows) == counts_meta["gpt_image"], (len(main_rows), counts_meta.get("gpt_image"))
    assert counts_meta["main_collected"] == counts_meta.get("frontier_sourced", 0)
    assert counts_meta["gpt_image_subproject"] == "collections/gpt-image-gifs/"

    files = manifest.get("files") or []
    ok = [f for f in files if f.get("ok")]
    failed = [f for f in files if not f.get("ok")]
    counts = manifest.get("counts") or {}
    assert len(ok) == counts.get("ok"), (len(ok), counts.get("ok"))
    assert len(failed) == counts.get("failed"), (len(failed), counts.get("failed"))
    assert len(files) == counts.get("jobs"), (len(files), counts.get("jobs"))
    byte_sum = sum(int(f.get("bytes") or 0) for f in ok)
    assert byte_sum == counts.get("bytes"), (byte_sum, counts.get("bytes"))

    by_case: dict[str, list] = {}
    ok_by_url: dict[str, dict] = {}
    for f in ok:
        info = check_manifest_file(f)
        by_case.setdefault(f["case_id"], []).append(f)
        ok_by_url[f["source_url"]] = {**f, "_probe": info}

    x_urls = x_dynamic_urls(x_inv)
    manifest_x = [f for f in files if f.get("role") == "x-dynamic" and f["case_id"].startswith("x-")]
    assert counts.get("x_dynamic_ok") == sum(bool(f.get("ok")) for f in manifest_x)
    assert counts.get("x_dynamic_attempted") == len(manifest_x)
    missing_x = [u for u in x_urls if u not in ok_by_url]
    assert not missing_x, missing_x
    for url in x_urls:
        rec = ok_by_url[url]
        assert rec.get("ext") == "mp4", (url, rec.get("ext"))
        assert rec["_probe"].get("lfs_pointer") or rec["_probe"].get("has_video"), (url, rec["_probe"])

    x_by = {c["id"]: c for c in x_inv.get("author_claim_media_meta_checked") or []}
    web_by = {c["id"]: c for c in web_inv.get("confirmed_entries") or []}

    no_media = []
    for rec in main_rows:
        cid = rec["id"]
        case_dir = ROOT / "docs/cases" / cid
        assert case_dir.is_dir(), cid
        for name in ("prompt.md", "README.md", "post.md"):
            assert (case_dir / name).is_file(), f"{cid}/{name}"
        archive = (case_dir / "prompt.md").read_text(encoding="utf-8")
        sources = source_prompts_for(cid, rec, x_by, web_by, ideas)
        check_prompt_archive(cid, archive, sources)

        media = [f for f in by_case.get(cid, []) if f.get("ext") in {"gif", "mp4", "png", "jpg", "jpeg", "webp"}]
        catalog_files = rec.get("local_files") or []
        catalog_ok = {f.get("path") for f in catalog_files if f.get("path")}
        manifest_ok = {f["local_path"] for f in by_case.get(cid, [])}
        assert catalog_ok == manifest_ok, (cid, catalog_ok, manifest_ok)
        if rec.get("local_detail"):
            assert (ROOT / rec["local_detail"]).is_file(), (cid, rec["local_detail"])
        if rec.get("local_prompt"):
            assert (ROOT / rec["local_prompt"]).is_file(), (cid, rec["local_prompt"])
        if rec.get("media_url") and cid != "luffy-x-article":
            assert media, f"{cid}: catalog has media_url but no local attachment"
        if not media:
            no_media.append(cid)
            assert cid == "luffy-x-article", cid
            assert "库存无附件 URL" in missing or "inventory has no attachment URL" in missing
            assert "不能断言原长文绝无媒体" in missing or "cannot assert the original longform has no media" in missing
            for idea in ideas:
                if (idea.get("id") or "").startswith("luffy-") and idea.get("prompt"):
                    assert norm_text(idea["prompt"]) in prompt_archive_body(archive), idea["id"]

    assert no_media == ["luffy-x-article"], no_media
    assert "HWWn8n7b0AAN1xP.mp4" in missing
    krouxzz_media = ROOT / "docs/cases/krouxzz-wave-ref/media"
    assert krouxzz_media.exists()
    assert any(p.suffix == ".mp4" for p in krouxzz_media.iterdir())

    for rec in catalog_rows(catalog):
        for key in ("local_dir", "local_prompt", "local_detail", "local_page", "local_preview"):
            p = rec.get(key) or ""
            if not p or p.startswith(("http://", "https://", "mailto:")):
                continue
            target = ROOT / p
            assert target.exists(), f"{rec.get('id')} {key} -> missing {p}"

    via = "ffprobe" if ffprobe_bin() else "iso-bmff"
    print(
        f"local media ok: {len(ok)} files, {len(by_case)} cases with files, "
        f"{len(x_urls)}/{len(x_urls)} X dynamics ({via}), {len(main_rows)-len(no_media)}/{len(main_rows)} main cases have media, "
        f"luffy documented miss (no attachment URL; API attempt retrieved none; "
        f"not an assertion the longform has none), {counts['bytes']} bytes"
    )
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
