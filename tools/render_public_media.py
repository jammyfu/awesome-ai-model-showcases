#!/usr/bin/env python3
"""Refresh only case media sections; preserve original evidence and prompt text."""
from __future__ import annotations
import json
import re
from html import escape
from pathlib import Path
from media_policy import ROOT, grants, is_public_asset, write_browser_registry

NOTICE = 'Media is shown here only with a documented publication grant. Otherwise, view the original source. / 仅展示有明确授权记录的素材，其余请查看原帖。'


def refresh_case(rec: dict, root: Path = ROOT) -> None:
    folder=root/'docs/cases'/rec['id']
    if not folder.is_dir(): return
    source=rec.get('source_url') or ''
    html=[f'<p>{NOTICE}</p>',f'<p><a href="{escape(source,quote=True)}" target="_blank" rel="noopener noreferrer">View original source / 查看原帖</a></p>']
    md=[NOTICE,'',f'[View original source / 查看原帖]({source})']
    rights=grants(root)
    for item in rec.get('local_files') or []:
        path=item.get('path') or ''
        if not is_public_asset(path,root): continue
        grant=rights[path]; rel='media/'+Path(path).name
        if item.get('ext')=='mp4':
            html.append(f'<video src="{rel}" controls playsinline preload="metadata">Your browser cannot play this video. <a href="{escape(source,quote=True)}">View original source</a>.</video>')
            md.append(f'<video src="{rel}" controls playsinline preload="metadata"></video>')
        else:
            html.append(f'<img src="{rel}" alt="{escape(rec.get("title") or rec["id"],quote=True)}" style="max-width:100%;height:auto">')
            md.append(f'![{rec["id"]}]({rel})')
        html.append(f'<p>{escape(grant["credit"])} · <a href="{escape(grant["license_url"],quote=True)}">{escape(grant["license"])}</a> · <a href="{escape(grant["evidence_url"],quote=True)}">Source grant</a>. {escape(grant["changes"])}</p>')
        md.append(f'{grant["credit"]} · [{grant["license"]}]({grant["license_url"]}) · [Source grant]({grant["evidence_url"]}). {grant["changes"]}')
    page=folder/'index.html'
    if page.is_file():
        text=page.read_text(encoding='utf-8')
        if '<h2>Media</h2>' not in text: raise ValueError(f'No media section: {page}')
        text=re.sub(r'<h2>Media</h2>.*?(?=<h2>|</body>)','<h2>Media</h2>\n'+'\n'.join(html)+'\n',text,count=1,flags=re.S)
        text=text.replace('<p>Local video is a credited copy, not a reuse license. MIT covers source code only.</p>','<p>MIT covers source code only. Public media requires its own documented grant.</p>')
        page.write_text(text,encoding='utf-8')
    page=folder/'README.md'
    if page.is_file():
        text=page.read_text(encoding='utf-8')
        # Older frontier pages appended an unlicensed video link after Prompt status.
        text=re.sub(r'^- Video: \[video\.mp4\]\(media/video\.mp4\)\n?','',text,flags=re.M)
        text=re.sub(r'^- Local `video\.mp4` is a credited copy.*\n?','',text,flags=re.M)
        block='## Media\n\n'+'\n\n'.join(md)+'\n\n'
        if re.search(r'^## Media\s*$',text,re.M):
            text=re.sub(r'^## Media\s*\n.*?(?=^## |\Z)',lambda _:block,text,count=1,flags=re.M|re.S)
        else:
            text=text.rstrip()+'\n\n'+block
        page.write_text(text.rstrip()+'\n',encoding='utf-8')


def main():
    catalog=json.loads((ROOT/'docs/data/community-cases.json').read_text(encoding='utf-8'))
    for group in catalog.values():
        if isinstance(group,list):
            for rec in group: refresh_case(rec)
    write_browser_registry()
    print('Case media sections refreshed; provenance, prompts, and original archive files preserved')

if __name__=='__main__': main()
