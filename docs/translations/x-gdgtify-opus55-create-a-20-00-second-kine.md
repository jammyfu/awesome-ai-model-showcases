# x-gdgtify-opus55-create-a-20-00-second-kine

Author / 作者 / 作者 / 作者: @Gdgtify

[Original source / 原帖 / 原帖 / 原投稿](https://x.com/Gdgtify/status/2105669567036989608)
[Archived case / 归档案例 / 歸檔案例 / 収録事例](../cases/x-gdgtify-opus55-create-a-20-00-second-kine/README.md)


[English](#en) · [简体中文](#zh-cn) · [繁體中文](#zh-tw) · [日本語](#ja)

## Original / 原文

```text
Create a 20.00-second kinetic typography film titled “ESCAPE THE ORBIT,” based on John F
```

### Model evidence / 模型依据

```text
Citing repo lists this under Claude Opus 5.5 and links the original post. Previous mainstream generation. Not independently re-run.
```

### Original prompt / 原始提示词

```text
Create a 20.00-second kinetic typography film titled “ESCAPE THE ORBIT,” based on John F. Kennedy’s Rice University address, September 12, 1962.

The central experience: a sentence discovers that it can change its own trajectory.

Deliver one complete, self-contained HTML file. Composition: 1080×1080. Target: 60fps. Use Canvas, SVG, or embedded WebGL. Embed required assets and libraries. The film must work without audio.

EXACT DISPLAY TEXT
“We choose to go to the moon”
“[…]”
“not because they are easy,”
“but because they are hard”
Preserve this order. The bracketed ellipsis explicitly indicates omitted speech. Attribution is separate from the excerpt. No additional slogans.
ART DIRECTION
Background: midnight # 080D23.
Primary type: warm white # FFF4DD.
Trajectory: electric coral # FF654F.
Secondary orbital geometry: blue # 6685FF.
Use a broad, confident grotesque for the speech and a sharply drawn italic for the final emphatic word. Avoid the appearance of a spacecraft dashboard. No rockets, astronaut illustrations, starfield wallpaper, lens flares, or decorative telemetry.
The frame should resemble an exceptionally refined astronomical instrument that has become expressive.

CENTRAL VISUAL RULE
The baseline of the sentence is a trajectory.

At first it is trapped in a closed orbit. A rhetorical decision changes that orbit into an open path. The letters remain the same travelers throughout.
Use an abstract orbital metaphor; do not present invented mission data or imply a physically accurate flight simulation.
STORYBOARD
0.00–3.50
The opening excerpt appears across the center, large and horizontal. Reveal it in three meaningful phrase groups.
A single hairline ellipse passes behind the baseline. A small circular lunar mark occupies its distant focus.
Hold the completed phrase motionless for 700ms.

3.50–6.00
The camera pulls back. The previously straight baseline reveals a shallow curvature.

The phrase travels along the ellipse as a coherent unit. Keep its glyphs upright during the initial movement. Only after the reading hold may they progressively adopt the tangent of the path.

The viewer realizes the sentence is circling rather than advancing.
6.00–7.00
Show the bracketed omission in an uncluttered central opening. The orbital movement decelerates.

7.00–10.50
Reveal the next clause on the near side of the orbit. Its final word travels through one smooth, effortless arc and returns toward where it started.

This ease should feel elegant but unproductive. Avoid comic bouncing.

10.50–14.50
Reveal the final clause horizontally before transforming it.
At its emphasis, the ellipse opens at one precise point. The same tracked letter group takes the new tangent and departs.
Perform one deliberate 70-degree camera roll. Counter-rotate the active phrase so it remains readable while the orbital field changes orientation around it.

The trajectory sweeps from lower left to upper right. Acceleration is conveyed by expanding spacing between its trailing marks, not by shaking the camera.

14.50–17.00
The camera matches the departing phrase’s velocity. The phrase becomes visually still while the old orbit recedes beneath it.

The lunar mark enlarges into a restrained crescent through geometric overlap. The crescent brackets the destination without becoming a cartoon illustration.
17.00–20.00
Resolve into a spacious editorial composition containing the selected excerpt in reading order, including its omission marker.

The open trajectory runs through the margins and exits the frame. Hold the entire image completely still for the final 1.2 seconds.

CHOREOGRAPHY
Use only three camera operations: pullback, roll, velocity match.
Give each operation a rhetorical purpose.
Keep the currently read phrase at least 64px high in the 1080px composition.
Motion blur may affect trailing geometry, never the active text.
No word may begin its ornamental travel before its reading hold finishes.

IMPLEMENTATION
Represent the ellipse and departure path analytically. Blend position and tangent continuously at the departure point; no teleportation.
Use arc-length sampling for consistent spacing along curves.
Separate camera transforms from glyph orientation.
Cache glyph rendering and static geometry.
Expose window.ready and window. seek(t). Seeking must pause playback and render any time from 0 through 20 deterministically, including out-of-order calls.
Provide window.frame(n) for n=0…1199 at t=n/60.
Render t=20 as the final held composition.
Use no accumulated physics or runtime randomness.

QUALITY GATE
Inspect frames at 0, 3, 5, 7.5, 10.5, 13, 16, and 19 seconds.
Verify that the same tracked phrase visibly follows its own trajectory.
```

### Source rights / 来源许可

```text
许可未知 · 仅出处链接（不本地再托管）· MIT 只覆盖源码
```

<a id="en"></a>
## English

AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.

```text
Create a 20.00-second kinetic typography film titled “ESCAPE THE ORBIT,” based on John F
```

### Method

Three.js / HTML scene captured as video on X

### Verification

Primary X URL listed by yihui-dev/awesome-opus5-5-videos · not independently re-run

### Model evidence (translation)

```text
Citing repo lists this under Claude Opus 5.5 and links the original post. Previous mainstream generation. Not independently re-run.
```

### Published prompt (translation)

```text
Create a 20.00-second kinetic typography film titled “ESCAPE THE ORBIT,” based on John F. Kennedy’s Rice University address, September 12, 1962.

The central experience: a sentence discovers that it can change its own trajectory.

Deliver one complete, self-contained HTML file. Composition: 1080×1080. Target: 60fps. Use Canvas, SVG, or embedded WebGL. Embed required assets and libraries. The film must work without audio.

EXACT DISPLAY TEXT
“We choose to go to the moon”
“[…]”
“not because they are easy,”
“but because they are hard”
Preserve this order. The bracketed ellipsis explicitly indicates omitted speech. Attribution is separate from the excerpt. No additional slogans.
ART DIRECTION
Background: midnight # 080D23.
Primary type: warm white # FFF4DD.
Trajectory: electric coral # FF654F.
Secondary orbital geometry: blue # 6685FF.
Use a broad, confident grotesque for the speech and a sharply drawn italic for the final emphatic word. Avoid the appearance of a spacecraft dashboard. No rockets, astronaut illustrations, starfield wallpaper, lens flares, or decorative telemetry.
The frame should resemble an exceptionally refined astronomical instrument that has become expressive.

CENTRAL VISUAL RULE
The baseline of the sentence is a trajectory.

At first it is trapped in a closed orbit. A rhetorical decision changes that orbit into an open path. The letters remain the same travelers throughout.
Use an abstract orbital metaphor; do not present invented mission data or imply a physically accurate flight simulation.
STORYBOARD
0.00–3.50
The opening excerpt appears across the center, large and horizontal. Reveal it in three meaningful phrase groups.
A single hairline ellipse passes behind the baseline. A small circular lunar mark occupies its distant focus.
Hold the completed phrase motionless for 700ms.

3.50–6.00
The camera pulls back. The previously straight baseline reveals a shallow curvature.

The phrase travels along the ellipse as a coherent unit. Keep its glyphs upright during the initial movement. Only after the reading hold may they progressively adopt the tangent of the path.

The viewer realizes the sentence is circling rather than advancing.
6.00–7.00
Show the bracketed omission in an uncluttered central opening. The orbital movement decelerates.

7.00–10.50
Reveal the next clause on the near side of the orbit. Its final word travels through one smooth, effortless arc and returns toward where it started.

This ease should feel elegant but unproductive. Avoid comic bouncing.

10.50–14.50
Reveal the final clause horizontally before transforming it.
At its emphasis, the ellipse opens at one precise point. The same tracked letter group takes the new tangent and departs.
Perform one deliberate 70-degree camera roll. Counter-rotate the active phrase so it remains readable while the orbital field changes orientation around it.

The trajectory sweeps from lower left to upper right. Acceleration is conveyed by expanding spacing between its trailing marks, not by shaking the camera.

14.50–17.00
The camera matches the departing phrase’s velocity. The phrase becomes visually still while the old orbit recedes beneath it.

The lunar mark enlarges into a restrained crescent through geometric overlap. The crescent brackets the destination without becoming a cartoon illustration.
17.00–20.00
Resolve into a spacious editorial composition containing the selected excerpt in reading order, including its omission marker.

The open trajectory runs through the margins and exits the frame. Hold the entire image completely still for the final 1.2 seconds.

CHOREOGRAPHY
Use only three camera operations: pullback, roll, velocity match.
Give each operation a rhetorical purpose.
Keep the currently read phrase at least 64px high in the 1080px composition.
Motion blur may affect trailing geometry, never the active text.
No word may begin its ornamental travel before its reading hold finishes.

IMPLEMENTATION
Represent the ellipse and departure path analytically. Blend position and tangent continuously at the departure point; no teleportation.
Use arc-length sampling for consistent spacing along curves.
Separate camera transforms from glyph orientation.
Cache glyph rendering and static geometry.
Expose window.ready and window. seek(t). Seeking must pause playback and render any time from 0 through 20 deterministically, including out-of-order calls.
Provide window.frame(n) for n=0…1199 at t=n/60.
Render t=20 as the final held composition.
Use no accumulated physics or runtime randomness.

QUALITY GATE
Inspect frames at 0, 3, 5, 7.5, 10.5, 13, 16, and 19 seconds.
Verify that the same tracked phrase visibly follows its own trajectory.
```

<a id="zh-cn"></a>
## 简体中文

AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。

```text
制作一支 20.00 秒的动态字体影片，标题为“ESCAPE THE ORBIT”，基于 John F…
```

### 做法

Three.js／HTML 场景，录制为 X 视频

### 核验状态

由 yihui-dev/awesome-opus5-5-videos 收录的原始 X URL · 未独立复测

### 模型依据（译文）

```text
引用仓库将此列于 Claude Opus 5.5 下，并链接原帖。属于上一代主流模型。未独立复跑。
```

### 公开提示词（译文）

```text
创作一部 20.00 秒的动态文字短片，标题为 “ESCAPE THE ORBIT”，以 John F. Kennedy 于 1962 年 9 月 12 日在 Rice University 的演讲为基础。

核心体验：一个句子发现自己能够改变自身的轨迹。

交付一个完整、自包含的 HTML 文件。画面：1080×1080。目标：60fps。使用 Canvas、SVG 或嵌入式 WebGL。嵌入所需素材与库。短片必须在无音频情况下也能成立。

准确显示文字
“We choose to go to the moon”
“[…]”
“not because they are easy,”
“but because they are hard”
保持这一顺序。方括号中的省略号明确表示省略的演讲内容。出处署名与摘录分开。不要添加其他口号。
美术指导
背景：午夜蓝 # 080D23。
主要文字：暖白色 # FFF4DD。
轨迹：电光珊瑚色 # FF654F。
次要轨道几何图形：蓝色 # 6685FF。
演讲文字使用宽阔、自信的无衬线字体，最后一个强调词使用笔画利落的斜体。避免做成航天器仪表盘。不要火箭、宇航员插画、星空壁纸、镜头光斑或装饰性遥测数据。
画面应像一台极为精致、开始表达情感的天文仪器。

核心视觉规则
句子的基线就是一条轨迹。

起初它被困在封闭轨道中。一个修辞上的决断把这条轨道变成开放路径。字母始终是同一批旅行者。
使用抽象的轨道隐喻；不要展示虚构任务数据，也不要暗示这是物理准确的飞行模拟。
分镜
0.00–3.50
开场摘录以大号水平文字出现在中央。分成三个有意义的短语组逐组揭示。
一条发丝般细的椭圆线经过基线后方。一个小圆形月球标记位于远端焦点。
完整短语保持静止 700ms。

3.50–6.00
镜头拉远。此前笔直的基线显露出浅浅的曲率。

短语作为一个连贯整体沿椭圆运动。初始运动期间保持字形直立。只有在阅读停留结束后，字形才可以逐渐顺应路径的切线方向。

观众意识到句子在绕圈，而不是前进。
6.00–7.00
在简洁的中央空白区域显示带方括号的省略标记。轨道运动减速。

7.00–10.50
在轨道近侧揭示下一分句。最后一个词沿一条平滑、毫不费力的弧线运行，再返回起点附近。

这种轻松感应当优雅却无所进展。避免滑稽的弹跳。

10.50–14.50
先水平揭示最后一个分句，再对其进行变换。
在强调之处，椭圆在一个精确的位置打开。同一组被跟踪的字母沿新的切线离开。
进行一次有意设计的 70 度镜头滚转。将当前短语反向旋转，保证周围轨道场改变方向时，它仍然易于阅读。

轨迹从左下扫向右上。通过逐渐扩大尾随标记之间的间距表现加速，而不是摇晃镜头。

14.50–17.00
镜头匹配离去短语的速度。短语在视觉上变得静止，旧轨道则从它下方退远。

月球标记通过几何叠合扩大成克制的新月。新月框定目的地，但不要变成卡通插画。
17.00–20.00
最终形成留白充裕的编辑式构图，按阅读顺序包含所选摘录及其省略标记。

开放轨迹穿过页边并离开画面。最后 1.2 秒让整幅画面完全静止。

动作编排
只使用三种镜头操作：拉远、滚转、速度匹配。
每种操作都要有修辞目的。
在 1080px 的构图中，当前阅读短语的高度至少为 64px。
运动模糊可以作用于尾随几何图形，绝不能影响当前文字。
任何单词都不得在阅读停留结束前开始装饰性运动。

实现
以解析形式表示椭圆和离开路径。在离开点连续混合位置与切线；不得瞬移。
使用弧长采样来保持沿曲线的间距一致。
将镜头变换与字形方向分开处理。
缓存字形渲染和静态几何图形。
暴露 window.ready 和 window. seek(t)。定位时间时必须暂停播放，并能够确定性地渲染从 0 到 20 的任何时刻，包括乱序调用。
提供 window.frame(n)，其中 n=0…1199，对应 t=n/60。
将 t=20 渲染为最终静止构图。
不要使用累积式物理模拟或运行时随机性。

质量门槛
检查 0、3、5、7.5、10.5、13、16 和 19 秒的画面。
确认同一组被跟踪的短语在视觉上确实沿自己的轨迹移动。
```

<a id="zh-tw"></a>
## 繁體中文

AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。

```text
製作一支 20.00 秒的動態字體影片，標題為“ESCAPE THE ORBIT”，基於 John F…
```

### 做法

Three.js／HTML 場景，錄製為 X 影片

### 核驗狀態

由 yihui-dev/awesome-opus5-5-videos 收錄的原始 X URL · 未獨立重現

### 模型依據（譯文）

```text
引用倉庫將此列於 Claude Opus 5.5 下，並鏈接原帖。屬於上一代主流模型。未獨立復跑。
```

### 公開提示詞（譯文）

```text
創作一部 20.00 秒的動態文字短片，標題為 “ESCAPE THE ORBIT”，以 John F. Kennedy 於 1962 年 9 月 12 日在 Rice University 的演講為基礎。

核心體驗：一個句子發現自己能夠改變自身的軌跡。

交付一個完整、自包含的 HTML 文件。畫面：1080×1080。目標：60fps。使用 Canvas、SVG 或嵌入式 WebGL。嵌入所需素材與庫。短片必須在無音頻情況下也能成立。

準確顯示文字
“We choose to go to the moon”
“[…]”
“not because they are easy,”
“but because they are hard”
保持這一順序。方括號中的省略號明確表示省略的演講內容。出處署名與摘錄分開。不要添加其他口號。
美術指導
背景：午夜藍 # 080D23。
主要文字：暖白色 # FFF4DD。
軌跡：電光珊瑚色 # FF654F。
次要軌道幾何圖形：藍色 # 6685FF。
演講文字使用寬闊、自信的無襯線字體，最後一個強調詞使用筆畫利落的斜體。避免做成航天器儀錶盤。不要火箭、宇航員插畫、星空壁紙、鏡頭光斑或裝飾性遙測數據。
畫面應像一台極為精緻、開始表達情感的天文儀器。

核心視覺規則
句子的基線就是一條軌跡。

起初它被困在封閉軌道中。一個修辭上的決斷把這條軌道變成開放路徑。字母始終是同一批旅行者。
使用抽象的軌道隱喻；不要展示虛構任務數據，也不要暗示這是物理準確的飛行模擬。
分鏡
0.00–3.50
開場摘錄以大號水平文字出現在中央。分成三個有意義的短語組逐組揭示。
一條發絲般細的橢圓線經過基線後方。一個小圓形月球標記位於遠端焦點。
完整短語保持靜止 700ms。

3.50–6.00
鏡頭拉遠。此前筆直的基線顯露出淺淺的曲率。

短語作為一個連貫整體沿橢圓運動。初始運動期間保持字形直立。只有在閱讀停留結束後，字形才可以逐漸順應路徑的切線方向。

觀眾意識到句子在繞圈，而不是前進。
6.00–7.00
在簡潔的中央空白區域顯示帶方括號的省略標記。軌道運動減速。

7.00–10.50
在軌道近側揭示下一分句。最後一個詞沿一條平滑、毫不費力的弧線運行，再返回起點附近。

這種輕鬆感應當優雅卻無所進展。避免滑稽的彈跳。

10.50–14.50
先水平揭示最後一個分句，再對其進行變換。
在強調之處，橢圓在一個精確的位置打開。同一組被跟蹤的字母沿新的切線離開。
進行一次有意設計的 70 度鏡頭滾轉。將當前短語反向旋轉，保證周圍軌道場改變方向時，它仍然易於閱讀。

軌跡從左下掃向右上。通過逐漸擴大尾隨標記之間的間距表現加速，而不是搖晃鏡頭。

14.50–17.00
鏡頭匹配離去短語的速度。短語在視覺上變得靜止，舊軌道則從它下方退遠。

月球標記通過幾何疊合擴大成克制的新月。新月框定目的地，但不要變成卡通插畫。
17.00–20.00
最終形成留白充裕的編輯式構圖，按閱讀順序包含所選摘錄及其省略標記。

開放軌跡穿過頁邊並離開畫面。最後 1.2 秒讓整幅畫面完全靜止。

動作編排
只使用三種鏡頭操作：拉遠、滾轉、速度匹配。
每種操作都要有修辭目的。
在 1080px 的構圖中，當前閱讀短語的高度至少為 64px。
運動模糊可以作用於尾隨幾何圖形，絕不能影響當前文字。
任何單詞都不得在閱讀停留結束前開始裝飾性運動。

實現
以解析形式表示橢圓和離開路徑。在離開點連續混合位置與切線；不得瞬移。
使用弧長採樣來保持沿曲線的間距一致。
將鏡頭變換與字形方向分開處理。
緩存字形渲染和靜態幾何圖形。
暴露 window.ready 和 window. seek(t)。定位時間時必須暫停播放，並能夠確定性地渲染從 0 到 20 的任何時刻，包括亂序調用。
提供 window.frame(n)，其中 n=0…1199，對應 t=n/60。
將 t=20 渲染為最終靜止構圖。
不要使用累積式物理模擬或運行時隨機性。

質量門檻
檢查 0、3、5、7.5、10.5、13、16 和 19 秒的畫面。
確認同一組被跟蹤的短語在視覺上確實沿自己的軌跡移動。
```

<a id="ja"></a>
## 日本語

AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。

```text
「ESCAPE THE ORBIT」という題名の20.00秒のキネティックタイポグラフィ映像を、John F…をもとに制作
```

### 制作方法

Three.js／HTML のシーンを X の動画として収録

### 検証状況

yihui-dev/awesome-opus5-5-videos に掲載された原投稿の X URL · 独立した再実行なし

### モデルの根拠（翻訳）

```text
引用元リポジトリではClaude Opus 5.5に分類し、元投稿へリンク。前世代の主流モデル。独立した再実行は未実施。
```

### 公開プロンプト（翻訳）

```text
John F. Kennedy が 1962 年 9 月 12 日に Rice University で行った演説をもとに、“ESCAPE THE ORBIT” と題する 20.00 秒のキネティックタイポグラフィ映像を制作してください。

中心となる体験：ひとつの文が、自分自身の軌道を変えられることに気づきます。

完成した自己完結型 HTML ファイルを 1 つ納品してください。構図：1080×1080。目標：60fps。Canvas、SVG、または埋め込み WebGL を使ってください。必要なアセットとライブラリは埋め込んでください。音声がなくても成立する映像にしてください。

正確な表示テキスト
“We choose to go to the moon”
“[…]”
“not because they are easy,”
“but because they are hard”
この順序を守ってください。角括弧付きの省略記号は、演説の一部を省略したことを明示します。出典表記は引用文と分離してください。スローガンは追加しないでください。
アートディレクション
背景：ミッドナイト # 080D23。
主要文字：暖かい白 # FFF4DD。
軌道：エレクトリックコーラル # FF654F。
補助的な軌道の幾何形状：青 # 6685FF。
演説には幅広く堂々としたグロテスク体を使い、最後の強調語には鋭く描かれたイタリック体を使ってください。宇宙船の計器盤のような見た目は避けてください。ロケット、宇宙飛行士のイラスト、星空の壁紙、レンズフレア、装飾的な遠隔測定表示は不要です。
非常に洗練された天文観測機器が表現力を持ったかのような画面にしてください。

中心的な視覚ルール
文のベースラインが軌道になります。

最初は閉じた軌道に閉じ込められています。修辞上の決断によって、その軌道が開いた経路に変わります。文字は終始、同じ旅人であり続けます。
抽象的な軌道の比喩を使ってください。架空のミッションデータを示したり、物理的に正確な飛行シミュレーションであるかのように見せたりしないでください。
ストーリーボード
0.00–3.50
冒頭の引用を中央に、大きく水平に表示します。意味のまとまりに沿って 3 つのフレーズ群に分けて出現させます。
細い 1 本の楕円線がベースラインの背後を通ります。遠方の焦点に小さな円形の月のマークを置きます。
完成したフレーズを 700ms 静止させます。

3.50–6.00
カメラが引きます。それまで直線だったベースラインに緩やかな曲率が見えてきます。

フレーズがひとまとまりになって楕円に沿って動きます。動き始めは文字を直立させておきます。読むための静止時間が終わってから、徐々に経路の接線方向に向けてかまいません。

観客は、この文が前進せず周回していると気づきます。
6.00–7.00
整理された中央の空間に、角括弧付きの省略記号を表示します。軌道上の動きは減速します。

7.00–10.50
軌道の手前側に次の節を表示します。その最後の語は滑らかで無理のない弧を描き、出発点付近に戻ります。

この容易さは優雅でありながら、成果のないものに感じられるようにします。コミカルな跳ね返りは避けてください。

10.50–14.50
最後の節を水平に表示してから変形します。
その強調の瞬間、楕円が正確な 1 点で開きます。同じ追跡対象の文字群が新しい接線に乗って離脱します。
意図の明確な 70 度のカメラロールを 1 回行います。読んでいるフレーズを逆方向に回転させ、周囲の軌道場の向きが変わっても読みやすさを保ちます。

軌道は左下から右上に弧を描きます。カメラを揺らすのではなく、後に続くマークの間隔を広げて加速を表現します。

14.50–17.00
カメラが離脱するフレーズの速度に合わせます。フレーズは視覚的に静止し、古い軌道がその下で遠ざかります。

月のマークは幾何形状の重なりによって、控えめな三日月へと拡大します。三日月は目的地を囲みますが、漫画的なイラストにはしません。
17.00–20.00
選んだ引用文を省略記号も含めて読む順序に配置し、余白の多いエディトリアルな構図に着地します。

開いた軌道は余白を通り、画面の外へ出ます。最後の 1.2 秒は画面全体を完全に静止させます。

振り付け
カメラ操作は、引き、ロール、速度合わせの 3 種類だけにします。
それぞれの操作に修辞上の意味を持たせます。
1080px の構図で、現在読むフレーズの高さを最低 64px に保ちます。
モーションブラーは後続する幾何形状には使えますが、現在読む文字には絶対にかけません。
どの語も、読ませるための静止時間が終わる前に装飾的な移動を始めてはいけません。

実装
楕円と離脱経路を解析的に表現します。離脱点で位置と接線を連続的にブレンドし、瞬間移動させません。
弧長サンプリングで曲線に沿った間隔を一定にします。
カメラ変換と文字の向きを分離します。
文字の描画と静的な幾何形状をキャッシュします。
window.ready と window. seek(t) を公開します。シーク時は再生を停止し、0～20 の任意の時刻を、順不同の呼び出しも含めて決定論的に描画できるようにします。
n=0…1199、t=n/60 に対応する window.frame(n) を提供します。
t=20 は最終的な静止構図として描画します。
蓄積型の物理演算や実行時の乱数を使わないでください。

品質確認
0、3、5、7.5、10.5、13、16、19 秒のフレームを確認します。
同じ追跡対象のフレーズが、自分自身の軌道に沿って進むことを視覚的に確認してください。
```
