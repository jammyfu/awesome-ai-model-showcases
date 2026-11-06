#!/usr/bin/env python3
"""Require local archives for the 43 main cases and the 42 X dynamic attachments."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "docs/data/local-media-manifest.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "docs/data/community-cases.json").read_text(encoding="utf-8"))
X = json.loads((ROOT / "playbooks/research/x-inventory.json").read_text(encoding="utf-8"))
MISSING = (ROOT / "playbooks/local-media-missing.md").read_text(encoding="utf-8")

MAIN = (
    CATALOG["collected_x_author_claim"]
    + CATALOG["collected_web_gif"]
    + CATALOG["collected_already_in_repo"]
    + CATALOG["collected_game_author_claim"]
)
assert len(MAIN) == 43, len(MAIN)

files = MANIFEST.get("files") or []
ok = [f for f in files if f.get("ok")]
by_case: dict[str, list] = {}
for f in ok:
    by_case.setdefault(f["case_id"], []).append(f)

required = (
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
for f in ok:
    for key in required:
        assert f.get(key) not in (None, ""), f"manifest missing {key}: {f.get('case_id')}"
    path = ROOT / f["local_path"]
    assert path.is_file(), f["local_path"]
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == f["sha256"], f["local_path"]
    assert path.stat().st_size == f["bytes"]
    assert path.stat().st_size < 90 * 1024 * 1024, f["local_path"]
    if f.get("ext") == "mp4":
        assert not str(f["local_path"]).endswith(".gif"), f["local_path"]

x_dyn_urls = []
for c in X["author_claim_media_meta_checked"]:
    for m in c.get("media") or []:
        url = m.get("url") or ""
        kind = (m.get("content_type") or "") + (m.get("platform_media_type") or "")
        if "mp4" in kind or m.get("platform_media_type") in ("animated_gif", "video") or url.endswith(".mp4"):
            x_dyn_urls.append(url)
assert len(x_dyn_urls) == 42, len(x_dyn_urls)
ok_urls = {f["source_url"] for f in ok}
missing_x = [u for u in x_dyn_urls if u not in ok_urls]
assert not missing_x, missing_x

no_media = []
for rec in MAIN:
    cid = rec["id"]
    case_dir = ROOT / "docs/cases" / cid
    assert case_dir.is_dir(), cid
    assert (case_dir / "prompt.md").is_file(), cid
    assert (case_dir / "README.md").is_file(), cid
    assert (case_dir / "post.md").is_file(), cid
    prompt = (case_dir / "prompt.md").read_text(encoding="utf-8")
    if rec.get("original_prompt"):
        assert rec["original_prompt"][:80] in prompt or "Original prompt" in prompt
    media = [f for f in by_case.get(cid, []) if f.get("ext") in {"gif", "mp4", "png", "jpg", "jpeg", "webp"}]
    if not media:
        no_media.append(cid)
        assert cid == "luffy-x-article", cid
        assert "inventory has no original GIF/MP4 URL" in MISSING
        assert "路飞" in prompt or "luffy" in prompt.lower() or "Original prompts" in prompt

assert no_media == ["luffy-x-article"], no_media
assert "HWWn8n7b0AAN1xP.mp4" in MISSING
assert (ROOT / "docs/cases/krouxzz-wave-ref/media").exists()
assert any(p.suffix == ".mp4" for p in (ROOT / "docs/cases/krouxzz-wave-ref/media").iterdir())

print(
    f"local media ok: {len(ok)} files, {len(by_case)} cases with files, "
    f"42/42 X dynamics, 42/43 main cases have media, "
    f"luffy documented miss, {MANIFEST['counts']['bytes']} bytes"
)
