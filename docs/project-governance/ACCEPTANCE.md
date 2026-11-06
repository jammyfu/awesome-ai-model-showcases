# Acceptance

This round is accepted when:

- [x] 42 X dynamic media URLs from `x-inventory.json` are archived locally as MP4
- [x] 42 of 43 main cases have local media files
- [x] Luffy miss is listed with a concrete reason, prompts stored in full
- [x] Each main case has `docs/cases/<id>/{README,prompt,post}.md`
- [x] README/site use local media paths; original URLs are citations
- [x] Link-only “do not copy third-party GIF” copy is removed from the main catalog
- [x] `tools/verify.py` runs existing validators + local-media checks
- [x] CoderSkills loop files exist; git-autosync-signal does not
- [ ] CI on PR #2 is green after push
