# Korean localization review

Baseline: `adbad4665fc68ad594a33ac3fb6bd79824f7e0f3` (main). This is a separate draft change, not a merge or deployment. Reviewed 2026-11-12 using the project's source-preserving localization workflow.

## Scope and facts

- Added `README.ko.md`, `docs/catalog.ko.md`, `docs/licensed-gallery.ko.html`, and Korean content/navigation in the existing translated-case web reader.
- 312 unique archived records, including appendices, receive Korean titles, methods, verification notes, model evidence and every nonempty collected prompt. The authoritative per-field counts and zero-missing checks are in `docs/data/translation-coverage.json`.
- 311 distinct titles, 87 methods, 54 verification statements, 129 model-evidence strings, 68 prompt bodies and 13 collection-site descriptions translated. The eight licensed works have Korean title, summary and alt text, plus existing modification statements where applicable.
- The main catalog remains 183 cases, with 51 separate GPT Image cases. Translations, eight supplemental/spotlight works and pending records are not new main cases.
- Original source keys/text and all prior language translations were compared against the baseline and remain unchanged. URLs, model identifiers, numbers, requested output text and code identifiers are retained. Existing truncated source text stays truncated; no missing prompt was invented.
- All assets, their hashes, source identities, license evidence and ordering inputs are unchanged. AI translation is not source verification, generation reproduction or a new rights grant. Existing rights limitations continue to apply.
- Shared discovery ordering is retained. Comparable recent popularity remains unknown; the dated source-repository star snapshot is not refreshed or presented as per-film popularity.

## Language review

**AI-translated; not human-reviewed.** A second AI pass reviewed the README, licensed artwork descriptions and visible Korean UI against their source meaning. It refined license wording, source sanitization terminology and a Korean particle. This is not native-speaker certification. Tests check completeness and invariants, not linguistic quality.

## Verification

- **Passed:** `python3 tools/verify.py`, including deterministic regeneration, all existing Python/JavaScript validators, source-preservation checks, exact approved media hashes, public-artifact build and 1,269 generated Markdown/local-link checks.
- **Passed:** five-language README static checker, zero errors. Korean README is 35,368 bytes, within this project's 35 KiB budget.
- **Passed:** dedicated localization (9), presentation (14) and gallery (1) Python tests; JavaScript reader verifies all five locales and unchanged originals.
- **Blocked locally:** Playwright's bundled Chromium is absent. System `/usr/bin/chromium` exists, but launching it fails with `socket() failed: Operation not permitted`, including a permitted escalation retry. No local browser-render, playback or screenshot success is claimed.
- **Pending CI:** the existing real-browser test now includes Korean at 320/390/768/1280 px, image decoding, language navigation, unchanged original prompts and Korean reader text. Optional `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` supports environments with a system browser; CI retains its pinned Playwright install.
- **Not checked:** actual GitHub-rendered Korean README in desktop/narrow view, live deployed Korean pages and human linguistic review. These remain review gates, not implied by static tests.

## Explicit boundaries

The main searchable gallery UI remains English/Simplified Chinese, just as before this change. Korean has a separate licensed-work gallery, complete Markdown catalog and web case reader. Navigation discloses English fallback to the main catalog. The GPT Image archive landing page and historical research/provenance documents retain their existing languages; its collected case fields and prompts are available in the five-language reader. No About/Topics settings, new media copies, merges or deployments were performed.
