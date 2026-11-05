#!/usr/bin/env python3
"""Synchronize the visual-ideas browser data from JSON."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
source = root / 'docs/data/ideas.json'
data = json.loads(source.read_text(encoding='utf-8'))
out = '/* AUTO-GENERATED from ideas.json by tools/sync_ideas.py */\nwindow.GIF_IDEAS = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
(root / 'docs/data/ideas.js').write_text(out, encoding='utf-8')
print(f'Synced {len(data)} ideas')
