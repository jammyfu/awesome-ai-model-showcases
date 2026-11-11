# Quality gates

Read the sections relevant to the change. These are acceptance conditions, not claims that all historical entries already satisfy them.

## 1. Rights and source mapping

- Trace each output to its original case/post and documented attachments. Keep original author, source URL, published prompt status, and source-reported model/pipeline claims. A frame review is not model authentication.
- Review the specific license/grant and scope for media, screenshots, published prompts, and derivatives such as thumbnails or translations. A public post, download, attribution, repository MIT license, or archive request is not a grant covering every work. Unknown rights mean unknown, not proven infringement and not cleared reuse.
- For public media, use `data/public-media-rights.json`: bind exact path/SHA-256, credit, source, license/evidence URL, and modification notice. If the file changes, recheck the evidence and derivative obligations before updating its hash. Never refresh hashes just to silence validation.
- Unknown or inapplicable permission: keep factual annotations and the source link; do not newly copy, hotlink, translate/reproduce a full protected prompt, or publish a replacement thumbnail without a documented basis. Preserve existing archival records for review; do not silently delete archive/history as a cleanup step.
- Deployable media comes from `python3 tools/build_public_site.py --output _site`, not a raw `docs/` upload. Review `MEDIA_RIGHTS.md` for the current allowlist and limitations; counts are not permanent rules.

## 2. Representative previews, not the first frame

1. Confirm the media is real, readable bytes rather than a Git LFS pointer, an error page, or a mislabeled extension. X `animated_gif` can be MP4; preserve the real format.
2. For animation/video, inspect a contact sheet spanning the sequence, then inspect promising moments at full resolution. A practical initial sample is 10%, 25%, 50%, 75%, and 90% of duration; inspect additional moments if that misses the result or only captures transitions. Use GIF frame durations rather than assuming uniform timing. A contact sheet is not playback evidence.
3. Select the clearest representative achieved result, not necessarily the brightest frame. Reject loading/blank/error states, near-black frames with no discernible subject, title/end slates that hide the work, incomplete UI, and misleading crops. For a game or interactive page, wait for the demonstrated scene or interaction to render before capture. Preserve relevant labels and source watermarks.
4. Inspect the chosen preview in its actual README card and case-page crop on desktop and narrow mobile layouts. The distinguishing result must remain legible. Record case ID, source media path/hash, frame index or timestamp, crop/resize changes, reviewer, date, and a short selection reason.
5. If the relevant source cannot be accessed, permission is missing, or no useful frame exists, mark the case source-only or preview-pending with a reason. Do not use a generic model-family banner, unrelated screenshot, another case's result, or generated concept art to make it look complete.

Automation can flag candidates, not decide the best visual result. Examples: over 90% of pixels below grayscale 25, entropy below 1 bit, or unexpectedly tiny/invalid images warrant review. Dark scenes and minimalist designs can be valid. Record why a flagged image is retained, and do not use a clean score as a substitute for looking at the pixels.

## 3. Repeated and mismatched previews

- Compare exact byte hashes, decoded-image similarity/perceptual hashes, and source attachment identity across different case IDs. Check approved/public previews and any archival candidates being repaired. Common source image URLs at different resolutions can hide duplicates; compare observed source identity without stripping meaningful URL parameters from fetch requests.
- Inspect each flagged pair or cluster side by side and compare the posts/actual outputs. A perceptual-hash collision is a review candidate, not proof of duplication. Identical LFS OIDs show shared bytes, not which case owns them.
- Distinct works using one model-launch banner need their own verified result previews. A genuine same-work repost should retain the canonical source and be explicitly identified; do not quietly discard a case or invent a new source to make counts/duplicate checks pass.
- Keep a disposition for each flagged cluster: corrected mapping, replaced frame, documented intentional shared work, source-only pending evidence, or false positive with reason. Only resolved/publicly disabled failures pass the publication gate. Report disabled previews separately from replacements.

## 4. Real playback and rendered checks

There are separate checks: file/container integrity, decoded frame content, browser playback, and live deployment. Passing one does not establish the others.

