"""Presentation helpers; catalog evidence remains in write_community_catalog.py."""
from __future__ import annotations

from html import escape
from pathlib import Path
from string import Template

TEMPLATES = Path(__file__).resolve().parent / "templates"

# Local GIF previews. Wording for the paper-boat card is an evidence label, not a new prompt.
FEATURED = (
    (
        "lightlyn-orange-cat-mascot-gif",
        {
            "en": "Character sticker",
            "zh-CN": "角色贴纸",
            "zh-TW": "角色貼紙",
            "ja": "キャラクターのステッカー",
        },
        {
            "en": "Published mascot-animation prompt",
            "zh-CN": "公开的吉祥物动画提示词",
            "zh-TW": "公開的吉祥物動畫提示詞",
            "ja": "公開されているマスコット用プロンプト",
        },
    ),
    (
        "veevid-perfume-light-sweep-gif",
        {
            "en": "Product loop",
            "zh-CN": "产品循环",
            "zh-TW": "產品循環",
            "ja": "プロダクトのループ",
        },
        {
            "en": "Fixed-camera light sweep",
            "zh-CN": "固定机位光线扫过",
            "zh-TW": "固定機位光線掃過",
            "ja": "固定カメラの光のスイープ",
        },
    ),
    (
        "ravivit-paper-boat-gif",
        {
            "en": "Paper-boat loop",
            "zh-CN": "纸船循环",
            "zh-TW": "紙船循環",
            "ja": "紙のボートのループ",
        },
        {
            "en": "Source motion brief; verbatim wording unconfirmed",
            "zh-CN": "来源动作描述，逐字原文未确认",
            "zh-TW": "來源動作描述，逐字原文未確認",
            "ja": "出典の動作説明。逐語の原文は未確認",
        },
    ),
)

# (family, version, case id). Ids must already exist in the catalog.
FAMILY_FEATURED = (
    ("claude", "claude-fable-5.2", "x-himanshutwtxs-fable52-motion-showreel"),
    ("claude", "claude-fable-5.2", "x-wshuyi-fable52-sabertooth-hunt"),
    ("claude", "claude-opus-5.5", "web-jamesgreene-code1-opus55-isometric-city"),
    ("gemini", "gemini-4-argon", "web-jamesgreene-code1-gemini4-argon-isometric-city"),
    ("gemini", "gemini-4-carbon", "x-coodddaaaa-gemini-carbon-pelican-bike"),
    ("gemini", "gemini-4-carbon", "x-statswire-gemini-carbon-nyc-cruiser"),
    ("gpt-code", "gpt-6.2-sol", "x-marcthecreatorr-gpt62sol-sailing-ship"),
    ("gpt-code", "gpt-6.2-sol", "x-harshithlucky3-gpt62sol-pelican-svg-animation"),
    ("gpt-code", "gpt-6.1-sol", "web-jamesgreene-code1-gpt61-sol-isometric-city"),
    ("grok", "grok-4.7", "web-jamesgreene-code1-grok47-isometric-city"),
    ("grok", "grok-imagine-video", "x-radcybertruck-grok-imagine-cybertruck-cry"),
    ("qwen", "qwen3.8-27b", "web-jamesgreene-code1-qwen38-27b-isometric-city"),
    ("deepseek", "deepseek-v4.1-flash-1017", "web-jamesgreene-code1-deepseek-v41-flash-1017-isometric-city"),
    ("deepseek", "deepseek-v4.1-flash", "x-latentoperator-a380-deepseek-fable-sol"),
    ("gpt-image", "gpt-image-2.6", "lightlyn-orange-cat-mascot-gif"),
    ("gpt-image", "gpt-image-2.6", "veevid-perfume-light-sweep-gif"),
    ("gpt-image", "gpt-image-2.6", "ravivit-paper-boat-gif"),
)

FAMILY_ORDER = ("claude", "gemini", "gpt-code", "grok", "qwen", "deepseek", "gpt-image")

VERSION_ORDER = {
    "claude": ("claude-fable-5.2", "claude-mythos-5.2", "claude-opus-5.5"),
    "gemini": ("gemini-4-carbon", "gemini-4-argon"),
    "gpt-code": ("gpt-6.2-sol", "gpt-6.1-sol"),
    "grok": ("grok-4.7", "grok-imagine-video"),
    "qwen": ("qwen3.8-27b",),
    "deepseek": ("deepseek-v4.1-flash-1017", "deepseek-v4.1-flash"),
    "gpt-image": ("gpt-image-2.6",),
}

