# A source-first README pattern

A reusable pattern for collection projects, based on Awesome AI Model Showcases. Adapt the information hierarchy, not this project's model names, counts, rights claims, or repository paths. This is a documentation design, not a promise of search ranking or traffic.

## The reading path

1. **Visible project identity.** Keep an approved wide project hero visibly at the top when requested. A working asset file without a README reference is not a displayed hero. **Identity and outcome.** One H1 using the project name, one concrete sentence describing what readers can do, and language links.
2. **A real next action.** Link to the live gallery, working demo, documentation, or smallest executable command appropriate to the project. A collection's first action is browsing, not installation.
3. **Actual results, distinct from branding.** A collection needs representative, licensed case screenshots after its brand header. Do not substitute an unrelated licensed appendix just because those files are available. Give it useful alt text. Label concept art as concept art; do not present it as product or model-output evidence. Avoid oversized icons or repeated banners that push actual work away.
4. **A short reader journey.** Explain how to find, inspect, and use the material, including limitations that affect the reader's decision.
5. **Balanced discovery.** Give every category a bounded entry with counts and a complete-catalog link. If one category grows tenfold, the landing page should not grow tenfold. Explicitly distinguish editorial selection, recency, and ranking.
6. **Progressive detail.** Put evidence tables, exhaustive records, changelogs, and maintenance procedures on named pages. Use expandable sections for secondary setup, not to hide the entire dataset inside the README's HTML.
7. **Contribution and trust.** Include a clear contribution route, source/rights boundaries, supported languages, and a correction or removal channel.

## Concrete split in this repository

- `README*.md`: four generated landing pages, each under 280 lines and 30 KiB. The project hero is followed by actual Claude film frames with direct watch, prompt and source links; family navigation and at most five recent source posts support discovery. The limits are project-specific budgets, not universal README rules.
- `catalog.<locale>.md`: complete localized evidence tables, version anchors, and separate appendices. No new cases or altered source claims are needed to shorten the landing page.
- [showcase-index.md](showcase-index.md): work-type discovery and a complete index. Type tags describe the current inventory, not all model capabilities.
- [data/community-cases.json](data/community-cases.json): shared generated case data, not hand-edited content.
- [CONTRIBUTING.md](../CONTRIBUTING.md): authoring and verification workflow.
- [MEDIA_RIGHTS.md](../MEDIA_RIGHTS.md): media publication rules, distinct from the code license.

## Authoring contract

Update [the four templates](../tools/templates/) and [presentation helpers](../tools/readme_presentation.py), then run [the existing generator](../tools/write_community_catalog.py). Keep the generated-file warning and the `readme-tech-visualizer` start/end markers exactly once. Do not hand-edit generated README or catalog files.

Preserve stable anchors when moving sections. Links to a family or version should still lead to a useful entry with a route to all records. Source-date ordering requires full valid dates, a documented tie-breaker, and a defined place for unknown dates. Never rename source dates as ingestion dates.

Keep source text, claims, IDs, creator credits, and URLs intact. The landing page may summarize, but the full evidence must remain discoverable. Generated counts must come from the same inventory across languages. Do not fill empty categories, create imitation results, or imply unavailable prompts exist.

## Reuse checklist

- Verify capabilities and commands from source/configuration, not marketing language already in the README.
- Select one primary action and avoid redundant menus. Badges must describe useful, verified facts; neither three badges nor an installation command is mandatory.
- Use natural descriptive terms in the title and opening, plus descriptive links. Keep About, topics, README, and `llms.txt` consistent when those surfaces are in scope. Do not stuff keywords, fabricate metadata, change repository settings without authorization, or claim ranking gains without measured evidence.
- Translate the complete landing-page interface, numbers, boundaries, alt text, and example labels. Do not infer application-language support from translated README files. Preserve original evidence and disclose translation review status.
- Check attribution and exact media rights. A source link, public post, or download is not a license. Retain clear source-only fallbacks.
- Validate local paths, fragment anchors, locale links, sample bounds, counts, ordering, and generator idempotence. Regeneration must not rewrite unrelated source facts.
- Inspect real GitHub rendering on desktop and mobile, including dark mode, language switching, collapsible sections, and long titles. A local Markdown preview is useful but does not prove GitHub rendering.
- Record checks as passed, failed, blocked, or not run. Distinguish local preview, live repository, and deployed-site checks; identify the tested revision. A source diff is not visual verification.

## Verification here

Run `python3 tools/verify.py` after reviewing and staging intentional generated updates. `tools/test_readme_presentation.py` enforces the landing-page budgets, bounded samples, live local fragments, source dates, version coverage, and locale structure. Use `RUN_BROWSER_TESTS=1 python3 tools/verify.py` for the existing gallery browser suite when Playwright and Chromium are available. That suite is separate from GitHub README visual review.

### Popularity and important-version ordering

Within each relevant category, honor explicit user focus and important current platforms/versions. When comparable popularity measurements exist, record metric, source, observation time, window, and reason before ranking. Missing measurements are unknown, not zero; do not confuse recency, repository stars, or archive coverage with popularity. Disclose editorial fallback. Keep shared priorities and tie-breakers consistent across all locales. See the [current ordering policy](discovery-order.md).

### Case collections are not software landing pages

For a showcase collection, lead the first substantive section with actual case results, accessible prompts, creator credits, and sources. Navigation and category balance support those examples rather than displace them. Use only licensed or otherwise authorized media, clearly identify the true model/subcollection, and do not count those examples twice. When a frontier case is source-only, keep its source route rather than borrowing another model’s result image. Compression is a guardrail, not the goal: measure whether visitors find an interesting result and its evidence, not just the README byte count.

A modest star invitation may follow demonstrated value. Measure baseline and subsequent repository views, unique visitors, referral sources, and stars over a comparable window where authorized analytics are available. Distinguish association from causation; do not promise ranking or star growth.
