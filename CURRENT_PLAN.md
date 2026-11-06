# Current plan

**Goal:** Archive real third-party media for the 43 main catalog cases, with author and source kept, and wire a lean CoderSkills loop around that one goal.

## Tasks

1. [x] Vendor latest scout JSON and download every main-table GIF/MP4/reference still. Incremental sha256 skip.
2. [x] Write per-case `docs/cases/<id>/` with full original prompt, post text, and local embeds.
3. [x] Point EN/ZH README and the website at local media; original URLs become citations only.
4. [x] Replace link-only validators with `tools/validate_local_media.py` + `tools/verify.py` (sys.executable) in CI.
5. [x] Add readme-tech-visualizer header/badges from the real stack (no SVG fallback, no paid images).
6. [x] Add lean continuous-project-loop files. Do not add git-autosync-signal.

## Status

Done on this branch. Next: CI green on PR #2; then pending-12 review stays in backlog.

## Out of scope

GitHub Settings, merging to main, pending-12 promotion, watching MP4s, generation features, autosync/heartbeat.

## Next candidates

Pending-12 review; optional visual review of unwatched MP4s; rights-takedown process if an author asks.
