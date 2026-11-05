#!/usr/bin/env python3
"""Validate the source/media manifest against local files and catalog cross-links.

Does not fetch the network. External GIF frame counts were probed once and recorded.
"""
import json
from collections import Counter
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "docs/data/media-manifest.json").read_text(encoding="utf-8"))
ideas = json.loads((ROOT / "docs/data/ideas.json").read_text(encoding="utf-8"))
gallery = json.loads((ROOT / "docs/data/gallery.json").read_text(encoding="utf-8"))

assert isinstance(manifest, dict), "media-manifest.json must be an object"
items = manifest.get("items")
assert isinstance(items, list) and items, "media-manifest.json needs a nonempty items array"

required = (
    "id",
    "media_kind",
    "storage",
    "rights",
    "url",
    "content_type",
    "source_page",
    "source_label",
    "creator",
    "model_claim",
    "prompt_status",
)
kinds = ("gif", "mp4", "vimeo")
storages = ("local", "external")
rights = ("repo_seed", "unknown_link_only")
prompt_statuses = ("verbatim", "reconstructed", "empty")
idea_ids = {x["id"] for x in ideas}
gallery_ids = {x["id"] for x in gallery}
gallery_by_id = {x["id"]: x for x in gallery}
ideas_by_id = {x["id"]: x for x in ideas}

ids = []
hashes = []
for item in items:
    for key in required:
        assert item.get(key) not in (None, ""), f'{item.get("id")}: missing {key}'
    assert item["media_kind"] in kinds, f'{item["id"]}: bad media_kind'
    assert item["storage"] in storages
    assert item["rights"] in rights
    assert item["prompt_status"] in prompt_statuses
    assert str(item["url"]).startswith("https://") or (
        item["storage"] == "local" and not str(item["url"]).startswith(("http://",))
    ), f'{item["id"]}: url must be https or a local relative path'
    ids.append(item["id"])
    if item["storage"] == "local":
        assert item["rights"] == "repo_seed"
        path = (ROOT / "docs" / item["local_path"]).resolve()
        assert item.get("local_path"), f'{item["id"]}: local_path required'
        assert path.is_relative_to(ROOT / "docs") and path.is_file(), f'{item["id"]}: missing local file'
        if item["media_kind"] == "gif":
            with Image.open(path) as im:
                assert im.format == "GIF"
                assert im.is_animated and im.n_frames > 1
                assert im.n_frames == item["n_frames"], f'{item["id"]}: frame count drifted'
                ms = 0
                for frame_no in range(im.n_frames):
                    im.seek(frame_no)
                    ms += im.info.get("duration", 0)
                assert ms == item["duration_ms"], f'{item["id"]}: duration drifted'
                assert list(im.size) == [item["width"], item["height"]]
            data = path.read_bytes()
            import hashlib

            digest = hashlib.sha256(data).hexdigest()
            assert digest == item["sha256"], f'{item["id"]}: sha256 drifted'
            assert len(data) == item["bytes"]
    else:
        assert item["rights"] == "unknown_link_only"
        assert str(item["url"]).startswith("https://")
        assert not item.get("local_path"), f'{item["id"]}: external media must not ship a local copy'
        if item["media_kind"] == "gif":
            assert item["content_type"] == "image/gif"
            assert item["n_frames"] >= 2
            assert item["duration_ms"] > 0
            assert item.get("sha256") and item.get("bytes")
            hashes.append(item["sha256"])
        elif item["media_kind"] == "mp4":
            assert "mp4" in item["content_type"]
            assert item.get("x_declared_type") in (None, "animated_gif", "video")
            if item.get("visual_review_status") == "unwatched":
                assert item.get("n_frames") in (None, 0)
                assert item.get("original_gif_available") in (None, False)
                assert item.get("gallery_id") in (None, ""), f'{item["id"]}: unwatched MP4 must not enter the GIF gallery'
        elif item["media_kind"] == "vimeo":
            assert "vimeo.com" in item["url"]
    for idea_id in item.get("idea_ids") or []:
        assert idea_id in idea_ids, f'{item["id"]}: unknown idea_id {idea_id}'
        idea = ideas_by_id[idea_id]
        if item["media_kind"] == "gif" and idea.get("media_id") == item["id"]:
            assert idea.get("media_kind") == "gif"
            assert idea.get("media_url") == item["url"]
        if item["media_kind"] == "mp4" and idea.get("media_id") == item["id"]:
            assert idea.get("media_kind") == "mp4"
            assert idea.get("media_url") == item["url"]
    gallery_id = item.get("gallery_id")
    if gallery_id:
        assert gallery_id in gallery_ids, f'{item["id"]}: unknown gallery_id {gallery_id}'
        g = gallery_by_id[gallery_id]
        assert g.get("media_id") == item["id"]
        if item["storage"] == "local":
            assert g["image"] == item["local_path"]
        else:
            assert g["image"] == item["url"]
        if item["media_kind"] == "gif":
            assert g["frames"] == item["n_frames"]
            assert g["duration_ms"] == item["duration_ms"]
            assert g["width"] == item["width"]
            assert g["height"] == item["height"]
            assert g.get("media_kind") == "gif"

assert len(ids) == len(set(ids)), "duplicate media id"
dup_hashes = [h for h, n in Counter(hashes).items() if n > 1]
assert not dup_hashes, f"duplicate external gif sha256: {dup_hashes}"

expected_js = (
    "/* AUTO-GENERATED from media-manifest.json by tools/sync_media_js.py */\n"
    "window.MEDIA_MANIFEST = "
    + json.dumps(manifest, indent=2, ensure_ascii=False)
    + ";\n"
)
assert (ROOT / "docs/data/media.js").read_text(encoding="utf-8") == expected_js, "media.js out of sync"

for item in items:
    if item.get("gallery_id"):
        g = gallery_by_id[item["gallery_id"]]
        assert g.get("media_kind") != "mp4"
        assert g.get("storage") == item["storage"]

excluded = manifest.get("excluded") or []
excl_ids = {x["id"] for x in excluded}
assert "atlas-robot-wave-pre26" in excl_ids
assert "atlas-teacup-pre26" in excl_ids
pending = manifest.get("pending") or []
assert len(pending) >= 12, "X pending candidates must stay listed, not merged into confirmed works"
pending_ids = {x["id"] for x in pending}
assert "x-chaoranya-orange-cat" in pending_ids
assert "x-iskunzhenbai-fatfish-reply" in pending_ids
for row in pending:
    assert row.get("bucket") == "pending_verification"
    assert row.get("url", "").startswith("https://")
gallery_images = {x["image"] for x in gallery}
for row in excluded:
    assert row.get("url") not in gallery_images, f'excluded {row["id"]} must not appear in the GIF gallery'

gif_local = sum(1 for x in items if x["media_kind"] == "gif" and x["storage"] == "local")
gif_ext = sum(1 for x in items if x["media_kind"] == "gif" and x["storage"] == "external")
mp4 = sum(1 for x in items if x["media_kind"] == "mp4")
vimeo = sum(1 for x in items if x["media_kind"] == "vimeo")
print(
    f"OK: {len(items)} media records "
    f"({gif_local} local GIF, {gif_ext} external GIF, {mp4} mp4, {vimeo} vimeo); "
    f"{len(excluded)} excluded; hashes unique"
)
