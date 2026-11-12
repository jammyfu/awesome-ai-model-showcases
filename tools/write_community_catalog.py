#!/usr/bin/env python3
"""Build the community-case catalog from scout inventories + in-repo extras.

This is the repo's primary index: collected public cases, not this project's
original remake playbooks.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from media_policy import is_public_asset
from case_localization import attach_translations, localized, translation_link, write_translated_cases

from readme_presentation import (
    FAMILY_TITLE,
    VERSION_ORDER,
    _date_desc,
    version_anchor,
    TYPE_INDEX_LABEL,
    TYPE_ORDER,
    UI,
    VERSION_LABEL,
    featured_cards,
    main_case_rows,
    render_readme,
    write_site_spotlight,
    write_preview_credits,
    sol_note,
    work_type_of,
)

ROOT = Path(__file__).resolve().parents[1]
X_SRC = ROOT / "playbooks/research/x-inventory.json"
WEB_SRC = ROOT / "playbooks/research/web-inventory.json"
FRONTIER_SRC = ROOT / "playbooks/research/frontier-models-inventory.json"
COLLECTION_SITES = ROOT / "playbooks/research/showcase-collection-sites.json"
IDEAS = ROOT / "docs/data/ideas.json"
GALLERY = ROOT / "docs/data/gallery.json"
OUT_JSON = ROOT / "docs/data/community-cases.json"
OUT_JS = ROOT / "docs/data/cases.js"
OUT_MD = ROOT / "playbooks/community-cases.md"
OUT_README = ROOT / "README.md"
OUT_README_ZH = ROOT / "README.zh-CN.md"
OUT_README_ZH_TW = ROOT / "README.zh-TW.md"
OUT_README_JA = ROOT / "README.ja.md"
README_LANGS = (
    ("en", OUT_README),
    ("zh-CN", OUT_README_ZH),
    ("zh-TW", OUT_README_ZH_TW),
    ("ja", OUT_README_JA),
)
OUT_LLMS = ROOT / "llms.txt"
OUT_LLMS_DOCS = ROOT / "docs/llms.txt"
OUT_ABOUT = ROOT / "docs/github-about.json"
LOCAL_MANIFEST = ROOT / "docs/data/local-media-manifest.json"
CASE_IMAGES = ROOT / "data/case-images.json"
OUT_INDEX_JSON = ROOT / "data/showcase-index.json"
OUT_INDEX_MD = ROOT / "docs/showcase-index.md"
OUT_MISSING = ROOT / "docs/missing-thumbnails.md"
OUT_MISSING_VIDEOS = ROOT / "docs/missing-videos.md"
CASE_VIDEOS = ROOT / "data/case-videos.json"
OUT_GPT_EN = ROOT / "collections/gpt-image-gifs/README.md"
OUT_GPT_ZH = ROOT / "collections/gpt-image-gifs/README.zh-CN.md"

GITHUB_ABOUT = {
    "description": (
        "AI 模型制作案例集 / Awesome AI Model Showcases: latest and still-mainstream "
        "model cases (animation, HTML/game, image, video) by frontier family. "
        "Claude, Gemini, GPT-6.2 Sol, Grok, Qwen, DeepSeek. "
        "GPT Image GIFs: collections/gpt-image-gifs. EN / 简体中文 / 繁體中文 / 日本語."
    ),
    "homepage": "https://jammyfu.github.io/awesome-ai-model-showcases/",
    "topics": [
        "awesome-list",
        "ai-models",
        "animated-gif",
        "chinese",
        "claude",
        "gemini",
        "gif",
        "gpt-image",
        "prompt-engineering",
        "showcase",
    ],
}

MODEL_FAMILY_PLACEHOLDERS = (
    ("claude", "Claude", "Claude", "Fable 5.2 / Opus 5.5 / Mythos 5.2"),
    ("gemini", "Gemini", "Gemini", "4 Carbon / 4 Argon"),
    (
        "gpt-code",
        "GPT-6.2 Sol / Astra (code models)",
        "GPT-6.2 Sol / Astra（代码模型）",
        "GPT-6.2 Sol (owner) · OpenAI pages still list GPT-6.1 Sol",
    ),
    ("grok", "Grok", "Grok", "Grok 4.7 / Imagine Video"),
    ("qwen", "Qwen", "Qwen", "Qwen3.8 / Qwen 4 Preview"),
    ("deepseek", "DeepSeek", "DeepSeek", "V4.1 Flash"),
)

BUCKET_FRONTIER = "collected_frontier_sourced"

FAMILY_LABELS_EN = {
    "claude": "Claude",
    "gemini": "Gemini",
    "gpt-code": "GPT-6.2 Sol",
    "grok": "Grok",
    "qwen": "Qwen",
    "deepseek": "DeepSeek",
    "multi": "Cross-family",
}
FAMILY_LABELS_ZH = {
    "claude": "Claude",
    "gemini": "Gemini",
    "gpt-code": "GPT-6.2 Sol",
    "grok": "Grok",
    "qwen": "Qwen",
    "deepseek": "DeepSeek",
    "multi": "跨家族",
}
FAMILY_LABELS_ZH_TW = {
    "claude": "Claude",
    "gemini": "Gemini",
    "gpt-code": "GPT-6.2 Sol",
    "grok": "Grok",
    "qwen": "Qwen",
    "deepseek": "DeepSeek",
    "multi": "跨家族",
}
FAMILY_LABELS_JA = {
    "claude": "Claude",
    "gemini": "Gemini",
    "gpt-code": "GPT-6.2 Sol",
    "grok": "Grok",
    "qwen": "Qwen",
    "deepseek": "DeepSeek",
    "multi": "横断",
}
FAMILY_LABELS = {
    "en": FAMILY_LABELS_EN,
    "zh-CN": FAMILY_LABELS_ZH,
    "zh-TW": FAMILY_LABELS_ZH_TW,
    "ja": FAMILY_LABELS_JA,
}


def format_collection_sites(sites_raw: dict, *, lang: str) -> str:
    site_translations = json.loads((ROOT / "data/collection-site-translations.json").read_text(encoding="utf-8"))["entries"]
    by_family = sites_raw.get("by_family") or {}
    labels = FAMILY_LABELS.get(lang, FAMILY_LABELS_EN)
    parts: list[str] = []
    # Prefer GPT-6.2 Sol first, then other families, then multi.
    order = ["gpt-code"] + [k for k in by_family if k not in ("gpt-code", "multi")] + (
        ["multi"] if "multi" in by_family else []
    )
    seen: set[str] = set()
    for fam in order:
        if fam in seen or fam not in by_family:
            continue
        seen.add(fam)
        items = by_family[fam] or []
        if not items:
            continue
        label = labels.get(fam, fam)
        parts.append(f"**{label}**")
        for site in items:
            name = (site.get("name") or "").strip()
            url = (site.get("url") or "").strip()
            original_desc = (site.get("description") or "").strip()
            desc = site_translations[original_desc][lang] if original_desc else ""
            if not name or not url:
                continue
            parts.append(f"- [{name}]({url}) — {desc}" if desc else f"- [{name}]({url})")
        parts.append("")
    return "\n".join(parts).rstrip() + ("\n" if parts else "")


EN_LEAD = (
    "Awesome AI Model Showcases collects real public production cases from the latest large models "
    "(Claude Fable 5.2 / Mythos 5.2, Gemini 4 Argon / Carbon, GPT-6.2 Sol, Grok, Qwen, DeepSeek, and others) "
    "and from the previous generation that is still mainstream: GIFs, animations, HTML and game demos, and images, "
    "with creator credits, source links, available prompts or explicit missing markers, and recorded methods."
)
ZH_LEAD = (
    "AI 模型制作案例集收录最新一代大模型（Claude Fable 5.2 / Mythos 5.2、Gemini 4 Argon / Carbon、"
    "GPT-6.2 Sol、Grok、Qwen、DeepSeek 等）以及上一代仍在主流使用的模型的真实制作案例："
    "动图、动画、HTML / 游戏 demo、图像；保留原帖、作者、可获得的提示词或未公开标记，以及已记录的做法"
)

BUCKET_MAIN = "collected_author_claim_26"
BUCKET_WEB = "collected_web_gif"
BUCKET_GAME = "collected_game_author_claim"
BUCKET_INREPO = "collected_already_in_repo"
BUCKET_PENDING = "pending"
BUCKET_PROMPT_ONLY = "prompt_only"
BUCKET_EXCLUDED = "excluded"
BUCKET_APPENDIX = "appendix_not_confirmed_success"
BUCKET_SEED = "repo_seed"


def media_kind_of(item: dict) -> str:
    for m in item.get("media") or []:
        ct = str(m.get("content_type") or "")
        url = str(m.get("url") or "")
        ptype = str(m.get("platform_media_type") or "")
        if "gif" in ct or url.endswith(".gif"):
            return "gif"
        if "mp4" in ct or url.endswith(".mp4") or ptype in ("animated_gif", "video"):
            return "mp4"
    return "unknown"


def first_media_url(item: dict) -> str:
    for m in item.get("media") or []:
        url = m.get("url") or ""
        if url:
            return url
    return item.get("media_url") or item.get("candidate_mp4_for_watch") or ""


def prompt_flag(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return "空"
    if len(t) < 40:
        return "短/部分"
    return "有原文"


def row(
    *,
    id: str,
    bucket: str,
    title: str,
    author: str,
    source_url: str,
    media_url: str,
    media_kind: str,
    prompt_status: str,
    model_claim: str,
    pipeline: str,
    verify: str,
    play: str,
    license_notes: str,
    extra: dict | None = None,
) -> dict:
    out = {
        "id": id,
        "bucket": bucket,
        "title": title,
        "author": author,
        "source_url": source_url,
        "media_url": media_url,
        "media_kind": media_kind,
        "prompt_status": prompt_status,
        "model_claim": model_claim,
        "pipeline": pipeline,
        "verify": verify,
        "play": play,
        "license_notes": license_notes or "许可未知 · 本地归档（非作者授权、非 CC0）。MIT 只覆盖源码。",
        "visual_review_status": "unwatched",
        "generation_verified": False,
    }
    if extra:
        out.update(extra)
    return out


def from_x(item: dict, bucket: str) -> dict:
    author = item.get("author") or {}
    handle = author.get("username") or "unknown"
    media_kind = media_kind_of(item)
    if media_kind == "mp4":
        pipeline = "作者称直出 GIF · X 附件实际 MP4"
    else:
        pipeline = item.get("workflow") or "未知"
    claim = item.get("model_claim") or {}
    quote = claim.get("quote") if isinstance(claim, dict) else str(claim or "")
    return row(
        id=item["id"],
        bucket=bucket,
        title=item.get("play_summary") or item["id"],
        author=f"@{handle}" + (f"（{author.get('name')}）" if author.get("name") else ""),
        source_url=item.get("post_url") or "",
        media_url=first_media_url(item),
        media_kind=media_kind,
        prompt_status=prompt_flag(item.get("original_prompt") or ""),
        model_claim=("作者声明 2.6" + (f"：{quote[:80]}" if quote else "")),
        pipeline=pipeline,
        verify="作者声明 + 媒体元数据已核 · 未观看 · 未复测",
        play=item.get("play_summary") or "",
        license_notes=item.get("license_notes") or "许可未知 · 本地归档（非作者授权、非 CC0）",
        extra={
            "original_prompt": item.get("original_prompt") or "",
            "thread_group_id": item.get("thread_group_id"),
            "media_count": len(item.get("media") or []),
        },
    )


def from_web(item: dict) -> dict:
    return row(
        id=item["id"],
        bucket=BUCKET_WEB,
        title=item.get("playbook") or item["id"],
        author=item.get("author") or "unknown",
        source_url=item.get("source_url") or "",
        media_url=item.get("media_url") or "",
        media_kind=item.get("media_type") or "gif",
        prompt_status=item.get("prompt_status") or prompt_flag(item.get("prompt") or ""),
        model_claim=item.get("model_claim") or "页面声称 2.6",
        pipeline=item.get("pipeline") or "原生 GIF 直链（Pillow 多帧已核）",
        verify=item.get("verification") or "页面模型依据 + GIF 多帧探测 · 未复测生成",
        play=item.get("playbook") or "",
        license_notes=item.get("license_conclusion") or "许可未知 · 本地归档（非作者授权、非 CC0）",
        extra={
            "original_prompt": item.get("prompt") or "",
            "frames": (item.get("media_verify") or {}).get("frames"),
            **{key: item[key] for key in ("prompt_provenance", "license_label", "license_url", "model_evidence_url", "source_record_url", "visual_review_status") if item.get(key)},
        },
    )


def normalize_frontier_prompt_status(raw: str, prompt: str) -> str:
    status = (raw or "").strip()
    if status in {"有", "有原文", "original"}:
        return "有原文"
    if status in {"短/部分", "partial", "short"}:
        return "短/部分"
    if status in {"空", "unpublished", "empty"}:
        return "空"
    if status:
        return status
    return prompt_flag(prompt)


def from_frontier(item: dict) -> dict:
    prompt = item.get("prompt") or item.get("original_prompt") or ""
    return row(
        id=item["id"],
        bucket=BUCKET_FRONTIER,
        title=item.get("title") or item["id"],
        author=item.get("author") or "unknown",
        source_url=item.get("source_url") or "",
        media_url=item.get("media_url") or item.get("source_url") or "",
        media_kind=item.get("media_kind") or "source",
        prompt_status=normalize_frontier_prompt_status(item.get("prompt_status") or "", prompt),
        model_claim=item.get("model_claim") or item.get("model_version") or "",
        pipeline=item.get("pipeline") or "source-linked showcase",
        verify=item.get("verify") or "sourced public URL · not independently re-run",
        play=item.get("title") or "",
        license_notes=item.get("license_notes") or "许可未知 · 仅出处链接（不本地再托管）。MIT 只覆盖源码。",
        extra={
            "original_prompt": prompt,
            "model_family": item.get("model_family") or "",
            "model_version": item.get("model_version") or "",
            "media_storage": item.get("media_storage") or "source_link_only",
            "date": item.get("date") or "",
            "license_label": "Source link only",
            **{k: item[k] for k in ("also_models", "notes", "prompt_url") if item.get(k)},
        },
    )


HEADERS_ZH = "| # | 作者 | 玩法 | 原帖 | 媒体 | prompt | 模型依据 | 管线 | 验证 | 许可 |"
HEADERS_ZH_TW = "| # | 作者 | 做法 | 原帖 | 媒體 | prompt | 模型依據 | 管線 | 驗證 | 許可 |"
HEADERS_JA = "| # | 作者 | 内容 | 原投稿 | メディア | prompt | モデル根拠 | 作り方 | 検証 | ライセンス |"
HEADERS_EN = "| # | Author | Play | Post | Media | prompt | Model | Pipeline | Verification | License |"
HEADERS_FOR = {"en": HEADERS_EN, "zh-CN": HEADERS_ZH, "zh-TW": HEADERS_ZH_TW, "ja": HEADERS_JA}
TABLE_UI = {
    "en": {
        "source": "Source", "file": "File", "case": "Case", "origin": "Source",
        "published": "Published at source", "agg": "Aggregator only", "empty": "Unpublished",
        "partial": "Short / partial", "original": "Original", "unknown": "Unknown", "kind": "source",
    },
    "zh-CN": {
        "source": "出处", "file": "文件", "case": "案例", "origin": "来源",
        "published": "原文见来源", "agg": "仅聚合页", "empty": "未公开",
        "partial": "短 / 部分", "original": "原文", "unknown": "许可未知", "kind": "来源",
    },
    "zh-TW": {
        "source": "出處", "file": "檔案", "case": "案例", "origin": "來源",
        "published": "原文見來源", "agg": "僅聚合頁", "empty": "未公開",
        "partial": "短 / 部分", "original": "原文", "unknown": "許可未知", "kind": "來源",
    },
    "ja": {
        "source": "出典", "file": "ファイル", "case": "ケース", "origin": "出典",
        "published": "出典で公開", "agg": "集約ページのみ", "empty": "未公開",
        "partial": "短い / 部分", "original": "原文", "unknown": "ライセンス不明", "kind": "出典",
    },
}


def cell(text, limit: int | None = None) -> str:
    s = str(text or "").replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
    s = s.replace("|", "/").replace("  ", " ").strip()
    if limit is not None:
        s = s[:limit]
    return s


def existing_public_page(r: dict) -> str:
    """Seeds and similar: point at a file that already exists, else the source URL."""
    cid = r.get("id") or ""
    gif = ROOT / "docs" / "gifs" / f"{cid}.gif"
    if is_public_asset(str(gif.relative_to(ROOT)), root=ROOT):
        return str(gif.relative_to(ROOT)).replace("\\", "/")
    media = r.get("media_url") or ""
    if media and not media.startswith(("http://", "https://")):
        for cand in (ROOT / media, ROOT / "docs" / media):
            if is_public_asset(str(cand.relative_to(ROOT)), root=ROOT):
                return str(cand.relative_to(ROOT)).replace("\\", "/")
    return r.get("source_url") or ""


def attach_local(rows: list[dict]) -> None:
    """Only emit local archive links when docs/cases/<id>/ actually exists."""
    man: dict = {}
    if LOCAL_MANIFEST.exists():
        man = json.loads(LOCAL_MANIFEST.read_text(encoding="utf-8"))
    by: dict[str, list] = {}
    for f in man.get("files") or []:
        if f.get("ok") and is_public_asset(f.get("local_path") or "", root=ROOT):
            by.setdefault(f["case_id"], []).append(f)
    for r in rows:
        cid = r["id"]
        case_dir = ROOT / "docs" / "cases" / cid
        has_archive = (case_dir / "README.md").is_file()
        files = by.get(cid) or []
        if has_archive:
            r["local_dir"] = f"docs/cases/{cid}/"
            r["local_prompt"] = f"docs/cases/{cid}/prompt.md"
            r["local_detail"] = f"docs/cases/{cid}/README.md"
            r["local_page"] = f"docs/cases/{cid}/index.html"
            r["local_files"] = [
                {
                    "path": f.get("local_path"),
                    "public_allowed": True,
                    "ext": f.get("ext"),
                    "role": f.get("role"),
                    "bytes": f.get("bytes"),
                    "source_url": f.get("source_url"),
                }
                for f in files
            ]
            preview = next((f for f in files if f.get("ext") in {"gif", "png", "jpg", "jpeg", "webp"}), None)
            video = next((f for f in files if f.get("ext") == "mp4"), None)
            r["local_preview"] = (preview or video or {}).get("local_path") or ""
            if r.get("bucket") in {BUCKET_MAIN, BUCKET_WEB, BUCKET_INREPO, BUCKET_GAME} and not r.get("license_label"):
                r["license_notes"] = "许可未知 · 本地归档（非作者授权、非 CC0）。MIT 只覆盖源码。"
            continue
        r["local_dir"] = ""
        r["local_prompt"] = ""
        r["local_files"] = []
        r["local_preview"] = ""
        if r.get("bucket") == BUCKET_SEED:
            page = existing_public_page(r)
            r["local_detail"] = page
            r["local_page"] = page
        else:
            # Pending / appendix / excluded: cite source, do not invent case folders.
            r["local_detail"] = ""
            r["local_page"] = ""


def repo_href(path: str, from_file: Path) -> str:
    if not path:
        return ""
    if path.startswith(("http://", "https://", "mailto:")):
        return path
    target = (ROOT / path).resolve()
    return Path(os.path.relpath(target, from_file.parent.resolve())).as_posix()


def md_table(rows: list[dict], headers: str = HEADERS_ZH, from_file: Path | None = None, lang: str | None = None) -> str:
    from_file = from_file or OUT_README
    if lang is None:
        lang = "en" if headers == HEADERS_EN else "zh-CN"
    ui = TABLE_UI[lang]
    lines = [
        headers,
        "|---:|---|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        src = f"[{ui['source']}]({r['source_url']})" if r.get("source_url") else "—"
        if r.get("local_detail"):
            external = str(r["local_detail"]).startswith(("http://", "https://"))
            label = ui["origin"] if external else ui["case"]
            media = f"[{label}]({repo_href(r['local_detail'], from_file)})"
            if is_public_asset(r.get("local_preview") or "", root=ROOT):
                media += f" · [{ui['file']}]({repo_href(r['local_preview'], from_file)})"
            if is_public_asset(r.get("video") or "", root=ROOT):
                media += f" · [Video]({repo_href(r['video'], from_file)})"
        elif r.get("source_url"):
            media = f"[{ui['source']}]({r['source_url']})"
        else:
            media = "—"
        status = r.get("prompt_status") or "空"
        if status == "source_only":
            prompt_label = ui["published"]
        elif status == "aggregator_only":
            prompt_label = ui["agg"]
        elif status == "reconstructed":
            prompt_label = {"en": "Reconstructed", "zh-CN": "重建提示词", "zh-TW": "重建提示詞", "ja": "再構成プロンプト"}[lang]
        elif status == "有面向 2.6 的提示词":
            prompt_label = {"en": "Prompt targeting 2.6", "zh-CN": "面向 2.6 的提示词", "zh-TW": "面向 2.6 的提示詞", "ja": "2.6 向けプロンプト"}[lang]
        elif status == "空":
            prompt_label = ui["empty"]
        elif status == "短/部分":
            prompt_label = ui["partial"]
        elif status.startswith("有原文"):
            prompt_label = ui["original"]
        else:
            prompt_label = cell(status)
        prompt = (
            f"[{prompt_label}]({repo_href(r['local_prompt'], from_file)})"
            if r.get("local_prompt") else (f"[{prompt_label}]({r['prompt_url']})" if r.get("prompt_url") else prompt_label)
        )
        if translation_link(r, lang):
            label = {"en": "Read translation + original", "zh-CN": "译文与原文", "zh-TW": "譯文與原文", "ja": "翻訳と原文"}[lang]
            prompt += f" · [{label}]({repo_href(r['translation_page'], from_file)}#{lang.lower()})"
        lines.append(
            "| {i} | {author} | {title} | {src} | {media} | {prompt} | {model} | {pipe} | {verify} | {lic} |".format(
                i=i,
                author=cell(r.get("author")),
                title="`{id}` {title}".format(
                    id=r["id"],
                    title=cell(localized(r, "title", lang) or r["id"], 60),
                ),
                src=src,
                media=media,
                prompt=prompt,
                model=cell(localized(r, "model_claim", lang), 40),
                pipe=cell(localized(r, "pipeline", lang), 36),
                verify=cell(localized(r, "verify", lang), 36),
                lic=cell(({"en": "Source link only", "zh-CN": "仅来源链接", "zh-TW": "僅來源連結", "ja": "出典リンクのみ"}[lang] if r.get("license_label") == "Source link only" else r.get("license_label")) or ui["unknown"]),
            )
        )
    return "\n".join(lines)


def apply_case_images(rows: list[dict]) -> None:
    payload = json.loads(CASE_IMAGES.read_text(encoding="utf-8")) if CASE_IMAGES.is_file() else {"cases": []}
    by_id = {item["id"]: item for item in payload.get("cases") or []}
    for rec in rows:
        img = by_id.get(rec["id"]) or {}
        rec["image_url"] = img.get("image_url") or ""
        rec["image_source"] = img.get("image_source") or rec.get("source_url") or ""
        rec["image_credit"] = img.get("image_credit") or rec.get("author") or ""
        rec["thumb"] = (img.get("thumb") or "") if is_public_asset(img.get("thumb") or "", root=ROOT) else ""
        rec["thumb_public_allowed"] = bool(rec["thumb"])
        rec["image_download"] = img.get("download") or "missing"
        rec["image_note"] = img.get("note") or ""
        if img.get("date"):
            rec["date"] = img["date"]
        rec["work_type"] = work_type_of(rec)


def apply_case_videos(rows: list[dict]) -> None:
    """Attach a local video path only when data/case-videos.json records one."""
    payload = json.loads(CASE_VIDEOS.read_text(encoding="utf-8")) if CASE_VIDEOS.is_file() else {"cases": []}
    by_id = {item["id"]: item for item in payload.get("cases") or []}
    for rec in rows:
        item = by_id.get(rec["id"]) or {}
        rel = str(item.get("video") or "")
        if is_public_asset(rel, root=ROOT):
            rec["video"] = rel
        else:
            rec["video"] = ""
        rec["video_public_allowed"] = bool(rec["video"])


def write_missing_videos(catalog_rows: list[dict]) -> None:
    payload = json.loads(CASE_VIDEOS.read_text(encoding="utf-8")) if CASE_VIDEOS.is_file() else {"cases": []}
    known = {rec["id"] for rec in catalog_rows}
    failed = [
        item for item in payload.get("cases") or []
        if item.get("id") in known and item.get("status") == "failed"
    ]
    failed.sort(key=lambda item: item.get("id") or "")
    lines = [
        "# Cases where the video download failed",
        "",
        "Scope: collected cases whose source was treated as a downloadable video (X post, direct MP4, or yt-dlp). Cases with no video on the source are not listed here.",
        "",
        "Public copies require an exact-asset permission record; attribution alone is not permission. See [MEDIA_RIGHTS.md](../MEDIA_RIGHTS.md). A rights holder can ask for removal.",
        "",
        f"Failed: **{len(failed)}**.",
        "",
    ]
    if not failed:
        lines.append("None in this pass.")
    for item in failed:
        lines.extend([
            f"## `{item['id']}`",
            "",
            f"- Source: {item.get('source_url') or '—'}",
            f"- Reason: {item.get('reason') or 'download failed'}",
            "",
        ])
    OUT_MISSING_VIDEOS.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_showcase(catalog: dict) -> None:
    rows = main_case_rows(catalog)
    records = []
    for rec in rows:
        records.append(
            {
                "id": rec["id"],
                "title": rec.get("title") or "",
                "model_family": rec.get("model_family") or "",
                "model_version": rec.get("model_version") or "",
                "work_type": rec.get("work_type") or "",
                "date": rec.get("date") or "",
                "author": rec.get("author") or "",
                "source_url": rec.get("source_url") or "",
                "image_url": rec.get("image_url") or "",
                "image_source": rec.get("image_source") or "",
                "image_credit": rec.get("image_credit") or "",
                "thumb": rec.get("thumb") or "",
                "thumb_public_allowed": rec.get("thumb_public_allowed") is True,
                "video": rec.get("video") or "",
                "video_public_allowed": rec.get("video_public_allowed") is True,
            }
        )
    OUT_INDEX_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_INDEX_JSON.write_text(
        json.dumps(
            {
                "meta": {
                    "updated": catalog["meta"]["updated"],
                    "count": len(records),
                    "scope": "main collected cases",
                },
                "cases": records,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    def one_table(items: list[dict]) -> str:
        lines = [
            "| 缩略图 | 标题 | 模型家族 | 版本 | 作品类型 | 日期 | 作者 | 来源 | 视频 |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
        for rec in items:
            thumb = f'<img src="../{rec["thumb"]}" alt="" width="120">' if rec.get("thumb") else "—"
            title = cell(rec.get("title") or rec["id"], 72)
            fam = FAMILY_TITLE.get(rec.get("model_family") or "", rec.get("model_family") or "")
            ver = VERSION_LABEL.get(rec.get("model_version") or "", rec.get("model_version") or "")
            kind = TYPE_INDEX_LABEL.get(rec.get("work_type") or "", rec.get("work_type") or "")
            date = rec.get("date") or "—"
            author = cell(rec.get("image_credit") or rec.get("author") or "")
            src = f"[来源]({rec['source_url']})" if rec.get("source_url") else "—"
            video_rel = rec.get("video") or ""
            if video_rel.startswith("docs/"):
                video_rel = video_rel[len("docs/"):]
            video = f"[Video]({video_rel})" if video_rel else "—"
            lines.append(
                f"| {thumb} | `{rec['id']}` {title} | {fam} | {ver} | {kind} | {date} | {author} | {src} | {video} |"
            )
        return "\n".join(lines)

    type_lines = []
    for key in TYPE_ORDER:
        ids = [rec["id"] for rec in records if rec.get("work_type") == key]
        type_lines.append(f'<a id="{key}"></a>')
        type_lines.append(f"### {TYPE_INDEX_LABEL[key]} ({len(ids)})")
        for rec in records:
            if rec["id"] in ids:
                type_lines.append(f"- [{cell(rec['title'])}](translations/{rec['id']}.md#zh-cn) · {FAMILY_TITLE[rec['model_family']]}")
        if not ids:
            type_lines.append("暂无此标签案例 / No cases with this tag.")
        type_lines.append("")
    OUT_INDEX_MD.write_text(
        "\n".join(
            [
                "# Showcase index / 案例总表",
                "",
                "一行一条主表案例。缩略图链回原帖，作者列是署名。代码许可证不覆盖这些图，见 [MEDIA_RIGHTS.md](../MEDIA_RIGHTS.md)。",
                "",
                f"共 **{len(records)}** 条。排序是模型家族，家族里最新一代在前。",
                "",
                "## 按作品类型检索",
                "",
                *type_lines,
                "",
                "## 全部案例",
                "",
                one_table(records),
                "",
            ]
        ),
        encoding="utf-8",
    )
    missing = [rec for rec in rows if not rec.get("image_url")]
    missing_lines = [
        "# 没有抓到代表图的案例",
        "",
        "范围是主表案例。下面只列没有原图直链的条目。没有编造图片或链接。",
        "",
        f"主表 {len(rows)} 条，没有代表图 {len(missing)} 条。",
        "",
    ]
    if not missing:
        missing_lines.append("这次没有。")
    for rec in missing:
        missing_lines.extend(
            [
                f"## `{rec['id']}`",
                "",
                f"- 标题：{rec.get('title') or ''}",
                f"- 作者：{rec.get('author') or ''}",
                f"- 来源：{rec.get('source_url') or '—'}",
                f"- 尝试：{rec.get('image_note') or '来源页没有 og:image、帖子图片或可对应的 demo 图。'}",
                "",
            ]
        )
    OUT_MISSING.write_text("\n".join(missing_lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    x = json.loads(X_SRC.read_text(encoding="utf-8"))
    web = json.loads(WEB_SRC.read_text(encoding="utf-8"))
    ideas = json.loads(IDEAS.read_text(encoding="utf-8"))
    gallery = json.loads(GALLERY.read_text(encoding="utf-8"))
    by_idea = {i["id"]: i for i in ideas}

    collected_x = [from_x(c, BUCKET_MAIN) for c in x["author_claim_media_meta_checked"]]
    for rec in collected_x:
        if rec["id"] == "x-thinkszyg-paperboat-verify":
            rec["title"] += "（与 Ravivit 纸船同题材，不另计独立 GIF 成功）"
        if rec["id"] == "x-abc123-static-to-gif":
            rec["title"] += "（与大肥鱼同模板族，仍单列原帖）"
        if rec["id"] == "x-okan-aitool-wave-laugh":
            rec["title"] += "（与 Krouxzz 挥手同类动作，不合并删帖）"
        if rec["id"] == "x-ihayato-markup-gif":
            rec["title"] += "（markup + GIF；与 mirai 规格测不同帖）"
    pending = [from_x(c, BUCKET_PENDING) for c in x.get("pending_verification") or []]
    prompt_only = [from_x(c, BUCKET_PROMPT_ONLY) for c in x.get("prompt_only") or []]
    excluded_x = []
    for c in x.get("duplicate_or_rejected") or []:
        excluded_x.append(
            row(
                id=c["id"],
                bucket=BUCKET_EXCLUDED,
                title=c.get("reason") or c.get("notes") or c["id"],
                author=str((c.get("author") or {}).get("username") or c.get("id")),
                source_url=c.get("post_url") or "",
                media_url="",
                media_kind="none",
                prompt_status="—",
                model_claim="不入库",
                pipeline="重复/不合格",
                verify="探子剔除",
                play=c.get("reason") or "",
                license_notes="不收录",
            )
        )

    web_confirmed = [from_web(c) for c in web.get("confirmed_entries") or []]
    web_cand = []
    for c in (web.get("candidates") or []) + (web.get("excluded") or []):
        web_cand.append(
            row(
                id=c.get("id") or c.get("url") or "web-cand",
                bucket=BUCKET_APPENDIX,
                title=c.get("playbook") or c.get("note") or c.get("id") or "web candidate",
                author=c.get("author") or "web",
                source_url=c.get("source_url") or c.get("url") or "",
                media_url=c.get("media_url") or "",
                media_kind=c.get("media_type") or "unknown",
                prompt_status=c.get("prompt_status") or prompt_flag(c.get("prompt") or ""),
                model_claim=c.get("model_claim") or c.get("conclusion") or "候选/排除",
                pipeline=c.get("pipeline") or "不混入已收集主表",
                verify=c.get("conclusion") or c.get("vs_baseline") or "候选/排除",
                play=c.get("playbook") or "",
                license_notes=c.get("license_conclusion") or "仅外链",
                extra={key: c[key] for key in ("prompt_url", "evidence_url", "media_download_status", "source_reported", "notes", "measured_media", "media_urls", "post_urls", "evidence_date") if c.get(key)},
            )
        )

    inrepo = []
    for iid, title, author, url, media, kind, prompt, pipeline in (
        (
            "krouxzz-wave-ref",
            "角色挥手循环",
            "@Krouxzz",
            "https://x.com/Krouxzz/status/2118283796181053637",
            "https://video.twimg.com/tweet_video/HWWnk8IXsAE0aXq.mp4",
            "mp4",
            "有原文",
            "作者称 looping GIF · X 附件实际 MP4（已本地归档）",
        ),
        (
            "luffy-x-article",
            "路飞 X Article：榨干 Image 2.6 的 10 个神级玩法（多玩法一组）",
            "@0xluffy_eth",
            "https://x.com/i/article/2118269816821919744",
            "",
            "none",
            "有原文（中文逐字）",
            "社区长文；原文提示词已本地全文归档；库存无附件 URL，文章接口尝试未取得，不能断言原长文绝无媒体",
        ),
    ):
        inrepo.append(
            row(
                id=iid,
                bucket=BUCKET_INREPO,
                title=title,
                author=author,
                source_url=url,
                media_url=media,
                media_kind=kind,
                prompt_status=prompt,
                model_claim="作者声明 2.6",
                pipeline=pipeline,
                verify="已在库 · 作者声明 · 未观看附件"
                if kind == "mp4"
                else "已在库 · 提示词逐字 · 库存无附件 URL · 接口未取得 · 不能断言原长文绝无媒体",
                play=title,
                license_notes="许可未知 · 本地归档（非作者授权、非 CC0）",
            )
        )

    game_main = []
    game_app = []
    for g in ideas:
        if not g.get("game_sequence"):
            continue
        status = g.get("image26_status") or ""
        rec = row(
            id=g["id"],
            bucket=BUCKET_GAME if status == "author_claim_unverified" else BUCKET_APPENDIX,
            title=g["title_zh"],
            author=g.get("source_label") or "",
            source_url=g.get("source_url") or "",
            media_url=g.get("media_url") or g.get("demo_site_url") or "",
            media_kind=g.get("media_kind") or ("mp4" if g.get("output_kind") == "gif" else g.get("output_kind") or "unknown"),
            prompt_status={"verbatim": "有原文", "empty": "空", "reconstructed": "本站改写"}.get(g.get("prompt_status"), g.get("prompt_status") or "空"),
            model_claim=g.get("model") or "",
            pipeline=g.get("pipeline") or "",
            verify=status,
            play=g.get("description_zh") or "",
            license_notes="无明确再分发授权 · 仅外链",
            extra={
                "prompt_audience": g.get("prompt_audience"),
                "production_notes": g.get("production_notes"),
                "original_prompt": g.get("prompt") or "",
            },
        )
        if status == "author_claim_unverified":
            rec["verify"] = "作者声明 2.6 · 非官方验证 · 未观看"
            game_main.append(rec)
        else:
            rec["verify"] = {
                "not_26": "GPT Image 2.5 · 不是 2.6",
                "multimodel_postprocess": "多模型后处理 · 不是纯 2.6",
                "promo_claim_unwatched": "宣传方宣称 · 未观看",
                "failure_sample": "失败样本 · 不计成功",
            }.get(status, status)
            game_app.append(rec)

    seeds = []
    for g in gallery:
        if g.get("rights") == "repo_seed":
            seeds.append(
                row(
                    id=g["id"],
                    bucket=BUCKET_SEED,
                    title=g.get("title") or g["id"],
                    author="仓库种子（本仓示例，不是社区征集主清单）",
                    source_url=g.get("source_url") or "",
                    media_url=g.get("image") or "",
                    media_kind="gif",
                    prompt_status=g.get("prompt_status") or "reconstructed",
                    model_claim=g.get("model") or "",
                    pipeline="本仓种子 GIF",
                    verify="本地 Pillow 多帧 · 非社区原作者案例",
                    play=g.get("description_zh") or "",
                    license_notes="见 MEDIA_RIGHTS.md · 不能因 MIT 自动商用",
                )
            )

    morphic = []
    for i in ideas:
        if "morphic.com" in str(i.get("source_url") or ""):
            morphic.append(
                row(
                    id=i["id"],
                    bucket=BUCKET_APPENDIX,
                    title=i["title_zh"],
                    author="Morphic",
                    source_url=i.get("source_url") or "",
                    media_url="",
                    media_kind="svg",
                    prompt_status="有面向 2.6 的提示词",
                    model_claim="示例跑在 2.5 / Ideogram · 不是 2.6 成品",
                    pipeline="提示词卡 · SVG 概念封面",
                    verify="示例非 2.6",
                    play=i.get("description_zh") or "",
                    license_notes="概念 SVG 不是模型成品",
                )
            )

    for rec in collected_x + web_confirmed + inrepo + game_main:
        rec["model_family"] = "gpt-image"
        rec["model_version"] = "gpt-image-2.6"

    frontier_raw = json.loads(FRONTIER_SRC.read_text(encoding="utf-8")) if FRONTIER_SRC.exists() else {"cases": []}
    frontier_by_family = {fid: [] for fid, *_ in MODEL_FAMILY_PLACEHOLDERS}
    for item in frontier_raw.get("cases") or []:
        fam = item.get("model_family") or ""
        if fam not in frontier_by_family:
            raise SystemExit(f"unknown model_family in frontier inventory: {fam} ({item.get('id')})")
        frontier_by_family[fam].append(from_frontier(item))
    frontier_all = [rec for fam in frontier_by_family.values() for rec in fam]

    sites_raw = (
        json.loads(COLLECTION_SITES.read_text(encoding="utf-8"))
        if COLLECTION_SITES.exists()
        else {"meta": {}, "by_family": {}}
    )
    collection_sites = {lang: format_collection_sites(sites_raw, lang=lang) for lang, _path in README_LANGS}

    gpt_image_rows = collected_x + web_confirmed + inrepo + game_main
    catalog = {
        "meta": {
            "title": "AI 模型制作案例集 / Awesome AI Model Showcases",
            "title_zh": "AI 模型制作案例集",
            "updated": max(
                web.get("meta", {}).get("updated", "2026-11-06"),
                frontier_raw.get("meta", {}).get("updated", "2026-11-06"),
                sites_raw.get("meta", {}).get("updated", "2026-11-06"),
            ),
            "coverage": "首页按前沿模型家族分栏。GPT Image 2.6 GIF 归档在子项目 collections/gpt-image-gifs/，不计入首页合计。Claude / Gemini / GPT-6.2 Sol / Grok / Qwen / DeepSeek 收录真实公开案例；来源视频在署名并链回原帖的前提下做本地副本。GPT-6.2 Sol 分栏名按主人确认；OpenAI 公开页截至核验日仍列 GPT-6.1 Sol。不是穷尽全网。",
            "not_exhaustive": True,
            "official_verified_26_game": 0,
            "structure": "model_family",
            "counts": {},
            "unverified_or_missing": frontier_raw.get("meta", {}).get("unverified_or_missing") or [],
            "gpt_sol_status": {
                "catalog_label": "GPT-6.2 Sol",
                "openai_public_docs_label": "GPT-6.1 Sol",
                "checked": "2026-11-11",
                "openai_intro_url": "https://openai.com/index/introducing-gpt-6-1-sol/",
                "openai_models_url": "https://platform.openai.com/docs/models",
            },
            "showcase_collection_sites": sites_raw.get("by_family") or {},
        },
        "collected_x_author_claim": collected_x,
        "collected_web_gif": web_confirmed,
        "collected_already_in_repo": inrepo,
        "collected_game_author_claim": game_main,
        "collected_claude": frontier_by_family["claude"],
        "collected_gemini": frontier_by_family["gemini"],
        "collected_gpt_code": frontier_by_family["gpt-code"],
        "collected_grok": frontier_by_family["grok"],
        "collected_qwen": frontier_by_family["qwen"],
        "collected_deepseek": frontier_by_family["deepseek"],
        "collected_by_family": {
            "gpt-image": gpt_image_rows,
            **frontier_by_family,
        },
        "pending": pending,
        "prompt_only": prompt_only,
        "excluded": excluded_x,
        "appendix": game_app + web_cand + morphic,
        "repo_seeds": seeds,
    }
    frontier_count = len(frontier_all)
    gpt_count = len(gpt_image_rows)
    catalog["meta"]["counts"] = {
        "x_author_claim_25": len(collected_x),
        "web_gif_12": len(web_confirmed),
        "already_in_repo": len(inrepo),
        "game_author_claim": len(game_main),
        "pending": len(pending),
        "prompt_only": len(prompt_only),
        "excluded": len(excluded_x),
        "appendix": len(catalog["appendix"]),
        "repo_seeds": len(seeds),
        "gpt_image": gpt_count,
        "gpt_image_subproject": "collections/gpt-image-gifs/",
        "frontier_sourced": frontier_count,
        "main_collected": frontier_count,
        **{f"family_{fid}": len(frontier_by_family[fid]) for fid, *_ in MODEL_FAMILY_PLACEHOLDERS},
    }

    for group in (
        collected_x,
        web_confirmed,
        inrepo,
        game_main,
        frontier_all,
        pending,
        prompt_only,
        excluded_x,
        catalog["appendix"],
        seeds,
    ):
        attach_local(group)

    homepage_and_archive = collected_x + web_confirmed + inrepo + game_main + frontier_all
    apply_case_images(homepage_and_archive)
    apply_case_videos(homepage_and_archive)
    write_missing_videos(homepage_and_archive)
    catalog["meta"]["counts"]["with_image"] = sum(
        1 for rec in collected_x + web_confirmed + inrepo + game_main + frontier_all if rec.get("image_url")
    )
    catalog["meta"]["counts"]["with_thumb"] = sum(
        1 for rec in collected_x + web_confirmed + inrepo + game_main + frontier_all if rec.get("thumb")
    )

    attach_translations(catalog)
    write_translated_cases(catalog)

    OUT_JSON.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JS.write_text(
        "/* AUTO-GENERATED by tools/write_community_catalog.py */\nwindow.COMMUNITY_CASES = "
        + json.dumps(catalog, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    write_showcase(catalog)

    c = catalog["meta"]["counts"]

    def tables_for(lang: str, from_file: Path, *, version_sections: bool = False) -> str:
        headers = HEADERS_FOR[lang]
        note = sol_note(catalog, lang)
        empty = {
            "en": "_No sourced cases yet for {versions}._\n",
            "zh-CN": "_此栏暂无已核实案例（{versions}）。_\n",
            "zh-TW": "_此欄暫無已核實案例（{versions}）。_\n",
            "ja": "_この版には、まだ出典付きの事例がない（{versions}）。_\n",
        }[lang]
        appendix = {
            "en": [
                f"## Appendix A — pending ({len(pending)})",
                "## Appendix B — prompt-only / rejected",
                "## Appendix C — not mixed into main success: 2.5 / promo / multimodel / failure / non-X candidates / Morphic",
                "## Appendix D — repository-seed GIFs (local examples, not the community collection)",
            ],
            "zh-CN": [
                f"## 附表 A · 待核（{len(pending)}）",
                "## 附表 B · 纯 prompt / 剔除",
                "## 附表 C · 不混入主表成功：2.5 / 宣传 / 多模型 / 失败 / 非X候选 / Morphic",
                "## 附表 D · 仓库种子 GIF（本仓示例，不是社区征集主清单）",
            ],
            "zh-TW": [
                f"## 附表 A · 待核（{len(pending)}）",
                "## 附表 B · 純 prompt / 剔除",
                "## 附表 C · 不混入主表成功：2.5 / 宣傳 / 多模型 / 失敗 / 非X候選 / Morphic",
                "## 附表 D · 倉庫種子 GIF（本倉示例，不是社群徵集主清單）",
            ],
            "ja": [
                f"## 付録 A — 未確認（{len(pending)}）",
                "## 付録 B — プロンプトのみ / 不採用",
                "## 付録 C — 主表の成功に混ぜない：2.5 / 宣伝 / 複数モデル / 失敗 / X 以外の候補 / Morphic",
                "## 付録 D — リポジトリの種 GIF（ローカル例。コミュニティ収集の本体ではない）",
            ],
        }[lang]
        name_of = {"en": 1, "zh-CN": 2, "zh-TW": 2, "ja": 1}[lang]
        parts: list[str] = []
        for fid, en, zh, versions in MODEL_FAMILY_PLACEHOLDERS:
            rows = frontier_by_family[fid]
            name = (en, zh)[name_of - 1] if name_of == 2 else en
            if lang == "ja":
                parts.append(f"## Family · {en} — {versions} ({len(rows)})")
            elif lang == "zh-TW":
                parts.append(f"## 家族 · {zh} — {versions}（{len(rows)}）")
            elif lang == "zh-CN":
                parts.append(f"## 家族 · {zh} — {versions}（{len(rows)}）")
            else:
                parts.append(f"## Family · {name} — {versions} ({len(rows)})")
            if version_sections:
                parts.insert(len(parts) - 1, f'<a id="{fid}"></a>')
            if fid == "gpt-code":
                parts.append(f"> {note}")
            if version_sections:
                for version in VERSION_ORDER[fid]:
                    version_rows = _date_desc([r for r in rows if r.get("model_version") == version])
                    if not version_rows and version != "claude-mythos-5.2":
                        continue
                    parts.extend([f'<a id="{version_anchor(version)}"></a>', f"### {VERSION_LABEL[version]} ({len(version_rows)})"])
                    parts.append(md_table(version_rows, headers, from_file=from_file, lang=lang) if version_rows else empty.format(versions=VERSION_LABEL[version]))
            else:
                parts.append(md_table(rows, headers, from_file=from_file, lang=lang) if rows else empty.format(versions=versions))
        appendix_rows = (pending, prompt_only + excluded_x, catalog["appendix"], seeds)
        for heading, rows in zip(appendix, appendix_rows):
            parts.append(heading)
            parts.append(md_table(rows, headers, from_file=from_file, lang=lang))
        return "\n\n".join(parts)

    OUT_MD.write_text(
        "\n".join(
            [
                "# Community case catalog / 社区真实案例总目录",
                "",
                f"> Updated {catalog['meta']['updated']} (Beijing time). Same inventory as README.md, README.zh-CN.md, README.zh-TW.md, and README.ja.md. Organized by model family, then version. Not exhaustive; not official verification.",
                "",
                f"- Homepage total: **{c['main_collected']}** frontier-family cases (GPT Image is not included)",
                f"- Frontier families: Claude {c['family_claude']} · Gemini {c['family_gemini']} · GPT-6.2 Sol {c['family_gpt-code']} · Grok {c['family_grok']} · Qwen {c['family_qwen']} · DeepSeek {c['family_deepseek']}",
                f"- GPT Image 2.6 GIF archive (subproject, not in the homepage total): **{c['gpt_image']}** = X {c['x_author_claim_25']} + web GIF {c['web_gif_12']} + in-repo {c['already_in_repo']} + game author-claim {c['game_author_claim']}. Listing: [collections/gpt-image-gifs](../collections/gpt-image-gifs/README.md)",
                f"- Pending {c['pending']} · prompt-only {c['prompt_only']} · excluded {c['excluded']} · appendix {c['appendix']} · seeds {c['repo_seeds']}",
                "- Officially verified 2.6 game outputs: **0**",
                "",
                "## Showcase collection sites / 展示站资源列表",
                "",
                collection_sites["zh-CN"],
                "",
                tables_for("zh-CN", OUT_MD),
                "",
            ]
        ),
        encoding="utf-8",
    )

    gpt_lines = {
        "en": (
            f"GPT Image 2.6 GIF archive (**{c['gpt_image']}** cases, not in the homepage total): "
            "[collections/gpt-image-gifs](collections/gpt-image-gifs/README.md)."
        ),
        "zh-CN": (
            f"GPT Image 2.6 GIF 归档（**{c['gpt_image']}** 条，不计入首页合计）："
            "[collections/gpt-image-gifs](collections/gpt-image-gifs/README.zh-CN.md)。"
        ),
        "zh-TW": (
            f"GPT Image 2.6 GIF 歸檔（**{c['gpt_image']}** 則，不計入首頁合計）："
            "[collections/gpt-image-gifs](collections/gpt-image-gifs/README.zh-CN.md)。"
        ),
        "ja": (
            f"GPT Image 2.6 の GIF アーカイブ（**{c['gpt_image']}** 件。ホームページの合計には入れない）: "
            "[collections/gpt-image-gifs](collections/gpt-image-gifs/README.md)."
        ),
    }

    def gpt_archive_body(lang: str, path: Path) -> str:
        headers = HEADERS_FOR[lang]
        titles = {
            "en": (
                "# GPT Image 2.6 GIF archive",
                "Subproject of [Awesome AI Model Showcases](../../README.md). These cases are not in the homepage totals.",
                f"**{c['gpt_image']}** cases: X author-claimed {c['x_author_claim_25']} · non-X GIFs {c['web_gif_12']} · in-repo {c['already_in_repo']} · game author-claimed {c['game_author_claim']}.",
                "Case files stay in `docs/cases/<id>/`. This page is the listing.",
            ),
            "zh-CN": (
                "# GPT Image 2.6 GIF 归档",
                "这是 [AI 模型制作案例集](../../README.zh-CN.md) 的子项目。这些案例不计入首页合计。",
                f"共 **{c['gpt_image']}** 条：X 作者声明 {c['x_author_claim_25']} · 非 X GIF {c['web_gif_12']} · 已在库 {c['already_in_repo']} · 游戏作者声明 {c['game_author_claim']}。",
                "案例文件仍在 `docs/cases/<id>/`。本页是目录。",
            ),
        }[lang]
        heads = {
            "en": [
                f"## X author-claimed ({len(collected_x)} groups, not split by attachment)",
                f"## Non-X real GIFs ({len(web_confirmed)})",
                f"## Already-in-repo community longform / posts ({len(inrepo)})",
                f"## Game action sequences — author-claimed ({len(game_main)}, not officially verified)",
            ],
            "zh-CN": [
                f"## X 作者声明（{len(collected_x)} 组，不按附件拆卡）",
                f"## 非 X 真 GIF（{len(web_confirmed)}）",
                f"## 本仓已收录社区长文 / 单帖（{len(inrepo)}）",
                f"## 游戏动作序列 · 作者声明（{len(game_main)}，非官方验证）",
            ],
        }[lang]
        ui = UI[lang]
        parts = list(titles)
        parts.append("")
        parts.append(ui["gif_intro"])
        parts.append(featured_cards(catalog["collected_web_gif"], lang, from_file=path))
        parts.append(ui["cards_note"])
        parts.append("")
        for heading, rows in zip(heads, (collected_x, web_confirmed, inrepo, game_main)):
            parts.append(heading)
            parts.append("")
            parts.append(md_table(rows, headers, from_file=path, lang=lang))
            parts.append("")
        return "\n".join(parts).rstrip() + "\n"

    OUT_GPT_EN.parent.mkdir(parents=True, exist_ok=True)
    OUT_GPT_EN.write_text(gpt_archive_body("en", OUT_GPT_EN), encoding="utf-8")
    OUT_GPT_ZH.write_text(gpt_archive_body("zh-CN", OUT_GPT_ZH), encoding="utf-8")

    catalog_labels = {
        "en": ("Full case catalog", "Back to the guide", "Source-linked cases, not verified model generations. Ordered by family, configured version order, then newest complete source date; missing dates go last. AI translations are not human-reviewed. Third-party rights remain separate from MIT.", "Collection sites"),
        "zh-CN": ("完整案例目录", "返回导览", "有来源案例不等于已验证的模型生成。按家族、既定版本顺序、完整来源日期倒序排列；无完整日期的放在最后。AI 翻译尚未经人工审校，第三方版权与 MIT 分开。", "案例收集站"),
        "zh-TW": ("完整案例目錄", "返回導覽", "有來源案例不等於已驗證的模型生成。依家族、既定版本順序、完整來源日期倒序排列；無完整日期的放在最後。AI 翻譯尚未經人工審校，第三方版權與 MIT 分開。", "案例收集站"),
        "ja": ("全事例目録", "案内に戻る", "出典付き事例は、検証済みのモデル生成を意味しません。ファミリー、既定のバージョン順、完全な出典日付の新しい順に並び、日付のない事例は最後です。AI 翻訳は人による校閲前です。第三者の権利は MIT と別です。", "事例収集サイト"),
    }
    for lang, path in README_LANGS:
        title, back, note, sites_title = catalog_labels[lang]
        catalog_path = ROOT / f"docs/catalog.{lang}.md"
        links = " · ".join(f"[{FAMILY_TITLE[fid]}](#{fid})" for fid in VERSION_ORDER if fid != "gpt-image")
        catalog_path.write_text(
            f"<!-- Generated by tools/write_community_catalog.py; do not edit. -->\n# {title}\n\n"
            f"[{back}](../{path.name}) · [English](catalog.en.md) · [简体中文](catalog.zh-CN.md) · [繁體中文](catalog.zh-TW.md) · [日本語](catalog.ja.md)\n\n"
            f"{note} [MEDIA_RIGHTS.md](../MEDIA_RIGHTS.md)\n\n{links}\n\n"
            + tables_for(lang, catalog_path, version_sections=True)
            + f"\n\n<a id=\"collection-sites\"></a>\n## {sites_title}\n\n" + collection_sites[lang],
            encoding="utf-8",
        )
        path.write_text(
            render_readme(
                lang,
                catalog=catalog,
                gpt_subproject_line=gpt_lines[lang],
            ),
            encoding="utf-8",
        )

    write_site_spotlight()
    write_preview_credits()
    from render_licensed_gallery import write_licensed_gallery
    write_licensed_gallery()

    llms = f"""# Awesome AI Model Showcases

