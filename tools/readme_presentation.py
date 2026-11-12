"""Presentation helpers; catalog evidence remains in write_community_catalog.py."""
from __future__ import annotations

import os
import json
from datetime import date
from functools import lru_cache
from html import escape
from pathlib import Path
from string import Template
from media_policy import is_public_asset
from case_localization import localized, translation_link

TEMPLATES = Path(__file__).resolve().parent / "templates"

# Exact licensed examples; source model/prompt claims remain unverified.
FEATURED = tuple(
    (cid, dict(zip(("en", "zh-CN", "zh-TW", "ja"), titles)),
     {lang: "CC BY 4.0 · ailingqu" for lang in ("en", "zh-CN", "zh-TW", "ja")})
    for cid, titles in (
        ("ailingqu-jelly-bear-wobble", ("Jelly bear wobble", "果冻熊摇晃", "果凍熊搖晃", "ゼリーベア")),
        ("ailingqu-flower-macro-flash", ("Flower macro flash", "花卉微距快闪", "花卉微距快閃", "花のマクロ")),
        ("ailingqu-cat-brand-reel", ("Cat logo reel", "猫头品牌快闪", "貓頭品牌快閃", "猫ロゴ")),
    )
)

# Homepage families. GPT Image stays in the catalog JSON and in
# collections/gpt-image-gifs/, and is not a homepage section.
# Editorial priorities are reviewable and shared by all language editions.
DISCOVERY_ORDER = json.loads((TEMPLATES.parent.parent / "data/discovery-order.json").read_text(encoding="utf-8"))
HOMEPAGE_FAMILIES = tuple(DISCOVERY_ORDER["family_order"])
FAMILY_ORDER = HOMEPAGE_FAMILIES + ("gpt-image",)
VERSION_ORDER = {family: tuple(versions) for family, versions in DISCOVERY_ORDER["version_order"].items()}

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
    "qwen4-max-preview": "Qwen 4 Max Preview",
    "qwen4-preview": "Qwen 4.0 Preview",
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
        "shown": "All {total} sourced cases in this family, grouped by version, newest first. {thumbs} have a thumbnail card (click the image for the original post); the rest are listed one per line. The same rows are in the full evidence tables.",
        "video": "▶ Video",
        "all": "All {total} sourced cases in this family are listed here. The same rows are in the full evidence tables.",
        "mythos": "This version is named in the inventory and has no separate sourced case here. The inventory sentence is quoted as stored:",
        "qwen": "The inventory also records a version with no separate sourced case. Quoted as stored:",
        "gif_intro": "Still-mainstream previous generation. The three cards below are local media already archived for these cases, not new generations.",
        "cards_note": 'CC BY 4.0 examples by ailingqu. Published prompts are source rewrites, not verified historical requests. Model attribution is a source claim; generation has not been reproduced. These featured thumbnails are resized derivatives.',
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
        "shown": "这个家族收了 {total} 条有出处的案例，下面按版本全部列出，新的在前。{thumbs} 条带缩略图卡片，点图看原帖；没有缩略图的各占一行。后面的完整证据表是同一批记录。",
        "video": "▶ 视频",
        "all": "这个家族 {total} 条有出处的案例都列在这里。后面的完整证据表是同一批记录。",
        "mythos": "清单里写了这一版，但没有单独的、带来源的案例。下面照录清单原话，不另编一条：",
        "qwen": "清单里还记了一版，没有单独案例。原话如下：",
        "gif_intro": "上一代里还在主流使用的图像模型。下面三张是这些案例已经归档的本地素材，不是新生成的图。",
        "cards_note": 'ailingqu 的 CC BY 4.0 示例。公开提示词是来源改写，不是已核实的历史提交请求。模型归属为来源声明，未复测生成。缩略图为缩放衍生版本。',
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
        "shown": "這個家族收了 {total} 則有出處的案例，下面按版本全部列出，新的在前。{thumbs} 則帶縮圖卡片，點圖看原帖；沒有縮圖的各占一行。後面的完整證據表是同一批紀錄。",
        "video": "▶ 影片",
        "all": "這個家族 {total} 則有出處的案例都列在這裡。後面的完整證據表是同一批紀錄。",
        "mythos": "清單裡寫了這一版，但沒有單獨、帶出處的案例。下面照錄清單原文，不另編一則：",
        "qwen": "清單裡還記了一版，沒有單獨案例。原文如下：",
        "gif_intro": "上一代仍在主流使用的圖像模型。下面三張是這些案例已經歸檔的本地素材，不是新生成的圖。",
        "cards_note": 'ailingqu 的 CC BY 4.0 範例。公開提示詞是來源改寫，非已核實的歷史提交請求。模型歸屬為來源聲明，未重跑生成。縮圖為縮放衍生版本。',
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
        "shown": "このファミリーの出典付き事例 {total} 件を、版ごとに新しい順ですべて並べる。{thumbs} 件はサムネイル付きのカード（画像をクリックすると原投稿へ）、サムネイルのないものは 1 行ずつ。同じ行が下の証拠表にもある。",
        "video": "▶ 動画",
        "all": "このファミリーの出典付き事例 {total} 件は、ここにすべてあります。同じ行が下の証拠表にもあります。",
        "mythos": "インベントリにはこの版の名があるが、出典付きの単独事例はない。原文のまま引用する：",
        "qwen": "インベントリには、単独事例のない版も書いてある。原文のまま：",
        "gif_intro": "いまも主流の前世代。下の 3 枚は、すでにアーカイブしてあるローカルのメディアで、新しく生成したものではない。",
        "cards_note": 'ailingqu の CC BY 4.0 作例。公開プロンプトは出典の書き換えで、実際の過去の入力は未検証。モデルは出典の主張で、生成は再現していない。サムネイルは縮小版。',
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


