#!/usr/bin/env python3
"""Build the community-case catalog from scout inventories + in-repo extras.

This is the repo's primary index: collected public cases, not this project's
original remake playbooks.
"""
from __future__ import annotations

import json
from pathlib import Path

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
        prompt_status=prompt_flag(item.get("prompt") or ""),
        model_claim=item.get("model_claim") or "页面声称 2.6",
        pipeline="原生 GIF 直链（Pillow 多帧已核）",
        verify="页面模型依据 + GIF 多帧探测 · 未复测生成",
        play=item.get("playbook") or "",
        license_notes=item.get("license_conclusion") or "许可未知 · 本地归档（非作者授权、非 CC0）",
        extra={
            "original_prompt": item.get("prompt") or "",
            "frames": (item.get("media_verify") or {}).get("frames"),
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


def attach_local(rows: list[dict]) -> None:
    if not LOCAL_MANIFEST.exists():
        return
    man = json.loads(LOCAL_MANIFEST.read_text(encoding="utf-8"))
    by: dict[str, list] = {}
    for f in man.get("files") or []:
        if f.get("ok"):
            by.setdefault(f["case_id"], []).append(f)
    for r in rows:
        files = by.get(r["id"]) or []
        r["local_dir"] = f"docs/cases/{r['id']}/"
        r["local_prompt"] = f"docs/cases/{r['id']}/prompt.md"
        r["local_detail"] = f"docs/cases/{r['id']}/README.md"
        r["local_page"] = f"docs/cases/{r['id']}/index.html"
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
        if r.get("bucket") in {BUCKET_MAIN, BUCKET_WEB, BUCKET_INREPO, BUCKET_GAME}:
            r["license_notes"] = "许可未知 · 本地归档（非作者授权、非 CC0）。MIT 只覆盖源码。"


def md_table(rows: list[dict], headers: str = HEADERS_ZH) -> str:
    lines = [
        headers,
        "|---:|---|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        src = f"[出处]({r['source_url']})" if r.get("source_url") else "—"
        if r.get("local_detail"):
            media = f"[本地]({r['local_detail']})"
            if r.get("local_preview"):
                media += f" · [文件]({r['local_preview']})"
        elif r.get("media_url"):
            media = f"[{r['media_kind']}]({r['media_url']})"
        else:
            media = "—"
        prompt = f"[全文]({r['local_prompt']})" if r.get("local_prompt") else cell(r.get("prompt_status") or "空")
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
                lic="许可未知",
            )
        )
    return "\n".join(lines)