VERSION_LABEL = {
    "claude-fable-5.2": "Claude Fable 5.2",
    "claude-mythos-5.2": "Claude Mythos 5.2",
    "claude-opus-5.5": "Claude Opus 5.5",
    "gemini-4-argon": "Gemini 4 Argon",
    "gemini-4-carbon": "Gemini 4 Carbon",
    "gpt-6.2-sol": "GPT-6.2 Sol",
    "gpt-6.1-sol": "GPT-6.1 Sol",
    "grok-4.7": "Grok 4.7",
    "grok-imagine-video": "Grok Imagine Video",
    "qwen3.8-27b": "Qwen3.8 27B",
    "deepseek-v4.1-flash-1017": "DeepSeek V4.1 Flash 1017",
    "deepseek-v4.1-flash": "DeepSeek V4.1 Flash",
    "gpt-image-2.6": "GPT Image 2.6",
}

TYPE_ORDER = ("gif", "animation", "html-3d", "minigame", "image")

TYPE_LABEL = {
    "en": {
        "gif": "GIF",
        "animation": "Animation",
        "html-3d": "HTML / 3D scene",
        "minigame": "Mini-game",
        "image": "Image",
    },
    "zh-CN": {
        "gif": "动图 / GIF",
        "animation": "动画 / 动效",
        "html-3d": "HTML / 3D 场景",
        "minigame": "小游戏",
        "image": "图像",
    },
    "zh-TW": {
        "gif": "動圖 / GIF",
        "animation": "動畫 / 動效",
        "html-3d": "HTML / 3D 場景",
        "minigame": "小遊戲",
        "image": "圖像",
    },
    "ja": {
        "gif": "GIF",
        "animation": "アニメーション",
        "html-3d": "HTML / 3D",
        "minigame": "ミニゲーム",
        "image": "画像",
    },
}

TYPE_INDEX_LABEL = {
    "gif": "动图 / GIF",
    "animation": "动画 / Animation",
    "html-3d": "HTML / 3D",
    "minigame": "小游戏 / Game",
    "image": "图像 / Image",
}

FAMILY_TITLE = {
    "claude": "Claude",
    "gemini": "Gemini",
    "gpt-code": "GPT-6.2 Sol",
    "grok": "Grok",
    "qwen": "Qwen",
    "deepseek": "DeepSeek",
    "gpt-image": "GPT Image",
}