def version_anchor(version: str) -> str:
    return "ver-" + version.replace(".", "-")


@lru_cache(maxsize=1)
def _work_type_overrides() -> dict[str, dict]:
    """Load reviewed exceptions to the legacy media-format classifier."""
    path = TEMPLATES.parent.parent / "data/work-type-overrides.json"
    entries = json.loads(path.read_text(encoding="utf-8"))["cases"]
    found = {}
    for entry in entries:
        cid = entry["case_id"]
        if cid in found or entry["work_type"] not in TYPE_ORDER:
            raise ValueError(f"Invalid or duplicate work-type evidence: {cid}")
        found[cid] = entry
    return found


def work_type_of(row: dict) -> str:
    """Classify the source-reported work, without claiming a successful playtest."""
    cid = row.get("id") or ""
    override = _work_type_overrides().get(cid)
    if override:
        for field in ("source_url", "title", "pipeline"):
            if row.get(field) != override[field]:
                raise ValueError(f"Stale work-type evidence for {cid}: {field}; review the source before reclassifying")
        return override["work_type"]
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
    """Only complete, valid publication dates participate in newest-first lists."""
    try:
        return len(value) == 10 and date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def _href(path: str, from_file: Path | None) -> str:
    if not from_file or not path or str(path).startswith(("http://", "https://", "mailto:", "#")):
        return path
    root = Path(__file__).resolve().parents[1]
    target = (root / path).resolve()
    return Path(os.path.relpath(target, Path(from_file).resolve().parent)).as_posix()


def latest_section(rows: list[dict], lang: str) -> str:
    ui = UI[lang]
    dated = _date_desc([row for row in rows if _full_day(str(row.get("date") or ""))])
    headings = {"en": "Recent source posts", "zh-CN": "近期原帖", "zh-TW": "近期原帖", "ja": "最近の原投稿"}
    notes = {
        "en": "Five recent source-dated cases, not an ingestion log or ranking. Same-day ties use case ID; undated cases remain in the full catalog.",
        "zh-CN": "按来源日期倒序列出五条，不代表入库时间或质量排名。同日按案例 ID 排序；无日期案例仍保留在完整目录。",
        "zh-TW": "依來源日期倒序列出五則，不代表收錄時間或品質排名。同日依案例 ID 排序；無日期案例仍保留在完整目錄。",
        "ja": "出典の日付が新しい 5 件です。収録順や品質ランキングではありません。同日は事例 ID 順とし、日付のない事例も全目録に残します。",
    }
    lines = ['<a id="latest"></a>', f"## {headings[lang]}", "", notes[lang], ""]
    missing_heat = {
        "en": "No comparable popularity snapshot is recorded as of {date}; this is source-date order, not a popularity ranking.",
        "zh-CN": "截至 {date} 尚无可比热度快照；这里按来源日期排列，不是热度榜。",
        "zh-TW": "截至 {date} 尚無可比熱度快照；此處依來源日期排列，不是熱度榜。",
        "ja": "{date} 時点で比較可能な人気指標は未収集です。ここは出典の日付順で、人気ランキングではありません。",
    }
    lines += [missing_heat[lang].format(date=DISCOVERY_ORDER["meta"]["reviewed_at"]), ""]
    for row in dated[:5]:
        family_label = "GPT Sol" if row["model_family"] == "gpt-code" else FAMILY_TITLE[row["model_family"]]
        lines.append(f"- **{row['date']} · {family_label}** · " + _compact_line(row, lang)[2:])
    return "\n".join(lines).rstrip() + "\n"