{EN_LEAD}

中文：{ZH_LEAD}。

Independent community project. Organized by model family, then version. Current public inventory, not exhaustive. Author claim ≠ official verification.

## What is this repository?
A sourced catalog of real production cases from the latest large models: animations, HTML and game demos, images, and source-linked videos; only explicitly approved media is embedded. Each record keeps the post, author, prompt-or-empty, model evidence, pipeline, verification, and license boundary. The GPT Image 2.6 GIF archive is a subproject at collections/gpt-image-gifs/ and is not part of the homepage total.

## What is in the current inventory?
Homepage total {c['main_collected']} frontier-family cases: Claude {c['family_claude']}, Gemini {c['family_gemini']}, GPT-6.2 Sol {c['family_gpt-code']}, Grok {c['family_grok']}, Qwen {c['family_qwen']}, DeepSeek {c['family_deepseek']}. GPT Image subproject {c['gpt_image']} (X {c['x_author_claim_25']} + web GIF {c['web_gif_12']} + in-repo {c['already_in_repo']} + game author-claim {c['game_author_claim']}), listed only under collections/gpt-image-gifs/. GPT-6.2 Sol is the owner catalog label; OpenAI public pages still list GPT-6.1 Sol. Claude Mythos 5.2 is named in the inventory and has no separate sourced case. Pending {c['pending']}. Prompt-only {c['prompt_only']}. Excluded {c['excluded']}. Appendix {c['appendix']}. Seeds {c['repo_seeds']}. Officially verified 2.6 game outputs: 0. One JSON source: docs/data/community-cases.json. English, Simplified Chinese, Traditional Chinese, and Japanese READMEs share the homepage inventory. Showcase collection sites: playbooks/research/showcase-collection-sites.json. Related GitHub projects: docs/related-projects.md. Case index: docs/showcase-index.md and data/showcase-index.json. Failed video downloads: docs/missing-videos.md.

