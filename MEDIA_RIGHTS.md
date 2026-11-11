# Media rights and attribution

**Code:** MIT, per `LICENSE`.

**Archived third-party media:** Main-catalog GIFs, MP4s, reference stills, and published prompts are stored under `docs/cases/<id>/` because the repository owner asked to keep the files locally with author and source citations. This is **not** an author grant, a redistribution license, or CC0. Treat each file as **license unknown** unless a specific work later receives a documented grant.

**Videos:** The owner asked to keep a local `docs/cases/<id>/media/video.mp4` when the source post has a downloadable video, including posts that restrict reposting. Each file stays credited to the original author and links to the original post. This is still not a license to reuse the video. If you own a clip and want it removed, open a GitHub Issue and it will be taken down.

**MIT does not cover media.** Stars, traffic, or the presence of a local copy are not permission to reuse someone else's GIF, video, likeness, or prompt commercially.

**Manifest:** `docs/data/local-media-manifest.json` records local path, original media URL, author, original post, sha256, download date, format, and size. Original URLs are citations, not the only media entry.

**X attachments:** An X `animated_gif` is usually delivered as `video/mp4`. This repository keeps that file as `.mp4` and does not rename it to `.gif`. Visual review status remains unwatched unless someone actually watched the file.

**Appendix / seeds:** Popular-GIF restages and SVG concept covers are this repository's planning material, not third-party originals. Local seed GIFs in `docs/gifs/` remain repository seeds, not the community collection.

**Morphic stills and sheets:** Morphic prompt-library images were made with GPT Image 2.5 / Ideogram Vector. They are not Images 2.6 outputs.

## Navigation thumbnails

`assets/thumbs/<case-id>.<ext>` holds one small preview per main-catalog case when a representative image could be fetched. Each file is at most 300KB. The catalog record stores `image_url` (the direct source URL), `image_source` (the post or page), and `image_credit` (the author). README grids and `docs/showcase-index.md` show that credit and link back to the original post.

These thumbnails are owner-requested navigation copies. They are **not** a new license. MIT still does not cover them. A multi-frame GIF may be stored as a still JPEG when the original file is larger than the cap. If a source page explicitly forbids republication, the catalog keeps the direct URL and does not save a file.

Cases with no representative image are listed in `docs/missing-thumbnails.md`. No image URL in that list was invented.

`assets/thumbs/<case-id>.<ext>` 是主表案例的导航缩略图，单张不超过 300KB。每条记录有 `image_url`（原始直链）、`image_source`（来源页）和 `image_credit`（作者）。README 和 `docs/showcase-index.md` 署名并链回原帖。这是主人要求的导览副本，不是新的授权；MIT 不覆盖这些图。原图超过上限时，多帧 GIF 可能只留一帧 JPEG。来源页写明禁止转载的，只保留直链，不下载。没有拿到图的案例写在 `docs/missing-thumbnails.md`，不编造链接。

If you own material here and have a rights concern, open a GitHub Issue to request review or removal.

## Documented grant: ailingqu examples

The eight `ailingqu-*` cases added in this expansion contain unmodified GIF files and published prompt bodies by [ailingqu / awesome-ai-gif-prompts](https://github.com/ailingqu/awesome-ai-gif-prompts/tree/a20f88b18a9abe8cd1531fb8a8e738a5a4701ce2). The source [explicitly licenses prompts and example GIFs](https://github.com/ailingqu/awesome-ai-gif-prompts/blob/a20f88b18a9abe8cd1531fb8a8e738a5a4701ce2/README.md#license) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). A [copy of the license text](docs/licenses/ailingqu-CC-BY-4.0.txt) is retained. Each case identifies credit, original source, license, and our added bilingual annotations. No endorsement or rights to unrelated third-party marks or likenesses are implied.

这八例的 GIF 与公开提示词正文保持原样，署名 ailingqu / awesome-ai-gif-prompts，遵循 CC BY 4.0；本仓增加双语说明与核验元数据。该许可不扩展至其他来源，也不证明底层模型或所有第三方权利。
