# Contributing / 参与贡献

Help people find useful animation ideas **with the original author, source, and evidence intact**. This repository's primary collection is community cases, not remake playbooks.

[English](#english) · [简体中文](#简体中文)

## English

### The easiest contribution: share a source

[Open the case submission form](https://github.com/jammyfu/awesome-ai-model-showcases/issues/new?template=case-submission.yml). You do not need to edit JSON or write code. Include:

- Original author and post URL, not only a repost or aggregator.
- Every GIF, MP4, and reference-image URL, including attachments in the documented thread.
- The prompt exactly as published. Say **unpublished** if it is unavailable, or **partial** if only an excerpt is public. Do not reconstruct a prompt and call it original.
- The source's model claim and evidence, the native-animation/sprite-sheet/post-processing pipeline, and what you actually checked.
- Any documented permission or reuse license. Otherwise keep **license unknown**.

Attribution fixes, broken-link reports, clearer English/Chinese wording, and source corrections are welcome too.

### Make a pull request

1. Fork the repository and create a focused branch. Keep unrelated content changes separate.
2. Read [source data conventions](docs/data/SOURCE_DATA.md). Update the appropriate input inventory, not the generated `docs/data/community-cases.json` or README files. README layout lives in `tools/templates/`.
3. For new community media, archive all documented attachments into `docs/cases/<id>/media/`. Preserve real extensions: X `animated_gif` often means `.mp4`. Store the published prompt or explicit empty marker in `prompt.md` and source/process notes in `post.md`.
4. Default to source links. Do not ingest or publish new third-party files until their specific grant is reviewed. Add approved exact paths, SHA-256, credit, source, evidence and change notices to `data/public-media-rights.json`. Regenerate with `python3 tools/write_community_catalog.py` and `python3 tools/render_public_media.py`.
5. Regenerate, inspect the diff, stage the intended generated files, then run the single verification entry:

```bash
python3 -m pip install -r requirements-dev.txt
python3 tools/write_community_catalog.py
git diff --check
git diff --stat
# Stage only files you reviewed, including intentional generated changes.
git add <reviewed-files>
python3 tools/verify.py
```

The freshness checks compare generated working files with the Git index, so un-staged intentional generated changes will fail. Python + Pillow are required; Node.js also runs the optional gallery JavaScript smoke test (explicitly skipped when unavailable); install ffmpeg to use the same MP4 stream checks as CI. Without `ffprobe`, the local ISO-BMFF fallback has narrower coverage.

6. Describe the source, prompt status, rights status, changed files, and validation results in your PR. A UI/docs change should include a preview when useful.

Do not add promo, 2.5, multimodel, failure, or unresolved cases to the confirmed main buckets. Keep their evidence in the appropriate pending/appendix category. Do not treat source claims as independently verified generation.

### Optional local seed GIFs

New original seed animations require verified rights before publication in `docs/gifs/` and `docs/data/gallery.json`, outside the community-case count. Use a genuine multi-frame GIF, preferably under 5 MiB, a lowercase ASCII filename, and a matching `prompts/<name>.md`. Clearly label exact prompts versus reconstructed briefs. Declare rights for source photos, characters, brands, and recognizable likenesses. Never include API keys or private user data.

## 简体中文

### 不写代码也能贡献

[提交案例表单](https://github.com/jammyfu/awesome-ai-model-showcases/issues/new?template=case-submission.yml)，附上原作者、原帖、全部媒体链接、公开提示词或“未公开”、模型依据与制作流程。只有部分提示词时请明确标注，不要把推测重写当成原文。没有可核实授权时，许可仍写“未知”。

署名更正、链接修复、来源补充和中英文说明改进，同样欢迎。

### 提交 PR 的要点

1. Fork 并新建专门分支，阅读[数据约定](docs/data/SOURCE_DATA.md)。修改来源清单；不要直接修改自动生成的目录或 README。排版源模板在 `tools/templates/`。
2. 新案例保留全部附件和真实格式，将素材、原文提示词（或明确的未公开标记）、来源过程说明分别存入 `docs/cases/<id>/media/`、`prompt.md`、`post.md`。
3. 默认只保留原帖链接。核实具体作品的发布授权后，才下载新素材并在 `data/public-media-rights.json` 记录路径、SHA-256、署名、许可证据和修改说明。
4. 按上方命令重新生成，审查差异，暂存预期生成结果后运行 `python3 tools/verify.py`。未暂存的预期生成改动会被新鲜度检查判为未同步。安装 ffmpeg 可与 CI 一样检查 MP4 视频流。
5. PR 中写清出处、提示词公开状态、许可与验证结果。作者声明不等于独立验证，待核或附录内容不要混入主表。

原创、已获许可的本地种子 GIF 单独放在 `docs/gifs/`，不计入社区案例数。不要上传 API Key 或私人数据。

## Rights / 许可

[MIT](LICENSE) covers source code and original project documentation, not third-party media, prompts, or likenesses. See [MEDIA_RIGHTS.md](MEDIA_RIGHTS.md). Rights holders can open an issue with the affected case URL for attribution or removal requests.

MIT 不自动覆盖第三方素材、提示词或肖像。权利人可附案例链接提出署名更正或移除请求。

Public deployment uses `tools/build_public_site.py`, not a direct upload of `docs/`. It rejects unresolved LFS pointers. Existing archive pointer checks are not playback tests. See [MEDIA_RIGHTS.md](MEDIA_RIGHTS.md).

CI also runs `RUN_BROWSER_TESTS=1 python3 tools/verify.py` with pinned Playwright 1.56.1 and Chromium. This exercises all case pages, source-only fallbacks, search, and visible licensed-GIF animation. Ordinary local verification explicitly reports when browser playback was not run.
