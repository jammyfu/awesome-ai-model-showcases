# README visual assets

- `project-icon.png`: AI-assisted brand illustration refreshed for this repository on 2026-11-11. Transparent RGBA PNG, 512 × 512. Display at 112 px in the English, Simplified Chinese, Traditional Chinese, and Japanese READMEs. The layered exhibit cards and play aperture represent the archive; the mark is not an OpenAI logo or an example of model output.
- The README previews link directly to original GIFs under `docs/cases/`, with author/source/prompt links. The icon is never counted as a case or used as a case result.
- `hero-wide.png` and `tech-stack.json` are legacy visual assets, retained for compatibility and not shown in the current README. `tools/generate_readme_visuals.py` only rebuilds that legacy hero and must not replace the approved icon.
- Update README layout in `tools/templates/README.en.md`, `README.zh-CN.md`, `README.zh-TW.md`, and `README.ja.md`; generate with `python3 tools/write_community_catalog.py`.
- Counts are generated from the catalog. Do not add hard-coded popularity claims, API-availability claims, or generated-by stamps to the opening section.

The refreshed mark, favicon, and touch icon share the project-created provenance in [ICON_DESIGN.md](ICON_DESIGN.md).
