#!/usr/bin/env python3
"""Keep generated landing pages bounded, navigable, localized, and source-faithful."""
import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit
from readme_presentation import DISCOVERY_ORDER, HOMEPAGE_FAMILIES, VERSION_ORDER, _date_desc, _full_day, family_sections, latest_section, main_case_rows, version_anchor, source_spotlights

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ('en', 'zh-CN', 'zh-TW', 'ja')


def readme_path(lang):
    return ROOT / ('README.md' if lang == 'en' else f'README.{lang}.md')


def anchors(text):
    found = set(re.findall(r'<a id="([^"]+)"', text))
    # Local targets use simple headings or explicit IDs. GitHub prefixes DOM IDs
    # with user-content-, but fragments use the unprefixed spelling.
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        heading = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        found.add(heading)
    return found


class ReadmePresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / 'docs/data/community-cases.json').read_text())
        cls.rows = main_case_rows(cls.catalog)

    def test_landing_pages_are_bounded_and_have_the_same_navigation(self):
        expected = None
        for lang in LOCALES:
            text = readme_path(lang).read_text()
            self.assertLessEqual(len(text.splitlines()), 280, lang)
            self.assertLessEqual(len(text.encode()), 30 * 1024, lang)
            self.assertEqual(len(re.findall(r'^# ', text, re.M)), 1)
            self.assertEqual(text.count('<table>'), 6, lang)
            self.assertNotIn('|---', text, lang)
            self.assertEqual(text.count('<!-- readme-tech-visualizer:start -->'), 1)
            self.assertEqual(text.count('<!-- readme-tech-visualizer:end -->'), 1)
            self.assertLess(text.index('github.io/'), text.index('id="examples"'))
            self.assertLess(text.index('id="examples"'), text.index('id="showcase"'))
            self.assertIn('src="assets/brand/hero.png"', text)
            self.assertLess(text.index('assets/brand/hero.png'), text.index('# Awesome'))
            opening = text.split('<a id="showcase">')[0]
            self.assertNotIn('/media/01-gif.gif', opening)
            self.assertNotIn('ailingqu', opening)
            for row in source_spotlights()['cases']:
                self.assertIn(f'src="{row["image_path"]}"', opening)
                self.assertIn(row['prompt_url'], opening)
                self.assertIn(row['source_code_url'], opening)
                self.assertIn(row['locales'][lang]['alt'], opening)
            self.assertIn('Claude Opus 5.5', opening)
            self.assertIn('3,434', opening)
            self.assertLess(text.index('id="showcase"'), text.index('id="how-to-use"'))
            actual = set(re.findall(r'<a id="([^"]+)"', text))
            if expected is None:
                expected = actual
            self.assertEqual(actual, expected, lang)
            self.assertIn(str(self.catalog['meta']['counts']['main_collected']), text)
            self.assertIn(f'docs/catalog.{lang}.md', text)
            for locale in LOCALES:
                self.assertIn(readme_path(locale).name, text)

    def test_three_examples_per_family_and_five_dated_posts(self):
        for lang in LOCALES:
            family = family_sections(self.catalog, lang)
            self.assertEqual(family.count('docs/translations/'), 3 * len(HOMEPAGE_FAMILIES))
            for family_id in HOMEPAGE_FAMILIES:
                self.assertIn(f'id="{family_id}"', family)
                self.assertIn(f'catalog.{lang}.md#{family_id}', family)
            latest = latest_section(self.rows, lang)
            dates = re.findall(r'^- \*\*(\d{4}-\d{2}-\d{2})', latest, re.M)
            self.assertEqual(len(dates), 5)
            self.assertEqual(dates, sorted(dates, reverse=True))
            self.assertEqual(latest.count('docs/translations/'), 5)

    def test_table_selections_are_distinct_source_matched_and_localized(self):
        selection = json.loads((ROOT / 'data/readme-model-tables.json').read_text())
        self.assertEqual(set(selection['families']), set(HOMEPAGE_FAMILIES))
        ids = []
        for fam, entries in selection['families'].items():
            self.assertEqual(len(entries), 3)
            by_id = {r['id']: r for r in self.catalog['collected_by_family'][fam]}
            for item in entries:
                row = by_id[item['case_id']]
                ids.append(row['id'])
                self.assertEqual(item['source_url'], row['source_url'])
                for lang in LOCALES:
                    for field in ('title', 'pipeline'):
                        self.assertTrue(row['translations'][lang][field].strip())
        self.assertEqual(len(ids), len(set(ids)))
        for lang in LOCALES:
            output = family_sections(self.catalog, lang)
            self.assertEqual(output.count('<table>'), 6)
            extras = json.loads((ROOT / 'data/readme-supplemental-previews.json').read_text())['cases']
            self.assertEqual(output.count('<tr><td>'), 18 + len(extras))
            self.assertEqual(output.count('</table>'), 6)
            # Current main-catalog media has no publication grant. No banner,
            # unlicensed hotlink, or unrelated licensed thumbnail may fill the gap.
            self.assertEqual(output.count('<img'), len(extras))
            self.assertNotIn('<video', output)
            self.assertNotIn('assets/brand', output)

    def test_supplemental_previews_have_exact_grants_and_localized_fields(self):
        import hashlib
        from media_policy import is_public_asset
        path = ROOT / 'data/readme-supplemental-previews.json'
        self.assertTrue(path.exists(), 'New licensed examples need source-bound metadata')
        rows = json.loads(path.read_text())['cases']
        self.assertTrue(rows)
        self.assertEqual(len({r['image_sha256'] for r in rows}), len(rows))
        for row in rows:
            self.assertEqual(row['catalog_membership'], 'separate_source_spotlight')
            self.assertTrue(is_public_asset(row['image_path']))
            self.assertEqual(hashlib.sha256((ROOT / row['image_path']).read_bytes()).hexdigest(), row['image_sha256'])
            self.assertNotIn(row['id'], {r['id'] for r in self.rows})
            for lang in LOCALES:
                for field in ('title', 'summary', 'alt'):
                    self.assertTrue(row['locales'][lang][field].strip())
                output = family_sections(self.catalog, lang)
                self.assertIn(f'src="{row["image_path"]}"', output)
                self.assertIn(row['license_url'], output)

    def test_editorial_priorities_and_unknown_popularity_are_explicit(self):
        self.assertEqual(len(HOMEPAGE_FAMILIES), len(set(HOMEPAGE_FAMILIES)))
        self.assertEqual(VERSION_ORDER['qwen'], ('qwen4-max-preview', 'qwen4-preview', 'qwen3.8-27b'))
        self.assertTrue(_full_day(DISCOVERY_ORDER['meta']['reviewed_at']))
        self.assertTrue(DISCOVERY_ORDER['meta']['reason'])
        heat = DISCOVERY_ORDER['popularity']
        self.assertEqual(heat['status'], 'not_collected', 'Implement and test comparable popularity sorting before enabling it')
        for field in ('metric', 'source', 'observed_at', 'window'):
            self.assertIsNone(heat[field], field)
        for lang in LOCALES:
            output = family_sections(self.catalog, lang)
            qwen = output.split('<a id="qwen"></a>', 1)[1].split('<a id="deepseek"></a>', 1)[0]
            self.assertIn('x-leo114119-qwen4max-wukong-plane', qwen)
            self.assertIn(DISCOVERY_ORDER['meta']['reviewed_at'], latest_section(self.rows, lang))
            sol = output.split('<a id="gpt-code"></a>', 1)[1].split('<a id="grok"></a>', 1)[0]
            self.assertIn("x-cfenghub-gpt62sol-colosseum", sol)
            self.assertIn('GPT-6.2 Sol', sol)
            self.assertIn(" · GPT Sol**", latest_section(self.rows, lang))

    def test_date_order_is_valid_and_deterministic(self):
        for bad in ('', '2026-11', '2026-02-30', '2026-13-01', 'tomorrow'):
            self.assertFalse(_full_day(bad), bad)
        rows = [{'id': 'a', 'date': ''}, {'id': 'b', 'date': '2026-11'}, {'id': 'c', 'date': '2026-11-10'}, {'id': 'd', 'date': '2026-11-11'}, {'id': 'e', 'date': '2026-11-11'}]
        self.assertEqual([r['id'] for r in _date_desc(rows)], ['e','d','c','a','b'])
        self.assertEqual(_date_desc(rows), _date_desc(list(reversed(rows))))

    def test_spotlight_frames_are_real_licensed_and_not_catalog_duplicates(self):
        import hashlib
        from PIL import Image
        from media_policy import grants
        data = source_spotlights()
        self.assertEqual(data['source_project_count'], 1)
        self.assertEqual(data['popularity']['scope'], 'repository')
        self.assertEqual(len(data['cases']), 2)
        self.assertTrue(data['popularity']['observed_at'].endswith('Z'))
        self.assertEqual(len({r['image_sha256'] for r in data['cases']}), 2)
        for row in data['cases']:
            self.assertNotIn(row['id'], {r['id'] for r in self.rows})
            self.assertEqual(row['catalog_membership'], 'separate_source_spotlight')
            grant = grants()[row['image_path']]
            self.assertEqual(grant['sha256'], row['image_sha256'])
            self.assertEqual(hashlib.sha256((ROOT/row['image_path']).read_bytes()).hexdigest(), row['image_sha256'])
            self.assertIn(row['source_revision'], row['image_source_url'])
            self.assertIn(row['source_revision'], row['license_evidence_url'])
            self.assertIn('Copyright (c) 2026 Vincentwei1021', (ROOT/row['local_license_path']).read_text())
            with Image.open(ROOT/row['image_path']) as im:
                self.assertEqual(im.size, (1920, 1080))
                im.verify()

    def test_full_catalog_preserves_every_main_case_and_version(self):
        for lang in LOCALES:
            text = (ROOT / f'docs/catalog.{lang}.md').read_text()
            for row in self.rows:
                self.assertIn(row['source_url'], text, (lang, row['id']))
                self.assertIn(f"translations/{row['id']}.md#{lang.lower()}", text, (lang, row['id']))
            for family_id in HOMEPAGE_FAMILIES:
                self.assertIn(f'id="{family_id}"', text)
                for version in VERSION_ORDER[family_id]:
                    self.assertIn(f'id="{version_anchor(version)}"', text)
            self.assertIn('ailingqu', (ROOT/'collections/gpt-image-gifs/README.md').read_text())

    def test_all_landing_page_links_and_fragments_resolve(self):
        for lang in LOCALES:
            path = readme_path(lang)
            text = path.read_text()
            urls = re.findall(r'\[[^\]]*\]\(([^)]+)\)', text) + re.findall(r'(?:href|src)="([^"]+)"', text)
            for url in urls:
                parts = urlsplit(url)
                if parts.scheme or parts.netloc:
                    continue
                target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
                self.assertTrue(target.exists(), (lang, url))
                if parts.fragment and target.suffix == '.md':
                    self.assertIn(unquote(parts.fragment), anchors(target.read_text()), (lang, url))


if __name__ == '__main__':
    unittest.main()