- Decode approved GIF frames and inspect timing. For MP4/WebM, probe and decode actual media bytes, not just a filename, HTTP status, or LFS OID/size. Verify duration, dimensions, and a video stream.
- On the final built site, open each changed approved playable item at its real route. Observe different rendered frames over time for GIFs; for video observe time progression and changing frames, including play/pause/seek and the source fallback if playback fails. Do not claim every item played based on a single representative GIF test.
- Test affected cards/detail pages and repeated navigation at desktop/mobile widths, source-only entries, search/filter interactions, and broken-media fallback. Confirm no unexpected external media requests or browser errors. A valid still preview is not proof that its linked animation plays.
- `python3 tools/verify.py` includes structural, artifact, and optional JavaScript checks. `RUN_BROWSER_TESTS=1 python3 tools/verify.py` enables the repository's browser suite. Read its assertions to report its actual coverage; supplement it for newly introduced media types or interactions.
- If Chromium, codecs, sockets, credentials, or source access are unavailable, report the exact blocked stage. Use authorized CI for the same commit where available; verify its result before claiming success. Do not turn a skip into a pass. Only check a live deployment after it is authorized and available.

## 5. Localization with original evidence preserved

Discover supported locale targets from the current renderer and templates. At skill creation, READMEs use `en`, `zh-CN`, `zh-TW`, and `ja`; the website exposes `en` and `zh`. Do not promise Japanese/Traditional Chinese website switching just because the README versions exist.

- Inventory visible fields before translating: case titles, summaries/descriptions, process/creation notes, verification limits, captions/alt text, source-only and missing-content notices, buttons, collection descriptions, and published prompt content where reuse is permitted. Apply this to Chinese, English, or any other source language. Translating headings alone is insufficient.
- Preserve exact source text and `original_prompt` separately from translated display fields. Model IDs, handles, URLs, commands, code, placeholders, and quoted output literals retain their meaning. Preserve raw `model_claim`/evidence; if a localized explanation is needed, keep it labeled and separate. Never convert a source claim into an independently verified fact.
- Supply meaning-equivalent text in every locale required for that surface. Review terminology, numbers, limitations, and negatives against the original. Simplified-to-Traditional conversion alone may not address wording; Japanese is not Traditional Chinese. Technical names or deliberately quoted literals are not untranslated-field failures.
- Keep full/partial/unpublished/source-only prompt status. A partial prompt gets a labeled partial translation; an unpublished prompt gets a localized unavailable notice, not an invented prompt. Put available permitted prompt translations alongside the original, clearly labeled as translations. Disclose AI translation and lack of human review accurately; do not present it as author-approved text.
- Bind translation entries to the exact source text or source revision/hash plus case ID/field/locale as supported by the implementation. Source changes invalidate dependent translations. Missing or stale entries must fail the relevant completeness check or show a visible localized pending/fallback notice. Never silently mark source-language fallback as translated.
- Measure coverage by **field and locale**, not only record count: e.g. titles complete can coexist with prompt translations pending. Validate required keys, source matching, empty values, and locale routing automatically; review semantics and actual rendering separately. State precisely which coverage is complete and which is not.

## 6. Project icon

When requested, create a suitable project-specific mark for the AI showcase/archive identity. Do not substitute an official provider logo, stock glyph, model-family cover, or generic placeholder for the requested original icon. Record AI-assisted creation when used; do not assert legal uniqueness or third-party clearance without evidence.

Check the actual placements: README, site header/favicon if present, and relevant share images. Inspect silhouette and detail at each displayed size (including 16/32 px for favicons), transparent edges, scaling, and light/dark backgrounds. Keep one approved master and intentional derivatives, update source templates/references rather than only generated outputs, and verify rendered integration. Preserve existing transparency unless the design calls for another background. Document provenance and brand-asset permissions separately from community case media; a project icon is never a model-output example.

## 7. Completion record

For each affected case/asset, retain a review record in the existing manifests or an appropriate `docs/project-governance/` report. Do not pretend an unimplemented JSON field is already enforced. Record:

- Source identity and exact asset hash; rights/evidence and any modification notice.
- Preview decision and selected time/frame/crop; duplicate flags and dispositions.
- Playback route/browser, observed behavior, scope, and screenshot/report evidence.
- Source language, target surface/locales, translated fields, missing/stale fields, and translation review status.
- Validation command, tested commit, result, date, and precise blockers. Use `not applicable` with a reason for genuinely unaffected gates, not to hide missing work.

A valid concise handoff could say: "Eight approved GIFs decode; one GIF was observed animating in Chromium. Five previews were replaced and visually checked. Four-language titles are complete; 12 published prompts still lack Japanese translations. No merge or deployment performed." Use only measured counts, never copy this example as a factual project report.
