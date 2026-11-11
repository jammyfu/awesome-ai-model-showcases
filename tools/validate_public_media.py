#!/usr/bin/env python3
"""Fail if public docs/catalog reintroduce unapproved embeds or direct media links."""
import json
from pathlib import Path
from build_public_site import check_references
from media_policy import ROOT, grants, is_public_asset, public_docs_paths


def main():
    for path in grants():
        assert is_public_asset(path), f'Missing or changed bytes for approved asset: {path}'
    paths=[*ROOT.glob('README*.md'),ROOT/'playbooks/community-cases.md',*ROOT.glob('collections/*/README*.md'),*ROOT.glob('docs/**/*.html'),ROOT/'docs/showcase-index.md',*ROOT.glob('docs/cases/*/README.md')]
    for path in paths: check_references(path,ROOT)
    catalog=json.loads((ROOT/'docs/data/community-cases.json').read_text())
    for group in catalog.values():
        if not isinstance(group,list): continue
        for rec in group:
            for key in ('thumb','video','local_preview'):
                if rec.get(key): assert is_public_asset(rec[key]), (rec['id'],key)
            for item in rec.get('local_files') or []:
                assert item.get('public_allowed') is True and is_public_asset(item['path']), (rec['id'],item)
    raw=(ROOT/'docs/data/public-media.js').read_text()
    browser=json.loads(raw.split('window.PUBLIC_MEDIA_PATHS = ',1)[1].rstrip().removesuffix(';'))
    assert browser == public_docs_paths(), 'Regenerate public-media.js'
    for name, app in [('index.html','cases-app.js'),('ideas.html','ideas-app.js'),('game.html','game-app.js'),('popular.html','popular-app.js')]:
        text=(ROOT/'docs'/name).read_text()
        assert text.index('data/public-media.js') < text.index(app), (name,'rights registry script order')
    print(f'public-media rights ok: {len(paths)} documents; exact grants and source-only fallback')

if __name__=='__main__': main()
