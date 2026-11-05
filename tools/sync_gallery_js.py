#!/usr/bin/env python3
"""Compile the canonical gallery JSON to an offline-friendly JS data file."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'docs' / 'data' / 'gallery.json'
target = ROOT / 'docs' / 'data' / 'gallery.js'
items = json.loads(source.read_text(encoding='utf-8'))
target.write_text('/* Auto-generated from gallery.json. Run python tools/sync_gallery_js.py */\nwindow.GALLERY_ITEMS = ' + json.dumps(items, indent=2, ensure_ascii=False) + ';\n', encoding='utf-8')
print(f'Wrote {target.relative_to(ROOT)}: {len(items)} items')
