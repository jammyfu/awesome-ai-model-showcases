# Current plan

**Goal:** Improve the bilingual repository landing page, visual identity, and contribution path without overstating source evidence or promising star growth.

## Scope

- Lead with the project identity, useful examples, gallery access, and an easy case-submission link.
- Keep all 43 main cases and every pending/appendix/seed record available; preserve authors, sources, media, and evidence.
- Use the original icon only as branding, not as a catalog result.
- Keep English and Chinese generated from shared data and editable presentation templates.
- Distinguish original, short/partial, and unpublished prompt links.
- Verify generated output, archive guards, links, and documentation before committing.

## Status

Implementation and independent content/code review are complete. The review's prompt-provenance wording finding has been corrected. `python3 tools/verify.py` passed, including 120 archived media files, 175 generated-document link checks, archive fault injections, bilingual presentation guards, and generated-file freshness checks. Static HTML parsing also confirmed 95 evidence rows and 9 balanced disclosures in each README. Publication uses an isolated branch and draft PR.

Browser visual QA is currently limited: local Chromium cannot open its required socket in this environment; the separate cloud browser cannot reach the local preview server. No browser-rendering pass is claimed.

## Boundaries

Publish through a dedicated pull request and merge only after the final review and CI checks pass. Do not change GitHub Settings, the case inventory, media files, model-evidence status, rights, or generation features for this presentation task.

## Prior work

The previous archive-guard review is complete. Its recorded CI run remains [42139299595](https://github.com/jammyfu/awesome-gpt-image-gifs/actions/runs/42139299595); this redesign needs its own verification and CI results.
