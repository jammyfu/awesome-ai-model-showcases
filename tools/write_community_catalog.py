#!/usr/bin/env python3
"""Build the community-case catalog from scout inventories + in-repo extras.

This is the repo's primary index: collected public cases, not this project's
original remake playbooks.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from readme_presentation import render_readme

ROOT = Path(__file__).resolve().parents[1]
X_SRC = ROOT / "playbooks/research/x-inventory.json"
WEB_SRC = ROOT / "playbooks/research/web-inventory.json"
IDEAS = ROOT / "docs/data/ideas.json"
GALLERY = ROOT / "docs/data/gallery.json"
OUT_JSON = ROOT / "docs/data/community-cases.json"
OUT_JS = ROOT / "docs/data/cases.js"
OUT_MD = ROOT / "playbooks/community-cases.md"
OUT_README = ROOT / "README.md"
OUT_README_ZH = ROOT / "README.zh-CN.md"
OUT_LLMS = ROOT / "llms.txt"
OUT_LLMS_DOCS = ROOT / "docs/llms.txt"
OUT_ABOUT = ROOT / "docs/github-about.json"
LOCAL_MANIFEST = ROOT / "docs/data/local-media-manifest.json"

GITHUB_ABOUT = {
    "description": (
        "Community catalog of real GPT Image GIF cases: original authors, "
        "media, prompts, sources, and pipelines. GPT Image 2.6. English & 中文."
    ),
    "homepage": "https://jammyfu.github.io/awesome-gpt-image-gifs/",
    "topics": [
        "animated-gif",
        "awesome-list",
        "chinese",
        "game-assets",
        "gif",
        "gpt-image",
        "gpt-image-2-6",
        "image-generation",
        "prompt-engineering",
        "sprite-sheet",
    ],
}

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


HEADERS_ZH = "| # | 作者 | 玩法 | 原帖 | 媒体 | prompt | 模型依据 | 管线 | 验证 | 许可 |"
HEADERS_EN = "| # | Author | Play | Post | Media | prompt | Model | Pipeline | Verification | License |"


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
    if gif.is_file():
        return str(gif.relative_to(ROOT)).replace("\\", "/")
    media = r.get("media_url") or ""
    if media and not media.startswith(("http://", "https://")):
        for cand in (ROOT / media, ROOT / "docs" / media):
            if cand.is_file():
                return str(cand.relative_to(ROOT)).replace("\\", "/")
    return r.get("source_url") or ""


def attach_local(rows: list[dict]) -> None:
    """Only emit local archive links when docs/cases/<id>/ actually exists."""
    man: dict = {}
    if LOCAL_MANIFEST.exists():
        man = json.loads(LOCAL_MANIFEST.read_text(encoding="utf-8"))
    by: dict[str, list] = {}
    for f in man.get("files") or []:
        if f.get("ok"):
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


def md_table(rows: list[dict], headers: str = HEADERS_ZH, from_file: Path | None = None) -> str:
    from_file = from_file or OUT_README
    lines = [
        headers,
        "|---:|---|---|---|---|---|---|---|---|---|",
    ]
    english = headers == HEADERS_EN
    source_label = "Source" if english else "出处"
    file_label = "File" if english else "文件"
    for i, r in enumerate(rows, 1):
        src = f"[{source_label}]({r['source_url']})" if r.get("source_url") else "—"
        if r.get("local_detail"):
            external = str(r["local_detail"]).startswith(("http://", "https://"))
            label = ("Source" if external else "Case") if english else ("来源" if external else "案例")
            media = f"[{label}]({repo_href(r['local_detail'], from_file)})"
            if r.get("local_preview"):
                media += f" · [{file_label}]({repo_href(r['local_preview'], from_file)})"
        elif r.get("source_url") and r.get("bucket") not in {BUCKET_MAIN, BUCKET_WEB, BUCKET_INREPO, BUCKET_GAME}:
            if r.get("media_url"):
                media = f"[{r['media_kind'] or '来源'}]({r['media_url']})"
            else:
                media = f"[{source_label}]({r['source_url']})"
        elif r.get("media_url"):
            media = f"[{r['media_kind']}]({r['media_url']})"
        else:
            media = "—"
        status = r.get("prompt_status") or "空"
        if status == "source_only":
            prompt_label = "Published at source" if english else "原文见来源"
        elif status == "aggregator_only":
            prompt_label = "Aggregator only" if english else "仅聚合页"
        elif status == "空":
            prompt_label = "Unpublished" if english else "未公开"
        elif status == "短/部分":
            prompt_label = "Short / partial" if english else "短 / 部分"
        elif status.startswith("有原文"):
            prompt_label = "Original" if english else "原文"
        else:
            prompt_label = cell(status)
        prompt = (
            f"[{prompt_label}]({repo_href(r['local_prompt'], from_file)})"
            if r.get("local_prompt") else (f"[{prompt_label}]({r['prompt_url']})" if r.get("prompt_url") else prompt_label)
        )
        lines.append(
            "| {i} | {author} | {title} | {src} | {media} | {prompt} | {model} | {pipe} | {verify} | {lic} |".format(
                i=i,
                author=cell(r.get("author")),
                title="`{id}` {title}".format(
                    id=r["id"],
                    title=cell(r.get("title") or r["id"], 60),
                ),
                src=src,
                media=media,
                prompt=prompt,
                model=cell(r.get("model_claim"), 40),
                pipe=cell(r.get("pipeline"), 36),
                verify=cell(r.get("verify"), 36),
                lic=cell(r.get("license_label") or ("Unknown" if english else "许可未知")),
            )
        )
    return "\n".join(lines)


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

    catalog = {
        "meta": {
            "title": "GPT Image 2.6 社区真实案例收集库",
            "updated": web.get("meta", {}).get("updated", "2026-11-06"),
            "coverage": "当前公开搜集核实清单完整入库，不是穷尽全网。主表媒体已本地归档，原 URL 仅作出处。许可与视觉检查按条目标注；帧序列检查不等于完整播放或生成复现。",
            "not_exhaustive": True,
            "official_verified_26_game": 0,
            "counts": {},
        },
        "collected_x_author_claim": collected_x,
        "collected_web_gif": web_confirmed,
        "collected_already_in_repo": inrepo,
        "collected_game_author_claim": game_main,
        "pending": pending,
        "prompt_only": prompt_only,
        "excluded": excluded_x,
        "appendix": game_app + web_cand + morphic,
        "repo_seeds": seeds,
    }
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
        "main_collected": len(collected_x) + len(web_confirmed) + len(inrepo) + len(game_main),
    }

    for group in (
        collected_x,
        web_confirmed,
        inrepo,
        game_main,
        pending,
        prompt_only,
        excluded_x,
        catalog["appendix"],
        seeds,
    ):
        attach_local(group)

    OUT_JSON.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JS.write_text(
        "/* AUTO-GENERATED by tools/write_community_catalog.py */\nwindow.COMMUNITY_CASES = "
        + json.dumps(catalog, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )

    c = catalog["meta"]["counts"]

    def tables_zh(from_file: Path) -> str:
        return "\n\n".join(
            [
                f"## 1. X 作者声明 2.6（{len(collected_x)} 组，不按附件拆卡）",
                md_table(collected_x, from_file=from_file),
                f"## 2. 非 X 真 GIF（{len(web_confirmed)}）",
                md_table(web_confirmed, from_file=from_file),
                f"## 3. 本仓已收录的社区长文 / 单帖（{len(inrepo)}）",
                md_table(inrepo, from_file=from_file),
                f"## 4. 游戏动作序列 · 作者声明（{len(game_main)}，非官方验证）",
                md_table(game_main, from_file=from_file),
                f"## 附表 A · 待核（{len(pending)}）",
                md_table(pending, from_file=from_file),
                "## 附表 B · 纯 prompt / 剔除",
                md_table(prompt_only + excluded_x, from_file=from_file),
                "## 附表 C · 不混入 2.6 成功：2.5 / 宣传 / 多模型 / 失败 / 非X候选 / Morphic",
                md_table(catalog["appendix"], from_file=from_file),
                "## 附表 D · 仓库种子 GIF（本仓示例，不是社区征集主清单）",
                md_table(seeds, from_file=from_file),
            ]
        )

    def tables_en(from_file: Path) -> str:
        return "\n\n".join(
            [
                f"## 1. X author-claimed 2.6 ({len(collected_x)} groups, not split by attachment)",
                md_table(collected_x, HEADERS_EN, from_file=from_file),
                f"## 2. Non-X real GIFs ({len(web_confirmed)})",
                md_table(web_confirmed, HEADERS_EN, from_file=from_file),
                f"## 3. Already-in-repo community longform / posts ({len(inrepo)})",
                md_table(inrepo, HEADERS_EN, from_file=from_file),
                f"## 4. Game action sequences — author-claimed ({len(game_main)}, not officially verified)",
                md_table(game_main, HEADERS_EN, from_file=from_file),
                f"## Appendix A — pending ({len(pending)})",
                md_table(pending, HEADERS_EN, from_file=from_file),
                "## Appendix B — prompt-only / rejected",
                md_table(prompt_only + excluded_x, HEADERS_EN, from_file=from_file),
                "## Appendix C — not mixed into 2.6 success: 2.5 / promo / multimodel / failure / non-X candidates / Morphic",
                md_table(catalog["appendix"], HEADERS_EN, from_file=from_file),
                "## Appendix D — repository-seed GIFs (local examples, not the community collection)",
                md_table(seeds, HEADERS_EN, from_file=from_file),
            ]
        )

    OUT_MD.write_text(
        "\n".join(
            [
                "# Community case catalog / 社区真实案例总目录",
                "",
                f"> Updated {catalog['meta']['updated']} (Beijing time). Same inventory as README.md and README.zh-CN.md. Not exhaustive; not official verification.",
                "",
                f"- Main collected: **{c['main_collected']}** (X {c['x_author_claim_25']} + web GIF {c['web_gif_12']} + in-repo {c['already_in_repo']} + game author-claim {c['game_author_claim']})",
                f"- Pending {c['pending']} · prompt-only {c['prompt_only']} · excluded {c['excluded']} · appendix {c['appendix']} · seeds {c['repo_seeds']}",
                "- Officially verified 2.6 game outputs: **0**",
                "",
                tables_zh(OUT_MD),
                "",
            ]
        ),
        encoding="utf-8",
    )

    count_table = f"""| Bucket | Count | Outside the main catalog | Count |
