# Public media repair, 2026-11-11

Base revision: `fd831de2ac684776fc8e5fb2a95b4103082a8bd8`.

The archive had grown beyond the earlier 151-video snapshot: 225 saved thumbnails, 181 `video.mp4` copies, and 52 older MP4 paths. At this revision, all 233 MP4 paths were Git LFS pointers in an ordinary checkout. The previous Pages workflow uploaded that checkout directly. Hash/size agreement with LFS metadata proved archive consistency, not playable deployment bytes.

The source's pinned ailingqu README explicitly licenses its prompts and example GIFs under CC BY 4.0. Eight original GIFs and their navigation previews retain attribution and license evidence. Other cases retain their authors, sources, prompt scope and verification caveats, with source-only media presentation. Project artwork is listed separately.

The new deployment artifact excludes 217 unverified thumbnails (these are outside `docs` already), 301 unverified case assets and legacy seeds whose reference ownership is unverified. It includes only byte-matched approved media. Unknown media has no remote-embed fallback. All 183 homepage case records and 51 GPT Image subproject records remain.

No original media bytes were deleted or replaced. The public Git repository and history still contain archival copies; this repair is not a complete copyright clearance or a history purge. Unknown permission is not a legal finding of infringement.

Verification includes deterministic generation, all existing validators, source-link preservation, explicit-grant/hash checks, negative embed tests, all 946 generated document links and a separately validated Pages artifact. CI additionally loads the public site in Chromium, checks every case page, observes changing GIF frames, and checks for external media requests and console exceptions. The local environment could not launch Chromium because socket creation was denied, so local non-browser checks must not be described as a browser pass.

## Final integrated review

The curation quality skill, four-locale translations with original-text access, and the refreshed project icon are integrated. Local validation passes across 1,260 generated links and a 1,308-file approved Pages artifact. Translation coverage reports 312 case records across title, method, verification and model-claim fields; 73 collected prompts have AI translations. These are coverage counts, not human language review or new permission to reuse protected text.

All eight approved navigation previews were visually inspected side by side on 2026-11-11: each displays its corresponding subject clearly, with no blank/near-black preview or repeated generic cover. Seven are still/resize derivatives and the typing-indicator GIF is byte-identical to its original. Their original media remain unchanged. The new icon was inspected at 16/32/48/64/112 pixels on light and dark backgrounds.

PR CI checks visible animation for all eight approved GIFs, every case route, desktop and narrow mobile search, four-locale translation-reader switching, and source-link access when an image fails. No local browser pass is claimed. PR #13 and merge were explicitly authorized after the prepared branch was reviewed with the owner; merge remains contingent on passing CI.