## What can I do with it?
Inspect eight separately licensed source works at licensed-gallery.en.html (also zh-CN, zh-TW and ja), with large still images, work-type labels, source and permission links. These supplemental works do not increase the main catalog count.
Browse https://jammyfu.github.io/awesome-ai-model-showcases/?lang=en (EN) or ?lang=zh (中文). Open local media and published prompts or labeled excerpts under docs/cases/<id>/. Follow source licenses and provenance notes. Original URLs are citations. Submit cases. Do not treat SVG concept covers or prompt_adaptation as originals.

## What can it not do?
No Images API at browse time. No paid generation. No blanket author-grant or CC0 claim. No exhaustive-web or official-verification claim. Appendix idea/popular pages are Chinese-first and not a second inventory.

## Which languages are maintained?
English README.md, Simplified Chinese README.zh-CN.md (AI 模型制作案例集), Traditional Chinese README.zh-TW.md, and Japanese README.ja.md. Same inventory and the same case counts. Case titles, methods, verification notes, model evidence and collected prompts have four-language AI translations marked not human-reviewed, with originals preserved. See docs/translation-policy.md and docs/data/translation-coverage.json. The web catalog is English/Simplified Chinese (`?lang=en` / `?lang=zh`); translated-case.html supports all four content languages.

## License boundaries
MIT covers source code only. Third-party media remains license-unknown unless a specific source grant is recorded. Follow per-case attribution; no blanket grant or CC0 claim.

## Canonical URLs
- https://jammyfu.github.io/awesome-ai-model-showcases/?lang=en
- https://jammyfu.github.io/awesome-ai-model-showcases/?lang=zh
- https://github.com/jammyfu/awesome-ai-model-showcases
- docs/data/community-cases.json
- playbooks/community-cases.md
"""
    OUT_LLMS.write_text(llms, encoding="utf-8")
    OUT_LLMS_DOCS.write_text(llms, encoding="utf-8")
    OUT_ABOUT.write_text(json.dumps(GITHUB_ABOUT, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"community catalog: homepage {c['main_collected']} frontier; "
        f"gpt-image subproject {c['gpt_image']} "
        f"(X{c['x_author_claim_25']}+web{c['web_gif_12']}+inrepo{c['already_in_repo']}+game{c['game_author_claim']}); "
        f"pending {c['pending']}; appendix {c['appendix']}"
    )


if __name__ == "__main__":
    main()
