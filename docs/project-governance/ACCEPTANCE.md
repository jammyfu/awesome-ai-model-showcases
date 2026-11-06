# Acceptance

This P2 hardening round is accepted when:

- [x] Format probe rejects HTML pretending to be MP4 (hash/size/ext updates are not enough)
- [x] Ingest rejects wrong content-type / HTML body
- [x] Prompt check uses full source/ideas/game text; heading fallback removed
- [x] Unpublished prompts carry the explicit empty marker; WRONG PROMPT fails
- [x] Local archive links only for directories that exist; generated Markdown links resolve
- [x] Luffy miss wording is narrowed (no attachment URL; API attempt retrieved none; not an assertion the longform has none)
- [x] Facts hold: 42/42 X MP4, 120 local media files, 43 main cases
- [x] Local `python3 tools/verify.py` is green, including fault-injection tests
- [ ] CI on PR #2 is green after **this** push (unchecked until the cloud run is visible)

Previous archive round (commit `7186396`) remains in effect:

- [x] 42 X dynamic media URLs from `x-inventory.json` are archived locally as MP4
- [x] 42 of 43 main cases have local media files
- [x] Each main case has `docs/cases/<id>/{README,prompt,post}.md`
- [x] README/site use local media paths; original URLs are citations
- [x] CoderSkills loop files exist; git-autosync-signal does not
