#!/usr/bin/env python3
"""Validate idea metadata and original local preview assets."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'docs/data/ideas.json').read_text(encoding='utf8'))
assert len(data)==20, f'expected 20 ideas; found {len(data)}'
assert len({x['id'] for x in data})==len(data),'duplicate id'
for x in data:
    for k in ('id','title_zh','title_en','category','description_zh','prompt','origin','model','frames','frame_duration_ms','preview','source_label'):
        assert x.get(k),f'{x.get("id")} missing {k}'
    assert x['origin'] in ('official','tested','community','concept')
    assert x['frames']>=2 and x['frames']<=16
    assert 20<=x['frame_duration_ms']<=2000
    assert x['preview_kind'] in ('existing_gif','concept_illustration')
    asset=(root/'docs'/x['preview']).resolve()
    assert asset.is_relative_to(root/'docs') and asset.is_file(),f'broken image: {x["id"]}'
    if x['preview_kind']=='concept_illustration':assert asset.suffix=='.svg'
    if x['preview_kind']=='existing_gif':assert asset.suffix=='.gif'
    if x['origin']=='concept':assert not x['source_url']
    else:assert x['source_url'].startswith('https://')
expected = '/* AUTO-GENERATED from ideas.json by tools/sync_ideas.py */\nwindow.GIF_IDEAS = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
assert (root/'docs/data/ideas.js').read_text(encoding='utf8')==expected,'ideas.js out of sync'
assert 'ideas.html' in (root/'docs/index.html').read_text(encoding='utf8')
print(f'OK: {len(data)} idea cards, sources, prompts, preview images, and browser data')
