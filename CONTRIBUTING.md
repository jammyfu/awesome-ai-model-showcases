# Contributing

This repo’s **primary index is the community case catalog**, not original remake playbooks.

Maintained languages: English [`README.md`](README.md) and Simplified Chinese [`README.zh-CN.md`](README.zh-CN.md) share one catalog (`docs/data/community-cases.json`). Do not add another README unless it is fully synced to that same inventory.

## Submit a community original-author case

1. Give the original post URL, author, real GIF/MP4/reference stills, verbatim prompt or an explicit empty prompt, model evidence, pipeline, and a license-unknown note.
2. Archive every attachment into `docs/cases/<id>/media/` (do not take only the first file). Keep X MP4 as `.mp4`.
3. Store the full original prompt in `docs/cases/<id>/prompt.md` and post/process notes in `post.md`.
4. Run `python3 tools/ingest_local_media.py` (incremental: skips unchanged sha256) then `python3 tools/verify.py`.
5. Do not put SVG concept art, this repo’s `prompt_adaptation`, promo/2.5/multimodel/failure samples in the main catalog.

See [`.github/ISSUE_TEMPLATE/case-submission.yml`](.github/ISSUE_TEMPLATE/case-submission.yml) and [`docs/data/SOURCE_DATA.md`](docs/data/SOURCE_DATA.md).

# Contributing GIFs (optional local seeds)

PRs are welcome for original, rights-cleared GIF animations and well-documented prompts. Local files in `docs/gifs/` are **repository seeds**, not the community collection.

1. Submit a genuine multi-frame `.gif` (not a PNG with a GIF extension), preferably under 5 MiB.
2. Use lowercase ASCII filenames in `docs/gifs/`, e.g. `smiling-robot.gif`.
3. Write `prompts/smiling-robot.md` and say whether it is the **verbatim original prompt** or a **reconstructed brief**. Never claim an unknown model checkpoint was used with certainty.
4. Add one record in `docs/data/gallery.json`.
5. Run `python3 tools/verify.py` after installing `requirements-dev.txt`.
6. In your PR, declare permission to share the animation and any source photo, original meme, fictional character, third-party brand, or recognizable person's likeness.
7. Please do not include API keys or private user data.

The **MIT LICENSE covers code**, not automatically every sample animation or third-party source. See `MEDIA_RIGHTS.md`.
