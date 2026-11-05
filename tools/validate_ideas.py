#!/usr/bin/env python3
"""Validate idea metadata, prompt provenance, preview kinds, and Morphic model honesty."""
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
preview_kinds = ("existing_gif", "concept_illustration", "link_only", "external_gif")
frames_bases = ("author_prompt_spec", "editorial_recommendation")

morphic_ids = set()
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
    if x.get("frames_basis"):
        assert x["frames_basis"] in frames_bases, f'{x["id"]}: bad frames_basis'
    if x.get("prompt_adaptation"):
        assert x["prompt_status"] == "verbatim", f'{x["id"]}: adaptations belong next to a verbatim original'
        assert "本站" in x["prompt_adaptation"] or "this repo" in x["prompt_adaptation"].lower() or "本站改写" in x["prompt_adaptation"]
    if x.get("media_kind") == "mp4":
        assert x["preview_kind"] == "link_only", f'{x["id"]}: MP4 cards stay link_only'
        assert x.get("visual_review_status") == "unwatched", f'{x["id"]}: X MP4 must stay unwatched'
        assert x.get("generation_verified") is False
        assert not x.get("preview")
        assert "mp4" in x["source_label"].lower() or "MP4" in x["source_label"] or "未视觉" in x["source_label"]
    if x["preview_kind"] == "link_only":
        assert not x.get("preview"), f'{x["id"]}: link_only must leave preview empty'
        assert str(x.get("source_url", "")).startswith("https://"), f'{x["id"]}: link_only needs source_url'
    elif x["preview_kind"] == "external_gif":
        assert not x.get("preview"), f'{x["id"]}: external_gif must leave local preview empty'
        assert x.get("media_kind") == "gif"
        assert x.get("media_storage") == "external"
        assert x.get("media_rights") == "unknown_link_only"
        assert str(x.get("media_url", "")).startswith("https://")
        assert x.get("example_is_image26") is True, f'{x["id"]}: external 2.6 GIF must set example_is_image26'
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
    if "morphic.com" in str(x.get("source_url", "")):
        morphic_ids.add(x["id"])
        assert x.get("example_is_image26") is False, f'{x["id"]}: Morphic examples are not 2.6 results'
        assert x["preview_kind"] == "concept_illustration", f'{x["id"]}: Morphic must not use a 2.6 GIF preview'
        assert "不是 2.6" in x["source_label"] or "2.5" in x["source_label"]

assert morphic_ids, "expected Morphic prompt cards to remain, honestly labeled"

expected = (
    "/* AUTO-GENERATED from ideas.json by tools/sync_ideas.py */\nwindow.GIF_IDEAS = "
    + json.dumps(data, ensure_ascii=False, indent=2)
    + ";\n"
)
assert (root / "docs/data/ideas.js").read_text(encoding="utf8") == expected, "ideas.js out of sync"
assert "ideas.html" in (root / "docs/index.html").read_text(encoding="utf8")
print(f"OK: {len(data)} idea cards, including {len(morphic_ids)} Morphic prompt-only cards")