def type_sections(rows: list[dict], lang: str) -> str:
    blocks = ['<a id="by-type"></a>', f"## {UI[lang]['by_type']}", ""]
    for key in TYPE_ORDER:
        count = sum(row.get("work_type") == key for row in rows)
        blocks.append(f'<a id="type-{key}"></a>')
        blocks.append(f"- [{TYPE_LABEL[lang][key]}](docs/showcase-index.md#{key}) · **{count}**")
    return "\n".join(blocks).rstrip() + "\n"


def main_case_rows(catalog: dict) -> list[dict]:
    """Homepage rows: frontier families only. GPT Image is a subproject."""
    rows: list[dict] = []
    by_family = catalog.get("collected_by_family") or {}
    for fam in HOMEPAGE_FAMILIES:
        bucket = list(by_family.get(fam) or [])
        order = {version: index for index, version in enumerate(VERSION_ORDER.get(fam, ()))}
        bucket = _date_desc(bucket)
        bucket.sort(key=lambda row: order.get(row.get("model_version"), 99))
        rows.extend(bucket)
    return rows


def featured_cards(rows: list[dict], lang: str, from_file: Path | None = None) -> str:
    by_id = {r["id"]: r for r in rows}
    ui = UI[lang]
    lines = ["<table>", "<tr>"]
    for cid, titles, notes in FEATURED:
        row = by_id[cid]
        media = next((f["path"] for f in row["local_files"] if f["ext"] == "gif" and is_public_asset(f["path"])), "")
        if not media:
            continue
        assert row["original_prompt"].strip(), f"Featured prompt is missing: {cid}"
        title = titles[lang]
        note = notes[lang]
        detail = escape(_href(row["local_detail"], from_file))
        prompt = escape(_href(row["local_prompt"], from_file))
        source = escape(row["source_url"])
        author = escape(row.get("image_credit") or row["author"])
        alt = escape(f"{title} by {row.get('image_credit') or row['author']}")
        thumb = (row.get("thumb") or "") if is_public_asset(row.get("thumb") or "") else ""
        preview = escape(_href(thumb if is_public_asset(thumb) else media, from_file))
        media_href = escape(_href(media, from_file))
        prompt_label = {"en": "Published prompt", "zh-CN": "公开提示词", "zh-TW": "公開提示詞", "ja": "公開プロンプト"}[lang]
        lines.extend([
            '<td align="center" width="33%">',
            f'<a href="{source}"><img src="{preview}" alt="{alt}" width="220"></a><br>',
            f'<strong><a href="{detail}">{escape(title)}</a></strong><br>',
            f'{ui["credit"]}: {author}<br><sub>{escape(note)}</sub><br>',
            f'<a href="{prompt}">{escape(prompt_label)}</a> · <a href="{source}">{escape(ui["post"])}</a> · <a href="{media_href}">GIF</a>',
            f'<br><a href="{escape(row.get("license_url") or "")}">{escape(row.get("license_label") or "")}</a>',
            "</td>",
        ])
    lines.extend(["</tr>", "</table>"])
    return "\n".join(lines)


def _date_desc(rows: list[dict]) -> list[dict]:
    """Newest complete source dates first; missing/partial dates last; stable ID ties."""
    dated = sorted((r for r in rows if _full_day(str(r.get("date") or ""))), key=lambda r: (r["date"], r["id"]), reverse=True)
    undated = sorted((r for r in rows if not _full_day(str(r.get("date") or ""))), key=lambda r: r["id"])
    return dated + undated


