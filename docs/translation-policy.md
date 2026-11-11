# Case translation policy

The four README editions use one inventory: English (`en`), Simplified Chinese (`zh-CN`), Traditional Chinese (`zh-TW`), and Japanese (`ja`). The catalog interface remains English and Simplified Chinese. Its linked case reader supports all four content languages.

## What is translated

- Case titles, including pending, excluded and appendix cases.
- Production methods, verification notes and model-evidence text, with uncertainty and source claims preserved.
- Every nonempty published prompt collected in the catalog. Translations are full text, not summaries. Missing or partial source text remains missing or partial; it is not completed by the translator.
- Literal requested output captions, API names, code identifiers, URLs, model names, numbers and technical constraints retain their original meaning. Quoted text may therefore intentionally remain in another language inside a translation.

The JSON source fields are not overwritten. Separate `translations` records supply the localized views; the original source and prompt can be read alongside them. Authors, source URLs, dates, rights labels, and verification flags are not translated into different identities or stronger claims. Research notes and source documents are retained as provenance; this does not claim that every document in the repository has four translations.

## Review and rights boundaries

All new translations are marked `ai-translated-not-human-reviewed`. Structural validation checks coverage and stable rendering; it is **not** human linguistic review or verification of the original generation. A translation does not change `generation_verified`, viewing status, license, attribution or publication permission. The source's rights continue to apply to its text and translations. MIT does not grant rights to third-party prompts or media.

## Updating content

Checked-in translation dictionaries use the exact original text as their key. If a title, method, verification note, evidence quotation or prompt changes, the generator stops until translations for the new source text are supplied in all four languages. It never silently marks original-language fallback as translated.

Edit the relevant `data/case-*-translations.json` file, preserving original quoted text and source qualifiers. Then run:

```sh
python3 tools/write_community_catalog.py
python3 tools/test_case_localization.py
python3 tools/verify.py
```

The generator writes per-case original/translation Markdown pages and embeds language records in the catalog JSON/JavaScript. Generated files are not the translation source of truth. `meta.localization` and `docs/data/translation-coverage.json` record exact coverage; the validation step rejects missing, empty or inconsistent locale entries. Future human review must be recorded explicitly, never inferred from passing tests.
