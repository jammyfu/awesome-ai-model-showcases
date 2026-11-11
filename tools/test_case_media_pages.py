#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path

class CaseMediaPageTests(unittest.TestCase):
    def test_replaces_media_without_touching_provenance_or_prompt(self):
        from render_public_media import refresh_case
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); folder=root/'docs/cases/test';folder.mkdir(parents=True)
            html='<h1>Title</h1><p>Author and model evidence</p><h2>Media</h2><video src="media/video.mp4"></video><h2>Prompt</h2><pre>Verbatim &lt;source&gt; prompt</pre>'
            markdown='# Title\n\nModel evidence retained\n\n## Media\n\n![preview](media/x.gif)\n\n## Prompt\n\nVerbatim prompt\n\n- Video: [video.mp4](media/video.mp4)\n'
            (folder/'index.html').write_text(html);(folder/'README.md').write_text(markdown)
            rec={'id':'test','source_url':'https://example.org/original','local_files':[]}
            refresh_case(rec,root)
            out=(folder/'index.html').read_text();md=(folder/'README.md').read_text()
            self.assertNotIn('<video',out);self.assertNotIn('media/',md)
            self.assertIn('https://example.org/original',out)
            self.assertIn('<pre>Verbatim &lt;source&gt; prompt</pre>',out)
            self.assertIn('Model evidence retained',md)
            refresh_case(rec,root)
            self.assertEqual(out,(folder/'index.html').read_text())
            self.assertEqual(md,(folder/'README.md').read_text())

if __name__=='__main__': unittest.main()
