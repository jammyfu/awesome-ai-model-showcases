#!/usr/bin/env python3
"""Unified verification entry. Uses sys.executable, not PATH python."""
from __future__ import annotations

import os
import tempfile
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
    run([py, str(ROOT / "tools/render_public_media.py")])
    run(
        [
            "git",
            "diff",
            "--exit-code",
            "--",
            "docs/cases",
            "docs/translations",
            "docs/data/public-media.js",
            "docs/index.html",
            "README.md",
            "README.zh-CN.md",
            "README.zh-TW.md",
            "README.ja.md",
            "playbooks/community-cases.md",
            "docs/data/community-cases.json",
            "docs/data/translation-coverage.json",
            "docs/data/cases.js",
            "llms.txt",
            "docs/llms.txt",
            "docs/github-about.json",
            "docs/showcase-index.md",
            "docs/catalog.en.md",
            "docs/catalog.zh-CN.md",
            "docs/catalog.zh-TW.md",
            "docs/catalog.ja.md",
            "data/showcase-index.json",
            "docs/missing-thumbnails.md",
            "docs/missing-videos.md",
            "collections/gpt-image-gifs/README.md",
            "collections/gpt-image-gifs/README.zh-CN.md",
        ]
    )
    run([py, str(ROOT / "tools/validate_community.py")])
    run([py, str(ROOT / "tools/test_case_localization.py")])
    run([py, str(ROOT / "tools/validate_local_media.py")])
    run([py, str(ROOT / "tools/test_archive_guards.py")])
    run([py, str(ROOT / "tools/test_catalog_expansion.py")])
    run([py, str(ROOT / "tools/test_readme_presentation.py")])
    run([py, str(ROOT / "tools/test_public_media.py")])
    run([py, str(ROOT / "tools/test_public_catalog.py")])
    run([py, str(ROOT / "tools/test_case_media_pages.py")])
    run([py, str(ROOT / "tools/validate_public_media.py")])
    run([py, str(ROOT / "tools/build_public_site.py")])
    node = shutil.which("node")
    if node:
        run([node, str(ROOT / "tools/test_case_gallery.cjs")])
        run([node, str(ROOT / "tools/test_case_localization.cjs")])
        run([node, str(ROOT / "tools/test_secondary_media.cjs")])
    else:
        print("SKIP: gallery JavaScript smoke test requires optional Node.js", flush=True)
    if os.environ.get("RUN_BROWSER_TESTS") == "1":
        if not node:
            raise RuntimeError("RUN_BROWSER_TESTS=1 requires Node.js and Playwright")
        with tempfile.TemporaryDirectory(prefix="showcase-browser-") as temporary:
            output = Path(temporary) / "site"
            run([py, str(ROOT / "tools/build_public_site.py"), "--output", str(output)])
            subprocess.check_call([node, str(ROOT / "tools/test_public_site.cjs")], cwd=ROOT,
                                  env={**os.environ, "PUBLIC_SITE_DIR": str(output)})
    else:
        print("Browser playback check not run locally; CI runs RUN_BROWSER_TESTS=1", flush=True)
    run([py, str(ROOT / "tools/validate_markdown_links.py")])
    print("verify ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