UI = {
    "en": {
        "case": "Case",
        "post": "Post",
        "method": "Method",
        "original": "Original prompt",
        "partial": "Short / partial",
        "empty": "Unpublished",
        "brief": "Source motion brief",
        "shown": "{shown} featured of {total} sourced cases in this family. The rest are in the full evidence tables.",
        "all": "All {total} sourced cases in this family are listed here. The same rows are in the full evidence tables.",
        "mythos": "This version is named in the inventory and has no separate sourced case here. The inventory sentence is quoted as stored:",
        "qwen": "The inventory also records a version with no separate sourced case. Quoted as stored:",
        "gif_intro": "Still-mainstream previous generation. The three cards below are local media already archived for these cases, not new generations.",
        "cards_note": "Multi-frame format is checked; generation has not been reproduced. The paper-boat brief keeps its unconfirmed wording status. Preview does not grant reuse rights.",
        "by_model": "By model",
        "by_type": "By type",
        "latest_h": "Latest additions",
        "latest_link": "Newest dated cases",
        "latest_note": "Dated cases only, newest first. A missing date stays out of this strip.",
        "index_link": "Full showcase index",
        "type_count": "{n} cases of this type. Four previews below when a thumbnail exists.",
        "credit": "Credit",
    },
    "zh-CN": {
        "case": "案例",
        "post": "原帖",
        "method": "做法",
        "original": "原文提示词",
        "partial": "短 / 部分",
        "empty": "未公开",
        "brief": "来源动作描述",
        "shown": "这个家族收了 {total} 条有出处的案例，这里放 {shown} 条。其余都在后面的完整证据表里。",
        "all": "这个家族 {total} 条有出处的案例都列在这里。后面的完整证据表是同一批记录。",
        "mythos": "清单里写了这一版，但没有单独的、带来源的案例。下面照录清单原话，不另编一条：",
        "qwen": "清单里还记了一版，没有单独案例。原话如下：",
        "gif_intro": "上一代里还在主流使用的图像模型。下面三张是这些案例已经归档的本地素材，不是新生成的图。",
        "cards_note": "只核过是多帧文件，没有复测生成。纸船那条保留“逐字原文未确认”。预览不等于可以拿去用。",
        "by_model": "按模型",
        "by_type": "按类型",
        "latest_h": "最新收录",
        "latest_link": "有日期的最新案例",
        "latest_note": "只排有完整日期的案例，新的在前。没有日期的不放进这一条。",
        "index_link": "案例总表",
        "type_count": "这一类 {n} 条。下面最多四张有缩略图的预览。",
        "credit": "署名",
    },
    "zh-TW": {
        "case": "案例",
        "post": "原帖",
        "method": "做法",
        "original": "原文提示詞",
        "partial": "短 / 部分",
        "empty": "未公開",
        "brief": "來源動作描述",
        "shown": "這個家族收了 {total} 則有出處的案例，這裡放 {shown} 則。其餘都在後面的完整證據表。",
        "all": "這個家族 {total} 則有出處的案例都列在這裡。後面的完整證據表是同一批紀錄。",
        "mythos": "清單裡寫了這一版，但沒有單獨、帶出處的案例。下面照錄清單原文，不另編一則：",
        "qwen": "清單裡還記了一版，沒有單獨案例。原文如下：",
        "gif_intro": "上一代仍在主流使用的圖像模型。下面三張是這些案例已經歸檔的本地素材，不是新生成的圖。",
        "cards_note": "只核過是多幀檔案，沒有重跑生成。紙船那則保留「逐字原文未確認」。預覽不等於可以拿去用。",
        "by_model": "按模型",
        "by_type": "按類型",
        "latest_h": "最新收錄",
        "latest_link": "有日期的最新案例",
        "latest_note": "只排有完整日期的案例，新的在前。沒有日期的不放進這一條。",
        "index_link": "案例總表",
        "type_count": "這一類 {n} 則。下面最多四張有縮圖的預覽。",
        "credit": "署名",
    },
    "ja": {
        "case": "ケース",
        "post": "原投稿",
        "method": "作り方",
        "original": "公開プロンプト",
        "partial": "短い / 部分",
        "empty": "未公開",
        "brief": "出典の動作説明",
        "shown": "このファミリーの出典付き事例は {total} 件。ここでは {shown} 件。残りは下の証拠表に入っています。",
        "all": "このファミリーの出典付き事例 {total} 件は、ここにすべてあります。同じ行が下の証拠表にもあります。",
        "mythos": "インベントリにはこの版の名があるが、出典付きの単独事例はない。原文のまま引用する：",
        "qwen": "インベントリには、単独事例のない版も書いてある。原文のまま：",
        "gif_intro": "いまも主流の前世代。下の 3 枚は、すでにアーカイブしてあるローカルのメディアで、新しく生成したものではない。",
        "cards_note": "複数フレームであることだけを確認し、生成の再現はしていない。紙のボートは原文未確認のまま。プレビューは再利用の許可ではない。",
        "by_model": "モデル別",
        "by_type": "種類別",
        "latest_h": "新しい収録",
        "latest_link": "日付のある新しい事例",
        "latest_note": "完全な日付がある事例だけ。新しい順。日付がないものはここには出さない。",
        "index_link": "事例インデックス",
        "type_count": "この種類は {n} 件。サムネイルがあるものから最大 4 件。",
        "credit": "クレジット",
    },
}


def cases_by_id(catalog: dict) -> dict[str, dict]:
    found: dict[str, dict] = {}
    for group in catalog.values():
        if isinstance(group, list):
            for row in group:
                found[row["id"]] = row
    return found


