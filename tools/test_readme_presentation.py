#!/usr/bin/env python3
"""Keep generated landing pages bounded, navigable, localized, and source-faithful."""
import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit
from readme_presentation import DISCOVERY_ORDER, HOMEPAGE_FAMILIES, VERSION_ORDER, _date_desc, _full_day, family_sections, latest_section, main_case_rows, version_anchor

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
            self.assertNotIn('<table', text, lang)
            self.assertNotIn('|---', text, lang)
            self.assertEqual(text.count('<!-- readme-tech-visualizer:start -->'), 1)
            self.assertEqual(text.count('<!-- readme-tech-visualizer:end -->'), 1)
            self.assertLess(text.index('github.io/'), text.index('id="examples"'))
            self.assertLess(text.index('id="examples"'), text.index('id="showcase"'))
            self.assertEqual(text.count('/media/01-gif.gif'), 3)
            self.assertEqual(text.count('/prompt.md'), 3)
            self.assertIn('CC BY 4.0', text)
            self.assertLess(text.index('id="how-to-use"'), text.index('id="showcase"'))
            actual = set(re.findall(r'<a id="([^"]+)"', text))
            if expected is None:
                expected = actual
            self.assertEqual(actual, expected, lang)
            self.assertIn(str(self.catalog['meta']['counts']['main_collected']), text)
            self.assertIn(f'docs/catalog.{lang}.md', text)
            for locale in LOCALES:
                self.assertIn(readme_path(locale).name, text)

    def test_one_example_per_family_and_five_dated_posts(self):
        for lang in LOCALES:
            family = family_sections(self.catalog, lang)
            self.assertEqual(family.count('docs/translations/'), len(HOMEPAGE_FAMILIES))
            for family_id in HOMEPAGE_FAMILIES:
                self.assertIn(f'id="{family_id}"', family)
                self.assertIn(f'catalog.{lang}.md#{family_id}', family)
            latest = latest_section(self.rows, lang)
            dates = re.findall(r'^- \*\*(\d{4}-\d{2}-\d{2})', latest, re.M)
            self.assertEqual(len(dates), 5)
            self.assertEqual(dates, sorted(dates, reverse=True))
            self.assertEqual(latest.count('docs/translations/'), 5)

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

    def test_date_order_is_valid_and_deterministic(self):
        for bad in ('', '2026-11', '2026-02-30', '2026-13-01', 'tomorrow'):
            self.assertFalse(_full_day(bad), bad)
        rows = [{'id': 'a', 'date': ''}, {'id': 'b', 'date': '2026-11'}, {'id': 'c', 'date': '2026-11-10'}, {'id': 'd', 'date': '2026-11-11'}, {'id': 'e', 'date': '2026-11-11'}]
        self.assertEqual([r['id'] for r in _date_desc(rows)], ['e','d','c','a','b'])
        self.assertEqual(_date_desc(rows), _date_desc(list(reversed(rows))))

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
