# Current plan

## Goal

Make the four-language README a useful, bounded entry to the case archive and a reusable documentation pattern, without changing source evidence or media permissions.

## This PR

- Put the reader outcome, gallery action, and three-step use path before the catalog.
- Balance six family entries; move complete evidence to generated localized catalog pages.
- Show five recent source-dated cases with deterministic ordering, and repair work-type links.
- Preserve all case records, original source fields, translations, rights grants, and separate GPT Image membership.
- Add a reusable README pattern, a review-only discovery metadata proposal, and presentation regression checks.

## Status

Local `python3 tools/verify.py` passed, including generated freshness, five new presentation tests, source/rights checks, JavaScript smoke tests, and 1,265 local document link checks. Source catalog and rights/translation data match the base revision; showcase-index records differ only in order. Local Chromium launch is blocked by the execution sandbox's socket restriction. GitHub rendering and the existing PR browser CI remain to be checked on the published draft branch. No merge or deployment is authorized by this change.
