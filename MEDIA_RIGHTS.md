# Media rights and attribution

**Source code:** MIT, per [LICENSE](LICENSE). MIT does not license third-party GIFs, videos, screenshots, likenesses, or published prompts.

## Public presentation: source links by default

A download, author credit, public post, owner request, or takedown notice is **not** an author grant. Unknown rights do not establish infringement either. Until a work has specific evidence permitting publication, the public catalog and case pages link to its original source instead of embedding a local copy or hotlinking the remote media.

The publication allowlist is [data/public-media-rights.json](data/public-media-rights.json). Each entry binds an exact path and SHA-256 to credit, source, a specific grant/evidence URL, and modification notes. A license label alone cannot enable publication. Review the actual scope and attribution obligations before adding an entry. A changed file needs a new review and hash; do not merely refresh hashes to make CI pass.

## Documented grant: ailingqu examples

Eight `ailingqu-*` cases use GIFs and published prompt bodies from [ailingqu / awesome-ai-gif-prompts at the pinned source revision](https://github.com/ailingqu/awesome-ai-gif-prompts/tree/a20f88b18a9abe8cd1531fb8a8e738a5a4701ce2). The source [explicitly licenses prompts and example GIFs](https://github.com/ailingqu/awesome-ai-gif-prompts/blob/a20f88b18a9abe8cd1531fb8a8e738a5a4701ce2/README.md#license) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). A [copy of the license text](docs/licenses/ailingqu-CC-BY-4.0.txt) is retained.

The eight original GIF files remain unmodified. Seven navigation thumbnails are resized and/or still-frame derivatives; the AI typing indicator preview retains the original GIF bytes unchanged. Each case retains the creator, original source, license link, and our bilingual annotations. This grant does not prove model provenance, endorsement, or clearance of unrelated trademarks or likenesses. Published rewritten prompts are not authenticated historical requests.

Project-created brand illustrations are tracked separately from third-party cases. They are not model-output evidence or official logos. See [brand artwork](docs/brand-artwork.md) and [project icon provenance](docs/readme-assets/README_SNIPPET.md).

## Documented grant: Claude motion-design spotlight

Two original 1920 × 1080 film-cover frames from [Vincentwei1021 / mg-styles-15 at revision 269f6ed](https://github.com/Vincentwei1021/mg-styles-15/tree/269f6ed788cf60aaf9c276b110c548d6e7d353e1) illustrate ISOPOLIS and KESTREL-9. The source [explicitly licenses its code, prompts, docs and films under MIT](https://github.com/Vincentwei1021/mg-styles-15/blob/269f6ed788cf60aaf9c276b110c548d6e7d353e1/README.md#license), not just software. The [original copyright notice and full license](docs/licenses/Vincentwei1021-mg-styles-15-MIT.txt) are included. The frames are unmodified; displayed size is smaller. Third-party components keep their original licenses, as the source explains.

This is one source project's two films, displayed as a separate source spotlight. The existing 183-case catalog count is unchanged. The author reports Claude Opus 5.5; we did not reproduce the generation. A dated GitHub star snapshot describes the source repository, not views of either film or a global popularity ranking. See [the exact source, hash and review manifest](data/readme-featured-cases.json).

## Existing archive versus deployed site

The pre-existing raw archive and research manifests remain in Git for review and recovery. This repair does **not** erase Git history, remove every public repository copy, or claim all underlying rights are cleared. Its scope is public embedding and the Pages artifact. A separate rights review is needed before continued distribution of archival files; removal from Git history is a separate, potentially destructive decision.

As of the 2026-11-11 review of `fd831de`, 217 of 225 saved thumbnails and 301 of 309 case-media files did not have the documented ailingqu grant. The 301 include all 233 MP4 paths. Those files are not embedded or included in the new Pages artifact. Six old repository-seed GIFs also lack verified reference ownership and are not enabled for public playback.

`docs/data/local-media-manifest.json`, `data/case-images.json`, and `data/case-videos.json` retain archival provenance. Their download status and raw URLs are not public rendering permission. No re-download is needed for this repair.

## Publication and playback checks

- `python3 tools/verify.py` remains the single verification entry point. It checks both archival integrity and public publication policy.
- `python3 tools/build_public_site.py --output _site` builds a **new** directory containing text/code and only approved media. Pages uploads `_site`, never the raw `docs` tree.
- Public builds reject Git LFS pointers, changed approved files, missing media, unapproved embeds, and remote media hotlinks. Archive-only pointer OID/size checks do not establish playback.
- Any future approved LFS video must be materialized before building; a pointer cannot be silently deployed. Test actual browser playback and source fallback before publishing it.
- X animated GIFs are often MP4. Keep the real format; never rename MP4 bytes to GIF. A format probe is not a visual review or proof of model provenance.

未经核实授权的媒体默认只提供原帖入口。署名、下载成功、仓库所有者要求归档，都不是作者授权。本次保留旧归档以便复核与恢复，但停止公开页面嵌入，并从 Pages 发布包排除未授权素材；没有清除 Git 历史，也不等于所有素材的权利问题已经解决。八个 ailingqu GIF 及其注明修改的缩略图按明确的 CC BY 4.0 来源授权保留。

If you own material here and have a rights concern, open a GitHub Issue for review or removal.

## Documented grants: additional model-table stills

Three separately labeled still-image works accompany the README model tables. They do not enter the 183-case main catalog or imply the current coding models produced these images. Exact hashes, source revisions, four-language descriptions and original credit chains are in [the supplemental manifest](data/readme-supplemental-previews.json); visible attribution and modification records are in [preview credits](docs/readme-preview-credits.md).

- Qwen-Image-2.1: Mats2208's snowy-street adaptation of Mbaro01's Calle Charcas photograph. The pinned project explicitly licenses edits of its CC BY-SA benchmark photographs under CC BY-SA 4.0. The original photographer, original photo link, adapting author and license are retained. This output and any derivatives remain CC BY-SA 4.0.
- Imagen through the Gemini app, 2025: VulcanSphere's valley image on Wikimedia Commons, with an explicit file-specific CC0 dedication. The current description says Imagen 4.0 while the initial upload summary says 3.0; the public caption discloses this uncertainty instead of asserting a precise version. This is not Gemini 4 Carbon.
- Grok Aurora, December 2024: VulcanSphere's astronaut riding a horse on the Moon, with an explicit file-specific CC0 dedication. This is not a Grok 4.7 coding or video example.

All three files are unchanged original WebPs, with source marks preserved; the HTML only scales their display. The full [CC BY-SA 4.0](docs/licenses/CC-BY-SA-4.0.txt) and [CC0 1.0](docs/licenses/CC0-1.0.txt) texts are included. Source statements are not independent reproduction of generation. License grants do not establish model authenticity.
