# GPT Image 2.6 玩法与 Prompt 图像列表（32 例）

> Updated: 2026-11-06（北京时间）。`official` = OpenAI 展示方向；`tested` = 公开第三方实测或可复制提示词库；`community` = 社区案例；`concept` = 本项目原创延伸模板。Prompt 标注 `verbatim` / `reconstructed` / `empty`。不是按真实搜索量排名。

[打开交互式图像列表](https://jammyfu.github.io/awesome-gpt-image-gifs/ideas.html) · [结构化 JSON](../docs/data/ideas.json) · [参考出处](sources.md) · [来源与方法](trends-2026-11.md)

| # | 玩法 | 类别 | 来源 | Prompt | 建议模型 / 规格 |
|---:|---|---|---|---|---|
| 1 | [猫咪怒撞屏幕](../docs/gifs/cat-screen-crack.gif) | 表情梗图 | [参考](https://github.com/jammyfu/awesome-gpt-image-gifs/blob/main/docs/gifs/cat-screen-crack.gif) | [本站改写，非第三方原文](#idea-1) | Sunburst / 12f |
| 2 | [摸头循环表情包](../docs/gifs/pixel-head-pat.gif) | 表情梗图 | [参考](https://github.com/jammyfu/awesome-gpt-image-gifs/blob/main/docs/gifs/pixel-head-pat.gif) | [本站改写，非第三方原文](#idea-2) | Flare / 12f |
| 3 | [动漫角色点头](../docs/previews/anime-nod.svg) | 角色动画 | [参考](https://www.reddit.com/r/OpenAI/comments/1xoh2u0/i_tried_the_new_image_26_gif_feature/) | [本站改写，非第三方原文](#idea-3) | Sunburst / 12f |
| 4 | [数字助手正在输入](../docs/previews/typing-companion.svg) | 网站交互 | [参考](https://openai.com/index/introducing-images-2-6/) | [本站改写，非第三方原文](#idea-4) | Flare / 9f |
| 5 | [手绘草图变活物](../docs/previews/sketch-owl.svg) | 角色动画 | [参考](https://openai.com/index/introducing-images-2-6/) | [本站改写，非第三方原文](#idea-5) | Sunburst / 12f |
| 6 | [耳机盒开合](../docs/previews/earbuds-product.svg) | 产品广告 | [参考](https://image.lightlyn.com/gpt-image-2-6?lang=en) | [本站改写，非第三方原文](#idea-6) | Sunburst / 12f |
| 7 | [香水瓶流光](../docs/previews/perfume-light.svg) | 产品广告 | [参考](https://veevid.ai/blog/gpt-image-2-6-gif) | [本站改写，非第三方原文](#idea-7) | Sunburst / 9f |
| 8 | [霓虹字切换](../docs/previews/neon-word-switch.svg) | 创意特效 | [参考](https://nowrap.ai/tools/chatgpt-images-2-6) | [本站改写，非第三方原文](#idea-8) | Sunburst / 12f |
| 9 | [Sprite 分镜再转 GIF](../docs/previews/sprite-sheet-stock-crash.svg) | Sprite 分镜 | [参考](https://openai.com/index/introducing-images-2-6/) | [逐字公开提示词](#idea-9) | Sunburst / 6 格 |
| 10 | [面包师吉祥物分镜表](../docs/previews/baker-mascot-sprite.svg) | Sprite 分镜 | [参考](https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts) | [逐字公开提示词](#idea-10) | Sunburst / 6 格 |
| 11 | [剪纸锦鲤环游](../docs/previews/papercraft-koi.svg) | 创意特效 | [参考](https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts) | [逐字公开提示词](#idea-11) | Sunburst / 6 格 |
| 12 | [圈选花瓶改色](../docs/previews/markup-vase-recolor.svg) | 局部改图 | [参考](https://developers.openai.com/api/docs/guides/image-prompting) | [逐字公开提示词](#idea-12) | Sunburst / 编辑 |
| 13 | [圈选替换招牌字](../docs/previews/markup-sign-text.svg) | 局部改图 | [参考](https://www.nereo.io/blog/gpt-2-6-prompts) | [逐字公开提示词](#idea-13) | Sunburst / 编辑 |
| 14 | [可缩放面包店 SVG 标志](../docs/previews/svg-field-flour.svg) | SVG 与 Logo | [参考](https://developers.openai.com/api/docs/guides/image-prompting) | [逐字公开提示词](#idea-14) | Flare / SVG |
| 15 | [天气图标 SVG 套件](../docs/previews/svg-weather-icons.svg) | SVG 与 Logo | [参考](https://image.lightlyn.com/gpt-image-2-6?lang=en) | [逐字公开提示词](#idea-15) | Sunburst / SVG |
| 16 | [吉祥物三视图设定表](../docs/previews/character-ref-sheet.svg) | 角色设定 | [参考](https://morphic.com/resources/how-to/chatgpt-images-2-6-guide) | [逐字公开提示词](#idea-16) | Sunburst / 静图 |
| 17 | [同一角色换场景](../docs/previews/character-new-scene.svg) | 角色设定 | [参考](https://www.nereo.io/blog/gpt-2-6-prompts) | [逐字公开提示词](#idea-17) | Sunburst / 静图 |
| 18 | [提灯小猴循环](../docs/previews/lantern-monkey-gif.svg) | 角色动画 | [参考](https://developers.openai.com/api/docs/guides/image-prompting) | [逐字公开提示词](#idea-18) | Sunburst / 9f |
| 19 | [精确文字促销徽章](../docs/previews/sale-badge-gif.svg) | 文字海报 | [参考](https://www.nereo.io/blog/gpt-2-6-prompts) | [逐字公开提示词](#idea-19) | Flare / 9f |
| 20 | [茶叶盒展开刀模](../docs/previews/packaging-dieline.svg) | 产品广告 | [参考](https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts) | [逐字公开提示词](#idea-20) | Sunburst / 静图 |
| 21 | [六区标注烘焙剖面](../docs/previews/labelled-bakery-cutaway.svg) | 文字海报 | [参考](https://morphic.com/resources/how-to/chatgpt-images-2-6-guide) | [逐字公开提示词](#idea-21) | Sunburst / 静图 |
| 22 | [只改一处的冬季版](../docs/previews/winter-edition-edit.svg) | 局部改图 | [参考](https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts) | [逐字公开提示词](#idea-22) | Sunburst / 编辑 |
| 23 | [橱窗里的精确字海报](../docs/previews/autumn-bake-poster.svg) | 文字海报 | [参考](https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts) | [逐字公开提示词](#idea-23) | Sunburst / 静图 |
| 24 | 上传角色让它招手 | 角色动画 | [参考](https://x.com/Krouxzz/status/2118283796181053637) | [逐字公开提示词](#idea-24) | Flare / 9f |
| 25 | [实拍咖啡只动蒸汽](../docs/previews/photo-to-gif-steam.svg) | 照片微动效 | [参考](https://image.lightlyn.com/gpt-image-2-6?lang=en) | [逐字公开提示词](#idea-25) | Flare / 9f |
| 26 | [雨衣水獭挥手 GIF](../docs/previews/luffy-otter-wave-gif.svg) | 角色动画 | [参考](https://x.com/i/article/2118269816821919744) | [逐字公开提示词](#idea-26) | Flare / 6f |
| 27 | [六宫格连续帧再合成 GIF](../docs/previews/luffy-six-frame-then-gif.svg) | Sprite 分镜 | [参考](https://x.com/i/article/2118269816821919744) | [逐字公开提示词](#idea-27) | Sunburst / 6 格 |
| 28 | [同一角色九宫格表情包](../docs/previews/luffy-nine-stickers.svg) | 表情梗图 | [参考](https://x.com/i/article/2118269816821919744) | [逐字公开提示词](#idea-28) | Sunburst / 静图 |
| 29 | [只换背景保住商品](../docs/previews/luffy-product-bg-keep.svg) | 局部改图 | [参考](https://x.com/i/article/2118269816821919744) | [逐字公开提示词](#idea-29) | Sunburst / 编辑 |
| 30 | [清晰化但不要编造细节](../docs/previews/luffy-deblur-keep.svg) | 局部改图 | [参考](https://x.com/i/article/2118269816821919744) | [逐字公开提示词](#idea-30) | Sunburst / 编辑 |
| 31 | [软装预览不改户型](../docs/previews/luffy-interior-staging.svg) | 局部改图 | [参考](https://x.com/i/article/2118269816821919744) | [逐字公开提示词](#idea-31) | Sunburst / 编辑 |
| 32 | [同一商品放进生活场景](../docs/previews/luffy-product-lifestyle.svg) | 产品广告 | [参考](https://x.com/i/article/2118269816821919744) | [逐字公开提示词](#idea-32) | Sunburst / 静图 |

## 完整提示词（公开原文或本站改写）

标注 `verbatim` 的条目复制自注明来源的公开页面；`reconstructed` 是本站按创意目标改写的模板，不是第三方作者的逐字提示词；`empty` 表示来源只描述了能力、没有给出可复制提示词，本站留空。均未在此仓库逐项实测。

<a id="idea-1"></a>
### 01. 猫咪怒撞屏幕 / Cat vs. Cracked Screen

类型：表情梗图 ｜输出：GIF ｜证据：本项目已有 GIF 案例 ｜提示词：本站改写，非第三方原文 ｜推荐：`Sunburst`, `12` frames, `130` ms/frame, `4:5` ｜编辑优先级：P1

![猫咪怒撞屏幕 — 已有 GIF](../docs/gifs/cat-screen-crack.gif)

角色向镜头冲刺、头撞玻璃、裂纹扩散；可用已有猫咪动图预览。

```text
Create a funny looping animated GIF of an original black-and-white cat headbutting the camera glass. Beat 1: cat stares intensely. Beat 2: it lunges head-first without using its paws. Beat 3: a small spiderweb crack appears, then grows. Beat 4: the camera returns to the starting view to loop. Keep the eyes, whisker markings and background consistent. Fixed camera; expressive but non-graphic cartoon impact; no words or watermark.
```

参考链接（2026-11-05）：https://github.com/jammyfu/awesome-gpt-image-gifs/blob/main/docs/gifs/cat-screen-crack.gif。


<a id="idea-2"></a>
### 02. 摸头循环表情包 / Looping Head Pat Meme

类型：表情梗图 ｜输出：GIF ｜证据：本项目已有 GIF 案例 ｜提示词：本站改写，非第三方原文 ｜推荐：`Flare`, `12` frames, `180` ms/frame, `3:4` ｜编辑优先级：P1

![摸头循环表情包 — 已有 GIF](../docs/gifs/pixel-head-pat.gif)

左右角色保持站位，单手抬起、摸头、收回，天然循环。

```text
Create a seamless GIF with two ORIGINAL friendly cartoon characters. The taller blocky character on the left raises one hand, gently pats the shorter bald cartoon character on the head twice, then returns to the initial arm position. The receiver smiles and slightly nods in time. Keep faces, clothing, camera angle, grassy background and character positions unchanged. Clear contact and recovery poses, six to twelve distinct beats, no extra limbs, no captions.
```

参考链接（2026-11-05）：https://github.com/jammyfu/awesome-gpt-image-gifs/blob/main/docs/gifs/pixel-head-pat.gif。


<a id="idea-3"></a>
### 03. 动漫角色点头 / Anime Character Nodding

类型：角色动画 ｜输出：GIF ｜证据：社区公开案例 ｜提示词：本站改写，非第三方原文 ｜推荐：`Sunburst`, `12` frames, `140` ms/frame, `1:1` ｜编辑优先级：P1

![动漫角色点头 — 原创 SVG 概念示意](../docs/previews/anime-nod.svg)

上传原创角色，微抬头、快速点头、闭眼回位，适合贴纸。

```text
Animate an ORIGINAL anime-style adult character from a consistent front three-quarter portrait. She lifts her chin slightly, makes one quick affirmative nod, closes her eyes with a soft smile, then returns to the identical first-frame expression. Preserve hair strands, face proportions, outfit and line art between frames. Only the neck, eyelids and a few hair tips move. Simple clean background, locked camera, no speech bubbles, seamless looping GIF.
```

参考链接（2026-11-05）：https://www.reddit.com/r/OpenAI/comments/1xoh2u0/i_tried_the_new_image_26_gif_feature/。


<a id="idea-4"></a>
### 04. 数字助手正在输入 / AI Assistant Typing Indicator

类型：网站交互 ｜输出：GIF ｜证据：OpenAI 官方发布 ｜提示词：本站改写，非第三方原文 ｜推荐：`Flare`, `9` frames, `160` ms/frame, `1:1` ｜编辑优先级：P1

![数字助手正在输入 — 原创 SVG 概念示意](../docs/previews/typing-companion.svg)

官方展示了助手小角色的输入反馈，可用于 AI Agent UI。

```text
Create an original tiny mint-green desk companion mascot for an AI chat interface. It taps an invisible keyboard with alternating paws, pauses to blink, then returns to the start. Show only its head, tiny arms and torso on a transparent-looking plain solid background. Very small readable movement, fixed alignment and scale, no text, no chat bubbles, no UI mockup. Loop must feel calm and unobtrusive like a typing indicator.
```

参考链接（2026-11-04）：https://openai.com/index/introducing-images-2-6/。


<a id="idea-5"></a>
### 05. 手绘草图变活物 / Hand-drawn Owl Comes Alive

类型：角色动画 ｜输出：GIF ｜证据：OpenAI 官方发布 ｜提示词：本站改写，非第三方原文 ｜推荐：`Sunburst`, `12` frames, `160` ms/frame, `1:1` ｜编辑优先级：P1

![手绘草图变活物 — 原创 SVG 概念示意](../docs/previews/sketch-owl.svg)

官方示例：简笔画角色保持草稿风格并眨眼转头。

```text
Make an original pencil-line owl drawing on cream notebook paper animate while preserving the hand-drawn sketch style. The owl blinks, tilts its head left, lifts one wing slightly, then returns to its original pencil pose. Keep the page fibers, outline weight and shading nearly static. No camera pan, no change of drawing identity, no extra strokes that drift between frames. Subtle, seamless looping GIF.
```

参考链接（2026-11-04）：https://openai.com/index/introducing-images-2-6/。


<a id="idea-6"></a>
### 06. 耳机盒开合 / Earbuds Case Product Loop

类型：产品广告 ｜输出：GIF ｜证据：公开实测案例 ｜提示词：本站改写，非第三方原文 ｜推荐：`Sunburst`, `12` frames, `160` ms/frame, `1:1` ｜编辑优先级：P1

![耳机盒开合 — 原创 SVG 概念示意](../docs/previews/earbuds-product.svg)

第三方实测：耳机盒开启、耳机浮起、归位、合盖。

```text
Premium unbranded wireless earbuds in a pristine white charging case on a soft sage-green seamless studio backdrop. The lid opens slowly, both earbuds rise a few centimeters together, pause, lower into their slots, and the lid closes to the starting position. Same product geometry, hinges, perspective and shadow throughout. One locked three-quarter product camera, photorealistic softbox lighting, no written marks, no extra earbuds, seamless GIF loop.
```

参考链接（2026-11-05）：https://image.lightlyn.com/gpt-image-2-6?lang=en。


<a id="idea-7"></a>
### 07. 香水瓶流光 / Perfume Highlight Sweep

类型：产品广告 ｜输出：GIF ｜证据：公开实测案例 ｜提示词：本站改写，非第三方原文 ｜推荐：`Sunburst`, `9` frames, `180` ms/frame, `1:1` ｜编辑优先级：P1

![香水瓶流光 — 原创 SVG 概念示意](../docs/previews/perfume-light.svg)

香水瓶不动，仅玻璃高光从左到右流过，突出高级感。

```text
An unbranded frosted-glass perfume bottle centered on a pale limestone pedestal in a neutral beige studio. The bottle never moves. A narrow warm highlight sweeps over the bottle from left to right while a few dust motes float upward. Return smoothly to the initial light pattern; identical logo-free bottle and pedestal in all frames. Premium luxury product photography, fixed camera, no text, no hands or morphing geometry. Seamless loop.
```

参考链接（2026-11-05）：https://veevid.ai/blog/gpt-image-2-6-gif。


<a id="idea-8"></a>
### 08. 霓虹字切换 / Neon Lettering Flicker Loop

类型：创意特效 ｜输出：GIF ｜证据：公开实测案例 ｜提示词：本站改写，非第三方原文 ｜推荐：`Sunburst`, `12` frames, `200` ms/frame, `16:9` ｜编辑优先级：P2

![霓虹字切换 — 原创 SVG 概念示意](../docs/previews/neon-word-switch.svg)

实测关注多帧文字保持一致：霓虹牌 A/B 状态切换。

```text
Nighttime rainy storefront with a single clean neon sign that alternates between the exact words OPEN and LATE, one at a time. The pink word OPEN slowly dims; blue LATE lights up, then reverses to the starting state. Keep all other lettering, reflections, windows, pavement and camera completely stable. Never display the two words at once. Crisp legible typography in every frame, no invented extra signs, seamless looping animated GIF.
```

参考链接（2026-11-05）：https://nowrap.ai/tools/chatgpt-images-2-6。


<a id="idea-9"></a>
### 09. Sprite 分镜再转 GIF / Sprite Sheet Then GIF

类型：Sprite 分镜 ｜输出：Sprite 分镜 ｜证据：OpenAI 官方发布 ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `6` frames, `1:1` ｜编辑优先级：P1

![Sprite 分镜再转 GIF — 原创 SVG 概念示意](../docs/previews/sprite-sheet-stock-crash.svg)

开脑洞点：官方把循环 GIF 写成 3×2 分镜表，先出齐 6 格再按序播放。与本站「股票下跌崩溃」是同一题材的分镜工作流变体，不是新梗。

```text
Create a single animation sprite sheet for a seamless looping GIF. A super-cute chibi adult office worker sits at a desk watching a computer monitor with a clearly plunging stock-market line chart. The sequence: hopeful expression, notices the chart falling, eyes widen, face crumples, large cartoon tears stream down both cheeks, then quietly wipes tears while still staring at the falling chart. Oversized round head, tiny body, big expressive eyes, soft rounded features, messy fluffy hair, white shirt and loosened tie. Exactly 6 sequential frames arranged in a precise 3-column by 2-row grid, read left-to-right then top-to-bottom. Every panel has identical dimensions. Fixed front three-quarter camera, same character, same desk, monitor, outfit, and cozy miniature office background. Clear incremental facial and tear motion; sixth frame transitions smoothly toward the first. Polished kawaii chibi 3D toy-like style, warm pastel lighting, funny and sympathetic mood. No captions, no words, no numbers, no logos, no speech bubbles, no panel labels, no borders, no gutters.
```

参考链接（2026-11-04）：https://openai.com/index/introducing-images-2-6/。


<a id="idea-10"></a>
### 10. 面包师吉祥物分镜表 / Dough Baker Mascot Sprite Sheet

类型：Sprite 分镜 ｜输出：Sprite 分镜 ｜证据：Morphic 公开提示词库（示例跑在 2.5） ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `6` frames, `1:1` ｜编辑优先级：P1

![面包师吉祥物分镜表 — 原创 SVG 概念示意](../docs/previews/baker-mascot-sprite.svg)

开脑洞点：先做角色设定表，再用同一顶帽/腮红/领巾出 6 帧揉面→挥手循环，比单句「吉祥物招手」更能锁身份。

```text
One animation sprite sheet for a looping GIF of the dough baker mascot from the sheet, same hat, cheeks and rust-red neckerchief: exactly 6 frames in a 3-column by 2-row grid, every panel the same size. Sequence: kneads a ball of dough, presses, folds, looks up and smiles, waves, and the sixth frame leads back into the first. Fixed front three-quarter camera, the same oak counter and plain oat-colored background in every panel, the same soft clay-like 3D render. No text, no numbers, no borders, no gutters, no panel labels.
```

参考链接（2026-11-06）：https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts。


<a id="idea-11"></a>
### 11. 剪纸锦鲤环游 / Papercraft Koi Loop

类型：创意特效 ｜输出：Sprite 分镜 ｜证据：Morphic 公开提示词库（示例跑在 2.5） ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `6` frames, `1:1` ｜编辑优先级：P1

![剪纸锦鲤环游 — 原创 SVG 概念示意](../docs/previews/papercraft-koi.svg)

开脑洞点：不是照片微动，而是整条鱼用层叠色纸游一圈；俯视锁定、第六帧接回第一帧，适合做手工质感 sticker。

```text
One animation sprite sheet for a looping GIF: exactly 6 frames in a 3-column by 2-row grid, every panel the same size. A papercraft koi made of layered cut paper in vermilion, cream and ink black swims one slow circle through a still pond of deep teal paper ripples, its tail sweeping a little further in each frame, and the sixth frame leads smoothly back into the first. Fixed overhead camera, the same pond, lily pad and soft paper shadows in every panel, warm diffused light, tactile handmade texture. No text, no borders, no gutters, no panel labels.
```

参考链接（2026-11-06）：https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts。


<a id="idea-12"></a>
### 12. 圈选花瓶改色 / Markup Recolor One Object

类型：局部改图 ｜输出：编辑 ｜证据：OpenAI 官方提示词指南 ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `4:3` ｜编辑优先级：P1

![圈选花瓶改色 — 原创 SVG 概念示意](../docs/previews/markup-vase-recolor.svg)

开脑洞点：2.6 把 ChatGPT 圈选 markup 接到 API。透明 PNG 叠层指出位置，提示词只说改什么、什么必须留下，并删掉红圈。

```text
Recolor the striped vase inside the red circle to solid cobalt blue ceramic. Keep its shape, the dried stems, and the rest of the kitchen unchanged. Remove the red circle from the finished photo.
```

参考链接（2026-11-04）：https://developers.openai.com/api/docs/guides/image-prompting。


<a id="idea-13"></a>
### 13. 圈选替换招牌字 / Markup Replace Sign Text

类型：局部改图 ｜输出：编辑 ｜证据：Nereo 可复制提示词 ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `1:1` ｜编辑优先级：P1

![圈选替换招牌字 — 原创 SVG 概念示意](../docs/previews/markup-sign-text.svg)

开脑洞点：局部改图不是重画整张海报，而是圈出招牌、指定精确文案，并要求匹配原字体、颜色和透视。

```text
Change the words on the sign inside the circle to "[OPEN LATE]". Match the original lettering, color and perspective. Keep everything else unchanged.
```

参考链接（2026-11-05）：https://www.nereo.io/blog/gpt-2-6-prompts。


<a id="idea-14"></a>
### 14. 可缩放面包店 SVG 标志 / Field & Flour SVG Logo

类型：SVG 与 Logo ｜输出：SVG ｜证据：OpenAI 官方提示词指南 ｜提示词：逐字公开提示词 ｜推荐：`Flare`, `1:1` ｜编辑优先级：P1

![可缩放面包店 SVG 标志 — 原创 SVG 概念示意](../docs/previews/svg-field-flour.svg)

开脑洞点：生成接口可直接 output_format=svg，得到可改路径的矢量标，而不是嵌了位图的假矢量。官方同时给了 Flare/Sunburst 对照。

```text
Create an original, non-infringing logo for a company called Field & Flour, a local bakery.
The logo should feel warm, simple, and timeless. Use clean, vector-like shapes, a strong silhouette, and balanced negative space.
Favor simplicity over detail so it reads clearly at small and large sizes. Flat design, minimal strokes, no gradients unless essential.
Fully transparent background. Deliver a single centered logo with generous padding, clean alpha edges, and no solid backdrop, scenery, checkerboard, or watermark.
```

参考链接（2026-11-04）：https://developers.openai.com/api/docs/guides/image-prompting。


<a id="idea-15"></a>
### 15. 天气图标 SVG 套件 / Matching Weather Icon SVG Set

类型：SVG 与 Logo ｜输出：SVG ｜证据：公开实测案例 ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `3:2` ｜编辑优先级：P1

![天气图标 SVG 套件 — 原创 SVG 概念示意](../docs/previews/svg-weather-icons.svg)

开脑洞点：一次生成 6 个同线宽、同端点的图标，而不是 6 次风格漂移。Lightlyn 实测 SVG 约 2–13 KB，可进 Figma。

```text
A set of six matching line icons for a weather app arranged in a 3 by 2 grid: sun, cloud, rain, snow, thunderstorm, wind. Consistent stroke width, rounded ends, one accent colour.
```

参考链接（2026-11-05）：https://image.lightlyn.com/gpt-image-2-6?lang=en。


<a id="idea-16"></a>
### 16. 吉祥物三视图设定表 / Character Reference Sheet

类型：角色设定 ｜输出：静图 ｜证据：Morphic 公开提示词库（示例跑在 2.5） ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `3:2` ｜编辑优先级：P1

![吉祥物三视图设定表 — 原创 SVG 概念示意](../docs/previews/character-ref-sheet.svg)

开脑洞点：2.6 可保存参考图并按名调用。先出正/侧/背 + 表情条，再拿去出分镜或新场景，比口头描述更稳。

```text
A character reference sheet for an invented bakery's mascot: a small round baker made of soft bread dough, with a tiny white chef hat, flour-dusted cheeks and a rust-red neckerchief, shown three times at the same scale, front view, side view and back view, with a row of four small facial expressions beneath (cheerful, proud, sleepy, surprised). Soft clay-like 3D render with visible fingerprint texture, warm even studio light, plain oat-colored background, identical proportions and colors in every view. No text, no labels, no logos.
```

参考链接（2026-11-06）：https://morphic.com/resources/how-to/chatgpt-images-2-6-guide。


<a id="idea-17"></a>
### 17. 同一角色换场景 / Same Character, New Scene

类型：角色设定 ｜输出：静图 ｜证据：Nereo 可复制提示词 ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `16:9` ｜编辑优先级：P1

![同一角色换场景 — 原创 SVG 概念示意](../docs/previews/character-new-scene.svg)

开脑洞点：把设定表当 image 输入，只改动作与环境，并逐项点名脸、头发、服装、配色不许变。

```text
Using the character in the reference image, show them [crossing a rope bridge in the rain]. Keep the face, hair, outfit and colors the same.
```

参考链接（2026-11-05）：https://www.nereo.io/blog/gpt-2-6-prompts。


<a id="idea-18"></a>
### 18. 提灯小猴循环 / Lantern Monkey Loop

类型：角色动画 ｜输出：GIF ｜证据：OpenAI 官方提示词指南 ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `9` frames, `200` ms/frame, `1:1` ｜编辑优先级：P1

![提灯小猴循环 — 原创 SVG 概念示意](../docs/previews/lantern-monkey-gif.svg)

开脑洞点：官方 GIF 范例把起始姿势、提灯、眨眼、回落写进同一段，并给出 9 帧 × 200 ms = 1.8 秒、512²、Sunburst high。

```text
A little monkey in an olive-green hooded coat stands in a snowy pine forest at dusk. A wooden cabin glows in the background. The monkey holds a glowing amber paper lantern at chest height, slowly lifts it, looks up and blinks, then lowers it back to its starting pose. Keep the lantern in its hands and the camera still. Make the motion loop smoothly.
```

参考链接（2026-11-04）：https://developers.openai.com/api/docs/guides/image-prompting。


<a id="idea-19"></a>
### 19. 精确文字促销徽章 / Exact-Text Sale Badge GIF

类型：文字海报 ｜输出：GIF ｜证据：Nereo 可复制提示词 ｜提示词：逐字公开提示词 ｜推荐：`Flare`, `9` frames, `180` ms/frame, `1:1` ｜编辑优先级：P1

![精确文字促销徽章 — 原创 SVG 概念示意](../docs/previews/sale-badge-gif.svg)

开脑洞点：短循环不是角色在动，而是徽章钉死、火花在闪，并把要印的字放进引号要求逐字拼写。

```text
Make a looping GIF of a round badge that says "[50% OFF]" with small sparkles appearing around it. Spell the text exactly. Keep the badge in one place.
```

参考链接（2026-11-05）：https://www.nereo.io/blog/gpt-2-6-prompts。


<a id="idea-20"></a>
### 20. 茶叶盒展开刀模 / Tea Carton Packaging Dieline

类型：产品广告 ｜输出：静图 ｜证据：Morphic 公开提示词库（示例跑在 2.5） ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `16:9` ｜编辑优先级：P2

![茶叶盒展开刀模 — 原创 SVG 概念示意](../docs/previews/packaging-dieline.svg)

开脑洞点：不是拍成品包装，而是一次画出六面展开图、折叠虚线和两句精确文案，给包装设计预演。

```text
A flat packaging dieline for an unbranded loose-leaf tea carton laid out on a pale grey surface: front, back, two sides, top and bottom panels unfolded. Front panel reads HIGHLAND BREAKFAST with a small mountain line illustration; back panel has a short brewing guide reading STEEP 4 MINUTES AT 95 C. Sage green and cream with a thin gold rule, dotted fold lines between panels. Every word spelled correctly, no other text, no barcodes, no logos.
```

参考链接（2026-11-06）：https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts。


<a id="idea-21"></a>
### 21. 六区标注烘焙剖面 / Labelled Bakery Cutaway

类型：文字海报 ｜输出：静图 ｜证据：Morphic 公开提示词库（示例跑在 2.5） ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `16:9` ｜编辑优先级：P2

![六区标注烘焙剖面 — 原创 SVG 概念示意](../docs/previews/labelled-bakery-cutaway.svg)

开脑洞点：把 complexity 写进提示词——六区六块牌、每词只出现一次，并禁止门窗再长字。适合信息图与空间说明。

```text
Isometric cutaway illustration of a small corner bakery seen from above at a 45-degree angle, the front wall removed. Six areas, each with one short label on a small plaque, exactly once each: OVEN, PROOFING, COUNTER, PANTRY, SINK, SEATING. A baker shaping loaves, a customer at the counter, trays of bread cooling on racks, warm pastel palette, clean line work, soft shadows, plenty of fine detail. Those six plaques are the only text in the image: the door, windows, boxes and walls carry no signs or writing. Every word spelled correctly, no logos.
```

参考链接（2026-11-06）：https://morphic.com/resources/how-to/chatgpt-images-2-6-guide。


<a id="idea-22"></a>
### 22. 只改一处的冬季版 / One-Change Winter Edition

类型：局部改图 ｜输出：编辑 ｜证据：Morphic 公开提示词库（示例跑在 2.5） ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `2:3` ｜编辑优先级：P1

![只改一处的冬季版 — 原创 SVG 概念示意](../docs/previews/winter-edition-edit.svg)

开脑洞点：分轮编辑的最小单位——上一张海报只改标题和配色，版式不动。比一次重写整张更接近生产改稿。

```text
Make it the winter edition: headline WINTER BAKE, frost blue and rust. Keep the layout.
```

参考链接（2026-11-06）：https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts。


<a id="idea-23"></a>
### 23. 橱窗里的精确字海报 / In-Situ Exact-Text Poster

类型：文字海报 ｜输出：静图 ｜证据：Morphic 公开提示词库（示例跑在 2.5） ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `2:3` ｜编辑优先级：P1

![橱窗里的精确字海报 — 原创 SVG 概念示意](../docs/previews/autumn-bake-poster.svg)

开脑洞点：不是透明背景招贴，而是把海报贴进真实橱窗，要求 AUTUMN BAKE / EMBER & OAT 拼写正确，并禁止多余日期网址。

```text
A risograph-printed seasonal poster taped inside the front window of a small bakery, photographed straight on from the street in soft morning light. Headline AUTUMN BAKE in a bold rounded serif in rust red, a smaller line beneath reading EMBER & OAT, a two-color illustration of a scored loaf and wheat stalks in rust and deep green on cream paper, visible riso grain and slight misregistration, faint reflections of the street on the glass. Every word spelled correctly, no other text, no dates, no web addresses.
```

参考链接（2026-11-06）：https://morphic.com/resources/prompts/chatgpt-images-2-6-prompts。


<a id="idea-24"></a>
### 24. 上传角色让它招手 / Reference Character Wave GIF

类型：角色动画 ｜输出：GIF ｜证据：社区公开案例 ｜提示词：逐字公开提示词 ｜推荐：`Flare`, `9` frames, `180` ms/frame, `1:1` ｜编辑优先级：P2

本地不转载第三方成品图；请打开来源链接查看。

开脑洞点：最短可用句。上传参考图后只说 loop + waving；X 帖带演示 GIF，本仓库不转载该动画。

```text
Make a looping GIF of this character waving.
```

参考链接（2026-11-05）：https://x.com/Krouxzz/status/2118283796181053637。


<a id="idea-25"></a>
### 25. 实拍咖啡只动蒸汽 / Animate This Photo: Steam Only

类型：照片微动效 ｜输出：GIF ｜证据：公开实测案例 ｜提示词：逐字公开提示词 ｜推荐：`Flare`, `9` frames, `200` ms/frame, `3:2` ｜编辑优先级：P1

![实拍咖啡只动蒸汽 — 原创 SVG 概念示意](../docs/previews/photo-to-gif-steam.svg)

开脑洞点：与本站「咖啡热气微动」文生图模板不同，这条是上传实拍后只允许蒸汽和光线动。Lightlyn 2026-11-05 实测杯子/桌子/窗户保持不动。

```text
Make this photo move: gentle steam rises and curls above the latte, soft light flickers slightly. Keep the cup, the table and the window exactly as they are. Seamless loop.
```

参考链接（2026-11-05）：https://image.lightlyn.com/gpt-image-2-6?lang=en。


<a id="idea-26"></a>
### 26. 雨衣水獭挥手 GIF / Raincoat Otter Wave GIF

类型：角色动画 ｜输出：GIF ｜证据：路飞 @0xluffy_eth · X Article ｜提示词：逐字公开提示词 ｜推荐：`Flare`, `6` frames, `160` ms/frame, `1:1` ｜编辑优先级：P1

![雨衣水獭挥手 GIF — 原创 SVG 概念示意](../docs/previews/luffy-otter-wave-gif.svg)

开脑洞点：路飞强调先做一个短挥手，只动手臂、锁镜头和身份，再谈复杂动作。中文提示词要求直接输出可播放 GIF，不要静态预览。封面为本站 SVG，不转载原文动图。

```text
生成一个约 1 秒、可循环播放的 GIF 聊天表情。
角色：原创小水獭，奶咖色皮毛、奶油白嘴部、短圆耳朵，穿向日葵黄色连帽雨衣，头顶一只很小的蓝色纸船。
风格：软萌 3D 黏土玩具，大头小身体，轮廓干净。
动作：水獭面朝镜头微笑，举起右手，左右轻轻挥手，再放回胸口，接回开头。
正方形画面，纯白背景，全身完整。
相机固定，角色的大小、位置、服装和配色不变。
只做挥手，不跳跃、不转身、不切镜头。
不要文字、编号、边框、水印或额外角色。
请输出可以下载和播放的 GIF 文件，不要只给静态预览图。
```

参考链接（2026-11-05）：https://x.com/i/article/2118269816821919744。


<a id="idea-27"></a>
### 27. 六宫格连续帧再合成 GIF / Six-Frame Sheet Then GIF

类型：Sprite 分镜 ｜输出：Sprite 分镜 ｜证据：路飞 @0xluffy_eth · X Article ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `6` frames, `3:2` ｜编辑优先级：P1

![六宫格连续帧再合成 GIF — 原创 SVG 概念示意](../docs/previews/luffy-six-frame-then-gif.svg)

开脑洞点：表情轮播≠连续运动。先出无间隔 3×2 六格，再切帧对齐身体中心合成循环。下面两段按原文发表顺序收录，不是本站改写；封面为原创 SVG。

```text
以上传图片为角色参考，生成一张连续动作分镜图。
横向 3:2 画面，严格 3 列 2 行，共 6 个等大的正方形格子。
每格纯白背景，不画分隔线，不留格子之间的间隔。
按从左到右、从上到下排列。
第 1 格：右手放在胸口。
第 2 格：右手抬到肩膀。
第 3 格：抬至脸旁，向外摆。
第 4 格：向内摆。
第 5 格：再向外摆。
第 6 格：放回胸口附近，方便接回第 1 格。
所有格子保持同一个角色、同一服装和表情。
身体中心、脚底位置、镜头距离和角色大小固定。
左手自然垂下，不增加道具、文字、编号或边框。

请按 3 列 2 行切出这 6 帧，从左到右、从上到下播放。
每秒约 6 帧，合成为无限循环的 GIF。
保留纯白背景，画布大小一致。
如果角色位置有轻微偏移，先对齐身体中心和脚底，再合成。
给我可下载的 GIF 文件。
```

参考链接（2026-11-05）：https://x.com/i/article/2118269816821919744。


<a id="idea-28"></a>
### 28. 同一角色九宫格表情包 / Nine-Grid Chat Stickers

类型：表情梗图 ｜输出：静图 ｜证据：路飞 @0xluffy_eth · X Article ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `1:1` ｜编辑优先级：P1

![同一角色九宫格表情包 — 原创 SVG 概念示意](../docs/previews/luffy-nine-stickers.svg)

开脑洞点：先锁脸型/毛色/衣服，再换九种聊天情绪，中文短词固定在角色上方。比每次从零描述人物更不容易长歪。不转载原文九宫格成品。

```text
以上传图片为唯一角色参考，制作一张九宫格聊天表情包。
先提取角色最容易辨认的特征：脸型、发型或毛色、衣服、配饰、主要配色。
把这些特征保留在每一个表情中，不更换人物。
风格：软萌 3D 黏土玩具，大头小身体，轮廓清楚。
严格 3 列 3 行，每个格子等大，纯白背景，不画网格线。
从左到右、从上到下依次制作：
挥手，文字“早呀”。
双手合十，文字“谢谢”。
敬礼，文字“收到”。
委屈掉泪，文字“委屈”。
瘫坐，文字“累了”。
兴奋挥拳，文字“好耶”。
抱着爱心，文字“爱你”。
叉腰，文字“不干”。
盖着小毯子，文字“晚安”。
中文位于每个角色上方，清晰准确。
每个表情独立完整，四周留白，不重叠、不裁切。
不要水印、品牌标志、编号或多余角色。
```

参考链接（2026-11-05）：https://x.com/i/article/2118269816821919744。


<a id="idea-29"></a>
### 29. 只换背景保住商品 / Swap Backdrop, Keep the Product

类型：局部改图 ｜输出：编辑 ｜证据：路飞 @0xluffy_eth · X Article ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `3:2` ｜编辑优先级：P1

![只换背景保住商品 — 原创 SVG 概念示意](../docs/previews/luffy-product-bg-keep.svg)

开脑洞点：改图把「改什么」和「保留什么」拆开写。这段只换墙色，瓶子形状、水珠、豆粒数量和台面颜色都点名留下。

```text
只把背景墙从奶油米色改为低饱和的深墨绿色。
保留原图瓶子的形状、尺寸、位置、银色瓶盖、水珠、琥珀色液体、台面纹理、咖啡豆数量与位置。
镜头角度、光照方向和画面构图保持不变。
不要改变台面颜色，不要增加文字、Logo、花草、杯子或额外瓶子。
输出与原图相同比例的照片。
```

参考链接（2026-11-05）：https://x.com/i/article/2118269816821919744。


<a id="idea-30"></a>
### 30. 清晰化但不要编造细节 / Sharpen Without Inventing Detail

类型：局部改图 ｜输出：编辑 ｜证据：路飞 @0xluffy_eth · X Article ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `3:2` ｜编辑优先级：P1

![清晰化但不要编造细节 — 原创 SVG 概念示意](../docs/previews/luffy-deblur-keep.svg)

开脑洞点：低清修复要禁止「8K 堆砌」和编造看不清的标签/人脸。适合整理压缩图，不能把补出来的纹理当成原图信息。

```text
请对这张低清图片做自然的清晰化处理。
去除明显压缩块和模糊感，整理主体边缘、材质和色彩层次。
保留原图主体的形状、比例、位置、配色、背景、光线方向和画面裁切。
不要换一种画风，不要过度锐化，不要增加原图没有的文字、装饰或物品。
如果某处细节已经看不清，不要自行编造标签内容或人脸特征。
输出与原图相同比例的高清晰度图片。
```

参考链接（2026-11-05）：https://x.com/i/article/2118269816821919744。


<a id="idea-31"></a>
### 31. 软装预览不改户型 / Stage Soft Furnishings, Keep the Room

类型：局部改图 ｜输出：编辑 ｜证据：路飞 @0xluffy_eth · X Article ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `3:2` ｜编辑优先级：P2

![软装预览不改户型 — 原创 SVG 概念示意](../docs/previews/luffy-interior-staging.svg)

开脑洞点：室内改图先锁门窗、墙角、尺度和透视，只换地毯/靠垫/茶几。比一句「改成豪宅」更接近能下单的搭配预览。

```text
基于这张客厅照片做软装搭配预览，只更换软装和茶几，不改变空间结构。
保持原有门窗、墙角、天花板、房间尺度、地板和镜头透视位置。
保留同一张沙发的位置与外形。
把黑色长方茶几换成浅橡木椭圆茶几。
沙发前增加奶油白短绒地毯。
靠垫换成鼠尾草绿与米白色。
沙发后墙挂两幅小尺寸抽象植物装饰画。
窗边放一盆中等大小绿植，加轻薄白纱帘。
保留原有自然光方向，不移门窗，不增加壁炉、隔断或吊顶，不把房间扩大。
输出与原照片相同比例的真实室内效果图。
```

参考链接（2026-11-05）：https://x.com/i/article/2118269816821919744。


<a id="idea-32"></a>
### 32. 同一商品放进生活场景 / Same Product, Lifestyle Scene

类型：产品广告 ｜输出：静图 ｜证据：路飞 @0xluffy_eth · X Article ｜提示词：逐字公开提示词 ｜推荐：`Sunburst`, `3:2` ｜编辑优先级：P1

![同一商品放进生活场景 — 原创 SVG 概念示意](../docs/previews/luffy-product-lifestyle.svg)

开脑洞点：白底图负责认得出商品，场景图只搬家不重新设计。点名保留外形、盖子、标签和真实比例，手不能挡产品、不能把瓶子放大成道具。

```text
将参考照片中的同一件商品放进真实的生活场景，输出横向 3:2 照片。
保留商品的外形、材质、颜色、盖子、标签及真实比例，不重新设计商品。
场景：午后窗边的木桌。
一位成年人只有手和浅米色针织袖口进入画面，自然拿着商品展示。
背景有一本虚化的合上杂志和少量绿植，暖调自然光，像手机拍下的生活片段。
手的结构自然，不遮住整件商品，不把商品放大成巨型道具。
不出现人物面部，不添加额外商品、宣传文字或使用评价。
```

参考链接（2026-11-05）：https://x.com/i/article/2118269816821919744。


## 参考出处 / Sources

完整列表见 [sources.md](sources.md)。本页卡片若引用路飞 X Article，出处统一为：

- 路飞 [@0xluffy_eth](https://x.com/0xluffy_eth)，《榨干 Image 2.6 的 10 个神级玩法！【附完整提示词】》
- [X Article](https://x.com/i/article/2118269816821919744) · [介绍帖](https://x.com/0xluffy_eth/status/2118274913337552992) · 2026-11-05
- 中文提示词按原文逐字收录；封面为原创 SVG，不转载文中 GIF。
