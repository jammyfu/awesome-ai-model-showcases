# Git Project Harness review — 2026-11-12

## Baseline and scope

PR #16 merged by explicit owner request to main `01bf3e351e6c9728f857e19609647c203dd06b1a`. Its tree matches the locally verified `846f0cc676939c249002e825f8f727c4ce22296d`; exact-head PR CI passed. Actual main README review found eight loaded work images: two at 720px and six at 213px. Pages deployment run 43126825593 completed for the same main SHA, and the live catalog was inspected. This is deployment provenance, not a claim of a byte-level live-site comparison.

Optimization runs on an independent branch, with a clean starting tree and no parallel uncommitted changes. Sources: [CoderSkills Git Project Harness](https://github.com/jammyfu/CoderSkills/tree/c2b79a54c92eef8d7dbab41f5ae0bc186e8c4ef5/skills/git-project-harness), its README, prioritization, and verification contracts. No repository settings, topics, analytics or tracking are changed.

## Reader-facing improvement

The existing eight licensed works become discoverable in four static large-image pages, linked before the README's opening films and from the website's main action area. Existing model tables remain. A model jump navigation, clear work-type labels, descriptions, original-image link, source and grant links let readers inspect actual results rather than squint at the 213px table thumbnails. Still previews are not passed off as playable demos. No new artwork is generated or copied; original reviewed bytes and permissions remain unchanged. The 183 main records and 51-case archive counts remain distinct from the supplemental works.

The main catalog's two interface languages are unchanged. The new gallery has four fully localized content/UI pages; AI translation and source-reported model attribution remain explicit. Current comparable heat is unknown, so family ordering is editorial, not a star-based trend claim.

## Verification boundaries

- Test-first gallery structure check failed before generation, then passed for eight distinct results, all four locales and direct source/permission links.
- Browser regression covers four gallery languages at 1280px and 390px, all image decodes, useful rendered width, no horizontal document overflow, model anchor navigation, and source fallback when a preview fails. CI retains screenshots for visual review.
- Local browser execution attempted with permitted local sockets; the current runtime's Playwright browser executable is missing. CI is the execution path, not a claimed local browser pass.
- Full local `python3 tools/verify.py`: passed, including 14 presentation tests, gallery metadata checks, publication rights/build, localization, JavaScript smoke tests and 1,267 document links. New-branch CI and screenshot review: pending.
- Independent review caught and fixed Chinese-entry routing and raw-Markdown credit anchors. Main-site language switching now selects the matching gallery; credit links target rendered GitHub anchors.
- GitHub README narrow layout remains unverified; gallery responsive tests are not GitHub sanitizer tests.
- Original media totals about 10.5 MB across README references. Images use lazy loading below the first result in the new gallery; no compression or payload reduction is claimed.

New changes require review in a separate PR; the earlier merge authorization is not assumed to approve this optimization PR.

## First exact-head CI and visual follow-up

Commit f86c13d passed CI run 43127865263, including all 1280/390px gallery checks. Downloaded screenshots showed readable English, eight real images and no clipping/overflow, but CJK glyphs were missing from the runner fonts. This is not counted as multilingual visual acceptance. CI now installs the official Noto CJK font package before screenshots. Independent GitHub review confirmed all four README languages and eight images, and requested moving the all-family gallery entrance above the Claude heading; that placement is corrected with a regression assertion.

## Responsive follow-up

The owner's follow-up asks for fully adaptive pages. The test matrix now covers 320, 390, 768 and 1280 CSS pixels, every licensed-gallery language, both main-catalog UI languages, plus appendix and translated-case routes. Added checks exercise navigation visibility/bounds, searches, filters, empty results, images, anchors and source fallback. On phone/tablet the wide catalog becomes labeled stacked records; every label follows the selected language. Navigation wraps instead of hiding destinations, search fields can shrink, and checkbox controls no longer inherit search-field sizing. The original image bytes, rights, model labels and catalog totals are untouched.

GitHub README layout belongs to GitHub's renderer. Repository CSS cannot force its HTML tables into stacked cards or guarantee behavior in every GitHub client. The prominent four-language large-gallery entry is the controlled responsive alternative. A finite viewport/browser test matrix is not a claim of universal 100% compatibility.

Final responsive CI and screenshots: pending.

The six GitHub README tables are now single-column case blocks: preview above introduction, with percentage-width tables/images instead of a fixed 240px preview column. This preserves the table structure and all evidence while removing the competing side-by-side columns. Automated structure tests cover all four languages; actual GitHub mobile rendering remains a separate required check.
