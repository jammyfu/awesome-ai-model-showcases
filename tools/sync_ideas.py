#!/usr/bin/env python3
"""Synchronize browser data and the prompt playbook from ideas.json."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root / "docs/data/ideas.json"
data = json.loads(source.read_text(encoding="utf-8"))
out = (
    "/* AUTO-GENERATED from ideas.json by tools/sync_ideas.py */\nwindow.GIF_IDEAS = "
    + json.dumps(data, ensure_ascii=False, indent=2)
    + ";\n"
)
(root / "docs/data/ideas.js").write_text(out, encoding="utf-8")

status_zh = {
    "verbatim": "逐字公开提示词",
    "reconstructed": "本站改写，非第三方原文",
    "empty": "来源未公开完整提示词，本站不编造",
}
kind_zh = {
    "gif": "GIF",
    "still": "静图",
    "svg": "SVG",
    "edit": "编辑",
    "sprite_sheet": "Sprite 分镜",
}
origin_zh = {
    "official": "OpenAI 官方发布",
    "tested": "公开实测 / 可复制提示词",
    "community": "社区公开案例",
    "concept": "原创延伸模板",
}

lines = [
    f"# GPT Image 2.6 玩法与 Prompt 图像列表（{len(data)} 例）",
    "",
    f"> Updated: 2026-11-06（北京时间）。`official` = OpenAI 展示方向；`tested` = 公开第三方实测或可复制提示词库；`community` = 社区案例；`concept` = 本项目原创延伸模板。Prompt 标注 `verbatim` / `reconstructed` / `empty`。不是按真实搜索量排名。",
    "",
    "[打开交互式图像列表](https://jammyfu.github.io/awesome-gpt-image-gifs/ideas.html) · [结构化 JSON](../docs/data/ideas.json) · [参考出处](sources.md) · [来源与方法](trends-2026-11.md)",
    "",
    "| # | 玩法 | 类别 | 来源 | Prompt | 建议模型 / 规格 |",
    "|---:|---|---|---|---|---|",
]
for i, x in enumerate(data, 1):
    title = x["title_zh"]
    if x.get("preview"):
        title = f"[{title}](../docs/{x['preview']})"
    source_cell = "延伸创意"
    if x.get("source_url"):
        source_cell = f"[参考]({x['source_url']})"
    spec = f"{x['model']}"
    if x["output_kind"] == "gif":
        spec += f" / {x['frames']}f"
    elif x["output_kind"] == "sprite_sheet":
        spec += f" / {x['frames']} 格"
    else:
        spec += f" / {kind_zh[x['output_kind']]}"
    lines.append(
        f"| {i} | {title} | {x['category']} | {source_cell} | [{status_zh[x['prompt_status']]}](#idea-{i}) | {spec} |"
    )

lines += ["", "## 完整提示词（公开原文或本站改写）", ""]
lines.append("标注 `verbatim` 的条目复制自注明来源的公开页面；`reconstructed` 是本站按创意目标改写的模板，不是第三方作者的逐字提示词；`empty` 表示来源只描述了能力、没有给出可复制提示词，本站留空。均未在此仓库逐项实测。")
lines.append("")

for i, x in enumerate(data, 1):
    lines.append(f'<a id="idea-{i}"></a>')
    lines.append(f"### {i:02d}. {x['title_zh']} / {x['title_en']}")
    lines.append("")
    rec = f"`{x['model']}`"
    if x["frames"]:
        rec += f", `{x['frames']}` frames"
    if x["frame_duration_ms"]:
        rec += f", `{x['frame_duration_ms']}` ms/frame"
    rec += f", `{x['aspect']}`"
    lines.append(
        f"类型：{x['category']} ｜输出：{kind_zh[x['output_kind']]} ｜证据：{x['source_label']} ｜提示词：{status_zh[x['prompt_status']]} ｜推荐：{rec} ｜编辑优先级：{x['priority']}"
    )
    lines.append("")
    if x["preview_kind"] == "existing_gif" and x.get("preview"):
        lines.append(f"![{x['title_zh']} — 已有 GIF](../docs/{x['preview']})")
        lines.append("")
    elif x["preview_kind"] == "concept_illustration" and x.get("preview"):
        lines.append(f"![{x['title_zh']} — 原创 SVG 概念示意](../docs/{x['preview']})")
        lines.append("")
    else:
        lines.append("本地不转载第三方成品图；请打开来源链接查看。")
        lines.append("")
    lines.append(x["description_zh"])
    lines.append("")
    if x["prompt_status"] == "empty":
        lines.append("公开来源未给出完整提示词，本站不编造第三方原文。")
        lines.append("")
    else:
        lines.append("```text")
        lines.append(x["prompt"])
        lines.append("```")
        lines.append("")
    if x.get("source_url"):
        date = f"（{x['evidence_date']}）" if x.get("evidence_date") else ""
        lines.append(f"参考链接{date}：{x['source_url']}。")
    else:
        lines.append("参考链接：原创延伸，无第三方参考。")
    lines.append("")
    lines.append("")

lines += [
    "## 参考出处 / Sources",
    "",
    "完整列表见 [sources.md](sources.md)。本页卡片若引用路飞 X Article，出处统一为：",
    "",
    "- 路飞 [@0xluffy_eth](https://x.com/0xluffy_eth)，《榨干 Image 2.6 的 10 个神级玩法！【附完整提示词】》",
    "- [X Article](https://x.com/i/article/2118269816821919744) · [介绍帖](https://x.com/0xluffy_eth/status/2118274913337552992) · 2026-11-05",
    "- 中文提示词按原文逐字收录；封面为原创 SVG，不转载文中 GIF。",
    "",
]

playbook = root / "playbooks/ideas-and-prompts.md"
playbook.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
print(f"Synced {len(data)} ideas -> docs/data/ideas.js and playbooks/ideas-and-prompts.md")
