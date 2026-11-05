#!/usr/bin/env python3
"""Community catalog is the primary index: full inventory, not a playbook showcase."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    subprocess.check_call([sys.executable, str(ROOT / "tools/write_community_catalog.py")])
    catalog = json.loads((ROOT / "docs/data/community-cases.json").read_text(encoding="utf-8"))
    js = (ROOT / "docs/data/cases.js").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    md = (ROOT / "playbooks/community-cases.md").read_text(encoding="utf-8")
    index = (ROOT / "docs/index.html").read_text(encoding="utf-8")
    counts = catalog["meta"]["counts"]

    assert counts["x_author_claim_25"] == 25, counts
    assert counts["web_gif_12"] == 12, counts
    assert counts["pending"] == 12, counts
    assert counts["already_in_repo"] == 2, counts
    assert counts["game_author_claim"] == 4, counts
    assert counts["main_collected"] == 43, counts
    assert "window.COMMUNITY_CASES" in js
    assert catalog["meta"]["not_exhaustive"] is True
    assert catalog["meta"]["official_verified_26_game"] == 0

    for rec in catalog["collected_x_author_claim"]:
        assert rec["id"] in readme and rec["id"] in md, rec["id"]
        assert rec.get("source_url"), rec["id"]
        assert rec.get("license_notes")
        if rec["media_kind"] == "mp4":
            assert rec.get("media_url"), rec["id"]

    for rec in catalog["collected_web_gif"]:
        assert rec["id"] in readme and rec["id"] in md, rec["id"]
        assert rec["media_kind"] == "gif", rec["id"]
        assert rec.get("media_url", "").endswith(".gif") or "gif" in rec.get("media_url", "")

    head = readme[:1800]
    assert "社区" in head and "收集" in head
    assert "不是穷尽全网" in head or "不是穷尽" in head
    for banned in ("pixel-head-pat.gif", "cat-screen-crack.gif", "Motion worth"):
        assert banned not in head, banned
    assert "popular.html" not in head.split("## 收集规模")[0]
    assert "本项目方案" not in head or "不是本项目" in head or "不是" in head

    # Homepage must lead with the catalog, not SVG/playbook hero.
    assert "COMMUNITY_CASES" in index or "cases.js" in index
    assert "gifs/cat-screen-crack.gif" not in index
    assert "ideas.html" in index  # appendix link ok
    assert "案例" in index or "收集" in index

    print(
        "community catalog ok: "
        f"main {counts['main_collected']}, pending {counts['pending']}, "
        f"excluded {counts['excluded']}, appendix {counts['appendix']}, seeds {counts['repo_seeds']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
