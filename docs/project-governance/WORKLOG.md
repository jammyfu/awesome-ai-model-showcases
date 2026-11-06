# Worklog

## 2026-11-06 — P2 validator hardening (Codex review of 7186396)

Independent review: media itself passed; NEEDS CHANGES on four P2s.

- Added `tools/media_format.py`: ffprobe video stream/duration when present; ISO-BMFF ftyp/moov/vide parser otherwise; Pillow for images; GIF requires multiple frames.
- `tools/validate_local_media.py` now checks format, prompt full-text (no heading fallback), unpublished marker, manifest ok-count/bytes/jobs, and case↔attachment correspondence.
- `tools/ingest_local_media.py` rejects `text/html` / `text/plain` / `application/json` and HTML/JSON bodies even if named `.mp4`.
- `tools/write_community_catalog.py` `attach_local` only sets local detail/prompt/page when `docs/cases/<id>/README.md` exists. Seeds point at `docs/gifs/<id>.gif`. Pending/appendix cite source/media URL.
- `tools/validate_markdown_links.py` walks generated README / catalog / case Markdown+HTML and requires local targets to exist.
- `tools/test_archive_guards.py`: HTML-as-MP4 must fail; WRONG PROMPT must fail.
- CI workflow installs `ffmpeg` so GitHub Actions uses ffprobe.
- Luffy wording narrowed: inventory has no attachment URL; article API attempt did not retrieve media; cannot assert the original longform has no media. Existing 404/no-attachment evidence kept. No media invented.

Local commands (before commit; same checks `tools/verify.py` runs after the generated-file git diffs):

```
$ python3 tools/test_archive_guards.py
archive guards ok: HTML-as-MP4 fails, WRONG PROMPT fails, unpublished marker required

$ python3 tools/validate_local_media.py
local media ok: 120 files, 42 cases with files, 42/42 X dynamics (ffprobe), 42/43 main cases have media, luffy documented miss (no attachment URL; API attempt retrieved none; not an assertion the longform has none), 38704608 bytes

$ python3 tools/validate_markdown_links.py
local markdown links ok: 175 generated files, 0 missing targets

$ python3 tools/validate_community.py
community catalog ok: main 43, pending 12, excluded 9, appendix 24, seeds 6; topics 10
```

`python3 tools/verify.py` is run after this commit so `git diff --exit-code` sees a clean generated tree. CI for this commit is **not** recorded as passed until the cloud run is visible.

## 2026-11-06 — local media archive

- Vendored `x_c7f8` / `web_e378` / `game-sequences_fe91` / `game-sequences-deep_79e9` into `playbooks/research/`.
- Downloaded main-table media into `docs/cases/<id>/media/`.
- 42/42 X dynamic MP4s archived. 42/43 cases have local media.
- `luffy-x-article`: inventory has no attachment URL; article API attempt did not retrieve media; cannot assert the original longform has no media. Seven verbatim prompts archived.
- Stale Krouxzz URL `HWWn8n7b0AAN1xP.mp4` 404; live attachment `HWWnk8IXsAE0aXq.mp4` archived.
- Ravivit paper-boat GIF needed a browser User-Agent + Atlas Referer.
- Added `tools/verify.py`, local-media manifest, CoderSkills header + loop files.
- Did not merge main. Did not change GitHub Settings. Did not add git-autosync-signal.
