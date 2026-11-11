"""Source-preserving, checked-in case translations; no translation service at build time."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import json
import re
import os

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ('en', 'zh-CN', 'zh-TW', 'ja')
STATUS = 'ai-translated-not-human-reviewed'
FILES = {
    'title': 'case-title-translations.json',
    'pipeline': 'case-pipeline-translations.json',
    'verify': 'case-verification-translations.json',
    'model_claim': 'case-model-translations.json',
    'original_prompt': 'case-prompt-translations.json',
}
LABELS = {
    'en': ('English', 'AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.', 'Method', 'Verification', 'Model evidence (translation)', 'Published prompt (translation)', 'No prompt text was collected. See the source; no prompt has been invented.'),
    'zh-CN': ('简体中文', 'AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。', '做法', '核验状态', '模型依据（译文）', '公开提示词（译文）', '未收集到提示词正文。请查看来源，未编造提示词。'),
    'zh-TW': ('繁體中文', 'AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。', '做法', '核驗狀態', '模型依據（譯文）', '公開提示詞（譯文）', '未收集到提示詞內文。請查看來源，未編造提示詞。'),
    'ja': ('日本語', 'AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。', '制作方法', '検証状況', 'モデルの根拠（翻訳）', '公開プロンプト（翻訳）', 'プロンプト本文は収集されていません。出典をご確認ください。プロンプトの補作はしていません。'),
}


@lru_cache(maxsize=None)
def dictionary(field: str) -> dict:
    path = ROOT / 'data' / FILES[field]
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('schema_version') != 1 or data.get('status') != STATUS:
        raise ValueError(f'Invalid translation metadata: {path}')
    entries = data['entries']
    for source, translations in entries.items():
        if not source.strip() or set(translations) != set(LOCALES):
            raise ValueError(f'Invalid translation locales: {field}: {source[:80]!r}')
        if not all(isinstance(v, str) and v.strip() for v in translations.values()):
            raise ValueError(f'Empty translation: {field}: {source[:80]!r}')
    return entries


def all_rows(catalog: dict) -> list[dict]:
    rows = {}
    for values in catalog.values():
        if isinstance(values, list):
            for row in values:
                rows.setdefault(row['id'], row)
    return list(rows.values())


def attach_translations(catalog: dict) -> None:
    """Fail closed when collected text changes; never silently copy a foreign source."""
    rows = all_rows(catalog)
    for row in rows:
        localized = {lang: {} for lang in LOCALES}
        for field in FILES:
            source = row.get(field) or ''
            values = dictionary(field).get(source) if source else {lang: '' for lang in LOCALES}
            if values is None:
                raise ValueError(f'Missing {field} translations for {row["id"]}: {source[:100]!r}')
            for lang in LOCALES:
                localized[lang][field] = values[lang]
        row['translations'] = localized
        row['translation_status'] = STATUS
        row['translation_page'] = f'docs/translations/{row["id"]}.md'
    coverage = {
        'schema_version': 1, 'status': STATUS, 'case_count': len(rows),
        'fields': {field: {
            'source_cases': sum(bool(r.get(field)) for r in rows),
            'unique_sources': len({r[field] for r in rows if r.get(field)}),
            'locales': {lang: {
                'complete': sum(bool(r['translations'][lang][field]) for r in rows),
                'missing': sum(bool(r.get(field)) and not r['translations'][lang][field] for r in rows),
            } for lang in LOCALES},
        } for field in FILES},
    }
    (ROOT / 'docs/data/translation-coverage.json').write_text(
        json.dumps(coverage, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    catalog['meta']['localization'] = {
        'locales': list(LOCALES), 'status': STATUS, 'case_count': len(rows),
        'fields': list(FILES),
        'prompt_case_count': sum(bool(r.get('original_prompt')) for r in rows),
        'original_fields_preserved': True,
    }


def localized(row: dict, field: str, lang: str) -> str:
    lang = 'zh-CN' if lang == 'zh' else lang
    return row.get('translations', {}).get(lang, {}).get(field, row.get(field) or '')


def translation_link(row: dict, lang: str) -> str:
    path = row.get('translation_page') or ''
    return f'{path}#{lang.lower()}' if path else ''


def fenced(text: str) -> str:
    # A source can contain Markdown, XML and code. Render it verbatim, not as instructions.
    fence = '`' * (max([len(x) for x in re.findall(r'`+', text)] + [2]) + 1)
    return f'{fence}text\n{text}\n{fence}'


def write_translated_cases(catalog: dict) -> None:
    output = ROOT / 'docs/translations'
    output.mkdir(exist_ok=True)
    for row in all_rows(catalog):
        # IDs originate in validated inventories, not user URL parameters.
        if Path(row['id']).name != row['id']:
            raise ValueError(f'Unsafe case ID: {row["id"]}')
        lines = [f'# {row["id"]}', '', f'Author / 作者 / 作者 / 作者: {row.get("author") or ""}', '',
                 f'[Original source / 原帖 / 原帖 / 原投稿]({row.get("source_url") or ""})', '',
                 ' · '.join(f'[{LABELS[lang][0]}](#{lang.lower()})' for lang in LOCALES), '',
                 '## Original / 原文', '', fenced(row.get('title') or ''), '',
                 '### Model evidence / 模型依据', '', fenced(row.get('model_claim') or ''), '',
                 '### Original prompt / 原始提示词', '', fenced(row.get('original_prompt') or ''), '',
                 '### Source rights / 来源许可', '', fenced(row.get('license_notes') or ''), '']
        if row.get('local_detail') and not row['local_detail'].startswith(('http://', 'https://')):
            archived = Path(os.path.relpath(ROOT / row['local_detail'], output)).as_posix()
            lines[5:5] = [f'[Archived case / 归档案例 / 歸檔案例 / 収録事例]({archived})', '']
        for lang in LOCALES:
            label, notice, method, verification, evidence, prompt, empty = LABELS[lang]
            values = row['translations'][lang]
            lines += [f'<a id="{lang.lower()}"></a>', f'## {label}', '', notice, '',
                      fenced(values['title']), '', f'### {method}', '', values['pipeline'], '',
                      f'### {verification}', '', values['verify'], '', f'### {evidence}', '',
                      fenced(values['model_claim']), '', f'### {prompt}', '',
                      fenced(values['original_prompt']) if values['original_prompt'] else empty, '']
        (output / f'{row["id"]}.md').write_text('\n'.join(lines).rstrip()+'\n', encoding='utf-8')
