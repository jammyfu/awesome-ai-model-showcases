# Current plan

**Goal:** Close the four P2 findings from the independent review of `7186396` (media itself passed). No new features. Do not merge main. Do not change GitHub Settings.

## Tasks

1. [x] Real format detection for local media (ffprobe video stream/duration when present; ISO-BMFF parser otherwise). Pillow for images; GIF multi-frame per existing semantics. Manifest ok-count / bytes / case-attachment correspondence. Ingest rejects wrong content-type. HTML-as-MP4 fault injection must fail.
2. [x] Prompt check compares archived `prompt.md` body to source/ideas/game verbatim text. Remove heading fallback. Unpublished prompts require the explicit empty marker. WRONG PROMPT fault injection must fail.
3. [x] `attach_local` emits local detail/prompt links only when `docs/cases/<id>/` exists. Appendix / pending / seeds point at existing pages or sources. `verify` recursively checks generated local Markdown/HTML link targets.
4. [x] Narrow Luffy wording: inventory has no attachment URL; article API attempt retrieved none; cannot assert the original longform has no media. Keep existing evidence; do not invent media.
5. [x] Local `python3 tools/verify.py` including fault-injection tests (`verify ok` on `94ef9fb`; Python 3.12.3 / ffprobe 6.1.1).
6. [ ] CI on PR #2 green for **this** commit. Local passed; pushed pending CI. Do not record CI passed until the cloud run is visible.

## Status

Local verify green. Next: push this commit, then record the GitHub Actions result when the cloud can see it. No new features.

## Out of scope

GitHub Settings, merging to main, pending-12 promotion, watching MP4s, generation features, autosync/heartbeat, unrelated features.

## Next candidates

1. Record CI outcome for this P2 commit (pass or fail from the cloud run).
2. Pending-12 review stays backlog.
3. Optional visual review of unwatched MP4s; rights-takedown if an author asks.
