#!/usr/bin/env python3
"""Validate idea metadata, prompt provenance, and local preview assets."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "docs/data/ideas.json").read_text(encoding="utf8"))
assert len(data) >= 20, f"expected at least 20 ideas; found {len(data)}"
assert len({x["id"] for x in data}) == len(data), "duplicate id"

required = (
    "id",
    "title_zh",
    "title_en",
    "category",
    "description_zh",
    "origin",
    "model",
    "frames",
    "frame_duration_ms",
    "preview_kind",
    "source_label",
    "prompt_status",
    "output_kind",
)
origins = ("official", "tested", "community", "concept")
prompt_statuses = ("verbatim", "reconstructed", "empty")
output_kinds = ("gif", "still", "svg", "edit", "sprite_sheet")
preview_kinds = ("existing_gif", "concept_illustration", "link_only")

for x in data:
    for k in required:
        assert x.get(k) not in (None, ""), f'{x.get("id")} missing {k}'
    assert x["origin"] in origins
    assert x["prompt_status"] in prompt_statuses
    assert x["output_kind"] in output_kinds
    assert x["preview_kind"] in preview_kinds
    prompt = x.get("prompt", "")
    if x["prompt_status"] == "empty":
        assert prompt == "", f'{x["id"]}: empty status must have empty prompt'
    else:
        assert prompt.strip(), f'{x["id"]}: missing prompt'
    if x["output_kind"] in ("gif", "sprite_sheet"):
        assert 2 <= x["frames"] <= 16, f'{x["id"]}: bad frame count'
        if x["output_kind"] == "gif":
            assert 20 <= x["frame_duration_ms"] <= 2000, f'{x["id"]}: bad duration'
        else:
            assert x["frame_duration_ms"] == 0, f'{x["id"]}: sprite sheets are still grids'
    else:
        assert x["frames"] == 0 and x["frame_duration_ms"] == 0, f'{x["id"]}: non-GIF must use 0 frames'
    if x["preview_kind"] == "link_only":
        assert not x.get("preview"), f'{x["id"]}: link_only must leave preview empty'
        assert str(x.get("source_url", "")).startswith("https://"), f'{x["id"]}: link_only needs source_url'
    else:
        assert x.get("preview"), f'{x["id"]} missing preview'
        asset = (root / "docs" / x["preview"]).resolve()
        assert asset.is_relative_to(root / "docs") and asset.is_file(), f'broken image: {x["id"]}'
        if x["preview_kind"] == "concept_illustration":
            assert asset.suffix == ".svg"
        if x["preview_kind"] == "existing_gif":
            assert asset.suffix == ".gif"
    if x["origin"] == "concept":
        assert not x["source_url"]
    else:
        assert x["source_url"].startswith("https://")

expected = (
    "/* AUTO-GENERATED from ideas.json by tools/sync_ideas.py */\nwindow.GIF_IDEAS = "
    + json.dumps(data, ensure_ascii=False, indent=2)
    + ";\n"
)
assert (root / "docs/data/ideas.js").read_text(encoding="utf8") == expected, "ideas.js out of sync"
assert "ideas.html" in (root / "docs/index.html").read_text(encoding="utf8")
print(f"OK: {len(data)} idea cards, sources, prompts, preview images, and browser data")
