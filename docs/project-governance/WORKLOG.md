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

After commit `94ef9fb` (clean tree so generated-file `git diff --exit-code` can pass):

```
$ python3 tools/verify.py
...
+ /usr/bin/python3 /workspace/tools/validate_local_media.py
local media ok: 120 files, 42 cases with files, 42/42 X dynamics (ffprobe), 42/43 main cases have media, luffy documented miss (no attachment URL; API attempt retrieved none; not an assertion the longform has none), 38704608 bytes
+ /usr/bin/python3 /workspace/tools/test_archive_guards.py
archive guards ok: HTML-as-MP4 fails, WRONG PROMPT fails, unpublished marker required
+ /usr/bin/python3 /workspace/tools/validate_markdown_links.py
local markdown links ok: 175 generated files, 0 missing targets
verify ok
```

Local interpreter: Python 3.12.3. Local ffprobe: 6.1.1 (Ubuntu). CI workflow: `ubuntu-latest` + setup-python 3.12 + apt ffmpeg + `python tools/verify.py`.

Cloud CI for commit `28eddd6183a6e0b8e2fcc7718b4a41a183d39ff9`: GitHub Actions run [42139299595](https://github.com/jammyfu/awesome-gpt-image-gifs/actions/runs/42139299595) **success**. Validate job: all steps succeeded (checkout, setup-python 3.12, Pillow, ffmpeg, `python tools/verify.py`).

Mac mini Codex second independent review: **PASS**. Fault injections rejected (HTML-as-MP4, WRONG PROMPT). Generated local Markdown/HTML: 175 files, 0 dead links.

This P2 round is closed on the evidence above. Did not merge main. Did not change GitHub Settings.

## 2026-11-06 — local media archive

- Vendored `x_c7f8` / `web_e378` / `game-sequences_fe91` / `game-sequences-deep_79e9` into `playbooks/research/`.
- Downloaded main-table media into `docs/cases/<id>/media/`.
- 42/42 X dynamic MP4s archived. 42/43 cases have local media.
- `luffy-x-article`: inventory has no attachment URL; article API attempt did not retrieve media; cannot assert the original longform has no media. Seven verbatim prompts archived.
- Stale Krouxzz URL `HWWn8n7b0AAN1xP.mp4` 404; live attachment `HWWnk8IXsAE0aXq.mp4` archived.
- Ravivit paper-boat GIF needed a browser User-Agent + Atlas Referer.
- Added `tools/verify.py`, local-media manifest, CoderSkills header + loop files.
- Did not merge main. Did not change GitHub Settings. Did not add git-autosync-signal.

## 2026-11-11 — Bounded four-language README navigation

- Replaced repeated full inventories in the landing pages with six balanced family entries, complete version links, and five explicitly source-dated recent posts. Moved full evidence to generated `docs/catalog.<locale>.md` pages; preserved old README anchors.
- Kept 183 homepage records and the separate 51-case GPT Image archive. Original source catalog, localization data, and publication grants are unchanged; index records are reordered, not rewritten.
- Fixed missing work-type anchor destinations and made type entries clickable. Kept zero-count tags explicit rather than claiming missing previews.
- Added `docs/readme-pattern.md`, review-only `GEO.md`, and five presentation regressions. Corrected `llms.txt` prompt-availability wording. No GitHub About/topics setting changes.
- Local unified verification passed. Browser launch is blocked locally by `socket() failed: Operation not permitted`; real GitHub visual review and PR browser CI are separate remaining checks. No merge or deployment performed.
