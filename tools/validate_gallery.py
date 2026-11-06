#!/usr/bin/env python3
"""Check gallery integrity. Local GIFs are Pillow-verified; archived third-party GIFs stay local."""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
items = json.loads((ROOT / "docs/data/gallery.json").read_text(encoding="utf-8"))
assert isinstance(items, list) and items, "Gallery must be a nonempty array"
ids = set()
local_gifs = 0
external_gifs = 0
for item in items:
    for key in ("id", "title", "description", "category", "tags", "image", "frames", "duration_ms", "prompt_status"):
        assert item.get(key) not in (None, ""), f'{item.get("id")}: missing {key}'
    assert item["id"] not in ids, f'duplicate id {item["id"]}'
    ids.add(item["id"])
    storage = item.get("storage", "local")
    media_kind = item.get("media_kind", "gif")
    rights = item.get("rights", "repo_seed")
    assert storage in ("local", "external"), f'{item["id"]}: bad storage'
    assert media_kind == "gif", f'{item["id"]}: GIF gallery cannot include {media_kind}'
    assert rights in ("repo_seed", "unknown_link_only", "unknown_archived")
    assert item["prompt_status"] in ("verbatim", "reconstructed", "empty")
    if item["prompt_status"] == "empty":
        assert item.get("prompt", "") == ""
    else:
        assert str(item.get("prompt", "")).strip(), f'{item["id"]}: missing prompt'
    if storage == "local":
        assert rights in ("repo_seed", "unknown_archived"), f'{item["id"]}: local rights'
        assert not item["image"].startswith(("/", "http:", "https:")), f'{item["id"]}: local image must be relative'
        path = (ROOT / "docs" / item["image"]).resolve()
        assert path.is_relative_to(ROOT / "docs") and path.is_file(), f'{item["id"]}: bad image path'
        with Image.open(path) as im:
            assert im.format == "GIF", f"{path.name}: not GIF"
            assert im.is_animated and im.n_frames > 1, f"{path.name}: not animated"
            assert im.n_frames == item["frames"], f"{path.name}: wrong frame count"
            ms = 0
            for frame_no in range(im.n_frames):
                im.seek(frame_no)
                ms += im.info.get("duration", 0)
            assert ms == item["duration_ms"], f"{path.name}: wrong duration"
        if item.get("rights") == "repo_seed":
            prompt_path = ROOT / item["prompt_file"]
            assert prompt_path.is_file(), f'{item["id"]}: missing prompt file'
        local_gifs += 1
    else:
        assert rights == "unknown_link_only"
        assert item["image"].startswith("https://"), f'{item["id"]}: external GIF needs https'
        assert item.get("source_url", "").startswith("https://")
        assert item.get("creator")
        assert item.get("media_id")
        external_gifs += 1

compiled = ROOT / "docs/data/gallery.js"
assert compiled.read_text(encoding="utf-8").split("window.GALLERY_ITEMS = ", 1)[1].rstrip().endswith(";")
print(f"OK: {len(items)} gallery GIFs ({local_gifs} local Pillow-checked, {external_gifs} still remote)")
