#!/usr/bin/env python3
"""Rights gates and deployment payload are distinct from archival validation."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

class PublicMediaTests(unittest.TestCase):
    def fixture(self, base):
        root = Path(base)
        (root/'data').mkdir()
        (root/'docs/cases/test/media').mkdir(parents=True)
        asset = root/'docs/cases/test/media/ok.gif'
        from PIL import Image
        Image.new('RGB',(2,2),'red').save(asset,save_all=True,append_images=[Image.new('RGB',(2,2),'blue')],duration=100,loop=0)
        grant = {'path':'docs/cases/test/media/ok.gif','sha256':hashlib.sha256(asset.read_bytes()).hexdigest(),'credit':'Creator','source_url':'https://example.org/work','license':'CC BY 4.0','license_url':'https://creativecommons.org/licenses/by/4.0/','evidence_url':'https://example.org/license','changes':'Unmodified'}
        (root/'data/public-media-rights.json').write_text(json.dumps({'assets':[grant]}))
        (root/'docs/index.html').write_text('<img src="cases/test/media/ok.gif">')
        return root, asset, grant

    def test_policy_exists(self):
        self.assertTrue(Path(__file__).with_name('media_policy.py').is_file(), 'A fail-closed public rights gate must exist')

    def test_unlisted_changed_external_and_symlink_denied(self):
        from media_policy import is_public_asset
        with tempfile.TemporaryDirectory() as tmp:
            root, asset, _ = self.fixture(tmp)
            self.assertTrue(is_public_asset(str(asset.relative_to(root)),root))
            self.assertFalse(is_public_asset('https://example.org/ok.gif',root))
            self.assertFalse(is_public_asset('docs/missing.gif',root))
            self.assertFalse(is_public_asset('../outside.gif',root))
            original = asset.read_bytes(); asset.write_bytes(b'changed')
            self.assertFalse(is_public_asset('docs/cases/test/media/ok.gif',root))
            asset.unlink(); target=root/'real.gif'; target.write_bytes(original); asset.symlink_to(target)
            self.assertFalse(is_public_asset('docs/cases/test/media/ok.gif',root))

    def test_label_without_evidence_is_not_permission(self):
        from media_policy import is_public_asset
        with tempfile.TemporaryDirectory() as tmp:
            root, _, grant = self.fixture(tmp)
            grant['evidence_url']=''
            (root/'data/public-media-rights.json').write_text(json.dumps({'assets':[grant]}))
            self.assertFalse(is_public_asset(grant['path'],root))

    def test_build_excludes_unknown_assets_and_rejects_stale_embed(self):
        from build_public_site import build_site
        with tempfile.TemporaryDirectory() as tmp:
            root, _, _ = self.fixture(tmp)
            bad = root/'docs/cases/test/media/unknown.mp4'
            bad.write_text('version https://git-lfs.github.com/spec/v1\noid sha256:'+'0'*64+'\nsize 99\n')
            build_site(root,root/'site')
            self.assertTrue((root/'site/cases/test/media/ok.gif').is_file())
            self.assertFalse((root/'site/cases/test/media/unknown.mp4').exists())
            (root/'docs/index.html').write_text('<video src="cases/test/media/unknown.mp4"></video>')
            with self.assertRaisesRegex(ValueError,'unapproved|missing'):
                build_site(root,root/'bad-site')

    def test_even_allowlisted_pointer_cannot_ship(self):
        from build_public_site import build_site
        with tempfile.TemporaryDirectory() as tmp:
            root, asset, grant = self.fixture(tmp)
            asset.write_text('version https://git-lfs.github.com/spec/v1\noid sha256:'+'0'*64+'\nsize 99\n')
            grant['sha256']=hashlib.sha256(asset.read_bytes()).hexdigest()
            (root/'data/public-media-rights.json').write_text(json.dumps({'assets':[grant]}))
            with self.assertRaisesRegex(ValueError,'LFS pointer'):
                build_site(root,root/'site')

    def test_remote_embed_cannot_ship(self):
        from build_public_site import build_site
        with tempfile.TemporaryDirectory() as tmp:
            root, _, _ = self.fixture(tmp)
            (root/'docs/index.html').write_text('<img src="https://example.org/unknown.gif">')
            with self.assertRaisesRegex(ValueError,'external|unapproved'):
                build_site(root,root/'site')

    def test_indirect_image_embeds_cannot_ship(self):
        from build_public_site import build_site
        for html in ['<input type="image" src="https://example.org/x.png">', '<svg><image href="https://example.org/x.png"/></svg>', '<svg><image xlink:href="https://example.org/x.png"/></svg>']:
            with self.subTest(html=html), tempfile.TemporaryDirectory() as tmp:
                root, _, _ = self.fixture(tmp)
                (root/'docs/index.html').write_text(html)
                with self.assertRaisesRegex(ValueError,'external|unapproved'):
                    build_site(root,root/'site')

    def test_output_cannot_overwrite_checkout(self):
        from build_public_site import build_site
        with tempfile.TemporaryDirectory() as tmp:
            root, asset, _ = self.fixture(tmp)
            with self.assertRaises((ValueError,FileExistsError)):
                build_site(root,root/'docs')
            self.assertTrue(asset.exists())

if __name__ == '__main__': unittest.main()
