#!/usr/bin/env python3
"""Sync popular-playbooks.json to docs/data/popular.js and playbooks/popular-gifs.md."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "docs/data/popular-playbooks.json").read_text(encoding="utf-8"))
js = (
    "/* AUTO-GENERATED from popular-playbooks.json by tools/sync_popular.py */\n"
    "window.POPULAR_PLAYBOOKS = "
    + json.dumps(data, ensure_ascii=False, indent=2)
    + ";\n"
)
(root / "docs/data/popular.js").write_text(js, encoding="utf-8")

items = data["items"]
lines = [
    f"# {data['title_zh']}",
    "",
    f"> **不是 GPT Image 2.6 作品。** Updated 2026-11-06（北京时间）。参考库 23 条 = 年度榜 15 + 活动榜 1 + 近期趋势 3 + 经典知名度 4；本页精选 {len(items)} 个可执行原创角色重演方案，不凑 23。不是世界总榜。views ≠ 使用次数。方案是本项目策划，未实测、未付费出图。",
    "",
    data["policy"],
    "",
    "## 方法（不要混用）",
    "",
]
for note in data["methodology_notes"]:
    lines.append(f"- {note}")
lines += ["", "## 缺口与未选", ""]
for gap in data["gaps"] + data.get("skipped_from_19", []) + data.get("skipped_from_recent", []):
    lines.append(f"- {gap}")
lines += [
    "",
    f"[打开独立页面](https://jammyfu.github.io/awesome-ai-model-showcases/popular.html) · [JSON](../docs/data/popular-playbooks.json)",
    "",
    "| # | 方案 | 年/桶 | 平台指标 | 原作 |",
    "|---:|---|---|---|---|",
]
for i, x in enumerate(items, 1):
    year = x["year"] if x.get("year") else x.get("year_label", "经典")
    lines.append(
        f"| {i} | {x['title_zh']} | {year} · {x['chart_bucket']} | [{x['rank']}]({x['evidence_url']}) | [{x['original_work']}]({x['original_gif_page']}) |"
    )
lines += ["", "## 可执行复刻方案", ""]
for i, x in enumerate(items, 1):
    year = x["year"] if x.get("year") else x.get("year_label", "经典")
    lines += [
        f"### {i:02d}. {x['title_zh']} / {x['title_en']}",
        "",
        f"- 不是 2.6。本项目策划，未实测。",
        f"- 年/桶：{year} · {x['chart_bucket']} · {x['platform']}",
        f"- 榜单：{x['chart']} · {x['rank']}",
        *( [f"- 采样时刻：{x['sampled_at']}"] if x.get("sampled_at") else [] ),
        f"- 指标：{x['metric']}",
        f"- 证据：[{x['evidence_label']}]({x['evidence_url']})",
        f"- 原作 / 作者：{x['original_work']} · {x['original_author']}",
        f"- 原 GIF 页（参考，非本仓成品）：{x['original_gif_page']}",
        f"- 情绪：{x['emotion']}",
        f"- 动作节拍：{x['motion_beats']}",
        f"- 逐帧：{x['frame_plan']}",
        f"- 为何能传：{x['why_it_spreads']}",
        f"- 普通人场景：{x['everyday_scene']}",
        f"- 参考图：{x['need_reference']}",
        f"- 镜头：{x['camera']}",
        f"- 循环：{x['loop']}",
        f"- 预期文件：{x['expected_file']}",
        f"- 验收：{x['acceptance']}",
        f"- 演示门槛：{x['demo_barrier']}",
        f"- 复现依赖：{x['reproduction_deps']}",
        f"- 权利：{x['rights_note']}",
        "",
        "本仓原创角色重演提示词（不是原作者原文，未实测）：",
        "",
        "```text",
        x["remake_prompt_zh"],
        "```",
        "",
    ]
(root / "playbooks/popular-gifs.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
print(f"Synced {len(items)} popular playbooks")
