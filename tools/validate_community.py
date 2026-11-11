#!/usr/bin/env python3
"""Community catalog is the primary index: full inventory, not a playbook showcase."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EN_LEAD = (
    "Awesome AI Model Showcases collects real public AI model GIF and animation cases: "
    "original authors, original media, public prompts, sources, and production pipelines. "
    "It is organized by model family (GPT Image is one subsection), not this repository's original playbook showcase."
)
ZH_LEAD = "AI 模型制作案例集收集全网公开的 AI 模型 GIF/动图制作案例、原作者、原媒体、提示词、出处与制作流程；按模型家族分栏（现有 GPT Image 为其中一个子栏目）；不是本站原创方案集"
ABOUT_DESC = (
    "AI 模型制作案例集 / Awesome AI Model Showcases: public GIF & animation "
    "cases by model family (GPT Image, Claude, Gemini, GPT-6.2 Sol, Grok, Qwen, "
    "DeepSeek…). Authors, media, prompts, sources. English & 中文."
)
# 4 GPT Image subsections + 6 reserved families + 4 appendices + 1 contributor <details>
EXPECTED_DETAILS = 15


def first_words(text: str, n: int = 50) -> list[str]:
    body = re.sub(r"<[^>]+>", " ", text)
    body = body.split("# Awesome AI Model Showcases", 1)[-1]
    words = re.findall(r"[A-Za-z0-9.6']+", body)
    return words[:n]


def main() -> int:
    subprocess.check_call([sys.executable, str(ROOT / "tools/write_community_catalog.py")])
    catalog = json.loads((ROOT / "docs/data/community-cases.json").read_text(encoding="utf-8"))
    js = (ROOT / "docs/data/cases.js").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    md = (ROOT / "playbooks/community-cases.md").read_text(encoding="utf-8")
    index = (ROOT / "docs/index.html").read_text(encoding="utf-8")
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    llms_docs = (ROOT / "docs/llms.txt").read_text(encoding="utf-8")
    about = json.loads((ROOT / "docs/github-about.json").read_text(encoding="utf-8"))
    counts = catalog["meta"]["counts"]

    x_source = json.loads((ROOT / "playbooks/research/x-inventory.json").read_text())
    web_source = json.loads((ROOT / "playbooks/research/web-inventory.json").read_text())
    assert counts["x_author_claim_25"] == len(x_source["author_claim_media_meta_checked"]), counts
    assert counts["web_gif_12"] == len(web_source["confirmed_entries"]), counts
    assert counts["pending"] == len(x_source["pending_verification"]), counts
    gpt_keys = ("collected_x_author_claim", "collected_web_gif", "collected_already_in_repo", "collected_game_author_claim")
    frontier_keys = (
        "collected_claude",
        "collected_gemini",
        "collected_gpt_code",
        "collected_grok",
        "collected_qwen",
        "collected_deepseek",
    )
    assert counts["gpt_image"] == sum(len(catalog[key]) for key in gpt_keys), counts
    assert counts["frontier_sourced"] == sum(len(catalog[key]) for key in frontier_keys), counts
    assert counts["main_collected"] == counts["gpt_image"] + counts["frontier_sourced"], counts
    assert counts["already_in_repo"] == len(catalog["collected_already_in_repo"]), counts
    assert counts["game_author_claim"] == len(catalog["collected_game_author_claim"]), counts
    assert counts["repo_seeds"] == len(catalog["repo_seeds"]), counts
    assert catalog["meta"].get("structure") == "model_family"
    by_family = catalog.get("collected_by_family") or {}
    assert "gpt-image" in by_family and len(by_family["gpt-image"]) == counts["gpt_image"]
    for fam, key in (
        ("claude", "collected_claude"),
        ("gemini", "collected_gemini"),
        ("gpt-code", "collected_gpt_code"),
        ("grok", "collected_grok"),
        ("qwen", "collected_qwen"),
        ("deepseek", "collected_deepseek"),
    ):
        assert fam in by_family
        assert len(by_family[fam]) == counts[f"family_{fam}"]
        assert by_family[fam] == catalog[key]
        assert counts[f"family_{fam}"] == len(catalog[key])
        for rec in catalog[key]:
            assert rec.get("model_family") == fam, rec["id"]
            assert rec.get("source_url"), rec["id"]
            assert rec.get("media_storage") == "source_link_only", rec["id"]
    frontier_src = json.loads((ROOT / "playbooks/research/frontier-models-inventory.json").read_text(encoding="utf-8"))
    assert counts["frontier_sourced"] == len(frontier_src["cases"]), counts
    ids = [r["id"] for group in catalog.values() if isinstance(group, list) for r in group]
    assert len(ids) == len(set(ids)), "Duplicate catalog IDs"
    for rec in catalog["collected_x_author_claim"] + catalog["collected_web_gif"]:
        assert rec.get("model_family") == "gpt-image", rec["id"]
        assert rec.get("model_version") == "gpt-image-2.6", rec["id"]
    assert {r["id"] for r in catalog["collected_web_gif"]} == {r["id"] for r in web_source["confirmed_entries"]}
    assert "window.COMMUNITY_CASES" in js
    assert catalog["meta"]["not_exhaustive"] is True
    assert catalog["meta"]["official_verified_26_game"] == 0
    assert llms == llms_docs
    assert str(counts["main_collected"]) in llms and str(counts["main_collected"]) in readme_zh

    for rec in catalog["collected_x_author_claim"]:
        for blob in (readme, readme_zh, md):
            assert rec["id"] in blob, rec["id"]
        assert rec.get("source_url"), rec["id"]
        if rec["media_kind"] == "mp4":
            assert rec.get("media_url"), rec["id"]
        assert rec.get("local_detail"), rec["id"]
        assert rec.get("local_prompt"), rec["id"]

    for rec in catalog["collected_web_gif"]:
        assert rec["id"] in readme and rec["id"] in readme_zh

    assert EN_LEAD in readme
    words = first_words(readme, 50)
    joined = " ".join(words).lower()
    assert "collects" in joined and "original" in joined and "playbook" in joined
    assert ZH_LEAD in readme_zh
    assert "<!-- readme-tech-visualizer:start -->" in readme
    assert "<!-- readme-tech-visualizer:end -->" in readme
    assert "<!-- readme-tech-visualizer:start -->" in readme_zh
    # Presentation is generated, but evidence and prompt availability must survive.
    from readme_presentation import FEATURED
    from PIL import Image

    expected_ids = {r["id"] for key, group in catalog.items() if isinstance(group, list) for r in group}
    for blob, english in ((readme, True), (readme_zh, False)):
        for cid in expected_ids:
            assert f"`{cid}`" in blob, f"README dropped catalog evidence: {cid}"
        assert blob.count("<details>") == blob.count("</details>") == EXPECTED_DETAILS
        assert blob.index('<a id="showcase"></a>') < blob.index('<a id="catalog"></a>')
        assert "hero-wide.png" not in blob, "Do not put the legacy hero ahead of the real examples"
        assert "Technical Snapshot" not in blob
        family_marker = "Family · GPT Image 2.6" if english else "家族 · GPT Image 2.6"
        assert family_marker in blob
        for reserved in ("Claude", "Gemini", "GPT-6.2 Sol", "Grok", "Qwen", "DeepSeek"):
            assert reserved in blob, reserved
        assert "Showcase collection sites" in blob or "展示站资源列表" in blob
        assert "jamesgreene.com/models/" in blob
        assert "developers.openai.com/showcase" in blob
        assert "GPT-6.1 Sol" in blob  # honest dual-status vs OpenAI public docs
        for cid, *_ in FEATURED:
            assert f'docs/cases/{cid}/media/01-gif.gif' in blob
            assert f'docs/cases/{cid}/prompt.md' in blob
        for key in (
            "collected_x_author_claim",
            "collected_web_gif",
            "collected_already_in_repo",
            "collected_game_author_claim",
            "collected_claude",
            "collected_gemini",
            "collected_gpt_code",
            "collected_grok",
            "collected_qwen",
            "collected_deepseek",
        ):
            for rec in catalog[key]:
                rows = [line for line in blob.splitlines() if line.startswith("|") and f"`{rec['id']}`" in line]
                assert len(rows) == 1, rec["id"]
                if rec["prompt_status"] == "空":
                    expected_label = "[Unpublished]" if english else "[未公开]"
                    assert expected_label in rows[0], rec["id"]
                elif rec["prompt_status"] == "短/部分":
                    expected_label = "[Short / partial]" if english else "[短 / 部分]"
                    assert expected_label in rows[0], rec["id"]
    assert "Source motion brief" in readme and "来源动作描述" in readme_zh
    assert "verbatim wording unconfirmed" in readme and "逐字原文未确认" in readme_zh
    with Image.open(ROOT / "docs/readme-assets/project-icon.png") as icon:
        assert icon.format == "PNG" and icon.width == icon.height
        assert icon.mode == "RGBA" and icon.getchannel("A").getextrema()[0] == 0
    # Cap only initial README GIF transfer, never alter archived media for presentation.
    featured_bytes = 0
    for cid, *_ in FEATURED:
        media = ROOT / f"docs/cases/{cid}/media/01-gif.gif"
        featured_bytes += media.stat().st_size
        with Image.open(media) as gif:
            assert gif.format == "GIF" and gif.n_frames > 1
    assert featured_bytes < 5 * 1024 * 1024, featured_bytes

    assert "docs/cases/" in readme and "docs/cases/" in readme_zh
    assert "local media" in readme.lower() and "本地素材" in readme_zh
    assert "只外链" not in readme and "只外链" not in readme_zh
    assert "不转载第三方" not in readme and "不转载第三方" not in readme_zh
    for heading in (
        "## What is this repository?",
        "## What can I do with this catalog?",
        "## What can this repository not do?",
        "## How do I submit a case?",
        "## What are the license boundaries?",
        "## Which languages are maintained?",
    ):
        assert heading in readme, heading
    for heading in (
        "## 这是什么仓库？",
        "## 这个目录能做什么？",
        "## 这个仓库做不到什么？",
        "## 如何提交案例？",
        "## 许可边界是什么？",
        "## 有哪些语言版本？",
    ):
        assert heading in readme_zh, heading

    for banned in ("pixel-head-pat.gif", "cat-screen-crack.gif", "Motion worth"):
        assert banned not in readme[:2000]
        assert banned not in readme_zh[:2000]

    assert "lang.js" in index and "data-lang=\"en\"" in index and "data-lang=\"zh\"" in index
    assert "gifs/cat-screen-crack.gif" not in index
    assert "not this repository's original playbook showcase" in index.lower() or "not this repository" in index
    assert ZH_LEAD.split("；")[0] in llms or "organized by model family" in llms

    topics = about["topics"]
    assert 5 <= len(topics) <= 12
    for t in topics:
        assert re.fullmatch(r"[a-z0-9][a-z0-9-]{0,34}", t), t
    assert about["homepage"] == "https://jammyfu.github.io/awesome-ai-model-showcases/"
    assert about["description"] == ABOUT_DESC
    assert len(about["description"]) <= 350
    assert "awesome-ai-model-showcases" in about["homepage"]
    assert "gifs" not in about["homepage"].rsplit("/", 2)[-2]
    for path, blob in (("README.md", readme), ("README.zh-CN.md", readme_zh), ("community-cases.md", md)):
        for i, line in enumerate(blob.splitlines(), 1):
            if line.startswith("|") or not line.strip() or line.startswith("|---"):
                continue
            if i > 1 and blob.splitlines()[i - 2].startswith("|") and "|" in line:
                raise AssertionError(f"{path}:{i} table row split by newline: {line[:80]}")
    for name in ("x-miramusic-stretch", "x-xepher113-oc12", "x-yulikay-toast"):
        for blob in (readme, readme_zh):
            table_hits = [line for line in blob.splitlines() if name in line and line.startswith("|")]
            assert table_hits, name
            for line in table_hits:
                assert line.count("|") >= 10, (name, line)

    print(
        "community catalog ok: "
        f"main {counts['main_collected']}, pending {counts['pending']}, "
        f"excluded {counts['excluded']}, appendix {counts['appendix']}, seeds {counts['repo_seeds']}; "
        f"topics {len(topics)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
