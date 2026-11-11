# README hero and Claude case repair

## Scope and root cause

The merged README had no brand-hero reference. Its first images were three GPT Image appendix GIFs, while the Claude entry was text-only. The fix restores the existing approved project hero, then shows actual Claude film frames at a readable width. The existing 183-case main catalog and 51-case GPT Image archive are unchanged; the new source spotlight is explicitly separate.

## Sources, rights and review

Source: Vincentwei1021/mg-styles-15, revision `269f6ed788cf60aaf9c276b110c548d6e7d353e1`. The author's README explicitly applies MIT to project code, prompts, docs and films, with third-party exceptions retained. The original copyright notice and full license are saved alongside a pinned README text snapshot. See [exact provenance and review metadata](../../data/readme-featured-cases.json) and [media rights](../../MEDIA_RIGHTS.md).

- ISOPOLIS (`03-isometric.jpg`): unmodified original 1920 × 1080 author cover frame. Complete city, tower, wind turbines and transit are visible. Primary result.
- KESTREL-9 (`22-hud.jpg`): unmodified original 1920 × 1080 author cover frame. Dark but legible globe, target rings and telemetry; not a blank frame. Secondary result.
- Pixel Quest's title-heavy cover was inspected and rejected as an opening result image. It is not published by this change.
- No timestamp is claimed for the author-supplied covers; source does not provide their capture time. No generated or recreated result images were used.
- Exact hashes differ; no likely duplicate was flagged against existing archived thumbnails by a 32 × 32 grayscale comparison (normalized mean absolute difference < 0.025). Both actual images were independently inspected at full resolution.
- Model attribution remains the author's statement, not verified generation. The source repository had 3,434 stars and 428 forks at 2026-11-11T18:46:11Z, not two independent popularity observations or per-film view counts.

## Presentation and localization

Four generated README editions share the hero and two source frames, direct film/prompt/code links, credit, license and source scope. All 24 title/summary/alt fields (2 films × 3 fields × 4 locales) are populated and source-matched. Translation is AI-assisted and not author-approved or independently human-reviewed. The Pages hero uses the same primary frame and English/Simplified Chinese captions. GIF appendix records and existing case translations are not modified.

## Verification status

- Passed: `python3 tools/verify.py` on the staged repair, including generator freshness, seven README regression tests, source/media rights, public build, existing catalog/localization tests and 1,267 local document link checks.
- Passed: actual JPEG decode, dimensions, exact source-image hashes, no unapproved embeds in the built artifact, and `git diff --check`.
- Blocked locally: Chromium launch fails because the execution environment prohibits `socket()` even with an approved elevated run. This is not a visual-rendering pass.
- Pending at initial PR creation: CI browser suite and actual GitHub desktop/narrow-width review. The browser suite now checks the hero, actual result image, image decoding, language switching, small-screen overflow and source-link fallback after image failure.
- Not claimed: local playback of the linked external films or a new Pages deployment. This change publishes stills, not movie copies. No merge or deployment was performed.