def sol_note(catalog: dict, lang: str) -> str:
    """Dual status already stored on the catalog. Do not add a 6.2 launch claim."""
    st = catalog["meta"]["gpt_sol_status"]
    label = st["catalog_label"]
    public = st["openai_public_docs_label"]
    checked = st["checked"]
    intro = st["openai_intro_url"]
    models = st["openai_models_url"]
    if lang == "zh-CN":
        return (
            f"目录分栏名 **{label}** 按仓库主人确认。截至 {checked}，OpenAI 公开文档仍写 **{public}**"
            f"（[介绍页]({intro})、[Models]({models})）；本仓不编造官方 6.2 发布声明。"
        )
    if lang == "zh-TW":
        return (
            f"目錄分欄名 **{label}** 按倉庫主人確認。截至 {checked}，OpenAI 公開文件仍寫 **{public}**"
            f"（[介紹頁]({intro})、[Models]({models})）；本倉不編造官方 6.2 發布聲明。"
        )
    if lang == "ja":
        return (
            f"欄の名前 **{label}** はリポジトリ所有者の確認に従う。{checked} 時点で OpenAI の公開ページは **{public}** のまま"
            f"（[紹介]({intro})、[Models]({models})）。公式の 6.2 発表は作らない。"
        )
    return (
        f"Catalog section name **{label}** follows the repo owner. "
        f"As of {checked}, OpenAI’s public pages still document **{public}** "
        f"([introducing {public}]({intro}), [Models]({models})); "
        "this repo does not invent an official 6.2 announcement."
    )


def _prompt_bit(row: dict, lang: str) -> str:
    ui = UI[lang]
    status = row.get("prompt_status") or "空"
    if row["id"] == "ravivit-paper-boat-gif":
        label = ui["brief"]
    elif status == "空":
        label = ui["empty"]
    elif status == "短/部分":
        label = ui["partial"]
    elif str(status).startswith("有"):
        label = ui["original"]
    else:
        label = str(status)
    href = row.get("local_prompt") or row.get("source_url") or ""
    return f"[{label}]({href})" if href else label


def _bullet(row: dict, lang: str) -> str:
    ui = UI[lang]
    title = " ".join(str(row.get("title") or row["id"]).split())
    bits = [f"**{title}**", str(row.get("author") or "")]
    if row.get("local_detail"):
        bits.append(f"[{ui['case']}]({row['local_detail']})")
    if row.get("source_url"):
        bits.append(f"[{ui['post']}]({row['source_url']})")
    bits.append(_prompt_bit(row, lang))
    pipe = " ".join(str(row.get("pipeline") or "").split())
    if pipe:
        bits.append(f"{ui['method']}: {pipe}")
    return "- " + " · ".join(bit for bit in bits if bit)


def _inventory_quote(catalog: dict, needle: str) -> str:
    notes = catalog.get("meta", {}).get("unverified_or_missing") or []
    for note in notes:
        if needle in note:
            return str(note).strip()
    raise SystemExit(f"missing inventory note containing {needle!r}")


def version_anchor(version: str) -> str:
    return "ver-" + version.replace(".", "-")


def work_type_of(row: dict) -> str:
    """Classify a collected case from its recorded kind and pipeline. Not a new claim."""
    cid = row.get("id") or ""
    if cid.startswith("game-"):
        return "minigame"
    kind = str(row.get("media_kind") or "").lower()
    pipe = f"{row.get('pipeline') or ''} {row.get('title') or ''}".lower()
    media = str(row.get("media_url") or "").lower()
    if kind in {"html-prompts", "html-sprite-loops", "svg"} or "svg animation" in pipe or "svg code" in pipe:
        return "animation"
    if kind == "html" or any(
        token in pipe
        for token in ("three.js", "threejs", "isometric", "blender", "html/css", "html +", "html animation", "single html", "one html")
    ):
        return "html-3d"
    if row.get("model_family") == "gpt-image" and (kind in {"gif", "mp4"} or media.endswith(".gif") or "/tweet_video/" in media):
        return "gif"
    if kind == "gif" or media.endswith(".gif"):
        return "gif"
    if kind in {"png", "jpg", "jpeg", "image", "webp"}:
        return "image"
    if cid == "luffy-x-article":
        return "gif"
    return "animation"


def _full_day(value: str) -> bool:
    return len(value) == 10 and value[4] == "-" and value[7] == "-" and value[5:7].isdigit() and value[8:10].isdigit()


