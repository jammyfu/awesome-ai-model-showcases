# README visual assets

- `project-icon.png`: AI-assisted brand illustration refreshed for this repository on 2026-11-11. Transparent RGBA PNG, 512 × 512. Retained as the project icon and the source for site/favicon derivatives. The short README uses one existing hero instead of stacking the hero and a second large icon. The layered exhibit cards and play aperture represent the archive; the mark is not an OpenAI logo or an example of model output.
- README examples link to localized case evidence and original posts. There are no case-media embeds in the landing pages. The hero and icon are project branding, never case results or evidence of model output.
- `hero-wide.png` and `tech-stack.json` are legacy visual assets, retained for compatibility and not shown in the current README. `tools/generate_readme_visuals.py` only rebuilds that legacy hero and must not replace the approved icon.
- Update README layout in `tools/templates/README.en.md`, `README.zh-CN.md`, `README.zh-TW.md`, and `README.ja.md`; generate with `python3 tools/write_community_catalog.py`.
- Counts are generated from the catalog. Do not add hard-coded popularity claims, API-availability claims, or generated-by stamps to the opening section.

The refreshed mark, favicon, and touch icon share the project-created provenance in [ICON_DESIGN.md](ICON_DESIGN.md).
