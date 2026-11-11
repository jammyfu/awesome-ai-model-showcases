# Current plan

## Goal

Make the four-language README a useful, bounded entry to the case archive and a reusable documentation pattern, without changing source evidence or media permissions.

## This PR

- Lead with real licensed GIF results, direct published-prompt links, creator credits, and source links before navigation.
- Identify the actual GPT Image subcollection and its separate count; balance six frontier-family entries; move complete evidence to generated localized catalog pages.
- Show five recent source-dated cases with deterministic ordering, and repair work-type links.
- Preserve all case records, original source fields, translations, rights grants, and separate GPT Image membership.
- Add a reusable README pattern, a review-only discovery metadata proposal, and presentation regression checks.

## Status

Local `python3 tools/verify.py` passed, including generated freshness, six presentation tests, source/rights checks, JavaScript smoke tests, and 1,267 local document link checks. Source catalog and rights/translation data match the base revision; showcase-index records differ only in order. Local Chromium launch is blocked by the execution sandbox's socket restriction. GitHub rendering and the existing PR browser CI remain to be checked on the published draft branch. No merge or deployment is authorized by this change.

The owner requested popularity and important-version priority during this work. Comparable popularity data is not yet recorded, so the README discloses a source-date fallback. Qwen 4 variants now lead the editorial version order. Shared configuration and policy document the missing-data gate.

Case-first follow-up: three explicitly approved ailingqu GIFs now lead the first substantive section, with true GPT Image 2.6 source attribution, CC BY 4.0 notice, separate-archive membership, and direct prompts. No new third-party assets or rights grants were added.
