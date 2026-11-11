#!/usr/bin/env python3
"""Community catalog is the primary index: full inventory, not a playbook showcase."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from write_community_catalog import EN_LEAD, GITHUB_ABOUT, ZH_LEAD

ABOUT_DESC = GITHUB_ABOUT["description"]
README_FILES = ("README.md", "README.zh-CN.md", "README.zh-TW.md", "README.ja.md")
# Secondary model notes and local browsing; evidence lives in catalog.<locale>.md.
EXPECTED_DETAILS = 2


def first_words(text: str, n: int = 50) -> list[str]:
    body = re.sub(r"<[^>]+>", " ", text)
    body = body.split("# Awesome AI Model Showcases", 1)[-1]
    words = re.findall(r"[A-Za-z0-9.6']+", body)
    return words[:n]


def main() -> int:
    subprocess.check_call([sys.executable, str(ROOT / "tools/write_community_catalog.py")])
    catalog = json.loads((ROOT / "docs/data/community-cases.json").read_text(encoding="utf-8"))
    js = (ROOT / "docs/data/cases.js").read_text(encoding="utf-8")
    readmes = {name: (ROOT / name).read_text(encoding="utf-8") for name in README_FILES}
    readme = readmes["README.md"]
    readme_zh = readmes["README.zh-CN.md"]
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
    assert counts["main_collected"] == counts["frontier_sourced"], counts
    assert counts.get("gpt_image_subproject") == "collections/gpt-image-gifs/"
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

    gpt_en_early = (ROOT / "collections/gpt-image-gifs/README.md").read_text(encoding="utf-8")
    gpt_zh_early = (ROOT / "collections/gpt-image-gifs/README.zh-CN.md").read_text(encoding="utf-8")
    for rec in catalog["collected_x_author_claim"]:
        for blob in (gpt_en_early, gpt_zh_early):
            assert rec["id"] in blob, rec["id"]
        assert rec["id"] not in readme and rec["id"] not in readme_zh
        assert rec.get("source_url"), rec["id"]
        if rec["media_kind"] == "mp4":
            assert rec.get("media_url"), rec["id"]
        assert rec.get("local_detail"), rec["id"]
        assert rec.get("local_prompt"), rec["id"]

    from readme_presentation import FEATURED
    showcase_ids = {cid for cid, *_ in FEATURED}
    for rec in catalog["collected_web_gif"]:
        assert rec["id"] in gpt_en_early and rec["id"] in gpt_zh_early
        if rec["id"] not in showcase_ids:
            assert rec["id"] not in readme and rec["id"] not in readme_zh

    words = first_words(readme, 80)
    joined = " ".join(words).lower()
    assert "find" in joined and "creator" in joined and "source" in joined
    assert "发现" in readme_zh and "原始出处" in readme_zh
    for name, blob in readmes.items():
        assert "<!-- readme-tech-visualizer:start -->" in blob, name
        assert "<!-- readme-tech-visualizer:end -->" in blob, name
        for edition in README_FILES:
            assert f"]({edition})" in blob, (name, edition)
    # Presentation is generated, but evidence and prompt availability must survive.
    from readme_presentation import FEATURED
    from media_policy import is_public_asset
    from PIL import Image

    gpt_ids = {r["id"] for key in gpt_keys for r in catalog[key]}
    homepage_ids = {r["id"] for key in frontier_keys for r in catalog[key]}
    expected_ids = {
        r["id"]
        for key, group in catalog.items()
        if isinstance(group, list) and key not in gpt_keys
        for r in group
    }
    assert gpt_ids.isdisjoint(expected_ids)
    assert homepage_ids <= expected_ids
    prompt_labels = {
        "README.md": ("[Unpublished]", "[Short / partial]"),
        "README.zh-CN.md": ("[未公开]", "[短 / 部分]"),
        "README.zh-TW.md": ("[未公開]", "[短 / 部分]"),
        "README.ja.md": ("[未公開]", "[短い / 部分]"),
    }
    evidence_pages = {}
    for name, blob in readmes.items():
        locale = 'en' if name == 'README.md' else name.removeprefix('README.').removesuffix('.md')
        catalog_path = f"docs/catalog.{locale}.md"
        evidence = (ROOT / catalog_path).read_text(encoding="utf-8")
        evidence_pages[catalog_path] = evidence
        assert catalog_path in blob, f"README must link to full evidence: {name}"
        for cid in expected_ids:
            assert f"`{cid}`" in evidence, f"Full catalog dropped evidence: {cid}"
        assert blob.count("<details>") == blob.count("</details>") == EXPECTED_DETAILS
        assert blob.index('<a id="showcase"></a>') < blob.index('<a id="catalog"></a>')
        assert "hero-wide.png" not in blob, "Do not put the legacy hero ahead of the real examples"
        assert "Technical Snapshot" not in blob
        assert "Family · GPT Image" not in blob, name
        assert "家族 · GPT Image" not in blob, name
        assert "assets/brand/families/gpt-image.png" not in blob, name
        assert "collections/gpt-image-gifs/" in blob, name
        assert blob.count("collections/gpt-image-gifs/") == 1, name
        for reserved in ("Claude", "Gemini", "GPT-6.2 Sol", "Grok", "Qwen", "DeepSeek"):
            assert reserved in blob, reserved
        assert 'id="collection-sites"' in blob and 'id="collection-sites"' in evidence
        assert "jamesgreene.com/models/" in evidence
        assert "developers.openai.com/showcase" in evidence
        assert "GPT-6.1 Sol" in blob  # honest dual-status vs OpenAI public docs
        from readme_presentation import source_spotlights
        assert 'src="assets/brand/hero.png"' in blob
        for spotlight in source_spotlights()['cases']:
            assert spotlight['image_path'] in blob
            assert spotlight['prompt_url'] in blob
            assert spotlight['local_license_path'] in blob
        for key in frontier_keys:
            for rec in catalog[key]:
                rows = [line for line in evidence.splitlines() if line.startswith("|") and f"`{rec['id']}`" in line]
                assert len(rows) == 1, rec["id"]
                empty_label, partial_label = prompt_labels[name]
                if rec["prompt_status"] == "空":
                    assert empty_label in rows[0], (name, rec["id"])
                elif rec["prompt_status"] == "短/部分":
                    assert partial_label in rows[0], (name, rec["id"])
    gpt_en = (ROOT / "collections/gpt-image-gifs/README.md").read_text(encoding="utf-8")
    gpt_zh = (ROOT / "collections/gpt-image-gifs/README.zh-CN.md").read_text(encoding="utf-8")
    assert "[Awesome AI Model Showcases](../../README.md)" in gpt_en
    assert "[AI 模型制作案例集](../../README.zh-CN.md)" in gpt_zh
    for cid in gpt_ids:
        assert f"`{cid}`" in gpt_en and f"`{cid}`" in gpt_zh, cid
    gpt_prompt_labels = {
        "en": ("[Unpublished]", "[Short / partial]"),
        "zh-CN": ("[未公开]", "[短 / 部分]"),
    }
    for lang, blob in (("en", gpt_en), ("zh-CN", gpt_zh)):
        for key in gpt_keys:
            for rec in catalog[key]:
                rows = [line for line in blob.splitlines() if line.startswith("|") and f"`{rec['id']}`" in line]
                assert len(rows) == 1, (lang, rec["id"])
                empty_label, partial_label = gpt_prompt_labels[lang]
                if rec["prompt_status"] == "空":
                    assert empty_label in rows[0], (lang, rec["id"])
                elif rec["prompt_status"] == "短/部分":
                    assert partial_label in rows[0], (lang, rec["id"])
    for cid, *_ in FEATURED:
        assert f"../../docs/cases/{cid}/media/01-gif.gif" in gpt_en
        assert f"../../docs/cases/{cid}/prompt.md" in gpt_en
    assert "Published prompt" in gpt_en and "公开提示词" in gpt_zh
    assert "not verified historical requests" in gpt_en and "不是已核实的历史提交请求" in gpt_zh
    assert "assets/brand/families/gpt-image.png" not in gpt_en
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

    assert "docs/translations/" in readme and "docs/translations/" in readme_zh
    assert "approved local media" in readme.lower() and "获准发布的本地媒体" in readme_zh
    assert "只外链" not in readme and "只外链" not in readme_zh
    assert "不转载第三方" not in readme and "不转载第三方" not in readme_zh
    for heading in ("## Start here", "## Browse by model", "## Contribute a case or correction", "## Rights, scope, and languages"):
        assert heading in readme, heading
    for heading in ("## 从这里开始", "## 按模型查找", "## 提交案例或更正", "## 版权、范围与语言"):
        assert heading in readme_zh, heading

    for banned in ("pixel-head-pat.gif", "cat-screen-crack.gif", "Motion worth"):
        assert banned not in readme[:2000]
        assert banned not in readme_zh[:2000]

    assert "lang.js" in index and "data-lang=\"en\"" in index and "data-lang=\"zh\"" in index
    assert "gifs/cat-screen-crack.gif" not in index
    assert "not this repository's original playbook showcase" in index.lower() or "not this repository" in index
    assert ZH_LEAD in llms and EN_LEAD in llms
    assert "README.zh-TW.md" in llms and "README.ja.md" in llms
    assert "No other README" not in llms

    topics = about["topics"]
    assert 5 <= len(topics) <= 12
    for t in topics:
        assert re.fullmatch(r"[a-z0-9][a-z0-9-]{0,34}", t), t
    assert about["homepage"] == "https://jammyfu.github.io/awesome-ai-model-showcases/"
    assert about["description"] == ABOUT_DESC
    assert len(about["description"]) <= 350
    assert "awesome-ai-model-showcases" in about["homepage"]
    assert "gifs" not in about["homepage"].rsplit("/", 2)[-2]
    for path, blob in (*readmes.items(), *evidence_pages.items(), ("community-cases.md", md)):
        for i, line in enumerate(blob.splitlines(), 1):
            if line.startswith("|") or not line.strip() or line.startswith("|---"):
                continue
            if i > 1 and blob.splitlines()[i - 2].startswith("|") and "|" in line:
                raise AssertionError(f"{path}:{i} table row split by newline: {line[:80]}")
    for name in ("x-miramusic-stretch", "x-xepher113-oc12", "x-yulikay-toast"):
        for blob in (gpt_en, gpt_zh):
            table_hits = [line for line in blob.splitlines() if name in line and line.startswith("|")]
            assert table_hits, name
            for line in table_hits:
                assert line.count("|") >= 10, (name, line)

    index = json.loads((ROOT / "data/showcase-index.json").read_text(encoding="utf-8"))
    missing_doc = (ROOT / "docs/missing-thumbnails.md").read_text(encoding="utf-8")
    index_md = (ROOT / "docs/showcase-index.md").read_text(encoding="utf-8")
    assert index["meta"]["count"] == counts["main_collected"] == len(index["cases"])
    main_ids = [rec["id"] for key in frontier_keys for rec in catalog[key]]
    assert gpt_ids.isdisjoint({rec["id"] for rec in index["cases"]})
    assert [rec["id"] for rec in index["cases"]] == [rec["id"] for rec in index["cases"] if rec["id"] in set(main_ids)]
    assert set(main_ids) == {rec["id"] for rec in index["cases"]}
    from readme_presentation import TYPE_ORDER, VERSION_ORDER

    allowed = set(TYPE_ORDER)
    seen_types = set()
    for rec in index["cases"]:
        assert rec["work_type"] in allowed, rec["id"]
        seen_types.add(rec["work_type"])
        assert rec.get("author"), rec["id"]
        assert rec.get("source_url", "").startswith("http"), rec["id"]
        assert f"`{rec['id']}`" in index_md
        if rec.get("image_url"):
            assert rec["image_url"].startswith("http"), rec["id"]
            assert rec.get("image_source", "").startswith("http"), rec["id"]
            assert rec.get("image_credit"), rec["id"]
        if rec.get("thumb"):
            assert is_public_asset(rec["thumb"]), rec["id"]
            thumb = ROOT / rec["thumb"]
            assert thumb.is_file(), rec["id"]
            assert thumb.stat().st_size <= 300 * 1024, rec["id"]
            assert f"../{rec['thumb']}" in index_md
        if not rec.get("image_url"):
            assert f"## `{rec['id']}`" in missing_doc, rec["id"]
        video = rec.get("video") or ""
        if video:
            assert is_public_asset(video), rec["id"]
            path = ROOT / video
            assert path.is_file(), rec["id"]
            assert path.stat().st_size < 95 * 1024 * 1024, rec["id"]
            assert f"[Video](cases/{rec['id']}/media/video.mp4)" in index_md
            case_readme = ROOT / "docs" / "cases" / rec["id"] / "README.md"
            assert "[video.mp4](media/video.mp4)" in case_readme.read_text(encoding="utf-8"), rec["id"]
    assert "luffy-x-article" not in {rec["id"] for rec in index["cases"]}
    assert (ROOT / "docs/missing-videos.md").is_file()
    for name, blob in readmes.items():
        assert 'id="latest"' in blob, name
        assert 'id="by-type"' in blob, name
        assert 'id="type-gif"' in blob and 'id="type-html-3d"' in blob, name
        assert "docs/showcase-index.md" in blob, name
        assert blob.find("ver-gemini-4-carbon") < blob.find("ver-gemini-4-argon"), name
        assert blob.find("ver-gpt-6-2-sol") < blob.find("ver-gpt-6-1-sol"), name
    assert VERSION_ORDER["gemini"][0] == "gemini-4-carbon"
    assert seen_types >= {"animation", "html-3d"}
    archive_types = {rec.get("work_type") for key in gpt_keys for rec in catalog[key]}
    assert {"gif", "minigame"} <= archive_types

    print(
        "community catalog ok: "
        f"main {counts['main_collected']}, pending {counts['pending']}, "
        f"excluded {counts['excluded']}, appendix {counts['appendix']}, seeds {counts['repo_seeds']}; "
        f"topics {len(topics)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
