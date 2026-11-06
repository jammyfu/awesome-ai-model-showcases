# game-xiaomovps-fighter

- Author: @xiaomovps
- Source: https://x.com/xiaomovps/status/2118274032227471705
- Model: 作者声明 GPT Images 2.6（非官方验证；本仓未观看、未复测）
- Pipeline: native_gif_and_or_sprite_claimed
- Verification: 作者声明 2.6 · 非官方验证 · 未观看
- Workflow: {'claimed': 'native_gif_and_or_sprite_sheet', 'author_words': '可以直接生成 GIF 动画和 Sprite Sheet 精灵序列图', 'certainty': 'author_claimed_both', 'note': '作者同时提到 GIF 与 Sprite Sheet；帖内可见 animated_gif + 静图；未观看，无法确认是否另有切帧合成'}

## Play / 玩法

复古 16 位街机格斗向：生成人物/场景/血条后继续出拳、蓄力等循环 GIF；作者讨论透明背景拆帧进 Unity/Godot 与 Sprite Sheet

## Original post text

GPT 最新图片模型有点离谱，连游戏人物的动作素材都能直接生成了 🔥

最近体验了一下 GPT 最新的 Images 2.6，发现这次更新对独立游戏开发者还挺有意思的

我直接让 GPT 生成了一个复古 16 位街机格斗游戏，人物、场景、血条这些元素都给生成出来了

然后继续让它把游戏人物做成 GIF 动图，没想到现在连人物出拳、蓄力这些动作都能生成，还可以做成循环动画

这次更新我觉得有 3 个比较实用的地方：

1、游戏人物动作生成

以前 AI 生成的基本都是静态角色，现在可以直接生成 GIF 动画和 Sprite Sheet 精灵序列图，像待机、出拳、跳跃这些动作，都可以尝试让 GPT 生成

2、透明背景人物素材

生成完人物之后，还可以直接去掉背景，只保留角色和动作，后续可以拆分成独立帧，放进 Unity、Godot 这些游戏引擎里面使用

3、SVG 矢量素材生成

这次连 SVG 也支持了，可以通过 API 生成游戏图标、技能按钮、血条等 UI 素材，后续修改尺寸和颜色也方便很多

当然目前还有一些问题，比如人物在连续动作中可能出现形象不一致，实际使用还需要调整动作帧和碰撞区域

但我觉得这次最大的变化，是 GPT 已经不只是帮你生成游戏概念图了，而是开始能直接参与游戏素材的制作

对于独立开发者来说，感觉以后一个人做 2D 小游戏的门槛又降低了不少

## Notes / process

真实制作缺口：完整图像 prompt；引擎导入与碰撞区；连续动作形象一致性。深挖未补上这些。
