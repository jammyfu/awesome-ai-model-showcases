#!/usr/bin/env python3
"""Coverage, preservation and rendering checks; not a human linguistic review."""
from __future__ import annotations
import copy
import json
import re
import unittest
from case_localization import ROOT, FILES, LOCALES, STATUS, all_rows, attach_translations, dictionary, fenced, localized


class LocalizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT/'docs/data/community-cases.json').read_text())
        cls.rows = all_rows(cls.catalog)

    def test_complete_field_locale_coverage(self):
        self.assertEqual(self.catalog['meta']['localization']['case_count'], len(self.rows))
        self.assertEqual(self.catalog['meta']['localization']['status'], STATUS)
        for row in self.rows:
            self.assertEqual(set(row['translations']), set(LOCALES), row['id'])
            self.assertEqual(row['translation_status'], STATUS)
            for field in FILES:
                source = row.get(field) or ''
                for lang in LOCALES:
                    value = row['translations'][lang][field]
                    if source:
                        self.assertEqual(value, dictionary(field)[source][lang], (row['id'], field, lang))
                        self.assertTrue(value.strip())
                    else:
                        self.assertEqual(value, '', (row['id'], field, lang))

    def test_collection_site_descriptions_follow_locale(self):
        from write_community_catalog import format_collection_sites
        data = json.loads((ROOT/'playbooks/research/showcase-collection-sites.json').read_text())
        translations = json.loads((ROOT/'data/collection-site-translations.json').read_text())['entries']
        for lang in LOCALES:
            output = format_collection_sites(data, lang=lang)
            for original in {r['description'] for group in data['by_family'].values() for r in group}:
                self.assertIn(translations[original][lang], output)

    def test_original_fields_are_not_rewritten(self):
        catalog = copy.deepcopy(self.catalog)
        before = {r['id']: {k: v for k,v in r.items() if k not in {'translations','translation_status','translation_page'}} for r in all_rows(catalog)}
        attach_translations(catalog)
        after = {r['id']: {k: v for k,v in r.items() if k not in {'translations','translation_status','translation_page'}} for r in all_rows(catalog)}
        self.assertEqual(before, after)

    def test_source_edits_require_fresh_translation(self):
        catalog = {'meta': {}, 'cases': [{'id':'test', 'title':'A changed source that has no translation'}]}
        with self.assertRaisesRegex(ValueError, 'Missing title translations'):
            attach_translations(catalog)

    def test_coverage_report(self):
        data = json.loads((ROOT/'docs/data/translation-coverage.json').read_text())
        for field, coverage in data['fields'].items():
            expected = sum(bool(r.get(field)) for r in self.rows)
            self.assertEqual(coverage['source_cases'], expected)
            for lang in LOCALES:
                self.assertEqual(coverage['locales'][lang], {'complete':expected,'missing':0})

    def test_markdown_reader_preserves_original_and_all_locales(self):
        for row in self.rows:
            text = (ROOT/row['translation_page']).read_text()
            self.assertIn(fenced(row.get('original_prompt') or ''), text)
            self.assertIn(fenced(row.get('model_claim') or ''), text)
            for lang in LOCALES:
                self.assertIn(f'<a id="{lang.lower()}"></a>', text)
                prompt = row['translations'][lang]['original_prompt']
                if prompt:
                    self.assertIn(fenced(prompt), text)

    def test_prompts_are_full_text_not_short_summaries(self):
        for source, translations in dictionary('original_prompt').items():
            for lang, value in translations.items():
                if len(source) >= 1000:
                    self.assertGreater(len(value), len(source) * .25, (source[:80], lang))
                # Explicit request values and API identifiers must survive translation.
                for token in re.findall(r'\b(?:\d+(?:\.\d+)?(?:px|fps|ms)|[a-z]+_[a-z_]+)\b', source):
                    self.assertIn(token, value, (source[:80], lang, token))

    def test_markdown_fence_cannot_be_closed_by_source(self):
        source = '```\n<script>alert(1)</script>\n````'
        self.assertTrue(fenced(source).startswith('`````text\n'))

    def test_readme_case_fields_follow_locale(self):
        from write_community_catalog import md_table, HEADERS_FOR
        from readme_presentation import _compact_line
        row = next(r for r in self.rows if r['id']=='x-gorden-sun-rice-gif')
        for lang in LOCALES:
            table = md_table([row], headers=HEADERS_FOR[lang], lang=lang)
            title = localized(row, 'title', lang)
            self.assertIn(title[:40], table)
            self.assertIn(f'#{lang.lower()}', table)
            self.assertIn(title, _compact_line(row,lang))

if __name__=='__main__':
    unittest.main()
