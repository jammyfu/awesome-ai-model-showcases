# 游戏动作序列（与普通 GIF 分开）

核实：北京时间 2026-11-06。独立页面：[docs/game.html](../docs/game.html)。深挖后计数：**旧案补全 4、独立新增成功工作流 0、独立失败样本 2**。同团队 evals 文章不计新案例。Higgsfield 9 帖=1 组宣传。检索页数是覆盖日志，见 [game-search-log.md](game-search-log.md)，不拿来充案例。

官方验证 **0**。媒体全部未观看，演示站未运行。X 附件写 GIF 的实际是 **MP4**。原文缺就空。

## 真实制作还要补的工序

- **Daft**：跳跃回复承认事后 flatten 背景去闪烁。不能称所有动作无需后处理。演示站 [gameslash.app](https://gameslash.app/) 未运行。
- **狐浪人**：公开全文是给 **游戏 agent** 的 one-shot，不是发给 2.6 的图像 prompt。图像 prompt 未公开。文章 4×4 品红底模板是重建。[@evals_ag 44 游戏场报](https://x.com/evals_ag/status/2118336675697090607) 是同团队补证。
- **walk**：Opus 量化到 7 色、锁头、镜像第 5–8 帧腿、手修 14 个头部像素。像素是假象。
- **小墨**：深挖后仍无 prompt、无引擎实机。
- **Pocketworld**：2.6 管 look/mood；最终 idle/attack 由代码画，不当纯 2.6 动画。

| 方案 | 验证级别 | 管线 | 原文 prompt |
|---|---|---|---|
| [像素三连击](https://x.com/Daft_Trade/status/2118283025498906800) | 原作者声明 | 自称直出 GIF；跳跃有修帧 | **空** |
| [狐浪人](https://x.com/maker_evan/status/2118222694345040253) | 原作者声明 | 2.6 出表 → Sol 切帧 | **游戏 agent one-shot**；图像 prompt 未公开 |
| [复古格斗](https://x.com/xiaomovps/status/2118274032227471705) | 原作者声明 | 自称 GIF/sheet | **空** |
| [walk cycle](https://x.com/maker_evan/status/2118235403430027495) | 多模型后处理 | 2.6 + Opus 修帧 | **空** |
| [骑士跑](https://github.com/vargHQ/skills/blob/main/gpt-image-sprite-sheet/SKILL.md) | 作者声明工作流 | 出表再切帧 | 逐字英文规格 |
| [Higgsfield 9 帖](https://x.com/higgsfield_ai/status/2118154923070439759) | 宣传 1 组 | 宣称 GIF sheets | **空** |
| [【2.5】4×4](https://x.com/SSSS_CRYPTOMAN/status/2097797456117539136) | 不是 2.6 · 默认隐藏 | 出表再切帧 | 逐字日文 |

## 失败样本（不计成功）

| 样本 | 要点 |
|---|---|
| [@AM09_21](https://x.com/AM09_21/status/2118143217434800219) | 动态+静态同帧会崩；应分 sprite 生成 |
| [@WrongNebula](https://x.com/WrongNebula/status/2118164394400182755) | 像素动画 not there yet；作者后写不适合 pixel art |

yrzhe vs Renoise coming soon：**仍待核**。弱相关/剔除见附录。
