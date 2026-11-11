#!/usr/bin/env python3
"""Public renderers must require exact-asset permission, not download/credit."""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import write_community_catalog as catalog
import ingest_local_media as ingest

class PublicCatalogTests(unittest.TestCase):
    def test_unknown_downloads_never_become_public(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            case = root / 'docs/cases/example'
            case.mkdir(parents=True)
            (case / 'README.md').touch()
            (root / 'unknown.mp4').touch()
            manifest = root / 'manifest.json'
            manifest.write_text(json.dumps({'files':[{'case_id':'example','ok':True,'local_path':'unknown.mp4','ext':'mp4'}]}))
            images = root / 'images.json'
            images.write_text(json.dumps({'cases':[{'id':'example','download':'saved','thumb':'unknown.jpg','image_url':'https://example.org/raw.jpg'}]}))
            videos = root / 'videos.json'
            videos.write_text(json.dumps({'cases':[{'id':'example','video':'unknown.mp4'}]}))
            rows = [{'id':'example','source_url':'https://example.org/post','license_label':'CC BY 4.0'}]
            with patch.multiple(catalog, ROOT=root, LOCAL_MANIFEST=manifest, CASE_IMAGES=images, CASE_VIDEOS=videos):
                catalog.attach_local(rows)
                catalog.apply_case_images(rows)
                catalog.apply_case_videos(rows)
            self.assertEqual(rows[0]['local_files'], [])
            self.assertEqual(rows[0]['local_preview'], '')
            self.assertEqual(rows[0]['thumb'], '')
            self.assertEqual(rows[0]['video'], '')
            self.assertEqual(rows[0]['image_url'], 'https://example.org/raw.jpg')

    def test_explicit_approved_files_get_render_permission(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            case = root / 'docs/cases/example'
            case.mkdir(parents=True)
            (case / 'README.md').touch()
            manifest = root / 'manifest.json'
            manifest.write_text(json.dumps({'files':[
                {'case_id':'example','ok':True,'local_path':'approved.gif','ext':'gif'},
                {'case_id':'example','ok':True,'local_path':'unknown.gif','ext':'gif'}]}))
            rows = [{'id':'example'}]
            with patch.multiple(catalog, ROOT=root, LOCAL_MANIFEST=manifest), patch.object(catalog, 'is_public_asset', side_effect=lambda path, **kw: path == 'approved.gif'):
                catalog.attach_local(rows)
            self.assertEqual([f['path'] for f in rows[0]['local_files']], ['approved.gif'])
            self.assertIs(rows[0]['local_files'][0]['public_allowed'], True)
            self.assertEqual(rows[0]['local_preview'], 'approved.gif')

    def test_unknown_case_docs_keep_source_not_media(self):
        with TemporaryDirectory() as temp, patch.object(ingest, 'CASES', Path(temp)):
            ingest.case_docs('test', {'source_url':'https://example.org/post'}, [{'ok':True,'local_path':'docs/unknown.gif','ext':'gif'}])
            for name in ('README.md','index.html'):
                text = (Path(temp)/'test'/name).read_text()
                self.assertNotIn('media/unknown.gif', text)
                self.assertIn('https://example.org/post', text)

if __name__ == '__main__': unittest.main()
