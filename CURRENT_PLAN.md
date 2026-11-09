# Current plan

**Goal:** Expand the sourced community GIF catalog while preserving prompt provenance, license scope, and the difference between file verification and model authentication.

## Scope

- Add eight CC BY 4.0 GIFs and their source's published prompt bodies, using immutable source links.
- Retain all previous 95 records and 120 media files; add 26 source-linked candidates outside the main table.
- Keep script-derived suffixes distinct from historical requests. Four source records name a website provider; four do not name a provider.
- Preserve source licenses and prompt scope in case pages, bilingual READMEs, and the gallery.
- Revalidate source inventories, hashes, actual media formats, generated output, links, and UI rendering logic.

## Status

Implementation, fresh independent source/code review, and local verification are complete. The eight GIF files were freshly decoded, hash-checked, and reviewed as frame contact sheets on 2026-11-09. The unified verification passed for 51 main cases, 128 media files, 42 X dynamic attachments, 207 generated-document links, Python regression guards and the gallery JavaScript smoke test. Candidate evidence is dated 2026-11-07 and is not presented as a new media check. No paid generation or independent model reproduction has been performed.

## Publication

Publish a dedicated pull request, complete review and CI against its exact head, then merge under the owner's explicit instruction. Confirm the main commit and its validation/Pages runs afterward.

See [the source report](playbooks/research/expansion-2026-11-09.md) for accepted cases and candidate restrictions.