|---|---:|---|---:|
| X author-claimed 2.6 | **{c['x_author_claim_25']}** | Pending | {c['pending']} |
| Non-X real GIFs | **{c['web_gif_12']}** | Prompt-only | {c['prompt_only']} |
| In-repo community longform/posts | **{c['already_in_repo']}** | Duplicate/rejected | {c['excluded']} |
| Game author-claimed | **{c['game_author_claim']}** | 2.5 / promo / multimodel / failure / Morphic / non-X candidates | {c['appendix']} |
| **Main total** | **{c['main_collected']}** | Repository seeds (local examples) | {c['repo_seeds']} |"""

    count_table_zh = f"""| 主表 | 数 | 附表（不计入主表） | 数 |
|---|---:|---|---:|
| X 作者声明 2.6 | **{c['x_author_claim_25']}** | 待核 | {c['pending']} |
| 非 X 真 GIF | **{c['web_gif_12']}** | 纯 prompt | {c['prompt_only']} |
| 已在库社区长文/单帖 | **{c['already_in_repo']}** | 重复/不合格 | {c['excluded']} |
| 游戏 · 作者声明 | **{c['game_author_claim']}** | 2.5 / 宣传 / 多模型 / 失败 / Morphic / 非X候选 | {c['appendix']} |
| **主表合计** | **{c['main_collected']}** | 仓库种子（本仓示例） | {c['repo_seeds']} |"""

    OUT_README.write_text(
        render_readme("en", catalog=catalog, count_table=count_table, tables=tables_en(OUT_README)),
        encoding="utf-8",
    )
    OUT_README_ZH.write_text(
        render_readme("zh-CN", catalog=catalog, count_table=count_table_zh, tables=tables_zh(OUT_README_ZH)),
        encoding="utf-8",
    )

    llms = f"""# Awesome GPT Image GIFs

