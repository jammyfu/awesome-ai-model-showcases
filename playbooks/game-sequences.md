# 游戏动作序列（与普通 GIF 分开）

核实：北京时间 2026-11-06。独立页面：[docs/game.html](../docs/game.html)。不是表情包凑数。股市哭脸 / Morphic 面包师 / 路飞六宫格挥手仍是循环 GIF 宫格，**不是** idle / run / attack。

验证级别：**官方验证 0**。原作者均声明 2.6，媒体 HEAD 已核，**全部未观看、未运行、未复测生成**。`counts_as_image26_game` 全部为 false。直出 GIF 是作者说法；X `animated_gif` 对外是 **MP4**。无授权只外链，不拿 SVG 充效果。原文 prompt 缺就空；中文改编是本站策划。

| 方案 | 验证级别 | 管线 | 引擎 | 原文 prompt |
|---|---|---|---|---|
| [像素三连击 / 翻滚 / 法术](https://x.com/Daft_Trade/status/2118283025498906800) | 原作者声明 2.6 | 作者称直出 GIF；4 条 MP4=1 案 | 无 | **空**（仅有设置摘录） |
| [狐浪人网页游戏](https://x.com/maker_evan/status/2118222694345040253) | 原作者声明 2.6 | **2.6 出表 → 另一 agent 切帧**，绝非原生 GIF | 作者给了页面/录像；**本仓未运行未观看** | 逐字 one-shot |
| [复古格斗出拳 / 蓄力](https://x.com/xiaomovps/status/2118274032227471705) | 原作者声明 2.6 | 作者称 GIF 和/或 sprite sheet | 讨论 Unity/Godot；**未见运行画面** | **空** |
| [像素 walk cycle 对照](https://x.com/maker_evan/status/2118235403430027495) | **多模型后处理** | 2.6 出表后再经 Claude Opus 5.5 修帧；纯代码对照**不算 2.6** | 无 | **空**（仅 32×32 / 8 色 / 8 帧摘录） |
| [骑士跑循环](https://github.com/vargHQ/skills/blob/main/gpt-image-sprite-sheet/SKILL.md) | 作者声明工作流（与狐浪人不同源，保留） | 出表再切帧 PNG | 文档有 Phaser/Godot，**未实机跑** | 逐字英文规格 |
| [拳击游戏视频](https://x.com/higgsfield_ai/status/2118154923070439759) | **宣传方宣称**，不算原作者强例 | 宣称 GIF sprite sheets；附件是 amplify **MP4** | 本仓未观看 | **空** |
| [【2.5 历史】4×4 分镜规格](https://x.com/SSSS_CRYPTOMAN/status/2097797456117539136) | **不是 2.6** · 默认隐藏 | 出表再切帧 | 无 | 逐字日文 |

[打开独立页面](https://jammyfu.github.io/awesome-gpt-image-gifs/game.html)

## 未收 / 不当确认

- [@yrzhe_top 2118211871777890325](https://x.com/yrzhe_top/status/2118211871777890325)：作者称 2.6 GIF 做小游戏素材，但 Renoise 官方帖写 2.6 **coming soon**。冲突项**不当确认**，见 [game-pending.md](game-pending.md)。
- Higgsfield 同线程废料场 / 花灯 / 武士 / 对打：挂在拳击卡 `related_source_urls`，不拆新卡。
- zone 像素动作已在旧 x 清单，不另开游戏强例。
- ToonBee / PoYo（写明 2.5）/ chongdashu（2.0）/ @xikhar（未写 2.6）/ 红发墙跳（开源 sprite-gen）。
- 仓库 `martial-arts-combo.gif`：训练房连招循环，不是等大格子图集。
