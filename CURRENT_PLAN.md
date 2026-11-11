# Current plan

## Goal

Separate archival provenance from permission to publish media, and prevent Git LFS pointers from reaching the public Pages artifact.

## This PR

- Keep all 183 main-catalog cases and their sources; use source links for unverified media.
- Retain eight documented CC BY 4.0 GIFs, credited previews, and project artwork.
- Gate catalog, case pages and legacy gallery renderers on exact approved assets.
- Build Pages from a separate approved-media artifact and reject unresolved LFS pointers.
- Add unit, generated-content, artifact and browser regression checks.

## Status

Implementation and local non-browser verification passed. Browser verification runs in PR CI because local Chromium cannot create the required sockets in this environment. PR #13 was opened after confirmation. The owner subsequently authorized merge after checks pass; browser CI and Pages verification remain pending. Existing raw archive and Git history are preserved for a separate rights review.
