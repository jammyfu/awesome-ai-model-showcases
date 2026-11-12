import json
import unittest
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
class Tags(HTMLParser):
    def __init__(self):super().__init__();self.images=[];self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='img':self.images.append(a)
        if tag=='a':self.links.append(a.get('href'))
class GalleryTests(unittest.TestCase):
    def test_eight_distinct_authorized_results_in_all_locales(self):
        rows=sum([json.loads((ROOT/'data'/f).read_text())['cases'] for f in ['readme-featured-cases.json','readme-supplemental-previews.json']],[])
        for lang in ('en','zh-CN','zh-TW','ja','ko'):
            p=ROOT/f'docs/licensed-gallery.{lang}.html'
            self.assertTrue(p.exists())
            text=p.read_text(); tags=Tags();tags.feed(text)
            self.assertEqual(len(tags.images),len(rows));self.assertEqual(len({i['src'] for i in tags.images}),len(rows))
            self.assertIn(f'<html lang="{lang}">',text)
            for row in rows:
                self.assertIn(row['locales'][lang]['title'],text)
                self.assertIn(row['source_url'],tags.links)
                self.assertIn(row['license_evidence_url'],tags.links)
                if row.get('model_family'):
                    self.assertIn('https://github.com/jammyfu/awesome-ai-model-showcases/blob/main/docs/readme-preview-credits.md#'+row['id'],tags.links)
            for other in ('en','zh-CN','zh-TW','ja','ko'):self.assertIn(f'licensed-gallery.{other}.html',tags.links)
            self.assertTrue(all(x.get('alt') and x.get('width') and x.get('height') for x in tags.images))
            self.assertNotIn('<video',text)
if __name__=='__main__':unittest.main()
