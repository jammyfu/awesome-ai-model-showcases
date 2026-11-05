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
3. Set `preview_kind` to `concept_illustration` (original SVG under `docs/previews/`), `existing_gif` (file in `docs/gifs/`), `external_gif` (HTTPS `media_url`, empty local `preview`, `media_rights=unknown_link_only`), or `link_only`. Do not download third-party GIFs without a documented redistribution license. Do not present Morphic 2.5 / Ideogram examples, Atlas pre-2.6 GIFs, or SVG covers as Image 2.6 generated results. If a source labeled GIF is actually MP4, set `media_kind` to `mp4`, `visual_review_status` to `unwatched` unless someone actually watched it, and keep it out of the GIF gallery. Put third-party wording in `prompt` and this repo's rewrite in `prompt_adaptation`. Pending X candidates stay in `playbooks/x-pending.md`, not in confirmed idea cards.
4. Set `output_kind` to `gif`, `sprite_sheet`, `still`, `svg`, or `edit`. Non-GIF kinds use `frames` 0 and `frame_duration_ms` 0.
5. Run `python3 tools/sync_ideas.py` then `python3 tools/validate_ideas.py`.
6. Popular-GIF remakes belong in `docs/data/popular-playbooks.json` (not `ideas.json`). They must stay labeled **not Image 2.6**. Keep the four evidence types separate (annual chart / event chart / trending snapshot / fame-only). Do not invent a world ranking or a missing 2024/2025 annual YIR. Reference-library size is not a playbook quota.
7. Game idle/run/attack sequences belong in `ideas.json` with `game_sequence: true`. Image 2.5 / other-model history uses category `其他模型参考`, `default_hidden: true`, and `image26_status: not_26` — it must not appear in the default 2.6 list or count as a 2.6 card. Author claims, promo claims, and multimodel postprocess are separate statuses; none of them are official verification (`counts_as_image26_game` stays false this round). X `animated_gif` is usually MP4. Say “used in a game” only when there is engine-import evidence that was actually run or watched. White-keying is not true alpha. Missing original prompts stay empty; this repo’s Chinese rewrite stays in `prompt_adaptation`. Game cards must not enter the GIF gallery.

The **MIT LICENSE covers code**, not automatically every sample animation or third-party source. See `MEDIA_RIGHTS.md`.
