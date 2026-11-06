# Decisions

- **Local archive, license unknown.** The owner asked to store third-party media in-repo and keep author/source. This is not treated as an author grant or CC0. MIT stays on source code only.
- **Main table stays 43.** X25 + web12 + Luffy/Krouxzz + 4 game author-claims. Promo / 2.5 / multimodel / failure stay in the appendix.
- **X animated_gif stays MP4.** Do not rename to `.gif`.
- **No git-autosync-signal.** That skill applies only to dramaforge/clippipeline.
- **verify.py is the single Python verification entry.** It calls existing validators with `sys.executable`.
- **Format detection is required.** Hash/size/extension are not enough. Prefer ffprobe; otherwise parse ISO-BMFF. CI installs ffmpeg.
- **Prompt archives compare full source text.** A heading such as `Original prompt` does not satisfy the check. Unpublished prompts need an explicit empty marker.
- **Local catalog links only when the archive exists.** Appendix / pending / seeds point at existing pages or sources.
- **Luffy miss is not “API 404 therefore no media.”** Inventory has no attachment URL; the article API attempt retrieved none; that cannot assert the original longform has no media.
- **README visualizer uses Pillow PNGs.** No persisted SVG fallback, no paid image API.