def _compact_line(row: dict, lang: str) -> str:
    ui = UI[lang]
    title = " ".join(str(localized(row, "title", lang) or row["id"]).split())
    bits = [f"**{title}**"]
    credit = row.get("image_credit") or row.get("author") or ""
    if credit:
        bits.append(f"{ui['credit']}: {credit}")
    if row.get("local_detail"):
        bits.append(f"[{ui['case']}]({translation_link(row, lang) or row['local_detail']})")
    if row.get("source_url"):
        bits.append(f"[{ui['post']}]({row['source_url']})")
    if is_public_asset(row.get("video") or ""):
        bits.append(f"[{ui['video']}]({row['video']})")
    return "- " + " · ".join(bits)


def family_sections(catalog: dict, lang: str) -> str:
    """A bounded entry per family; complete evidence belongs in the catalog, not the README."""
    words = {
        "en": ("cases", "Browse all", "No sourced case yet", "Example to start with"),
        "zh-CN": ("条", "查看全部", "暂无独立来源案例", "入门示例"),
        "zh-TW": ("則", "查看全部", "暫無獨立來源案例", "入門範例"),
        "ja": ("件", "全件を見る", "出典付きの単独事例は未収録", "最初に見る例"),
    }
    unit, browse, empty, sample = words[lang]
    blocks = []
    for fam in HOMEPAGE_FAMILIES:
        rows = catalog["collected_by_family"].get(fam) or []
        unknown = {row.get("model_version") for row in rows} - set(VERSION_ORDER[fam])
        if unknown:
            raise ValueError(f"{fam}: add explicit version order for {sorted(map(str, unknown))}")
        blocks += [f'<a id="{fam}"></a>', f"### {FAMILY_TITLE[fam]} · {len(rows)} {unit}", ""]
        blocks += [f"[{browse}](docs/catalog.{lang}.md#{fam})", ""]
        for version in VERSION_ORDER[fam]:
            count = sum(row.get("model_version") == version for row in rows)
            if not count and version != "claude-mythos-5.2":
                continue
            anchor = version_anchor(version)
            blocks += [f'<a id="{anchor}"></a>', f"- [{VERSION_LABEL[version]}](docs/catalog.{lang}.md#{anchor}) · {count}" + (f" · {empty}" if not count else "")]
        if rows:
            selected = json.loads((TEMPLATES.parent.parent / "data/readme-model-tables.json").read_text())["families"][fam]
            by_id = {row["id"]: row for row in rows}
            labels = {
                "en": ("Preview", "Case & introduction", "Model & sources", "View at source ↗", "Preview permission pending", "Source-reported"),
                "zh-CN": ("预览", "案例与介绍", "模型与来源", "到原帖看效果 ↗", "预览转载授权待核实", "来源声明"),
                "zh-TW": ("預覽", "案例與介紹", "模型與來源", "到原帖看效果 ↗", "預覽轉載授權待核實", "來源聲明"),
                "ja": ("プレビュー", "事例と紹介", "モデルと出典", "出典で見る ↗", "画像の掲載許諾は未確認", "出典による表記"),
            }[lang]
            blocks += ["", "<table>", "<thead><tr>" + "".join(f"<th>{label}</th>" for label in (labels[0], labels[1] + " · " + labels[2])) + "</tr></thead>", "<tbody>"]
            supplemental_path = TEMPLATES.parent.parent / "data/readme-supplemental-previews.json"
            supplemental = json.loads(supplemental_path.read_text())["cases"]
            extra_label = {
                "en": "Additional licensed work · outside catalog count",
                "zh-CN": "补充授权作品 · 不计入目录总数",
                "zh-TW": "補充授權作品 · 不計入目錄總數",
                "ja": "追加の許諾済み作品 · 目録件数には含めません",
            }[lang]
            for extra in supplemental:
                if extra["model_family"] != fam:
                    continue
                if not is_public_asset(extra["image_path"]):
                    raise ValueError(f"Unapproved supplemental preview: {extra['id']}")
                loc = extra["locales"][lang]
                link = escape(extra["source_url"], quote=True)
                image = escape(extra["image_path"], quote=True)
                alt = escape(loc["alt"], quote=True)
                preview = f'<a href="{link}"><img src="{image}" alt="{alt}" width="240"></a>'
                title = escape(loc["title"])
                intro = escape(loc["summary"])
                credit = escape(extra["display_credit"])
                model = escape(extra["model"])
                evidence_label = {"en": "Permission", "zh-CN": "授权依据", "zh-TW": "授權依據", "ja": "許諾の根拠"}[lang]
                credit_label = {"en": "Attribution & changes", "zh-CN": "署名与修改说明", "zh-TW": "署名與修改說明", "ja": "クレジットと変更"}[lang]
                license_url = escape(extra["license_url"], quote=True)
                license_label = escape(extra["license"])
                evidence = escape(extra["license_evidence_url"], quote=True)
                blocks.append(f'<tr><td width="240">{preview}</td><td><strong>{title}</strong><br>{intro}<br><small>{extra_label}</small><br><small>{escape(loc["changes"])}</small><br><br>{model}<br><small>{labels[5]}</small><br>{credit}<br><a href="{link}">{UI[lang]["post"]}</a> · <a href="{license_url}">{license_label}</a> · <a href="{evidence}">{evidence_label}</a><br><a href="docs/readme-preview-credits.md#{extra['id']}">{credit_label}</a></td></tr>')
            seen = set()
            for item in selected:
                row = by_id[item["case_id"]]
                if row["id"] in seen or row["source_url"] != item["source_url"]:
                    raise ValueError(f"Duplicate or stale table selection: {row['id']}")
                seen.add(row["id"])
                source = escape(row["source_url"], quote=True)
                # Source-only is explicit: never hotlink an unlicensed archive image
                # or substitute a family banner for an actual case result.
                preview = f'<a href="{source}">{labels[3]}</a><br><small>{labels[4]}</small>'
                title = escape(" ".join(localized(row, "title", lang).split()))
                intro = escape(" ".join(localized(row, "pipeline", lang).split()))
                model = escape(VERSION_LABEL[row["model_version"]])
                credit = escape(row.get("image_credit") or row.get("author") or "")
                detail = escape(translation_link(row, lang), quote=True)
                blocks.append(f'<tr><td width="240">{preview}</td><td><strong>{title}</strong><br>{intro}<br><br>{model}<br><small>{labels[5]}</small><br>{credit}<br><a href="{detail}">{UI[lang]["case"]}</a> · <a href="{source}">{UI[lang]["post"]}</a></td></tr>')
            blocks += ["</tbody>", "</table>"]
        blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"


