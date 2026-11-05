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
        "license_notes": license_notes or "无明确再分发授权 · 仅外链",
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
        license_notes=item.get("license_notes") or "无明确再分发授权 · 仅外链",
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
        license_notes=item.get("license_conclusion") or "无明确再分发授权 · 仅外链",
        extra={
            "original_prompt": item.get("prompt") or "",
            "frames": (item.get("media_verify") or {}).get("frames"),
        },
    )


def md_table(rows: list[dict]) -> str:
    lines = [
        "| # | 作者 | 玩法 | 原帖 | 媒体 | prompt | 模型依据 | 管线 | 验证 | 许可 |",
        "|---:|---|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        src = f"[原帖]({r['source_url']})" if r.get("source_url") else "—"
        media = f"[{r['media_kind']}]({r['media_url']})" if r.get("media_url") else "—"
        lines.append(
            "| {i} | {author} | {title} | {src} | {media} | {prompt} | {model} | {pipe} | {verify} | {lic} |".format(
                i=i,
                author=(r.get("author") or "").replace("|", "/"),
                title="`{id}` {title}".format(
                    id=r["id"],
                    title=(r.get("title") or r["id"]).replace("|", "/")[:60],
                ),
                src=src,
                media=media,
                prompt=r.get("prompt_status") or "空",
                model=(r.get("model_claim") or "")[:40].replace("|", "/"),
                pipe=(r.get("pipeline") or "")[:36].replace("|", "/"),
                verify=(r.get("verify") or "")[:36].replace("|", "/"),
                lic="仅外链",
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
            "https://video.twimg.com/tweet_video/HWWn8n7b0AAN1xP.mp4",
            "mp4",
            "有原文",
            "作者称 looping GIF · X 附件 MP4",
        ),
        (
            "luffy-x-article",
            "路飞 X Article：榨干 Image 2.6 的 10 个神级玩法（多玩法一组）",
            "@0xluffy_eth",
            "https://x.com/i/article/2118269816821919744",
            "",
            "none",
            "有原文（中文逐字）",
            "社区长文；本仓不转载其 GIF",
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
                verify="已在库 · 作者声明 · 未观看附件" if kind == "mp4" else "已在库 · 提示词逐字 · 不转载成品 GIF",
                play=title,
                license_notes="无明确再分发授权 · 仅外链/不转载",
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
        if g.get("storage") == "local":
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
            "coverage": "当前公开搜集核实清单完整入库，不是穷尽全网。X 官方引用未读完；媒体全部未观看；无明确授权只外链。",
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

    OUT_JSON.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JS.write_text(
        "/* AUTO-GENERATED by tools/write_community_catalog.py */\nwindow.COMMUNITY_CASES = "
        + json.dumps(catalog, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )

    c = catalog["meta"]["counts"]
    md = [
        "# 社区真实案例总目录",
        "",
        f"> 更新 {catalog['meta']['updated']}（北京时间）。这是**当前公开搜集核实清单**，不是穷尽全网、不是官方验证全集。作者声明 ≠ 已复测生成。X `animated_gif` 多为 MP4，未观看。无明确授权只外链。",
        "",
        f"- 主表已收集：**{c['main_collected']}**（X 作者声明 25 + 非X 真 GIF 12 + 已在库路飞/Krouxzz 2 + 游戏作者声明 4）",
        f"- 待核 {c['pending']} · 纯 prompt {c['prompt_only']} · 剔除 {c['excluded']} · 附表（2.5/宣传/多模型/失败/Morphic/非X候选）{c['appendix']} · 仓库种子 {c['repo_seeds']}",
        "- 官方验证的 2.6 游戏成品：**0**",
        "",
        "## 1. X 作者声明 2.6（25 组，不按附件拆卡）",
        "",
        md_table(collected_x),
        "",
        "## 2. 非 X 真 GIF（12）",
        "",
        md_table(web_confirmed),
        "",
        "## 3. 本仓已收录的社区长文 / 单帖（2）",
        "",
        md_table(inrepo),
        "",
        "## 4. 游戏动作序列 · 作者声明（4，非官方验证）",
        "",
        md_table(game_main),
        "",
        "## 附表 A · 待核（12）",
        "",
        md_table(pending),
        "",
        "## 附表 B · 纯 prompt / 剔除",
        "",
        md_table(prompt_only + excluded_x),
        "",
        "## 附表 C · 不混入 2.6 成功：2.5 / 宣传 / 多模型 / 失败 / 非X候选 / Morphic",
        "",
        md_table(catalog["appendix"]),
        "",
        "## 附表 D · 仓库种子 GIF（本仓示例，不是社区征集主清单）",
        "",
        md_table(seeds),
        "",
    ]
    OUT_MD.write_text("\n".join(md), encoding="utf-8")

    readme = f"""<div align="center">

# Awesome GPT Image GIFs

**全网社区 GPT Image 2.6 真实案例收集库**

当前公开搜集核实清单完整入库，**不是穷尽全网**，不是本项目原创复刻方案展示。作者声明 ≠ 官方验证；X 标 GIF 多为 MP4 且未观看；无明确授权只外链。

[案例总目录（网页）](https://jammyfu.github.io/awesome-gpt-image-gifs/) · [完整总表 Markdown](playbooks/community-cases.md) · [真实 GIF 外链](https://jammyfu.github.io/awesome-gpt-image-gifs/#gifs) · [GitHub](https://github.com/jammyfu/awesome-gpt-image-gifs)

</div>

> 独立社区整理，非 OpenAI 官方仓库。覆盖边界：X 公开检索（官方引用未读完）+ 非X 公开网页 + 游戏原作者深挖；不包含付费生成、不转载无授权媒体。

## 收集规模（主数字 = 社区案例，不是本站方案数）

| 主表 | 数 | 附表（不混入已确认 2.6 成功） | 数 |
|---|---:|---|---:|
| X 作者声明 2.6 | **{c['x_author_claim_25']}** | 待核 | {c['pending']} |
| 非 X 真 GIF | **{c['web_gif_12']}** | 纯 prompt | {c['prompt_only']} |
| 已在库社区长文/单帖 | **{c['already_in_repo']}** | 重复/不合格 | {c['excluded']} |
| 游戏 · 作者声明 | **{c['game_author_claim']}** | 2.5 / 宣传 / 多模型 / 失败 / Morphic / 非X候选 | {c['appendix']} |
| **主表合计** | **{c['main_collected']}** | 仓库种子（本仓示例） | {c['repo_seeds']} |

官方验证的 Image 2.6 游戏成品：**0**。本项目热门 GIF 重演 12 案、原创角色 prompt **不是**主数字，见 [附加参考](playbooks/popular-gifs.md)。

## 目录

- [X 25 组](#1-x-作者声明-26-25-组)
- [非 X 真 GIF 12](#2-非-x-真-gif-12)
- [已在库路飞 / Krouxzz](#3-本仓已收录的社区长文--单帖)
- [游戏作者声明 4](#4-游戏动作序列--作者声明)
- [附表：待核 / 剔除 / 非成功](#附表-a--待核12)
- [附加参考（本站方案，退出主案例）](#附加参考本站策划--退出主案例)
- [如何贡献](#how-do-i-submit-a-case)

每案字段：作者、原帖/原网站、真实 GIF 或 MP4 外链、公开原文 prompt（缺则空；改编不冒充原文）、模型依据、直出 GIF vs sprite/后处理、验证级别、许可边界。

{OUT_MD.read_text(encoding='utf-8').split('# 社区真实案例总目录',1)[-1]}

## 附加参考（本站策划 · 退出主案例）

这些**不是**社区原作者成品，不再作为 README/首页主视觉：

- [玩法与提示词附页](https://jammyfu.github.io/awesome-gpt-image-gifs/ideas.html) — 含本站 `prompt_adaptation`、Morphic 面向 2.6 但示例非 2.6 的提示词卡
- [全球热门 GIF → 原创角色重演](https://jammyfu.github.io/awesome-gpt-image-gifs/popular.html) — 12 个未实测方案，**不是 2.6 作品**
- [游戏页](https://jammyfu.github.io/awesome-gpt-image-gifs/game.html) — 作者声明 / 失败样本 / 2.5 历史分开标
- 仓库种子 6 个本地 GIF：见上表附表 D，Pillow 校验，**不是社区征集主清单**

## How do I browse locally?

```bash
git clone https://github.com/jammyfu/awesome-gpt-image-gifs.git
cd awesome-gpt-image-gifs
python3 -m http.server 8000 --directory docs
# http://localhost:8000/
```

## How do I submit a case?

社区原作者案例：在 `docs/data/community-cases.json` 对应分组补一行（或打开 PR 附原帖、媒体外链、prompt 原文或标明空、模型依据、许可）。不要把 SVG 概念图、本站改编 prompt 标成第三方原文。无授权不要把第三方 GIF 放进 `docs/gifs/`。

详情：[CONTRIBUTING.md](CONTRIBUTING.md) · [MEDIA_RIGHTS.md](MEDIA_RIGHTS.md)

## 校验

```bash
python3 tools/write_community_catalog.py
python3 tools/validate_community.py
python3 tools/validate_gallery.py
python3 tools/validate_ideas.py
python3 tools/validate_media.py
```

<!-- readme-tech-visualizer:start -->
## Technical Snapshot

静态 GitHub Pages + Python 校验。浏览不调用 Images API。技术细节不影响「这是案例收集库」的主定位。
<!-- readme-tech-visualizer:end -->

## 这个仓库是做什么的？

收集 **GPT Image / ChatGPT Images 2.6** 的全网社区真实案例：原作者、原帖、真 GIF/MP4 外链、公开 prompt。覆盖当前已搜集核实清单，不宣称穷尽。本站改编方案和热门 GIF 重演在附页。源码 MIT；第三方媒体不能因开源就商用。
"""
    OUT_README.write_text(readme, encoding="utf-8")
    print(
        f"community catalog: main {c['main_collected']} "
        f"(X{c['x_author_claim_25']}+web{c['web_gif_12']}+inrepo{c['already_in_repo']}+game{c['game_author_claim']}); "
        f"pending {c['pending']}; appendix {c['appendix']}"
    )


if __name__ == "__main__":
    main()
