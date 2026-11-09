#!/usr/bin/env python3
"""Keep source claims, prompt scope and licensing intact during expansion."""
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import ingest_local_media
from write_community_catalog import from_web, md_table, HEADERS_EN


def source():
    return {'id':'test-loop','playbook':'Example','author':'Example creator','source_url':'https://example.org/source','media_url':'https://example.org/loop.gif','prompt':'This deliberately long published excerpt must never be mistaken for the full original prompt.','prompt_status':'短/部分','prompt_provenance':'Published excerpt only; the complete request is at source.','model_claim':'Creator reports 2.6','model_evidence_url':'https://example.org/results','pipeline':'Source-reported GIF','verification':'Frames checked, generation not reproduced','license_label':'CC BY 4.0','license_url':'https://creativecommons.org/licenses/by/4.0/','license_conclusion':'Creator licenses prompts and example GIFs under CC BY 4.0.'}


def main():
    item=source(); rec=from_web(item)
    assert rec['prompt_status']=='短/部分', 'Do not infer full provenance from text length'
    for key in ('prompt_provenance','model_evidence_url','license_label','license_url'):
        assert rec[key]==item[key], key
    assert rec['pipeline']==item['pipeline'] and rec['verify']==item['verification']
    assert rec['generation_verified'] is False
    table=md_table([rec],HEADERS_EN)
    assert 'CC BY 4.0' in table and 'Short / partial' in table
    rec.update(prompt_status='source_only',prompt_url='https://example.org/prompt')
    assert '[Published at source](https://example.org/prompt)' in md_table([rec],HEADERS_EN)
    with TemporaryDirectory() as temp, patch.object(ingest_local_media,'CASES',Path(temp)):
        ingest_local_media.case_docs(item['id'],{**item,'title':item['playbook'],'original_prompt':item['prompt'],'verify':item['verification'],'license_notes':item['license_conclusion']},[])
        d=Path(temp)/item['id']
        for name in ('README.md','index.html'):
            assert 'CC BY 4.0' in (d/name).read_text()
            assert 'License: **unknown**' not in (d/name).read_text()
        assert item['prompt_provenance'] in (d/'prompt.md').read_text()
        assert item['prompt'] in (d/'prompt.md').read_text()
    print('catalog expansion guards ok: evidence, prompt scope and source license')

if __name__=='__main__': main()
