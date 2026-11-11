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
- Passed on remote `c20e1867bb44262d246ca0dda02a46e37b376d35` (same file tree as local `2fad98d`): [CI validation and real Chromium suite](https://github.com/jammyfu/awesome-ai-model-showcases/actions/runs/43082768681), including hero/result decode, 390 × 844 mobile viewport, language switching, page overflow and failed-image source fallback. Existing regression coverage also visited 234 case pages and observed all eight licensed GIFs animate, with zero external media requests and zero page errors.
- Passed actual GitHub README visual review: desktop hero 720 × 288 and both work frames 720 × 405; at a 500px browser-window width all images fit without distortion, captions remain readable, and source links remain accessible. This is a narrow desktop window, not a physical mobile-device test. Source and media permissions were independently reviewed.
- Passed both original external films: ISOPOLIS at 4.65 seconds and KESTREL-9 at 9.86 seconds, each 10 seconds long with readyState 4. This does not imply hosting or reproducing the films locally. The author site has horizontal overflow at a 500px window width, although its film and play button remain in view; that external page is outside this repair.
- Not claimed: local movie playback or a new Pages deployment. The built Pages layout passed browser assertions, but it has no public preview URL or manually captured new-site visual review; the old deployed site is not treated as evidence for this PR. This change publishes stills, not movie copies. No merge or deployment was performed.

The final evidence-only update records these checks without altering the inspected README, images, site layout or rendering code. PR remains draft and unmerged.
