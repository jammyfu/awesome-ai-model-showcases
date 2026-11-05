# Contributing GIFs

PRs are welcome for original, rights-cleared GIF animations and well-documented prompts.

1. Submit a genuine multi-frame `.gif` (not a PNG with a GIF extension), preferably under 5 MiB.
2. Use lowercase ASCII filenames in `docs/gifs/`, e.g. `smiling-robot.gif`.
3. Write `prompts/smiling-robot.md` and say whether it is the **verbatim original prompt** or a **reconstructed brief**. Never claim an unknown model checkpoint was used with certainty.
4. Add one record in `docs/data/gallery.json` with `id`, `title`, `description`, `description_zh`, `category`, `tags`, `image`, `prompt`, `prompt_file`, `prompt_status`, `model`, `frames`, `duration_ms`, `width`, `height`, and `source_note`.
5. Run `python3 tools/sync_gallery_js.py` then `python3 tools/validate_gallery.py` after installing `requirements-dev.txt`.
6. In your PR, declare that you have permission to share the animation and any source photo, original meme, fictional character, third-party brand, or recognizable person's likeness. Credit source creators and link to their original source where available.
7. Please do not include API keys, private user data or unlicensed source material. Submissions may be declined on attribution, quality, safety, or rights grounds.

## Quality checklist

- [ ] GIF visibly animates, with smooth/intentional loop
- [ ] Identity and camera remain stable unless movement is intentional
- [ ] Frame count and timing match the actual file
- [ ] English/Chinese summaries are informative, not keyword-stuffed
- [ ] Source and usage rights are provided
- [ ] No misleading claim of a tested API call or exact checkpoint
- [ ] Metadata sync + GIF validator pass

## Idea catalog (optional, no GIF required)

To add a sourced use case without shipping a GIF:

1. Append one object to `docs/data/ideas.json`.
2. Set `prompt_status` to `verbatim`, `reconstructed`, or `empty`. If the original prompt was not published, leave `prompt` as `""` — do not invent third-party wording.
3. Set `preview_kind` to `concept_illustration` (original SVG under `docs/previews/`), `existing_gif`, or `link_only` (empty `preview`, HTTPS `source_url` only). Do not download paywalled or personal photos, and do not pretend a third-party GIF was generated here.
4. Set `output_kind` to `gif`, `sprite_sheet`, `still`, `svg`, or `edit`. Non-GIF kinds use `frames` 0 and `frame_duration_ms` 0.
5. Run `python3 tools/sync_ideas.py` then `python3 tools/validate_ideas.py`.

The **MIT LICENSE covers code**, not automatically every sample animation or third-party source. See `MEDIA_RIGHTS.md`.