def readme_showcase_gifs(catalog: dict, lang: str) -> str:
    """Actual licensed case media, not project branding or unlicensed frontier previews."""
    rows = cases_by_id(catalog)
    prompt_label = {"en": "Published prompt", "zh-CN": "公开提示词", "zh-TW": "公開提示詞", "ja": "公開プロンプト"}[lang]
    lines = ["<p>"]
    links = []
    for cid, titles, _notes in FEATURED:
        row = rows[cid]
        media = next((f["path"] for f in row.get("local_files") or [] if f["ext"] == "gif" and is_public_asset(f["path"])), "")
        if not media:
            raise ValueError(f"Showcase GIF needs exact publication permission: {cid}")
        title = titles[lang]
        detail = translation_link(row, lang)
        lines.append(f'<a href="{escape(detail)}"><img src="{escape(media)}" alt="{escape(title)} · ailingqu · GPT Image 2.6" width="232"></a>')
        links.append(f"- **[{title}]({detail})** · ailingqu · [{prompt_label}]({row['local_prompt']}) · [{UI[lang]['post']}]({row['source_url']})")
    return "\n".join(lines + ["</p>", "", *links])


def write_preview_credits() -> None:
    """Visible credit chain and changes for the exact additional preview bytes."""
    root = TEMPLATES.parent.parent
    rows = json.loads((root / "data/readme-supplemental-previews.json").read_text())["cases"]
    lines = ["<!-- Generated by tools/write_community_catalog.py; edit data/readme-supplemental-previews.json. -->",
             "# Preview credits / 预览署名 / 預覽署名 / プレビューのクレジット", ""]
    for row in rows:
        lines += [f'<a id="{row["id"]}"></a>', f'## {row["model"]}', "", row['credit'], "",
                  f'[Source / 来源 / 來源 / 出典]({row["source_url"]}) · [{row["license"]}]({row["license_url"]}) · [Permission / 授权 / 授權 / 許諾]({row["license_evidence_url"]})', ""]
        original = row['source_evidence'].get('original_source_url')
        if original:
            lines += [f'[Original photograph / 原照片 / 原照片 / 原写真]({original})', ""]
        for lang in ("en", "zh-CN", "zh-TW", "ja"):
            loc = row['locales'][lang]
            lines += [f'### {lang}', "", f'**{loc["title"]}**', "", loc['summary'], "", loc['changes'], ""]
        lines += [f'Original modification record: {row["changes"]}', "",
                  f'SHA-256: {row["image_sha256"]}', "",
                  f'[License text / 许可全文 / 許可全文 / ライセンス全文]({row["local_license_path"].removeprefix("docs/")})', ""]
    (root / "docs/readme-preview-credits.md").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")