def local_embed_block(rows: list[dict]) -> str:
    bits = []
    for r in rows:
        path = r.get("local_preview") or ""
        if not path:
            continue
        ext = Path(path).suffix.lower()
        alt = f"{r['id']} by {r.get('author') or 'unknown'}"
        if ext in {".gif", ".png", ".jpg", ".jpeg", ".webp"}:
            bits.append(f'<a href="{r["local_detail"]}"><img src="{path}" alt="{alt}" width="220"></a>')
        elif ext == ".mp4":
            bits.append(f'<a href="{path}">{r["id"]} local MP4</a>')
    if not bits:
        return ""
    return "<p>\n" + "\n".join(bits) + "\n</p>\n"


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
                prompt_status=prompt_flag(c.get("prompt") or ""),
                model_claim=c.get("model_claim") or c.get("conclusion") or "候选/排除",
                pipeline="不混入已收集主表",
                verify=c.get("conclusion") or c.get("vs_baseline") or "候选/排除",
                play=c.get("playbook") or "",
                license_notes=c.get("license_conclusion") or "仅外链",
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
            "社区长文；原文提示词已本地全文归档；清单无成品媒体 URL",
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
                verify="已在库 · 作者声明 · 未观看附件" if kind == "mp4" else "已在库 · 提示词逐字 · 清单无成品媒体 URL",
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
            extra={"prompt_audience": g.get("prompt_audience"), "production_notes": g.get("production_notes")},
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
            "updated": "2026-11-06",
            "coverage": "当前公开搜集核实清单完整入库，不是穷尽全网。主表媒体已本地归档，原 URL 仅作出处。许可未知，不是作者授权或 CC0。媒体全部未观看。",
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
    assert catalog["meta"]["counts"]["x_author_claim_25"] == 25, catalog["meta"]["counts"]
    assert catalog["meta"]["counts"]["web_gif_12"] == 12
    assert catalog["meta"]["counts"]["pending"] == 12
    assert catalog["meta"]["counts"]["game_author_claim"] == 4  # daft fox xiaomo varg

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
    tables_zh = "\n\n".join(
        [
            "## 1. X 作者声明 2.6（25 组，不按附件拆卡）",
            md_table(collected_x),
            "## 2. 非 X 真 GIF（12）",
            md_table(web_confirmed),
            "## 3. 本仓已收录的社区长文 / 单帖（2）",
            md_table(inrepo),
            "## 4. 游戏动作序列 · 作者声明（4，非官方验证）",
            md_table(game_main),
            "## 附表 A · 待核（12）",
            md_table(pending),
            "## 附表 B · 纯 prompt / 剔除",
            md_table(prompt_only + excluded_x),
            "## 附表 C · 不混入 2.6 成功：2.5 / 宣传 / 多模型 / 失败 / 非X候选 / Morphic",
            md_table(catalog["appendix"]),
            "## 附表 D · 仓库种子 GIF（本仓示例，不是社区征集主清单）",
            md_table(seeds),
        ]
    )
    tables_en = "\n\n".join(
        [
            "## 1. X author-claimed 2.6 (25 groups, not split by attachment)",
            md_table(collected_x, HEADERS_EN),
            "## 2. Non-X real GIFs (12)",
            md_table(web_confirmed, HEADERS_EN),
            "## 3. Already-in-repo community longform / posts (2)",
            md_table(inrepo, HEADERS_EN),
            "## 4. Game action sequences — author-claimed (4, not officially verified)",
            md_table(game_main, HEADERS_EN),
            "## Appendix A — pending (12)",
            md_table(pending, HEADERS_EN),
            "## Appendix B — prompt-only / rejected",
            md_table(prompt_only + excluded_x, HEADERS_EN),
            "## Appendix C — not mixed into 2.6 success: 2.5 / promo / multimodel / failure / non-X candidates / Morphic",
            md_table(catalog["appendix"], HEADERS_EN),
            "## Appendix D — repository-seed GIFs (local examples, not the community collection)",
            md_table(seeds, HEADERS_EN),
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
                tables_zh,
                "",
            ]
        ),
        encoding="utf-8",
    )

    count_table = f"""| Bucket | Count | Not mixed into confirmed 2.6 success | Count |
|---|---:|---|---:|
| X author-claimed 2.6 | **{c['x_author_claim_25']}** | Pending | {c['pending']} |
| Non-X real GIFs | **{c['web_gif_12']}** | Prompt-only | {c['prompt_only']} |
| In-repo community longform/posts | **{c['already_in_repo']}** | Duplicate/rejected | {c['excluded']} |
| Game author-claimed | **{c['game_author_claim']}** | 2.5 / promo / multimodel / failure / Morphic / non-X candidates | {c['appendix']} |
| **Main total** | **{c['main_collected']}** | Repository seeds (local examples) | {c['repo_seeds']} |"""

    count_table_zh = f"""| 主表 | 数 | 附表（不混入已确认 2.6 成功） | 数 |
|---|---:|---|---:|
| X 作者声明 2.6 | **{c['x_author_claim_25']}** | 待核 | {c['pending']} |
| 非 X 真 GIF | **{c['web_gif_12']}** | 纯 prompt | {c['prompt_only']} |
| 已在库社区长文/单帖 | **{c['already_in_repo']}** | 重复/不合格 | {c['excluded']} |
| 游戏 · 作者声明 | **{c['game_author_claim']}** | 2.5 / 宣传 / 多模型 / 失败 / Morphic / 非X候选 | {c['appendix']} |
| **主表合计** | **{c['main_collected']}** | 仓库种子（本仓示例） | {c['repo_seeds']} |"""

    vis = """<!-- readme-tech-visualizer:start -->
<p align="center"><img src="docs/readme-assets/hero-wide.png" alt="Awesome GPT Image GIFs — community case archive with local media and original prompts" width="100%"></p>
<p align="center"><img src="docs/readme-assets/project-icon.png" alt="Awesome GPT Image GIFs" width="96" height="96"></p>
<p align="center">
<img src="https://img.shields.io/badge/cases-43-10131a?style=flat-square&labelColor=c2ff67" alt="43 cases">
<img src="https://img.shields.io/badge/local_media-archived-10131a?style=flat-square&labelColor=c2ff67" alt="local media archived">
<img src="https://img.shields.io/badge/prompts-verbatim_or_empty-10131a?style=flat-square&labelColor=c2ff67" alt="verbatim or empty prompts">
<img src="https://img.shields.io/badge/license-MIT_code_only-10131a?style=flat-square&labelColor=c2ff67" alt="MIT covers source code only">
</p>

## Technical Snapshot

### Tech Stack

<img src="https://img.shields.io/badge/HTML-e34f26?style=flat-square&logo=html5&logoColor=white&logoWidth=20&height=24" alt="HTML">
<img src="https://img.shields.io/badge/CSS-1572b6?style=flat-square&logo=css&logoColor=white&logoWidth=20&height=24" alt="CSS">
<img src="https://img.shields.io/badge/JavaScript-f7df1e?style=flat-square&logo=javascript&logoColor=black&logoWidth=20&height=24" alt="JavaScript">
<img src="https://img.shields.io/badge/Python-3776ab?style=flat-square&logo=python&logoColor=white&logoWidth=20&height=24" alt="Python">
<img src="https://img.shields.io/badge/GitHub_Pages-222222?style=flat-square&logo=githubpages&logoColor=white&logoWidth=20&height=24" alt="GitHub Pages">
<img src="https://img.shields.io/badge/Pillow-3776ab?style=flat-square&logo=python&logoColor=white&logoWidth=20&height=24" alt="Pillow">

### Engineering Capabilities

- Static GitHub Pages case archive (no Images API at browse time)
- Local media + verbatim prompt archival with source citations
- Python validators and GitHub Actions CI

<!-- readme-tech-visualizer:end -->
"""

    embed_x = local_embed_block(collected_x)
    embed_web = local_embed_block(web_confirmed)
    embed_in = local_embed_block(inrepo)
    embed_game = local_embed_block(game_main)

    OUT_README.write_text(
        f"""{vis}
# Awesome GPT Image GIFs

Awesome GPT Image GIFs collects real GPT Image GIF cases from the public web: original authors, original media, public prompts, sources, and production pipelines. It is a community catalog of GPT Image 2.6 work, not this repository's original playbook showcase.

**Real cases · Local media · Original prompts · Sources**

**Languages:** [English](README.md) · [简体中文](README.zh-CN.md) · [Catalog page EN](https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=en) · [案例页 中文](https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=zh) · [Case files](docs/cases/) · [Media manifest](docs/data/local-media-manifest.json)

No other language editions are maintained. Appendix playbook pages are Chinese-first and are **not** a second synced catalog.

Independent community project, not an OpenAI product. Current public inventory, not exhaustive web coverage. Each main-table case has a local folder with media, full original prompt, author, and source citation.

## What is this repository?

A library of **community original-author cases** for GPT Image / ChatGPT Images 2.6 (`gpt-image-2.6-sunburst` / `gpt-image-2.6-flare`): who made it, the original post, the real GIF or MP4, the public prompt (empty if unpublished; adaptations never impersonate the original), model evidence, native GIF vs sprite-slice/postprocess, and verification level.

It is **not** a gallery of this repo's remake playbooks, SVG concept cards, or local seed GIFs.

## What is in the current inventory?

Numbers come from one JSON source: `docs/data/community-cases.json`. English and Chinese pages must not invent a second count.

{count_table}

Officially verified Image 2.6 game outputs: **0**. Author claim ≠ official verification. X items labeled GIF are usually unwatched MP4. This repo's 12 popular-GIF restages are **not** the headline number.

## Is this an original playbook gallery?

No. Original-character remakes, Morphic prompt cards (examples are not 2.6), and SVG covers live on [appendix pages](https://jammyfu.github.io/awesome-gpt-image-gifs/ideas.html). Local seed GIFs are Appendix D only.

## What can I do with this catalog?

- Browse the [web catalog](https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=en) (same data as this README)
- Open **local** media and full prompts under `docs/cases/<id>/`
- Copy **public original** prompts from the local `prompt.md` when the source published them
- Use original URLs only as citations
- Contribute another original-author case with source, media, prompt-or-empty, and model evidence

## What can this repository not do?

- It does not generate images or call the Images API at browse time
- It does not claim exhaustive web coverage or official OpenAI verification
- It does not claim an author grant or CC0 for archived third-party media
- It does not treat SVG covers or this repo's `prompt_adaptation` as third-party originals
- Appendix pages (ideas / popular remakes) are not fully English-synced; do not treat them as a parallel inventory

{tables_en}

### Local media in this README

{embed_web}
{embed_x}
{embed_in}
{embed_game}

## How do I browse locally?

```bash
git clone https://github.com/jammyfu/awesome-gpt-image-gifs.git
cd awesome-gpt-image-gifs
python3 -m http.server 8000 --directory docs
# http://localhost:8000/?lang=en
```

## How do I submit a case?

Add a community original-author row and archive media into `docs/cases/<id>/` (or open a PR with the original post, media, verbatim prompt or explicit empty, model evidence, pipeline, license-unknown note). Do not label SVG concepts or this repo's rewrites as third-party originals.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [MEDIA_RIGHTS.md](MEDIA_RIGHTS.md).

## What are the license boundaries?

Source code is under the MIT license in `LICENSE`. That **does not** license third-party media, prompts, or likenesses. Archived files keep **license unknown**. This is not an author grant or CC0. Do not treat GitHub stars, traffic, or MIT as permission to reuse someone else's GIF.

## Which languages are maintained?

English (`README.md`) and Simplified Chinese (`README.zh-CN.md`) are complete and share one catalog. No Japanese or other README exists; do not fake a sync. Site language switch: `?lang=en` / `?lang=zh`.
""",
        encoding="utf-8",
    )

    OUT_README_ZH.write_text(
        f"""{vis}
# Awesome GPT Image GIFs

Awesome GPT Image GIFs 收集全网 GPT Image GIF 真实案例、原作者、原媒体、提示词、出处与制作流程；不是本站原创方案集。

**真实案例 · 本地素材 · 原文 prompt · 出处**

稳定英文名保持 **Awesome GPT Image GIFs**。这是社区 GPT Image 2.6 案例库，当前公开搜集核实清单完整入库，**不是穷尽全网**。

**语言：** [English](README.md) · [简体中文](README.zh-CN.md) · [Catalog EN](https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=en) · [案例页 中文](https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=zh) · [案例目录](docs/cases/) · [素材清单](docs/data/local-media-manifest.json)

没有其他已维护的语言版本。玩法/热门附页以中文为主，**不假装**与英文总目是第二套同步目录。

独立社区整理，非 OpenAI 官方。作者声明 ≠ 官方验证；X 标 GIF 多为未观看 MP4。主表媒体已本地归档，原 URL 只作出处。许可未知，不是作者授权或 CC0。

## 这是什么仓库？

收集 **GPT Image / ChatGPT Images 2.6**（`gpt-image-2.6-sunburst` / `gpt-image-2.6-flare`）的社区原作者真实案例：作者、原帖、真 GIF 或 MP4、公开原文 prompt（缺则空；改编不冒充原文）、模型依据、直出 GIF 还是 sprite 切帧/后处理、验证级别。

**不是**本站原创复刻方案、SVG 概念卡或本地种子 GIF 展示。

## 现在收集了哪些案例？

数字只来自一份数据：`docs/data/community-cases.json`。中英页面不得各写一套互相冲突的数。

{count_table_zh}

官方验证的 Image 2.6 游戏成品：**0**。本项目热门 GIF 重演 12 案**不是**主数字。

## 这是本站原创方案集吗？

不是。原创角色重演、Morphic 提示词卡（示例非 2.6）、SVG 封面在 [附页](https://jammyfu.github.io/awesome-gpt-image-gifs/ideas.html)。本地种子 GIF 只在附表 D。

## 这个目录能做什么？

- 打开 [网页总目录](https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=zh)（与本 README 同一份数据）
- 打开 `docs/cases/<id>/` 里的**本地**媒体和完整 prompt
- 在来源已公开时从本地 `prompt.md` 复制**原文** prompt
- 原 URL 只当作出处引用
- 提交新的原作者案例（出处、媒体、prompt 或标明空、模型依据）

## 这个仓库做不到什么？

- 浏览时不调用 Images API、不付费生成
- 不宣称穷尽全网或官方验证
- 不声称已获作者授权或 CC0
- 不把 SVG 或本站 `prompt_adaptation` 标成第三方原文
- 玩法/热门附页不是完整英文同步版，不能当成第二套案例数

{tables_zh}

### 本 README 中的本地媒体

{embed_web}
{embed_x}
{embed_in}
{embed_game}

## 如何本地浏览？

```bash
git clone https://github.com/jammyfu/awesome-gpt-image-gifs.git
cd awesome-gpt-image-gifs
python3 -m http.server 8000 --directory docs
# http://localhost:8000/?lang=zh
```

## 如何提交案例？

向 `docs/data/community-cases.json` 补社区原作者一行，并把素材归档进 `docs/cases/<id>/`（或 PR 附原帖、媒体、prompt 原文或标明空、模型依据、许可未知说明）。不要把 SVG 概念图、本站改编 prompt 标成第三方原文。

详见 [CONTRIBUTING.md](CONTRIBUTING.md) · [MEDIA_RIGHTS.md](MEDIA_RIGHTS.md)。

## 许可边界是什么？

源码见 `LICENSE` 的 MIT。这**不能**自动覆盖第三方媒体、提示词或肖像。入库素材保持**许可未知**。这不是作者授权，也不是 CC0。不要拿星数、访问量或 MIT 当可商用第三方 GIF 的许可。

## 有哪些语言版本？

英文 `README.md` 与简体中文 `README.zh-CN.md` 完整同步、共用一份目录。没有日文或其他 README，不假装同步。站点切换：`?lang=en` / `?lang=zh`。
""",
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
Browse https://jammyfu.github.io/awesome-gpt-image-gifs/?lang=en (EN) or ?lang=zh (中文). Open local media and full prompts under docs/cases/<id>/. Copy public original prompts only. Original URLs are citations. Submit cases. Do not treat SVG or prompt_adaptation as originals.

## What can it not do?
No Images API at browse time. No paid generation. No author-grant or CC0 claim. No exhaustive-web or official-verification claim. Appendix idea/popular pages are Chinese-first and not a second inventory.

## Which languages are maintained?
English README.md and Simplified Chinese README.zh-CN.md. No other README editions.

## License boundaries
MIT covers source code only. Archived third-party media remains license-unknown. Not an author grant or CC0.

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
