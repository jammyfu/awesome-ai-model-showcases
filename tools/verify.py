#!/usr/bin/env python3
"""Unified verification entry. Uses sys.executable, not PATH python."""
from __future__ import annotations

import subprocess
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(args: list[str]) -> None:
    print("+", " ".join(args), flush=True)
    subprocess.check_call(args, cwd=ROOT)


def main() -> int:
    py = sys.executable
    run([py, str(ROOT / "tools/sync_gallery_js.py")])
    run(["git", "diff", "--exit-code", "--", "docs/data/gallery.js"])
    run([py, str(ROOT / "tools/sync_media_js.py")])
    run(["git", "diff", "--exit-code", "--", "docs/data/media.js"])
    run([py, str(ROOT / "tools/validate_gallery.py")])
    run([py, str(ROOT / "tools/sync_ideas.py")])
    run(["git", "diff", "--exit-code", "--", "docs/data/ideas.js"])
    run([py, str(ROOT / "tools/validate_ideas.py")])
    run([py, str(ROOT / "tools/validate_media.py")])
    run([py, str(ROOT / "tools/sync_popular.py")])
    run(["git", "diff", "--exit-code", "--", "docs/data/popular.js", "playbooks/popular-gifs.md"])
    run([py, str(ROOT / "tools/validate_popular.py")])
    run([py, str(ROOT / "tools/write_community_catalog.py")])
    run(
        [
            "git",
            "diff",
            "--exit-code",
            "--",
            "README.md",
            "README.zh-CN.md",
            "README.zh-TW.md",
            "README.ja.md",
            "playbooks/community-cases.md",
            "docs/data/community-cases.json",
            "docs/data/cases.js",
            "llms.txt",
            "docs/llms.txt",
            "docs/github-about.json",
        ]
    )
    run([py, str(ROOT / "tools/validate_community.py")])
    run([py, str(ROOT / "tools/validate_local_media.py")])
    run([py, str(ROOT / "tools/test_archive_guards.py")])
    run([py, str(ROOT / "tools/test_catalog_expansion.py")])
    node = shutil.which("node")
    if node:
        run([node, str(ROOT / "tools/test_case_gallery.cjs")])
    else:
        print("SKIP: gallery JavaScript smoke test requires optional Node.js", flush=True)
    run([py, str(ROOT / "tools/validate_markdown_links.py")])
    print("verify ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