Awesome GPT Image GIFs collects real GPT Image GIF cases from the public web: original authors, original media, public prompts, sources, and production pipelines. It is a community catalog of GPT Image 2.6 (ChatGPT Images 2.6 / gpt-image-2.6-sunburst / gpt-image-2.6-flare) work, not this repository's original playbook showcase.

中文：收集全网 GPT Image GIF 真实案例、原作者、原媒体、提示词、出处与制作流程；不是本站原创方案集。

Independent community project. Current public inventory, not exhaustive. Author claim ≠ official verification.

## What is this repository?
A sourced catalog of original-author GPT Image 2.6 cases (post, real GIF/MP4, prompt-or-empty, model evidence, pipeline, verification, license boundary).

## What is in the current inventory?
Main collected {c['main_collected']} = X {c['x_author_claim_25']} + web GIF {c['web_gif_12']} + in-repo {c['already_in_repo']} + game author-claim {c['game_author_claim']}. Pending {c['pending']}. Prompt-only {c['prompt_only']}. Excluded {c['excluded']}. Appendix {c['appendix']}. Seeds {c['repo_seeds']}. Officially verified 2.6 game outputs: 0. One JSON source: docs/data/community-cases.json. English and Chinese must not disagree.

## What can I do with it?
Browse https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=en (EN) or ?lang=zh (中文). Open local media and published prompts or labeled excerpts under docs/cases/<id>/. Follow source licenses and provenance notes. Original URLs are citations. Submit cases. Do not treat SVG or prompt_adaptation as originals.

## What can it not do?
No Images API at browse time. No paid generation. No blanket author-grant or CC0 claim. No exhaustive-web or official-verification claim. Appendix idea/popular pages are Chinese-first and not a second inventory.

## Which languages are maintained?
English README.md and Simplified Chinese README.zh-CN.md. No other README editions.

## License boundaries
MIT covers source code only. Third-party media remains license-unknown unless a specific source grant is recorded. Follow per-case attribution; no blanket grant or CC0 claim.

## Canonical URLs
- https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=en
- https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=zh
- https://github.com/jammyfu/awesome-gpt-image-gifs
- docs/data/community-cases.json
- playbooks/community-cases.md
"""
    OUT_LLMS.write_text(llms, encoding="utf-8")
    OUT_LLMS_DOCS.write_text(llms, encoding="utf-8")
    OUT_ABOUT.write_text(json.dumps(GITHUB_ABOUT, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"community catalog: main {c['main_collected']} "
        f"(X{c['x_author_claim_25']}+web{c['web_gif_12']}+inrepo{c['already_in_repo']}+game{c['game_author_claim']}); "
        f"pending {c['pending']}; appendix {c['appendix']}"
    )


if __name__ == "__main__":
    main()
