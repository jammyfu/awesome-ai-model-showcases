"""Presentation helpers; catalog evidence remains in write_community_catalog.py."""
from __future__ import annotations

from html import escape
from pathlib import Path
from string import Template

TEMPLATES = Path(__file__).resolve().parent / "templates"
FEATURED = (
    ("lightlyn-orange-cat-mascot-gif", "Character sticker", "角色贴纸", "Published mascot-animation prompt", "公开的吉祥物动画提示词"),
    ("veevid-perfume-light-sweep-gif", "Product loop", "产品循环", "Fixed-camera light sweep", "固定机位光线扫过"),
    ("ravivit-paper-boat-gif", "Paper-boat loop", "纸船循环", "Source motion brief; verbatim wording unconfirmed", "来源动作描述，逐字原文未确认"),
)


def featured_cards(rows: list[dict], lang: str) -> str:
    by_id = {r["id"]: r for r in rows}
    zh = lang == "zh-CN"
    lines = ['<table>', '<tr>']
    for cid, en_title, zh_title, en_note, zh_note in FEATURED:
        row = by_id[cid]
        # Use only the original GIF attached to this case, never a concept cover.
        media = next(f["path"] for f in row["local_files"] if f["ext"] == "gif")
        assert row["original_prompt"].strip(), f"Featured prompt is missing: {cid}"
        title, note = (zh_title, zh_note) if zh else (en_title, en_note)
        detail, prompt, source = map(escape, (row["local_detail"], row["local_prompt"], row["source_url"]))
        author = escape(row["author"])
        alt = escape(f"{title} by {row['author']}")
        prompt_label = ("来源动作描述" if zh else "Source motion brief") if cid == "ravivit-paper-boat-gif" else ("原文提示词" if zh else "Original prompt")
        source_label = "出处" if zh else "Source"
        lines.extend([
            '<td align="center" width="33%">',
            f'<a href="{detail}"><img src="{escape(media)}" alt="{alt}" width="200"></a><br>',
            f'<strong><a href="{detail}">{title}</a></strong><br>',
            f'{author}<br><sub>{note}</sub><br>',
            f'<a href="{prompt}">{prompt_label}</a> · <a href="{source}">{source_label}</a>',
            '</td>',
        ])
    lines.extend(['</tr>', '</table>'])
    return "\n".join(lines)


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
    main_rows = [r for key in ("collected_x_author_claim", "collected_web_gif",
                              "collected_already_in_repo", "collected_game_author_claim")
                 for r in catalog[key]]
    media_count = sum(bool(r.get("local_files")) for r in main_rows)
    template = (TEMPLATES / f"README.{lang}.md").read_text(encoding="utf-8")
    return Template(template).substitute(
        main_count=c["main_collected"], media_count=media_count, web_count=c["web_gif_12"],
        game_count=c["game_author_claim"], pending_count=c["pending"],
        inventory_date=catalog["meta"]["updated"], count_table=count_table,
        catalog_tables=collapsed_tables(tables),
        featured=featured_cards(catalog["collected_web_gif"], lang),
        collection_sites=collection_sites,
    )
