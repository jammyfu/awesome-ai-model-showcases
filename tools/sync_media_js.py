#!/usr/bin/env python3
"""Compile the canonical media manifest JSON to an offline-friendly JS data file."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "docs/data/media-manifest.json"
target = ROOT / "docs/data/media.js"
data = json.loads(source.read_text(encoding="utf-8"))
target.write_text(
    "/* AUTO-GENERATED from media-manifest.json by tools/sync_media_js.py */\n"
    "window.MEDIA_MANIFEST = "
    + json.dumps(data, indent=2, ensure_ascii=False)
    + ";\n",
    encoding="utf-8",
)
print(f"Wrote {target.relative_to(ROOT)}: {len(data.get('items', []))} media records")
