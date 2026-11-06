# Agent guide

This repository is a **community case archive** for GPT Image 2.6: original authors, local media, verbatim prompts, and source citations. It is not a playbook showcase and not an Images API app.

## Loop files

- Current work: `CURRENT_PLAN.md`
- Long route: `MASTER_PLAN.md`
- Later work: `TODO_BACKLOG.md`
- Records: `docs/project-governance/`

## Verify

```bash
python3 tools/verify.py
```

`tools/verify.py` must use `sys.executable`. Do not call bare `python` from PATH. Prefer existing validators; do not add a second verify entry.

## Do not add

- `git-autosync-signal` (dramaforge/clippipeline only)
- heartbeat / LaunchAgent / `sync_or_queue.py` automation
- paid image generation
- SVG concept art as case results
- promo / 2.5 / multimodel / failure rows in the main catalog

## Media

User-requested local archive. License remains unknown. MIT covers source code only. Incremental ingest: `python3 tools/ingest_local_media.py`.