def source_spotlights() -> dict:
    """An explicit source project, not an incidental licensed appendix selection."""
    root = TEMPLATES.parent.parent
    data = json.loads((root / "data/readme-featured-cases.json").read_text(encoding="utf-8"))
    seen = set()
    for row in data["cases"]:
        if row["id"] in seen or not is_public_asset(row["image_path"]):
            raise ValueError(f"Duplicate or unapproved spotlight: {row['id']}")
        seen.add(row["id"])
        for lang in ("en", "zh-CN", "zh-TW", "ja"):
            for field in ("title", "summary", "alt"):
                if not row["locales"][lang].get(field):
                    raise ValueError(f"Missing spotlight translation: {row['id']} {lang} {field}")
    heat = data["popularity"]
    if heat["scope"] != "repository" or len({r["source_project_id"] for r in data["cases"]}) != 1:
        raise ValueError("Spotlight popularity describes one source repository, not individual films")
    return data


def readme_source_spotlights(lang: str) -> str:
    data = source_spotlights()
    rows = data["cases"]
    heat = data["popularity"]
    words = {
        "en": ("Watch the film", "Published prompt", "Source code", "Original frame", "**Claude Opus 5.5** · Vincentwei1021 · **{stars:,} GitHub stars** for the source project ({date}).", "Two films from the same source project; repository stars are not per-film views or a cross-model ranking. Author-published frames, unmodified. [MIT media permission]({evidence}) · [Copyright and license]({license}). This source spotlight is separate from the {count}-case catalog. Model attribution is the author's claim; we did not rerun generation."),
        "zh-CN": ("观看成片", "公开提示词", "源码", "作者原图", "**Claude Opus 5.5** · Vincentwei1021 · 源项目 **{stars:,} GitHub stars**（{date} 快照）。", "同一开源项目的两部短片；仓库 stars 不是单片播放量或跨模型排名。作者发布的成片画面，未修改。[媒体 MIT 授权]({evidence}) · [版权与完整许可]({license})。这组独立精选不计入 {count} 条目录；模型归属为作者声明，未重新生成验证。"),
        "zh-TW": ("觀看成片", "公開提示詞", "原始碼", "作者原圖", "**Claude Opus 5.5** · Vincentwei1021 · 來源專案 **{stars:,} GitHub stars**（{date} 快照）。", "同一開源專案的兩部短片；倉庫 stars 不是單片播放量或跨模型排名。作者發布的成片畫面，未修改。[媒體 MIT 授權]({evidence}) · [版權與完整許可]({license})。這組獨立精選不計入 {count} 則目錄；模型歸屬為作者聲明，未重新生成驗證。"),
        "ja": ("映像を見る", "公開プロンプト", "ソースコード", "作者の元画像", "**Claude Opus 5.5** · Vincentwei1021 · 元プロジェクトの **GitHub stars は {stars:,}**（{date} 確認）。", "同じプロジェクトの 2 作品です。stars は各作品の再生数やモデル横断の人気順位ではありません。作者が公開した映像フレームを無加工で掲載。[メディアの MIT 許諾]({evidence}) · [著作権・ライセンス全文]({license})。この特集は {count} 件の目録とは別です。モデルは作者の申告で、生成の再実行はしていません。"),
    }
    watch, prompt, code, original, intro, note = words[lang]
    lines = [intro.format(stars=heat["stars"], date=heat["observed_at"][:10]), ""]
    for row in rows:
        local = row["locales"][lang]
        lines += [f"**{local['title']}**", "",
                  f'<a href="{escape(row["demo_url"])}"><img src="{escape(row["image_path"])}" alt="{escape(local["alt"])}" width="720"></a>', "",
                  local["summary"], "",
                  f"**[{watch} →]({row['demo_url']})** · [{prompt}]({row['prompt_url']}) · [{code}]({row['source_code_url']}) · [{original}]({row['image_source_url']})", ""]
    # Count is substituted by render_readme without changing the source manifest.
    lines.append(note.format(evidence=rows[0]["license_evidence_url"], license=rows[0]["local_license_path"], count="${main_count}"))
    return "\n".join(lines)


