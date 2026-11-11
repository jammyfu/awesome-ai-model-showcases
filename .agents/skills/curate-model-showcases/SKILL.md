---
name: curate-model-showcases
description: Use when adding, repairing, or reviewing cases, previews, playback, project icons, or localized content in awesome-ai-model-showcases, including black thumbnails, repeated covers, and untranslated source text.
---

# Curate model showcases

Make each case recognizable, source-faithful, appropriately localized, and honest about rights and verification. A successful download, generated README, or green validator does not establish those qualities by itself.

## Start from the project

Read `AGENTS.md`, `CURRENT_PLAN.md`, `docs/data/SOURCE_DATA.md`, and `MEDIA_RIGHTS.md`. Inspect the current branch and generators before editing. This is a model-family case archive, not a collection of invented demonstrations. Preserve source URLs, authors, exact published prompts, model claims, and evidence boundaries.

Update source inventories, translation inputs, and templates; regenerate their outputs. Do not fix generated READMEs or case JSON by hand. Keep case counts and appendix/main-catalog membership intact unless the task explicitly changes them.

## Required quality gates

Read [quality-gates.md](references/quality-gates.md) for the affected work. Before calling a changed case or asset ready, record evidence for each applicable gate:

| Gate | Required result |
| --- | --- |
| Rights and provenance | The exact media/prompt and any derivative have a documented publication basis, credit, and source; otherwise retain an explicit source-only entry. |
| Representative preview | Visually inspected pixels show the actual case's meaningful result at the displayed size, with source mapping and selected frame/time recorded. |
| Distinctness | Exact and likely visual duplicates have been checked against the underlying works. Shared banners are not substituted for distinct outputs. |
| Playback | Materialized bytes decode and the affected approved animation visibly progresses in the browser; fallback behavior is checked. |
| Localization | Every required field has the target-language version or an explicit missing/blocked status; original evidence remains distinguishable from translation. |
| Project icon | An appropriate project-created mark works at real usage sizes and backgrounds; it is distinct from case evidence and official model logos. |

Do not manufacture a new result image to conceal a missing, black, or unlicensed preview. If no usable authorized preview is available, show a clear source link. That is a safe fallback, not a successfully repaired preview.

## Verification and handoff

Run the single entry point `python3 tools/verify.py` after regenerating and staging only reviewed changes. Run `RUN_BROWSER_TESTS=1 python3 tools/verify.py` when browser prerequisites are available. Inspect the final rendered README/card/detail layouts on desktop and mobile, not only the raw assets. Extend existing validators/tests for mechanical regressions; keep visual and language judgment as explicit review gates.

The handoff identifies the commit, changed case IDs/assets, exact checks and coverage, remaining failures, and screenshot/report paths. Report separate totals for catalog records, approved playable media, reviewed previews, and translated fields per locale. Distinguish **passed**, **failed**, **not run**, and **blocked**. State whether observations are measured, visually reviewed, source-reported, or AI-translated. Checks skipped or run on a different commit do not count as a full pass.

This skill grants no permission to merge, deploy, buy generation credits, or broaden third-party reuse. Follow the current task's authorization; a repair request alone does not authorize merging or deployment.
