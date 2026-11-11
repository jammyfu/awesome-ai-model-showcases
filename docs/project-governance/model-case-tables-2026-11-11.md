# Model case tables review — 2026-11-11

## Change and boundaries

Based on merged PR #15 (`d908536`), preserve the hero and both original Claude film frames. Replace each model's one-line navigation example with a two-column table: a 240px preview column, plus a combined localized introduction and exact model/creator/source column. Choose three distinct existing catalog subjects per family (18 total) via `data/readme-model-tables.json`. Their missing publication grants remain visible source-only entries, not claimed embedded thumbnails.

Add three separate licensed still-image spotlights: Gemini/Imagen valley, Grok Aurora lunar rider, and Qwen-Image-2.1 snowy street. These are accurately labeled older/image models, not substitutions for the current coding-model cases. Main catalog stays 183, GPT Image archive stays 51. No new animation or generation is claimed. This change is a draft PR, not a merge or deployment authorization.

## Preview review

Three new original WebPs were examined at full resolution by implementation and independent review. They are visibly different works: mountain valley, lunar astronaut/horse, and snow-covered urban street. Original signatures/watermarks remain. Qwen is intentionally a night scene, but buildings, pedestrians and snow are clearly visible. No exact duplicate hashes; distinctness also checked visually. Exact sources/hashes and four-language alt text are in `data/readme-supplemental-previews.json`.

Coverage across the README: Claude 2 existing licensed stills in the opening; Gemini 1 new still; GPT Sol 0; Grok 1 new still; Qwen 1 new still; DeepSeek 0. The 18 existing catalog table rows are source-only. All approved animation media elsewhere remains unchanged (8 playable GIFs); still-image review does not claim playback.

## Rejected candidates and remaining gaps

- James Greene model animation archive: no explicit artwork reuse grant, despite accessible generated results.
- Atelier GPT Sol loops: normal software MIT only, not explicit media permission.
- Rapidata SVG benchmark: licensing text excludes SVG/PNG outputs from its prompt-data CC-BY grant.
- Tihu: CC-BY covers records/comments, not the output SVGs.
- Grok Summer Engine candidate: cached CC0 text conflicts with the current live page, so not used.
- Gemini floating lettering: rejected as logo-like rather than an attractive case result.
- GPT-5.6 Sol Sadeyağ flowchart on Commons: affirmative CC BY-SA license, but transparent black artwork becomes invisible in dark mode, upstream labels are slightly clipped, and the full diagram is illegible at table size. No poor thumbnail is published merely to fill the model slot.
- DeepSeek: no qualifying explicitly licensed creative preview found. Remains an open media gap.

Gemini version evidence is inconsistent (current 4.0 versus initial upload summary 3.0); that uncertainty is visible in every language. Model attribution for all examples is source-reported, not independently rerun.

## Localization and rights

All 18 selected catalog rows use existing source-bound title and pipeline translations: 18 titles and 18 introductions per locale (en, zh-CN, zh-TW, ja). Three supplemental works add 3 titles, 3 summaries, 3 alt descriptions and 3 modification notices per locale. Creator names, model identifiers and original license/evidence records are preserved, not translated into new claims. New display labels and source-only notices are localized. Text is AI-translated and not independently human-reviewed.

Supplemental files have exact-hash grants in `data/public-media-rights.json`, full license texts and visible source/credit/modification links in `docs/readme-preview-credits.md`. Qwen's underlying photo credit and ShareAlike obligation remain explicit. The README does not silently fill a missing preview with a model logo or another case's result.

## Validation

Initial actual GitHub review found the three-column layout squeezed images to 108–119px on the desktop repository page and 75–100px on a Chinese blob page with the sidebar open. The layout was revised to two columns with a 240px preview column, and regression assertions now require that structure.

- Tests first: original implementation failed assertions for six tables and 18 rows; supplemental test failed until licensed metadata existed.
- Presentation suite: 9 tests passed after table generation and credit-page integration.
- `python3 tools/verify.py`: passed on the staged final source and generated outputs (including rights checks, public build, catalog/localization tests, JavaScript smoke tests and 1,267 local Markdown document checks). An earlier unstaged run stopped at generator-diff protection, not a test defect.
- Actual GitHub desktop layout at `fbcfc493`: English branch README and Chinese blob page reviewed at 1165px viewport. All three new images loaded and displayed at 213px wide (116/160/163px high), with 239px preview cells and 723px tables. No internal horizontal overflow; long English and Chinese titles wrapped. The former 75–119px preview-width defect is fixed.
- Narrow/mobile layout: not run. The available browser session had no supported viewport resize control, and keyboard zoom did not change the viewport. No physical-device or narrow-window pass is claimed.
- No local Chromium is installed. Repository CI browser suite checks the existing built Pages app, not the actual GitHub README layout.
- Actual new media playback: not applicable; all three are still images.
- No merge/deployment performed by this change.