def write_site_spotlight() -> None:
    """Keep the live gallery's first result tied to the same reviewed source."""
    import re
    data = source_spotlights()
    row = data["cases"][0]
    root = TEMPLATES.parent.parent
    parts = ['<figure class="source-spotlight">']
    for lang, watch, prompt, code, note in (
        ("en", "Watch", "Prompt", "Source", "One project, two featured films in the README. Repository stars; author-reported model. Separate from the catalog count."),
        ("zh-CN", "观看", "提示词", "源码", "同一项目的两部精选短片见 README。热度为仓库 stars，模型为作者声明，精选不计入目录总数。"),
    ):
        local = row["locales"][lang]
        parts += [f'<div class="spotlight-locale" lang="{lang}">',
                  f'<a href="{escape(row["demo_url"])}"><img src="{escape(row["image_path"].removeprefix("docs/"))}" alt="{escape(local["alt"])}" width="1920" height="1080"></a>',
                  f'<figcaption><strong>{escape(local["title"])} · Claude Opus 5.5</strong><br>',
                  f'Vincentwei1021 · {data["popularity"]["stars"]:,} GitHub stars · {data["popularity"]["observed_at"][:10]}<br>',
                  f'<a href="{escape(row["demo_url"])}">{watch} →</a> · <a href="{escape(row["prompt_url"])}">{prompt}</a> · <a href="{escape(row["source_code_url"])}">{code}</a> · <a href="{escape(row["local_license_path"].removeprefix("docs/"))}">MIT</a><br>',
                  f'<small>{note}</small></figcaption></div>']
    parts.append('</figure>')
    file = root / 'docs/index.html'
    text = file.read_text(encoding='utf-8')
    text, n = re.subn(r'<!-- source-spotlights:start -->.*?<!-- source-spotlights:end -->',
                      '<!-- source-spotlights:start -->\n'+'\n'.join(parts)+'\n<!-- source-spotlights:end -->', text, flags=re.S)
    if n != 1:
        raise ValueError('Expected exactly one source spotlight block in docs/index.html')
    file.write_text(text, encoding='utf-8')


def render_readme(
    lang: str,
    *,
    catalog: dict,
    gpt_subproject_line: str = "",
) -> str:
    c = catalog["meta"]["counts"]
    main_rows = main_case_rows(catalog)
    media_count = sum(any(is_public_asset(path) for path in [r.get("video") or "", *[f["path"] for f in r.get("local_files") or []]]) for r in main_rows)
    template = (TEMPLATES / f"README.{lang}.md").read_text(encoding="utf-8")
    return Template(template).substitute(
        main_count=c["main_collected"],
        gpt_count=c["gpt_image"],
        media_count=media_count,
        pending_count=c["pending"],
        inventory_date=catalog["meta"]["updated"],
        featured=family_sections(catalog, lang),
        latest=latest_section(main_rows, lang),
        type_sections=type_sections(main_rows, lang),
        gpt_subproject_line=gpt_subproject_line,
        sol_status=sol_note(catalog, lang),
        showcase_gifs=readme_showcase_gifs(catalog, lang),
        source_spotlights=readme_source_spotlights(lang).replace("${main_count}", str(c["main_collected"])),
    )
