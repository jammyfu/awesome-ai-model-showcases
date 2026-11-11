# x-heyiamnick-opus55-direction-build-a-30-secon

Author / 作者 / 作者 / 作者: @heyiamnick

[Original source / 原帖 / 原帖 / 原投稿](https://x.com/heyiamnick/status/2109174851412119558)
[Archived case / 归档案例 / 歸檔案例 / 収録事例](../cases/x-heyiamnick-opus55-direction-build-a-30-secon/README.md)


[English](#en) · [简体中文](#zh-cn) · [繁體中文](#zh-tw) · [日本語](#ja)

## Original / 原文

```text
<direction> Build a 30-second looping motion design showreel that introduces CLAUDE, a mot
```

### Model evidence / 模型依据

```text
Citing repo lists this under Claude Opus 5.5 and links the original post. Previous mainstream generation. Not independently re-run.
```

### Original prompt / 原始提示词

```text
<direction>
Build a 30-second looping motion design showreel that introduces CLAUDE, a motion designer.
Concept, in one line: one pencil line gets promoted three times (graphite on paper, wire on a blueprint, light on black) and never leaves the screen.

Every shot is made out of the previous one: shapes, type and colour transform into the next scene. No cuts, no fades.

Typeface: Geist only. Weight 900 for big words, 600 to 800 for small labels (24 to 28 px, tracked 0.14 to 0.3 em).
Palette: paper cream #EDE6D5, blueprint blue #1B3ED2, hologram cyan #45F0DD, plus black #07080A, graphite #16161A and white. Each stage's accent is the next stage's colour: blue pencil on paper, cyan on the blueprint, white on the hologram.
Camera: locked and front-on for the whole film, like a drafting table. Objects turn; the camera never moves.
Empty border: nothing at rest within 150 px of the sides or 90 px of the top and bottom. Things travelling through may cross it.

Three inks. The same geometry is drawn in whichever ink is on screen:
- PAPER: a cream paper background (use my paper image if I give one, otherwise flat cream with fine drawn grain) with a 60 px blue grid at about 13% and every fifth line at 26%. Lines are pencil: resampled and pushed off true by slow sine waves whose phase changes 8 times a second, stroked twice (full width at 90%, half width at 40% with more wobble), with paper tooth knocked out of the strokes, then multiplied onto the paper. Fills are diagonal hatching drawn on one line at a time. Big type is hatching cut to the letter shapes, with a doubled outline.
- BLUEPRINT: flat blue with the same grid in white. Clean white lines 3 to 4 px, hidden edges dashed and thinner, fills are fine clean hatching.
- HOLOGRAM: black with the same grid in cyan. Cyan lines with a white core 30% of the line width. Fills are horizontal scan lines on an 8 px pitch whose thickness follows how lit the surface is. No blur halo anywhere: it reads as light through line density only.

Banned: particle bursts, glows, lens flares, camera shake, RGB split, crossfades, generic gradients, bouncy easing, holds longer than half a second, anything that looks like a template.
</direction>

<structure>
120 BPM, 60 beats, 15 bars of 2 seconds. Something happens on every beat. Moves start 0.05 s before their beat so they land on it.
Easing: a critically damped spring, 1 - (1 + w t) e^(-w t) with w between 12 and 40, so nothing ever passes its target; exponential ease-in and ease-out for wipes, presses and exits.
Scene changes: paper to blueprint by a shape that floods the frame with a hard edge; blueprint to hologram and hologram to paper by one horizontal scan line.
The last frame is the first frame, so it loops.
Two corner labels stay on all film: top left "FIG. 07 — GEAR" (bar number and name), bottom right "BEAT 27 / 60". Bar names: DRAFT, TYPE, CURVE, MORPH, TILE, SOLID, GEAR, PANEL, DATA, LIGHT, WAVE, GLOBE, DRUM, FORM, END.
</structure>
<mascot>

The creative director: a small box character. Body 76 x 54 units with rounded corners, two short arm stubs (24 x 16) at mid height, four straight legs (11 x 33), two tall rounded-rectangle eyes (8 x 14). Draw it about 250 px wide. Its right arm is raised 58 degrees holding a pencil.
On paper: graphite outline with sparse blue hatching and graphite eyes. In the hologram: cyan outline with scan-line fill and white eyes. It is never a fourth colour.
It runs with alternate leg pairs lifting, six steps a second, leaning 7 degrees into the run.
</mascot>
<storyboard>

Bar 1, HOOK, 0-2 s, paper.
Frame 0: CLAUDE in Geist 900, fitted to 1500 px wide, centred, pencil-hatched. INTRODUCING small above it, A MOTION DESIGNER small below. A pencil rail 1620 px wide sits 96 px above the letters. The mascot stands on the rail at x = 1560 with CREATIVE DIRECTOR lettered to its left.

0.0: the small lines un-type; the mascot runs off the right edge, accelerating.

0.36 to 0.5: the rail drops, accelerating, to 26 px below the baseline and presses the letters flat into itself.

1.0: the line rises to the middle, shortens to 1320 px and splits into two rails 140 px apart; 41 blue ruler ticks sweep along the top rail.

1.5: the rails open to 300 px; a blue height dimension draws at the right with a live number.

Bar 2, KINETIC TYPE, 2-4 s, paper. Words sit between the rails and are clipped to that slot; the rails move to fit each word.

2.0: INTRODUCING rises through the baseline letter by letter, then lifts out through the top.

2.5: A MOTION whips in from the left (1400 px in 0.2 s).

3.0: the rails clap shut on it and reopen, stretching DESIGNER out of the line; its letters then fly out sideways.

3.5: CLAUDE in blue pencil, letters dropping from above one every 0.05 s. At 4.0 the rails close and crush it into one line 1476 px long.

Bar 3, CURVES, 4-6 s, paper.

4.1: the line gets pen-tool handles (430 px long at 58 degrees, small squares at the ends, circles on the handle tips, the label EASE) and bends into an S.

4.5: the handles swing to the mirror angle; eight blue copies fan out 34 px apart, joined at both ends like a leaf.

5.0: handles retract; the ribbon becomes travelling sine waves (amplitude 92 px, 2.75 cycles, each line a little out of phase).

5.5: it gathers back into one flat line.

Bar 4, SHAPE MORPH, 6-8 s, paper.

6.1: the line curls into a circle of radius 235 (curvature grows, length stays). 6.5: triangle, turning 120 degrees as it changes. 7.0: square. 7.5: hexagon, point up, radius 270. Blue hatching builds inside, then cross-hatching.

Bar 5, TILING, 8-10 s, paper.

8.0: the hexagon shrinks to radius 96 and six more slide out around it. 8.5: twelve more, a honeycomb of

19. 9.0: dense hatching sweeps across until every cell is solid blue. 9.6 to 10.0: the centre cell's shape grows past the frame with a hard edge; inside it is the blueprint, with the honeycomb in white line.

Bar 6, 2D TO 3D, 10-12 s, blueprint.

10.0: three lines draw inside every hexagon, plus three dashed hidden ones: each is a cube seen corner-on. 

10.5: the eighteen outer cubes slide into the centre one, which grows to radius 270. 11.0: it turns a quarter and perspective switches on. 11.5: it faces front.

Bar 7, MECHANISM, 12-14 s, blueprint.

12.0: the cube flattens and its front square grows teeth: a 16-tooth gear, pitch radius 208. From 12.25 the train steps 45 degrees on every eighth note. 12.5: a 10-tooth gear grows out to the upper right, meshing. 13.0: a 12-tooth gear to the upper left. Each has a dashed pitch circle, a hub and a label (16T, 10T, 12T). 13.5: the small gears retract; the gear becomes a square again and the cube gets its depth back.
Bar 8, UNFOLD, 14-16 s, blueprint.

14.0: the cube unfolds on its hinges into a cross of six squares. 14.5: the squares slide and stretch into six panels: a header strip, a tall sidebar, a wide chart, two tiles, a timeline strip.

15.0: they fill in. Header: "CLAUDE — MOTION REEL", a BARS / RING switch, a LIGHT toggle. Chart: 30 bars, one per second of this film, heights 42 30 36 44 50 46 52 62 50 56 62 72 60 66 58 76 56 62 68 74 70 78 86 94 100 93 97 90 80 50. Timeline: the 15 bar names, a keyframe diamond on each.
15.5: counters roll up: 120 BPM, 60 BEATS, 1800 FRAMES, 0 CUTS.
Bar 9, DATA, 16-18 s, blueprint.

16.0: a graph line draws across the bar tops; a cyan playhead lands on the timeline at the real time. The current second's bar is solid cyan, earlier ones hatched, later ones outlined. A cursor arrives.
16.5: it clicks RING: the chart's baseline bends round into a circle of radius 110 with the ba
```

### Source rights / 来源许可

```text
许可未知 · 仅出处链接（不本地再托管）· MIT 只覆盖源码
```

<a id="en"></a>
## English

AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.

```text
<direction> Build a 30-second looping motion design showreel that introduces CLAUDE, a mot
```

### Method

Code-made animation captured as video on X

### Verification

Primary X URL listed by yihui-dev/awesome-opus5-5-videos · not independently re-run

### Model evidence (translation)

```text
Citing repo lists this under Claude Opus 5.5 and links the original post. Previous mainstream generation. Not independently re-run.
```

### Published prompt (translation)

```text
<direction>
Build a 30-second looping motion design showreel that introduces CLAUDE, a motion designer.
Concept, in one line: one pencil line gets promoted three times (graphite on paper, wire on a blueprint, light on black) and never leaves the screen.

Every shot is made out of the previous one: shapes, type and colour transform into the next scene. No cuts, no fades.

Typeface: Geist only. Weight 900 for big words, 600 to 800 for small labels (24 to 28 px, tracked 0.14 to 0.3 em).
Palette: paper cream #EDE6D5, blueprint blue #1B3ED2, hologram cyan #45F0DD, plus black #07080A, graphite #16161A and white. Each stage's accent is the next stage's colour: blue pencil on paper, cyan on the blueprint, white on the hologram.
Camera: locked and front-on for the whole film, like a drafting table. Objects turn; the camera never moves.
Empty border: nothing at rest within 150 px of the sides or 90 px of the top and bottom. Things travelling through may cross it.

Three inks. The same geometry is drawn in whichever ink is on screen:
- PAPER: a cream paper background (use my paper image if I give one, otherwise flat cream with fine drawn grain) with a 60 px blue grid at about 13% and every fifth line at 26%. Lines are pencil: resampled and pushed off true by slow sine waves whose phase changes 8 times a second, stroked twice (full width at 90%, half width at 40% with more wobble), with paper tooth knocked out of the strokes, then multiplied onto the paper. Fills are diagonal hatching drawn on one line at a time. Big type is hatching cut to the letter shapes, with a doubled outline.
- BLUEPRINT: flat blue with the same grid in white. Clean white lines 3 to 4 px, hidden edges dashed and thinner, fills are fine clean hatching.
- HOLOGRAM: black with the same grid in cyan. Cyan lines with a white core 30% of the line width. Fills are horizontal scan lines on an 8 px pitch whose thickness follows how lit the surface is. No blur halo anywhere: it reads as light through line density only.

Banned: particle bursts, glows, lens flares, camera shake, RGB split, crossfades, generic gradients, bouncy easing, holds longer than half a second, anything that looks like a template.
</direction>

<structure>
120 BPM, 60 beats, 15 bars of 2 seconds. Something happens on every beat. Moves start 0.05 s before their beat so they land on it.
Easing: a critically damped spring, 1 - (1 + w t) e^(-w t) with w between 12 and 40, so nothing ever passes its target; exponential ease-in and ease-out for wipes, presses and exits.
Scene changes: paper to blueprint by a shape that floods the frame with a hard edge; blueprint to hologram and hologram to paper by one horizontal scan line.
The last frame is the first frame, so it loops.
Two corner labels stay on all film: top left "FIG. 07 — GEAR" (bar number and name), bottom right "BEAT 27 / 60". Bar names: DRAFT, TYPE, CURVE, MORPH, TILE, SOLID, GEAR, PANEL, DATA, LIGHT, WAVE, GLOBE, DRUM, FORM, END.
</structure>
<mascot>

The creative director: a small box character. Body 76 x 54 units with rounded corners, two short arm stubs (24 x 16) at mid height, four straight legs (11 x 33), two tall rounded-rectangle eyes (8 x 14). Draw it about 250 px wide. Its right arm is raised 58 degrees holding a pencil.
On paper: graphite outline with sparse blue hatching and graphite eyes. In the hologram: cyan outline with scan-line fill and white eyes. It is never a fourth colour.
It runs with alternate leg pairs lifting, six steps a second, leaning 7 degrees into the run.
</mascot>
<storyboard>

Bar 1, HOOK, 0-2 s, paper.
Frame 0: CLAUDE in Geist 900, fitted to 1500 px wide, centred, pencil-hatched. INTRODUCING small above it, A MOTION DESIGNER small below. A pencil rail 1620 px wide sits 96 px above the letters. The mascot stands on the rail at x = 1560 with CREATIVE DIRECTOR lettered to its left.

0.0: the small lines un-type; the mascot runs off the right edge, accelerating.

0.36 to 0.5: the rail drops, accelerating, to 26 px below the baseline and presses the letters flat into itself.

1.0: the line rises to the middle, shortens to 1320 px and splits into two rails 140 px apart; 41 blue ruler ticks sweep along the top rail.

1.5: the rails open to 300 px; a blue height dimension draws at the right with a live number.

Bar 2, KINETIC TYPE, 2-4 s, paper. Words sit between the rails and are clipped to that slot; the rails move to fit each word.

2.0: INTRODUCING rises through the baseline letter by letter, then lifts out through the top.

2.5: A MOTION whips in from the left (1400 px in 0.2 s).

3.0: the rails clap shut on it and reopen, stretching DESIGNER out of the line; its letters then fly out sideways.

3.5: CLAUDE in blue pencil, letters dropping from above one every 0.05 s. At 4.0 the rails close and crush it into one line 1476 px long.

Bar 3, CURVES, 4-6 s, paper.

4.1: the line gets pen-tool handles (430 px long at 58 degrees, small squares at the ends, circles on the handle tips, the label EASE) and bends into an S.

4.5: the handles swing to the mirror angle; eight blue copies fan out 34 px apart, joined at both ends like a leaf.

5.0: handles retract; the ribbon becomes travelling sine waves (amplitude 92 px, 2.75 cycles, each line a little out of phase).

5.5: it gathers back into one flat line.

Bar 4, SHAPE MORPH, 6-8 s, paper.

6.1: the line curls into a circle of radius 235 (curvature grows, length stays). 6.5: triangle, turning 120 degrees as it changes. 7.0: square. 7.5: hexagon, point up, radius 270. Blue hatching builds inside, then cross-hatching.

Bar 5, TILING, 8-10 s, paper.

8.0: the hexagon shrinks to radius 96 and six more slide out around it. 8.5: twelve more, a honeycomb of

19. 9.0: dense hatching sweeps across until every cell is solid blue. 9.6 to 10.0: the centre cell's shape grows past the frame with a hard edge; inside it is the blueprint, with the honeycomb in white line.

Bar 6, 2D TO 3D, 10-12 s, blueprint.

10.0: three lines draw inside every hexagon, plus three dashed hidden ones: each is a cube seen corner-on. 

10.5: the eighteen outer cubes slide into the centre one, which grows to radius 270. 11.0: it turns a quarter and perspective switches on. 11.5: it faces front.

Bar 7, MECHANISM, 12-14 s, blueprint.

12.0: the cube flattens and its front square grows teeth: a 16-tooth gear, pitch radius 208. From 12.25 the train steps 45 degrees on every eighth note. 12.5: a 10-tooth gear grows out to the upper right, meshing. 13.0: a 12-tooth gear to the upper left. Each has a dashed pitch circle, a hub and a label (16T, 10T, 12T). 13.5: the small gears retract; the gear becomes a square again and the cube gets its depth back.
Bar 8, UNFOLD, 14-16 s, blueprint.

14.0: the cube unfolds on its hinges into a cross of six squares. 14.5: the squares slide and stretch into six panels: a header strip, a tall sidebar, a wide chart, two tiles, a timeline strip.

15.0: they fill in. Header: "CLAUDE — MOTION REEL", a BARS / RING switch, a LIGHT toggle. Chart: 30 bars, one per second of this film, heights 42 30 36 44 50 46 52 62 50 56 62 72 60 66 58 76 56 62 68 74 70 78 86 94 100 93 97 90 80 50. Timeline: the 15 bar names, a keyframe diamond on each.
15.5: counters roll up: 120 BPM, 60 BEATS, 1800 FRAMES, 0 CUTS.
Bar 9, DATA, 16-18 s, blueprint.

16.0: a graph line draws across the bar tops; a cyan playhead lands on the timeline at the real time. The current second's bar is solid cyan, earlier ones hatched, later ones outlined. A cursor arrives.
16.5: it clicks RING: the chart's baseline bends round into a circle of radius 110 with the ba
```

<a id="zh-cn"></a>
## 简体中文

AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。

```text
<direction> 制作一支 30 秒循环动效作品集，介绍 CLAUDE，一位动…
```

### 做法

代码制作的动画，录制为 X 视频

### 核验状态

由 yihui-dev/awesome-opus5-5-videos 收录的原始 X URL · 未独立复测

### 模型依据（译文）

```text
引用仓库将此列于 Claude Opus 5.5 下，并链接原帖。属于上一代主流模型。未独立复跑。
```

### 公开提示词（译文）

```text
<direction>
制作一段 30 秒循环播放的动态设计作品集短片，介绍动态设计师 CLAUDE。
一句话概念：一条铅笔线经历三次升级（纸上的石墨线、蓝图上的线框、黑底上的光线），从未离开屏幕。

每个镜头都由前一个演化而来：形状、文字与颜色变换成下一个场景。不要切镜，不要淡入淡出。

字体：只用 Geist。大词用字重 900，小标签用 600 到 800（24 到 28 px，字距 0.14 到 0.3 em）。
配色：纸张奶油色 #EDE6D5、蓝图蓝 #1B3ED2、全息青 #45F0DD，加上黑色 #07080A、石墨色 #16161A 与白色。每个阶段的强调色都是下一阶段的颜色：纸上用蓝色铅笔，蓝图上用青色，全息中用白色。
镜头：全片锁定正面，如同制图桌。物体可以旋转；镜头绝不移动。
留白边界：静止物体不得进入左右各 150 px、上下各 90 px 的范围。经过的运动物体可以穿越。

三种墨色。同一套几何形状用当前画面中的墨色绘制：
- PAPER：奶油色纸张背景（如果我提供纸张图片就使用，否则用平涂奶油色加精细绘制的颗粒），搭配 60 px 的蓝色网格，约 13% 不透明度，每第五条线为 26%。线条为铅笔效果：重新采样，用缓慢的正弦波使其偏离准确路径，正弦相位每秒变化 8 次，描两遍（全线宽、90%，半线宽、40% 且抖动更多），在笔画中剔出纸张纹理，再以正片叠底方式合成到纸面。填充为逐条绘制的斜向排线。大字用裁剪到字形内的排线填充，并加双重轮廓。
- BLUEPRINT：纯蓝底，同样的网格改为白色。干净的白线 3 到 4 px，隐藏边用更细的虚线，填充为精细整齐的排线。
- HOLOGRAM：黑底，同样的网格改为青色。青色线条带白色线芯，线芯宽为线宽的 30%。填充为间距 8 px 的水平扫描线，粗细随表面受光程度变化。任何地方都不要模糊光晕：仅通过线条密度呈现发光感。

禁止：粒子爆发、辉光、镜头光斑、镜头抖动、RGB 分离、交叉淡化、泛用渐变、弹跳式缓动、超过半秒的停留，以及任何看起来像模板的东西。
</direction>

<structure>
120 BPM，60 拍，15 个各 2 秒的小节。每一拍都有事情发生。动作在所属节拍前 0.05 s 开始，以便正好落在拍点上。
缓动：临界阻尼弹簧，1 - (1 + w t) e^(-w t)，w 在 12 到 40 之间，因此没有任何元素会越过目标；擦拭、压下和退场使用指数式缓入和缓出。
场景切换：纸张到蓝图由一个硬边形状扩张铺满画面实现；蓝图到全息、全息到纸张都由一条水平扫描线实现。
最后一帧就是第一帧，使其循环。
两个角落标签全片常驻：左上 “FIG. 07 — GEAR”（小节编号与名称），右下 “BEAT 27 / 60”。小节名称：DRAFT、TYPE、CURVE、MORPH、TILE、SOLID、GEAR、PANEL、DATA、LIGHT、WAVE、GLOBE、DRUM、FORM、END。
</structure>
<mascot>

创意总监：一个小盒子角色。身体 76 x 54 单位，圆角，中部有两条短臂（24 x 16），四条直腿（11 x 33），两只竖向圆角矩形眼睛（8 x 14）。绘制宽度约 250 px。它的右臂抬起 58 度，握着铅笔。
在纸张阶段：石墨色轮廓、稀疏蓝色排线和石墨色眼睛。在全息阶段：青色轮廓、扫描线填充和白色眼睛。它绝不引入第四种颜色。
跑步时两组腿交替抬起，每秒六步，身体向跑动方向倾斜 7 度。
</mascot>
<storyboard>

第 1 小节，HOOK，0–2 s，纸张。
第 0 帧：CLAUDE 使用 Geist 900，宽度适配到 1500 px，居中，铅笔排线填充。上方小字 INTRODUCING，下方小字 A MOTION DESIGNER。一条宽 1620 px 的铅笔导轨位于字母上方 96 px。吉祥物站在导轨 x = 1560 处，左侧写着 CREATIVE DIRECTOR。

0.0：小字逐字撤回；吉祥物加速跑出右边缘。

0.36 到 0.5：导轨加速落下，降到基线下方 26 px，将字母压扁融入自身。

1.0：线升到中央，缩短为 1320 px，并分成相距 140 px 的两条导轨；41 个蓝色尺标刻度沿上方导轨扫过。

1.5：导轨张开到相距 300 px；右侧画出一个蓝色高度尺寸标注，带实时数字。

第 2 小节，KINETIC TYPE，2–4 s，纸张。词语位于导轨之间并裁剪在该槽内；导轨移动以适应每个词。

2.0：INTRODUCING 逐字母穿过基线升起，然后从顶部升出。

2.5：A MOTION 从左侧快速甩入（0.2 s 内移动 1400 px）。

3.0：导轨合拢夹住它，再重新张开，从线中拉伸出 DESIGNER；随后字母向两侧飞出。

3.5：蓝色铅笔绘制的 CLAUDE，字母每隔 0.05 s 从上方落下一个。4.0 时导轨闭合，将它压成一条长 1476 px 的线。

第 3 小节，CURVES，4–6 s，纸张。

4.1：线条出现钢笔工具控制柄（长 430 px、58 度，末端为小方块，控制柄尖端带圆点，标签 EASE），并弯成 S 形。

4.5：控制柄摆到镜像角度；八条蓝色副本以 34 px 间距扇形展开，两端连接，像一片叶子。

5.0：控制柄收回；带状图形变成行进的正弦波（振幅 92 px，2.75 个周期，各线之间略有相位差）。

5.5：它重新汇聚为一条平直线。

第 4 小节，SHAPE MORPH，6–8 s，纸张。

6.1：线卷成半径 235 的圆（曲率增加，长度不变）。6.5：变成三角形，变形时旋转 120 度。7.0：正方形。7.5：顶角朝上的六边形，半径 270。内部逐渐画出蓝色排线，然后交叉排线。

第 5 小节，TILING，8–10 s，纸张。

8.0：六边形缩到半径 96，周围滑出另外六个。8.5：再出现十二个，组成

19 个单元的蜂窝。9.0：密集排线扫过，直到每格都为实心蓝色。9.6 到 10.0：中心单元的形状以硬边扩张到画面外；内部是蓝图，蜂窝以白线呈现。

第 6 小节，2D TO 3D，10–12 s，蓝图。

10.0：每个六边形内部画出三条线，再加三条表示隐藏边的虚线：每个都是从角上观察的立方体。

10.5：外围十八个立方体滑入中心立方体，中心立方体扩大到半径 270。11.0：它转过四分之一圈并开启透视。11.5：它朝向正面。

第 7 小节，MECHANISM，12–14 s，蓝图。

12.0：立方体变扁，正面方形长出齿：一个 16 齿齿轮，分度圆半径 208。从 12.25 起，齿轮组在每个八分音符上步进 45 度。12.5：右上方长出一个 10 齿齿轮，与其啮合。13.0：左上方出现一个 12 齿齿轮。每个都带虚线分度圆、轮毂和标签（16T、10T、12T）。13.5：小齿轮收回；齿轮重新变成方形，立方体恢复深度。
第 8 小节，UNFOLD，14–16 s，蓝图。

14.0：立方体沿铰链展开，成为由六个方形组成的十字。14.5：方形滑动并拉伸成六个面板：一条页眉、一个高侧栏、一张宽图表、两个区块、一条时间线。

15.0：填入内容。页眉：“CLAUDE — MOTION REEL”、一个 BARS / RING 切换开关、一个 LIGHT 开关。图表：30 根柱，对应本片每一秒，高度为 42 30 36 44 50 46 52 62 50 56 62 72 60 66 58 76 56 62 68 74 70 78 86 94 100 93 97 90 80 50。时间线：15 个小节名称，每个上有一个关键帧菱形。
15.5：计数器向上滚动：120 BPM、60 BEATS、1800 FRAMES、0 CUTS。
第 9 小节，DATA，16–18 s，蓝图。

16.0：沿柱顶绘制一条图表折线；青色播放头落在时间线上对应真实时间的位置。当前秒的柱为实心青色，更早的柱为排线填充，后面的柱只有轮廓。一个光标到来。
16.5：它点击 RING：图表基线弯成半径 110 的圆，带着 ba
```

<a id="zh-tw"></a>
## 繁體中文

AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。

```text
<direction> 製作一支 30 秒循環動效作品集，介紹 CLAUDE，一位動…
```

### 做法

程式碼製作的動畫，錄製為 X 影片

### 核驗狀態

由 yihui-dev/awesome-opus5-5-videos 收錄的原始 X URL · 未獨立重現

### 模型依據（譯文）

```text
引用倉庫將此列於 Claude Opus 5.5 下，並鏈接原帖。屬於上一代主流模型。未獨立復跑。
```

### 公開提示詞（譯文）

```text
<direction>
製作一段 30 秒循環播放的動態設計作品集短片，介紹動態設計師 CLAUDE。
一句話概念：一條鉛筆線經歷三次升級（紙上的石墨線、藍圖上的線框、黑底上的光線），從未離開屏幕。

每個鏡頭都由前一個演化而來：形狀、文字與顏色變換成下一個場景。不要切鏡，不要淡入淡出。

字體：只用 Geist。大詞用字重 900，小標籤用 600 到 800（24 到 28 px，字距 0.14 到 0.3 em）。
配色：紙張奶油色 #EDE6D5、藍圖藍 #1B3ED2、全息青 #45F0DD，加上黑色 #07080A、石墨色 #16161A 與白色。每個階段的強調色都是下一階段的顏色：紙上用藍色鉛筆，藍圖上用青色，全息中用白色。
鏡頭：全片鎖定正面，如同製圖桌。物體可以旋轉；鏡頭絕不移動。
留白邊界：靜止物體不得進入左右各 150 px、上下各 90 px 的範圍。經過的運動物體可以穿越。

三種墨色。同一套幾何形狀用當前畫面中的墨色繪制：
- PAPER：奶油色紙張背景（如果我提供紙張圖片就使用，否則用平塗奶油色加精細繪制的顆粒），搭配 60 px 的藍色網格，約 13% 不透明度，每第五條線為 26%。線條為鉛筆效果：重新採樣，用緩慢的正弦波使其偏離準確路徑，正弦相位每秒變化 8 次，描兩遍（全線寬、90%，半線寬、40% 且抖動更多），在筆畫中剔出紙張紋理，再以正片疊底方式合成到紙面。填充為逐條繪制的斜向排線。大字用裁剪到字形內的排線填充，並加雙重輪廓。
- BLUEPRINT：純藍底，同樣的網格改為白色。乾淨的白線 3 到 4 px，隱藏邊用更細的虛線，填充為精細整齊的排線。
- HOLOGRAM：黑底，同樣的網格改為青色。青色線條帶白色線芯，線芯寬為線寬的 30%。填充為間距 8 px 的水平掃描線，粗細隨表面受光程度變化。任何地方都不要模糊光暈：僅通過線條密度呈現發光感。

禁止：粒子爆發、輝光、鏡頭光斑、鏡頭抖動、RGB 分離、交叉淡化、泛用漸變、彈跳式緩動、超過半秒的停留，以及任何看起來像模板的東西。
</direction>

<structure>
120 BPM，60 拍，15 個各 2 秒的小節。每一拍都有事情發生。動作在所屬節拍前 0.05 s 開始，以便正好落在拍點上。
緩動：臨界阻尼彈簧，1 - (1 + w t) e^(-w t)，w 在 12 到 40 之間，因此沒有任何元素會越過目標；擦拭、壓下和退場使用指數式緩入和緩出。
場景切換：紙張到藍圖由一個硬邊形狀擴張鋪滿畫面實現；藍圖到全息、全息到紙張都由一條水平掃描線實現。
最後一幀就是第一幀，使其循環。
兩個角落標籤全片常駐：左上 “FIG. 07 — GEAR”（小節編號與名稱），右下 “BEAT 27 / 60”。小節名稱：DRAFT、TYPE、CURVE、MORPH、TILE、SOLID、GEAR、PANEL、DATA、LIGHT、WAVE、GLOBE、DRUM、FORM、END。
</structure>
<mascot>

創意總監：一個小盒子角色。身體 76 x 54 單位，圓角，中部有兩條短臂（24 x 16），四條直腿（11 x 33），兩只竪向圓角矩形眼睛（8 x 14）。繪制寬度約 250 px。它的右臂抬起 58 度，握著鉛筆。
在紙張階段：石墨色輪廓、稀疏藍色排線和石墨色眼睛。在全息階段：青色輪廓、掃描線填充和白色眼睛。它絕不引入第四種顏色。
跑步時兩組腿交替抬起，每秒六步，身體向跑動方向傾斜 7 度。
</mascot>
<storyboard>

第 1 小節，HOOK，0–2 s，紙張。
第 0 幀：CLAUDE 使用 Geist 900，寬度適配到 1500 px，居中，鉛筆排線填充。上方小字 INTRODUCING，下方小字 A MOTION DESIGNER。一條寬 1620 px 的鉛筆導軌位於字母上方 96 px。吉祥物站在導軌 x = 1560 處，左側寫著 CREATIVE DIRECTOR。

0.0：小字逐字撤回；吉祥物加速跑出右邊緣。

0.36 到 0.5：導軌加速落下，降到基線下方 26 px，將字母壓扁融入自身。

1.0：線升到中央，縮短為 1320 px，並分成相距 140 px 的兩條導軌；41 個藍色尺標刻度沿上方導軌掃過。

1.5：導軌張開到相距 300 px；右側畫出一個藍色高度尺寸標注，帶實時數字。

第 2 小節，KINETIC TYPE，2–4 s，紙張。詞語位於導軌之間並裁剪在該槽內；導軌移動以適應每個詞。

2.0：INTRODUCING 逐字母穿過基線升起，然後從頂部升出。

2.5：A MOTION 從左側快速甩入（0.2 s 內移動 1400 px）。

3.0：導軌合攏夾住它，再重新張開，從線中拉伸出 DESIGNER；隨後字母向兩側飛出。

3.5：藍色鉛筆繪制的 CLAUDE，字母每隔 0.05 s 從上方落下一個。4.0 時導軌閉合，將它壓成一條長 1476 px 的線。

第 3 小節，CURVES，4–6 s，紙張。

4.1：線條出現鋼筆工具控制柄（長 430 px、58 度，末端為小方塊，控制柄尖端帶圓點，標籤 EASE），並彎成 S 形。

4.5：控制柄擺到鏡像角度；八條藍色副本以 34 px 間距扇形展開，兩端連接，像一片葉子。

5.0：控制柄收回；帶狀圖形變成行進的正弦波（振幅 92 px，2.75 個週期，各線之間略有相位差）。

5.5：它重新匯聚為一條平直線。

第 4 小節，SHAPE MORPH，6–8 s，紙張。

6.1：線捲成半徑 235 的圓（曲率增加，長度不變）。6.5：變成三角形，變形時旋轉 120 度。7.0：正方形。7.5：頂角朝上的六邊形，半徑 270。內部逐漸畫出藍色排線，然後交叉排線。

第 5 小節，TILING，8–10 s，紙張。

8.0：六邊形縮到半徑 96，周圍滑出另外六個。8.5：再出現十二個，組成

19 個單元的蜂窩。9.0：密集排線掃過，直到每格都為實心藍色。9.6 到 10.0：中心單元的形狀以硬邊擴張到畫面外；內部是藍圖，蜂窩以白線呈現。

第 6 小節，2D TO 3D，10–12 s，藍圖。

10.0：每個六邊形內部畫出三條線，再加三條表示隱藏邊的虛線：每個都是從角上觀察的立方體。

10.5：外圍十八個立方體滑入中心立方體，中心立方體擴大到半徑 270。11.0：它轉過四分之一圈並開啓透視。11.5：它朝向正面。

第 7 小節，MECHANISM，12–14 s，藍圖。

12.0：立方體變扁，正面方形長出齒：一個 16 齒齒輪，分度圓半徑 208。從 12.25 起，齒輪組在每個八分音符上步進 45 度。12.5：右上方長出一個 10 齒齒輪，與其嚙合。13.0：左上方出現一個 12 齒齒輪。每個都帶虛線分度圓、輪轂和標籤（16T、10T、12T）。13.5：小齒輪收回；齒輪重新變成方形，立方體恢復深度。
第 8 小節，UNFOLD，14–16 s，藍圖。

14.0：立方體沿鉸鏈展開，成為由六個方形組成的十字。14.5：方形滑動並拉伸成六個面板：一條頁眉、一個高側欄、一張寬圖表、兩個區塊、一條時間線。

15.0：填入內容。頁眉：“CLAUDE — MOTION REEL”、一個 BARS / RING 切換開關、一個 LIGHT 開關。圖表：30 根柱，對應本片每一秒，高度為 42 30 36 44 50 46 52 62 50 56 62 72 60 66 58 76 56 62 68 74 70 78 86 94 100 93 97 90 80 50。時間線：15 個小節名稱，每個上有一個關鍵幀菱形。
15.5：計數器向上滾動：120 BPM、60 BEATS、1800 FRAMES、0 CUTS。
第 9 小節，DATA，16–18 s，藍圖。

16.0：沿柱頂繪制一條圖表折線；青色播放頭落在時間線上對應真實時間的位置。當前秒的柱為實心青色，更早的柱為排線填充，後面的柱只有輪廓。一個光標到來。
16.5：它點擊 RING：圖表基線彎成半徑 110 的圓，帶著 ba
```

<a id="ja"></a>
## 日本語

AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。

```text
<direction> CLAUDEを紹介する30秒のループ・モーションデザイン作品集を制作。CLAUDEはモー…
```

### 制作方法

コードで制作したアニメーションを X の動画として収録

### 検証状況

yihui-dev/awesome-opus5-5-videos に掲載された原投稿の X URL · 独立した再実行なし

### モデルの根拠（翻訳）

```text
引用元リポジトリではClaude Opus 5.5に分類し、元投稿へリンク。前世代の主流モデル。独立した再実行は未実施。
```

### 公開プロンプト（翻訳）

```text
<direction>
モーションデザイナー CLAUDE を紹介する、30 秒でループするモーションデザインのショーリールを制作してください。
コンセプトを一言で：1 本の鉛筆線が 3 段階に昇格し（紙の上の黒鉛、青図の上のワイヤー、黒地の光）、一度も画面から消えません。

すべてのショットは前のショットから生まれます。形、文字、色が次のシーンへ変形します。カットもフェードも使いません。

書体：Geist のみ。大きな語はウェイト 900、小さなラベルは 600～800（24～28 px、字間 0.14～0.3 em）。
パレット：紙のクリーム #EDE6D5、青図の青 #1B3ED2、ホログラムのシアン #45F0DD に、黒 #07080A、黒鉛 #16161A、白を加えます。各段階のアクセントは次の段階の色です。紙上は青い鉛筆、青図上はシアン、ホログラム上は白。
カメラ：全編を通して、製図台のように正面で固定します。物体は回転しますが、カメラは動かしません。
余白：静止した要素は左右の端から 150 px、上下から 90 px 以内に置きません。通過するものは横切ってかまいません。

3 種類のインク。同じ幾何形状を、画面に出ているインクで描きます：
- PAPER：クリーム色の紙の背景（私が紙の画像を提供したらそれを使い、なければ均一なクリームに細かく描いた粒状感を加える）に、60 px の青いグリッドを約 13%、5 本ごとの線を 26% で重ねます。線は鉛筆です。再サンプリングして、位相が毎秒 8 回変わる緩やかな正弦波で正確な線からずらし、2 回描きます（全幅を 90%、半幅を 40% で、後者は揺らぎを増やす）。線から紙の凹凸を抜き、紙に乗算合成します。塗りは斜線ハッチングを 1 本ずつ描きます。大きな文字は字形で切り抜いたハッチングと、二重の輪郭線です。
- BLUEPRINT：均一な青に、同じグリッドを白で置きます。鮮明な白線は 3～4 px、隠れる辺は細い破線、塗りは細く整ったハッチングにします。
- HOLOGRAM：黒地に同じグリッドをシアンで描きます。シアンの線には、線幅の 30% の白い芯を入れます。塗りは 8 px ピッチの水平走査線で、面の明るさに応じて太さを変えます。ぼかした光の輪はどこにも置きません。線の密度だけで光に見せます。

禁止：粒子の噴出、グロー、レンズフレア、カメラシェイク、RGB 分離、クロスフェード、汎用的なグラデーション、弾むイージング、0.5 秒を超える静止、テンプレートに見えるもの。
</direction>

<structure>
120 BPM、60 拍、各 2 秒の 15 小節。毎拍何かが起こります。動きは拍の 0.05 s 前から始め、拍で着地させます。
イージング：臨界減衰のばね、1 - (1 + w t) e^(-w t)、w は 12～40。目標を行き過ぎるものは一切なし。ワイプ、押しつぶし、退場には指数的なイーズインとイーズアウトを使います。
シーンの変化：紙から青図へは、硬い輪郭の図形が画面を満たすことで切り替えます。青図からホログラム、ホログラムから紙へは、水平走査線 1 本で切り替えます。
最後のフレームを最初のフレームにしてループさせます。
全編を通して隅のラベル 2 つを表示します。左上に “FIG. 07 — GEAR”（小節番号と名前）、右下に “BEAT 27 / 60”。小節名：DRAFT、TYPE、CURVE、MORPH、TILE、SOLID、GEAR、PANEL、DATA、LIGHT、WAVE、GLOBE、DRUM、FORM、END。
</structure>
<mascot>

クリエイティブディレクター：小さな箱のキャラクター。体は角丸の 76 x 54 単位、中ほどに短い腕を 2 本（24 x 16）、まっすぐな脚を 4 本（11 x 33）、縦長の角丸長方形の目を 2 つ（8 x 14）。幅約 250 px で描きます。右腕は 58 度上げ、鉛筆を持っています。
紙では、黒鉛の輪郭とまばらな青いハッチング、黒鉛の目。ホログラムでは、シアンの輪郭と走査線の塗り、白い目。決して 4 色目にはしません。
脚を 2 本ずつ交互に上げ、毎秒 6 歩、進行方向へ 7 度傾いて走ります。
</mascot>
<storyboard>

第 1 小節、HOOK、0～2 s、紙。
フレーム 0：Geist 900 の CLAUDE を幅 1500 px に合わせ、中央に鉛筆のハッチングで置きます。その上に小さく INTRODUCING、下に小さく A MOTION DESIGNER。幅 1620 px の鉛筆のレールを文字の 96 px 上に置きます。マスコットはレール上の x = 1560 に立ち、左に CREATIVE DIRECTOR と記します。

0.0：小さな行が逆タイピングで消えます。マスコットは加速しながら右端へ走り去ります。

0.36～0.5：レールが加速しながらベースラインの 26 px 下まで落ち、文字を押しつぶして自身に取り込みます。

1.0：線が中央まで上がり、1320 px に縮み、140 px 離れた 2 本のレールに分裂します。上のレールに沿って青い定規の目盛り 41 本が走ります。

1.5：レールが 300 px まで開きます。右側に、数値が連動する青い高さ寸法線を描きます。

第 2 小節、KINETIC TYPE、2～4 s、紙。単語をレールの間に置き、その隙間でクリップします。レールは各単語に合わせて動きます。

2.0：INTRODUCING が 1 文字ずつベースラインを通ってせり上がり、そのまま上端から抜けます。

2.5：A MOTION が左から勢いよく入ります（0.2 s で 1400 px）。

3.0：レールがそれを挟むように閉じてから開き、線から DESIGNER を引き伸ばして出します。その文字は横方向に飛び去ります。

3.5：青い鉛筆の CLAUDE。0.05 s ごとに 1 文字ずつ上から落とします。4.0 にレールが閉じ、長さ 1476 px の 1 本の線に押しつぶします。

第 3 小節、CURVES、4～6 s、紙。

4.1：線にペンツールのハンドルを付けます（長さ 430 px、58 度、端に小さな四角、ハンドル先端に丸、EASE のラベル）。線は S 字に曲がります。

4.5：ハンドルが鏡像の角度まで振れます。青いコピー 8 本が 34 px 間隔で扇状に広がり、両端を結んで葉のようになります。

5.0：ハンドルが引っ込み、リボンが進行する正弦波になります（振幅 92 px、2.75 周期、各線の位相を少しずらす）。

5.5：再び 1 本の水平な線に集まります。

第 4 小節、SHAPE MORPH、6～8 s、紙。

6.1：線が丸まり、半径 235 の円になります（曲率を増やし、長さは維持）。6.5：変形しながら 120 度回転して三角形。7.0：正方形。7.5：頂点を上にした半径 270 の六角形。内部に青いハッチング、その後クロスハッチングを描き足します。

第 5 小節、TILING、8～10 s、紙。

8.0：六角形が半径 96 まで縮み、周りにさらに 6 個が滑り出ます。8.5：さらに 12 個、合計

19 個のハニカム。9.0：密なハッチングが走り、すべてのセルを青一色にします。9.6～10.0：中央のセルの形が硬い輪郭のまま画面を越えて大きくなります。その内部は青図で、ハニカムを白線で描きます。

第 6 小節、2D TO 3D、10～12 s、青図。

10.0：すべての六角形の中に 3 本の線と、隠れた辺の破線 3 本を描きます。それぞれが角から見た立方体になります。

10.5：外側の 18 個の立方体が中央の 1 個へ滑り込み、中央は半径 270 まで大きくなります。11.0：4 分の 1 回転し、透視投影を有効にします。11.5：正面を向きます。

第 7 小節、MECHANISM、12～14 s、青図。

12.0：立方体が平たくなり、前面の四角に歯が生えます。ピッチ半径 208 の 16 歯の歯車です。12.25 から歯車列が 8 分音符ごとに 45 度進みます。12.5：右上に 10 歯の歯車が伸びて出て、かみ合います。13.0：左上に 12 歯の歯車。それぞれに破線のピッチ円、ハブ、ラベル（16T、10T、12T）を付けます。13.5：小さい歯車が引っ込み、歯車が再び四角になって、立方体に奥行きが戻ります。
第 8 小節、UNFOLD、14～16 s、青図。

14.0：立方体がヒンジで開き、6 枚の正方形からなる十字になります。14.5：正方形が滑って伸び、6 つのパネルになります。ヘッダー帯、背の高いサイドバー、幅広のグラフ、タイル 2 枚、タイムライン帯。

15.0：内容を入れます。ヘッダー：“CLAUDE — MOTION REEL”、BARS / RING スイッチ、LIGHT トグル。グラフ：映像の各秒に 1 本ずつ、30 本の棒。高さは 42 30 36 44 50 46 52 62 50 56 62 72 60 66 58 76 56 62 68 74 70 78 86 94 100 93 97 90 80 50。タイムライン：15 の小節名と、それぞれにキーフレームの菱形。
15.5：カウンターが上へ回ります。120 BPM、60 BEATS、1800 FRAMES、0 CUTS。
第 9 小節、DATA、16～18 s、青図。

16.0：棒の上端をつなぐグラフ線を描きます。シアンの再生ヘッドが、タイムラインの実際の時刻に着地します。現在の秒の棒はシアンで塗りつぶし、それ以前はハッチング、それ以降は輪郭線にします。カーソルが到着します。
16.5：RING をクリックします。グラフのベースラインが半径 110 の円に曲がり、ba を伴って
```
