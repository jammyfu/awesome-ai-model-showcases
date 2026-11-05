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
        assert x["prompt_status"] in ("verbatim", "empty"), f'{x["id"]}: adaptations sit next to verbatim or empty originals, never invented third-party text'
        assert "本站" in x["prompt_adaptation"] or "this repo" in x["prompt_adaptation"].lower() or "本站改写" in x["prompt_adaptation"] or "本站策划" in x["prompt_adaptation"]
    if x.get("media_kind") == "mp4":
        assert x["preview_kind"] == "link_only", f'{x["id"]}: MP4 cards stay link_only'
        assert x.get("visual_review_status") == "unwatched", f'{x["id"]}: X MP4 must stay unwatched'
        assert x.get("generation_verified") is False
        assert not x.get("preview")
        assert "mp4" in x["source_label"].lower() or "MP4" in x["source_label"] or "未视觉" in x["source_label"]
    if x.get("media_kind") == "png":
        assert x["preview_kind"] == "link_only", f'{x["id"]}: PNG sheets stay link_only'
        assert str(x.get("media_url", "")).startswith("https://")
        assert x.get("game_sequence") is True, f'{x["id"]}: PNG sheet cards are game sequences'
    if x.get("game_sequence"):
        for key in ("pipeline", "action_kind", "alpha_status", "engine_import_status", "acceptance", "cell_spec", "image26_status"):
            assert x.get(key) not in (None, ""), f'{x["id"]} missing game field {key}'
        assert x["preview_kind"] == "link_only"
        assert x["category"] in ("游戏动作序列", "其他模型参考"), f'{x["id"]}: unexpected game category'
        assert x.get("counts_as_image26_game") is False, f'{x["id"]}: no official 2.6 game verification this round'
        if x["image26_status"] == "not_26":
            assert x.get("default_hidden") is True
            assert x.get("include_in_image26_list") is False
            assert x["category"] == "其他模型参考"
        claimed = "已经用于游戏" in x["description_zh"]
        negated = any(s in x["description_zh"] for s in ("不能说已经用于游戏", "不写成已核", "本仓未观看", "未见引擎"))
        if claimed and not negated:
            raise AssertionError(f'{x["id"]}: do not claim in-game use without engine evidence')
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

game_ids = [x["id"] for x in data if x.get("game_sequence")]
by_id = {x["id"]: x for x in data}
assert game_ids, "expected game-sequence playbooks"
for gid in (
    "game-daft-pixel-combo",
    "game-maker-evan-fox-ronin",
    "game-xiaomovps-fighter",
    "game-maker-evan-walk-cycle",
    "game-ssss-4x4-spec",
    "game-varg-knight-run",
    "game-higgsfield-boxing",
):
    assert gid in by_id, f"missing {gid}"
assert "yrzhe" not in json.dumps(data), "yrzhe coming-soon conflict must stay pending"
ssss = by_id["game-ssss-4x4-spec"]
assert ssss["image26_status"] == "not_26" and ssss["default_hidden"] is True
assert by_id["game-daft-pixel-combo"]["prompt_status"] == "empty"
assert by_id["game-xiaomovps-fighter"]["prompt_status"] == "empty"
assert "Cut the sheets into frames" in by_id["game-maker-evan-fox-ronin"]["prompt"]
assert by_id["game-maker-evan-walk-cycle"]["image26_status"] == "multimodel_postprocess"
assert by_id["game-higgsfield-boxing"]["image26_status"] == "promo_claim_unwatched"
assert by_id["game-varg-knight-run"]["image26_status"] == "author_claim_unverified"
author_x = [x for x in data if "x-original-author" in (x.get("tags") or [])]
assert {x["id"] for x in author_x} == {
    "game-daft-pixel-combo",
    "game-maker-evan-fox-ronin",
    "game-xiaomovps-fighter",
}
gallery = json.loads((root / "docs/data/gallery.json").read_text(encoding="utf8"))
gallery_ids = {x["id"] for x in gallery}
for gid in game_ids:
    assert gid not in gallery_ids, f"{gid} must not enter the GIF gallery"
game_html = (root / "docs/game.html").read_text(encoding="utf8")
assert "官方验证" in game_html
assert "coming soon" not in game_html.lower() or "不当确认" in game_html
assert "game.html" in (root / "docs/ideas.html").read_text(encoding="utf8")
assert "game.html" in (root / "docs/index.html").read_text(encoding="utf8")

expected = (
    "/* AUTO-GENERATED from ideas.json by tools/sync_ideas.py */\nwindow.GIF_IDEAS = "
    + json.dumps(data, ensure_ascii=False, indent=2)
    + ";\n"
)
assert (root / "docs/data/ideas.js").read_text(encoding="utf8") == expected, "ideas.js out of sync"
assert "ideas.html" in (root / "docs/index.html").read_text(encoding="utf8")
print(
    f"OK: {len(data)} idea cards, including {len(morphic_ids)} Morphic prompt-only cards "
    f"and {len(game_ids)} game-sequence playbooks"
)
