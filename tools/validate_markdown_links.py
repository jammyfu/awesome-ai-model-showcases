#!/usr/bin/env python3
"""Recursively verify local Markdown/HTML link targets that this repo generates."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_REF = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.I)
SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")
GENERATED = (
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "README.zh-TW.md",
    ROOT / "README.ja.md",
    ROOT / "README.ko.md",
    ROOT / "playbooks/community-cases.md",
    ROOT / "docs/showcase-index.md",
    ROOT / "docs/catalog.en.md",
    ROOT / "docs/catalog.zh-CN.md",
    ROOT / "docs/catalog.zh-TW.md",
    ROOT / "docs/catalog.ja.md",
    ROOT / "docs/catalog.ko.md",
    ROOT / "docs/readme-pattern.md",
    ROOT / "docs/discovery-order.md",
    ROOT / "GEO.md",
    ROOT / "docs/translated-case.html",
    ROOT / "docs/translation-policy.md",
    ROOT / "docs/missing-thumbnails.md",
    ROOT / "docs/missing-videos.md",
    ROOT / "collections/gpt-image-gifs/README.md",
    ROOT / "collections/gpt-image-gifs/README.zh-CN.md",
)


def skip_url(url: str) -> bool:
    u = url.strip()
    if not u or u.startswith("#") or u.startswith("?"):
        return True
    return u.lower().startswith(SKIP_SCHEMES)


def dest_of(url: str) -> str:
    u = url.strip()
    u = u.split(" ", 1)[0]
    u = u.split("#", 1)[0]
    u = u.split("?", 1)[0]
    return u


def resolve_local(from_file: Path, url: str) -> Path | None:
    dest = dest_of(url)
    if not dest or skip_url(url):
        return None
    if dest.startswith("/"):
        return (ROOT / dest.lstrip("/")).resolve()
    return (from_file.parent / dest).resolve()


def collect_urls(text: str, html: bool) -> list[str]:
    found = [m.group(1) for m in MD_LINK.finditer(text)]
    if html:
        found.extend(m.group(1) for m in HTML_REF.finditer(text))
    return found


def iter_generated() -> list[Path]:
    files = list(GENERATED)
    cases = ROOT / "docs/cases"
    if cases.is_dir():
        files.extend(sorted(cases.rglob("*.md")))
        files.extend(sorted(cases.rglob("*.html")))
    translations = ROOT / "docs/translations"
    if translations.is_dir():
        files.extend(sorted(translations.glob("*.md")))
    return files


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    html = path.suffix.lower() in {".html", ".htm"}
    errors = []
    for url in collect_urls(text, html=html or "<video" in text or "<img" in text):
        if skip_url(url):
            continue
        dest = dest_of(url)
        if not dest:
            continue
        target = resolve_local(path, url)
        if target is None:
            continue
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            # Allow only in-repo local targets.
            errors.append(f"{path.relative_to(ROOT)}: local link escapes repo: {url}")
            continue
        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing {url} -> {target.relative_to(ROOT)}")
    return errors


def main() -> int:
    errors: list[str] = []
    checked = 0
    for path in iter_generated():
        checked += 1
        errors.extend(check_file(path))
    if errors:
        print("local markdown/html link errors:")
        for e in errors[:80]:
            print(" ", e)
        if len(errors) > 80:
            print(f"  … {len(errors) - 80} more")
        raise SystemExit(f"{len(errors)} dead local links")
    print(f"local markdown links ok: {checked} generated files, 0 missing targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