def thumb_grid(rows: list[dict], lang: str) -> str:
    ui = UI[lang]
    if not rows:
        return ""
    lines = ["<table>", "<tr>"]
    for index, row in enumerate(rows):
        if index and index % 3 == 0:
            lines.extend(["</tr>", "<tr>"])
        title = str(row.get("title") or row["id"])
        source = escape(row.get("image_source") or row.get("source_url") or "")
        credit = escape(row.get("image_credit") or row.get("author") or "")
        alt = escape(f"{title} — {row.get('image_credit') or row.get('author') or ''}")
        thumb = row.get("thumb") or ""
        lines.append('<td align="center" width="33%">')
        if thumb and source:
            lines.append(f'<a href="{source}"><img src="{escape(thumb)}" alt="{alt}" width="220"></a><br>')
        elif thumb:
            lines.append(f'<img src="{escape(thumb)}" alt="{alt}" width="220"><br>')
        detail = row.get("local_detail") or ""
        title_html = escape(title[:80])
        if detail and not str(detail).startswith(("http://", "https://")):
            lines.append(f'<strong><a href="{escape(detail)}">{title_html}</a></strong><br>')
        elif source:
            lines.append(f'<strong><a href="{source}">{title_html}</a></strong><br>')
        else:
            lines.append(f"<strong>{title_html}</strong><br>")
        if credit and source:
            lines.append(f'{ui["credit"]}: {credit}<br><a href="{source}">{escape(ui["post"])}</a>')
        elif credit:
            lines.append(f'{ui["credit"]}: {credit}')
        lines.append("</td>")
    lines.extend(["</tr>", "</table>"])
    return "\n".join(lines)


def quick_nav(lang: str) -> str:
    ui = UI[lang]
    lines = [f"### {ui['by_model']}"]
    for fam in FAMILY_ORDER:
        bits = [f"[{VERSION_LABEL[version]}](#{version_anchor(version)})" for version in VERSION_ORDER[fam]]
        lines.append(f"- [{FAMILY_TITLE[fam]}](#{fam}) — " + " · ".join(bits))
    lines.append("")
    lines.append(f"### {ui['by_type']}")
    for key in TYPE_ORDER:
        lines.append(f"- [{TYPE_LABEL[lang][key]}](#type-{key})")
    lines.append("")
    lines.append(f"### {ui['latest_h']}")
    lines.append(f"- [{ui['latest_link']}](#latest)")
    lines.append(f"- [{ui['index_link']}](docs/showcase-index.md)")
    return "\n".join(lines)


def latest_section(rows: list[dict], lang: str) -> str:
    ui = UI[lang]
    dated = [row for row in rows if _full_day(str(row.get("date") or ""))]
    dated.sort(key=lambda row: (row["date"], row["id"]), reverse=True)
    lines = [f'<a id="latest"></a>', f"## {ui['latest_h']}", ui["latest_note"], ""]
    lines.append(thumb_grid(dated[:8], lang))
    return "\n".join(lines).rstrip() + "\n"


def type_sections(rows: list[dict], lang: str) -> str:
    ui = UI[lang]
    blocks = [f'<a id="by-type"></a>', f"## {ui['by_type']}", ""]
    for key in TYPE_ORDER:
        group = [row for row in rows if row.get("work_type") == key]
        shown = [row for row in group if row.get("thumb")][:4]
        blocks.append(f'<a id="type-{key}"></a>')
        blocks.append(f"### {TYPE_LABEL[lang][key]}")
        blocks.append(ui["type_count"].format(n=len(group)))
        if shown:
            blocks.append(thumb_grid(shown, lang))
        blocks.append(f"[{ui['index_link']}](docs/showcase-index.md#{key})")
        blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"


def main_case_rows(catalog: dict) -> list[dict]:
    rows: list[dict] = []
    by_family = catalog.get("collected_by_family") or {}
    for fam in FAMILY_ORDER:
        bucket = list(by_family.get(fam) or [])
        order = {version: index for index, version in enumerate(VERSION_ORDER.get(fam, ()))}
        bucket.sort(key=lambda row: (order.get(row.get("model_version"), 99), str(row.get("date") or ""), row["id"]))
        rows.extend(bucket)
    return rows


def featured_cards(rows: list[dict], lang: str) -> str:
    by_id = {r["id"]: r for r in rows}
    ui = UI[lang]
    lines = ["<table>", "<tr>"]
    for cid, titles, notes in FEATURED:
        row = by_id[cid]
        media = next(f["path"] for f in row["local_files"] if f["ext"] == "gif")
        assert row["original_prompt"].strip(), f"Featured prompt is missing: {cid}"
        title = titles[lang]
        note = notes[lang]
        detail, prompt, source = map(escape, (row["local_detail"], row["local_prompt"], row["source_url"]))
        author = escape(row.get("image_credit") or row["author"])
        alt = escape(f"{title} by {row.get('image_credit') or row['author']}")
        preview = row.get("thumb") or media
        prompt_label = ui["brief"] if cid == "ravivit-paper-boat-gif" else ui["original"]
        lines.extend([
            '<td align="center" width="33%">',
            f'<a href="{source}"><img src="{escape(preview)}" alt="{alt}" width="220"></a><br>',
            f'<strong><a href="{detail}">{escape(title)}</a></strong><br>',
            f'{ui["credit"]}: {author}<br><sub>{escape(note)}</sub><br>',
            f'<a href="{prompt}">{escape(prompt_label)}</a> · <a href="{source}">{escape(ui["post"])}</a> · <a href="{escape(media)}">GIF</a>',
            "</td>",
        ])
    lines.extend(["</tr>", "</table>"])
    return "\n".join(lines)


