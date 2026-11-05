#!/usr/bin/env python3
"""Check data integrity and actual animated GIF files (Pillow required)."""
import json
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'docs' / 'data' / 'gallery.json'
items = json.loads(source.read_text(encoding='utf-8'))
assert isinstance(items, list) and items, 'Gallery must be a nonempty array'
ids = set()
for item in items:
    for key in ('id','title','description','category','tags','image','frames','duration_ms','prompt','prompt_status'):
        assert item.get(key), f'{item.get("id")}: missing {key}'
    assert item['id'] not in ids, f'duplicate id {item["id"]}'
    ids.add(item['id'])
    assert not item['image'].startswith(('/', 'http:','https:')), 'Gallery images must be relative'
    path = (ROOT/'docs'/item['image']).resolve()
    assert path.is_relative_to(ROOT/'docs') and path.is_file(), f'{item["id"]}: bad image path'
    with Image.open(path) as im:
        assert im.format=='GIF', f'{path.name}: not GIF'
        assert im.is_animated and im.n_frames > 1, f'{path.name}: not animated'
        assert im.n_frames==item['frames'], f'{path.name}: wrong frame count'
        ms=0
        for frame_no in range(im.n_frames):
            im.seek(frame_no)
            ms+=im.info.get('duration', 0)
        assert ms==item['duration_ms'], f'{path.name}: wrong duration'
    prompt_path=ROOT/item['prompt_file']
    assert prompt_path.is_file(), f'{item["id"]}: missing prompt file'
compiled=ROOT/'docs/data/gallery.js'
assert compiled.read_text(encoding='utf-8').split('window.GALLERY_ITEMS = ',1)[1].rstrip().endswith(';')
print(f'OK: {len(items)} animated GIFs, prompts, frame counts, durations, and paths verified')
