#!/usr/bin/env python3
"""Validate the popular-GIF remake catalog. Must stay out of the 2.6 GIF gallery."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "docs/data/popular-playbooks.json").read_text(encoding="utf-8"))
gallery = json.loads((root / "docs/data/gallery.json").read_text(encoding="utf-8"))
ideas = json.loads((root / "docs/data/ideas.json").read_text(encoding="utf-8"))

assert data.get("not_image26") is True
assert data.get("scout_catalog") == "applied"
counts = data["catalog_counts"]
assert counts["reference_library"] == 23
assert counts["scout_global"] == 19
assert counts["scout_recent_confirmed"] == 4
assert counts["annual_platform_chart"] == 15
assert counts["event_platform_chart"] == 1
assert counts["recent_trending_snapshot"] == 3
assert counts["fame_only"] == 4
assert len(data["reference_library"]) == 23
assert len({x["id"] for x in data["reference_library"]}) == 23

items = data["items"]
assert 8 <= len(items) <= 12, f"expected 8–12 playbooks, found {len(items)}"
assert counts["selected_playbooks"] == len(items)

buckets = ("年度平台榜", "活动平台榜", "近期趋势采样", "仅经典知名度")
required = (
    "id",
    "title_zh",
    "title_en",
    "chart_bucket",
    "platform",
    "chart",
    "metric",
    "rank",
    "evidence_url",
    "original_work",
    "original_author",
    "original_gif_page",
    "emotion",
    "motion_beats",
    "why_it_spreads",
    "everyday_scene",
    "need_reference",
    "camera",
    "frame_plan",
    "loop",
    "expected_file",
    "acceptance",
    "demo_barrier",
    "reproduction_deps",
    "remake_prompt_zh",
)
ids = []
priority = set()
for x in items:
    for key in required:
        assert x.get(key) not in (None, ""), f'{x.get("id")} missing {key}'
    assert x["not_image26"] is True
    assert x["generation_tested"] is False
    assert str(x["evidence_url"]).startswith("https://")
    assert str(x["original_gif_page"]).startswith("https://")
    assert x["chart_bucket"] in buckets, f'{x["id"]}: bad bucket {x["chart_bucket"]}'
    if x["chart_bucket"] == "年度平台榜":
        assert isinstance(x.get("year"), int) and x["year"] >= 2013
    elif x["chart_bucket"] == "活动平台榜":
        assert isinstance(x.get("year"), int)
        assert "全年" in x["rank"] or "不是" in x["rank"]
        assert "活动" in x["chart"] or "当晚" in x["chart"] or "金球" in x["chart"]
    elif x["chart_bucket"] == "近期趋势采样":
        assert "无排名" in x["rank"] or "不为" in x["rank"] or "页面顺序" in x["chart"]
        assert x.get("sampled_at")
    else:
        assert x.get("year") in (None, "")
        assert "非年榜" in x.get("year_label", "") or "经典" in x.get("year_label", "")
    ids.append(x["id"])
    prompt = x["remake_prompt_zh"]
    assert len(prompt) >= 120, f'{x["id"]}: remake prompt too short'
    assert "2.6" not in prompt
    assert "gpt-image" not in prompt.lower()
    assert "循环" in prompt
    if x.get("priority_mechanism"):
        priority.add(x["priority_mechanism"])
assert len(ids) == len(set(ids))
for needed in ("连眨怀疑", "退入遮挡社死", "吃零食看戏", "致谢升级", "可爱容器冒火", "失语僵住", "麻烦逼近"):
    assert needed in priority, f"missing priority mechanism {needed}"

# Language #4 must stay unbound
blob = json.dumps(items, ensure_ascii=False)
assert "NRP1siu3kgCrUT6OKg" not in blob
assert "gg2024-lily-gladstone-language" not in ids
unbound = {x["id"] for x in data.get("candidates_unbound") or []}
assert "gg2024-lily-gladstone-language" in unbound

gallery_ids = {x["id"] for x in gallery}
idea_ids = {x["id"] for x in ideas}
for pid in ids:
    assert pid not in gallery_ids, f"{pid} must not enter the 2.6 GIF gallery"
    assert pid not in idea_ids, f"{pid} must not be mixed into 2.6 idea cards"

expected = (
    "/* AUTO-GENERATED from popular-playbooks.json by tools/sync_popular.py */\n"
    "window.POPULAR_PLAYBOOKS = "
    + json.dumps(data, ensure_ascii=False, indent=2)
    + ";\n"
)
assert (root / "docs/data/popular.js").read_text(encoding="utf-8") == expected
html = (root / "docs/popular.html").read_text(encoding="utf-8")
assert "不是 GPT Image 2.6" in html or "NOT GPT Image 2.6" in html
assert "活动平台榜" in html and "近期趋势采样" in html
assert "popular.html" in (root / "docs/index.html").read_text(encoding="utf-8")
assert "popular.html" in (root / "docs/ideas.html").read_text(encoding="utf-8")
assert "热门 GIF" in (root / "README.md").read_text(encoding="utf-8") or "popular" in (root / "README.md").read_text(encoding="utf-8").lower()
print(
    f"OK: {len(items)} playbooks from 23-reference library "
    f"(19 global + 4 recent); Language #4 unbound; not mixed into 2.6"
)