def family_sections(catalog: dict, lang: str) -> str:
    by_id = cases_by_id(catalog)
    by_family = catalog.get("collected_by_family") or {}
    ui = UI[lang]
    picked: dict[str, dict[str, list[str]]] = {fam: {} for fam in FAMILY_ORDER}
    for fam, version, cid in FAMILY_FEATURED:
        row = by_id.get(cid)
        if row is None:
            raise SystemExit(f"featured case is not in the catalog: {cid}")
        if row.get("model_family") != fam or row.get("model_version") != version:
            raise SystemExit(
                f"featured case {cid} is {row.get('model_family')}/{row.get('model_version')}, "
                f"not {fam}/{version}"
            )
        picked[fam].setdefault(version, []).append(cid)
    blocks: list[str] = []
    for fam in FAMILY_ORDER:
        total = len(by_family.get(fam) or [])
        shown = sum(len(ids) for ids in picked[fam].values())
        blocks.append(f'<a id="{fam}"></a>')
        blocks.append(f"## {FAMILY_TITLE[fam]}")
        key = "all" if shown == total else "shown"
        blocks.append(ui[key].format(shown=shown, total=total))
        if fam == "gpt-code":
            blocks.append(sol_note(catalog, lang))
        for version in VERSION_ORDER[fam]:
            blocks.append(f'<a id="{version_anchor(version)}"></a>')
            blocks.append(f"### {VERSION_LABEL[version]}")
            ids = picked[fam].get(version) or []
            if not ids:
                if version == "claude-mythos-5.2":
                    blocks.append(ui["mythos"])
                    blocks.append("> " + _inventory_quote(catalog, "Mythos 5.2"))
                continue
            if fam == "gpt-image" and version == "gpt-image-2.6":
                blocks.append(ui["gif_intro"])
                blocks.append(featured_cards(catalog["collected_web_gif"], lang))
                blocks.append(ui["cards_note"])
                continue
            blocks.append(thumb_grid([by_id[cid] for cid in ids], lang))
        if fam == "qwen":
            blocks.append(ui["qwen"])
            blocks.append("> " + _inventory_quote(catalog, "Qwen 3.8 Flash Next"))
        blocks.append("")
    return "\n\n".join(blocks).rstrip() + "\n"


def collapsed_tables(markdown: str) -> str:
    """Keep every evidence row, with each category independently expandable."""
    blocks = []
    for section in markdown.split("## "):
        if not section.strip():
            continue
        heading, body = section.split("\n", 1)
        blocks.append(
            f"<details>\n<summary><strong>{escape(heading)}</strong></summary>\n\n"
            f"{body.strip()}\n\n</details>"
        )
    return "\n\n".join(blocks)


def render_readme(
    lang: str,
    *,
    catalog: dict,
    count_table: str,
    tables: str,
    collection_sites: str = "",
) -> str:
    c = catalog["meta"]["counts"]
    main_rows = [r for key in (
        "collected_x_author_claim",
        "collected_web_gif",
        "collected_already_in_repo",
        "collected_game_author_claim",
    ) for r in catalog[key]]
    media_count = sum(bool(r.get("local_files")) for r in main_rows)
    template = (TEMPLATES / f"README.{lang}.md").read_text(encoding="utf-8")
    return Template(template).substitute(
        main_count=c["main_collected"],
        media_count=media_count,
        web_count=c["web_gif_12"],
        game_count=c["game_author_claim"],
        pending_count=c["pending"],
        inventory_date=catalog["meta"]["updated"],
        count_table=count_table,
        catalog_tables=collapsed_tables(tables),
        featured=family_sections(catalog, lang),
        collection_sites=collection_sites,
        quick_nav=quick_nav(lang),
        latest=latest_section(main_case_rows(catalog), lang),
        type_sections=type_sections(main_case_rows(catalog), lang),
    )
