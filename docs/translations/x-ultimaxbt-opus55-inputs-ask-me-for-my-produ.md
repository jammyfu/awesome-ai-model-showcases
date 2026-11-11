# x-ultimaxbt-opus55-inputs-ask-me-for-my-produ

Author / 作者 / 作者 / 作者: @ultimaxbt

[Original source / 原帖 / 原帖 / 原投稿](https://x.com/ultimaxbt/status/2108210884799549714)
[Archived case / 归档案例 / 歸檔案例 / 収録事例](../cases/x-ultimaxbt-opus55-inputs-ask-me-for-my-produ/README.md)


[English](#en) · [简体中文](#zh-cn) · [繁體中文](#zh-tw) · [日本語](#ja)

## Original / 原文

```text
<inputs> Ask me for: my product, the exact request a user types into it, 6 to 8 photos for
```

### Model evidence / 模型依据

```text
Citing repo lists this under Claude Opus 5.5 and links the original post. Previous mainstream generation. Not independently re-run.
```

### Original prompt / 原始提示词

```text
<inputs>
Ask me for: my product, the exact request a user types into it, 6 to 8 photos for the result cards, a royalty-free song around 130 BPM with a clear drop (Mixkit, free for commercial use), and my brand mark for the end card. If I skip anything, use the defaults: the food-ordering story below, food photos from Pexels (fire noodles, birria tacos, hot chicken, buffalo wings, smash burger, spicy ramen), and Mixkit "Cat Walk".
</inputs>

<direction>
A 15-second product launch film, 1920x1080 at 60fps. 2D only, one continuous take. No fades, blurs or cuts: each scene grows from the last. Text rises from a mask line, buttons expand into pages, and color floods from one object before shrinking into another. Give the camera one eased move per scene, and never zoom in and out consecutively.

Look: warm white canvas (#f5f5f2), black UI (#0e0e10), lime accent (#cdf24f), orange (#ff6a2a), and a blue send button (#2f6bff). Add an Apple Intelligence-style iridescent glow around the input: a blurred conic gradient rotating through pink, orange, lime, cyan and violet. Use real food photography on dark cards, Geist for UI and a serif for the product name on the end card.

Banned: crossfades, blur-ins, 3D, particles, camera moves that reverse direction, holds longer than 1s, anything that feels like a template.
</direction>

<structure>
130 BPM, 32 beats (14.8s). Start the song 12 beats before its drop.

Beats 0-6, ask: push slowly into the glowing composer, about 3x zoom. Type the request over three fixed lines with a natural keystroke rhythm:
"I'm really hungry, I don't know
what I want but something
spicy, crispy and filling"

Beat 6, send: press the send button. A lime ripple spreads from it and transforms the message into a chat bubble. Pull back once to reveal the phone around it (428x900 screen, 11px black bezel, 9:41 status bar).

Beats 6-12, think: the send button grows into an orange wok, a half-disc with a thin handle. It tosses 6 colorful ingredients on beats 8, 9, 10 and 11 beneath the shimmering text "Finding something for you…".

Beat 12, the drop: a lime circle expands from the wok to fill the frame in about 0.35s. Dark food cards (330x440, radius 28, photo on top, name, one-line description, price and rating) burst in from the center. Slide the strip across three cards and land on "Fire Noodles", which lifts with a "Best match" pill.

Beats 16-21, chat: the lime contracts back into the user's bubble, carrying its words as the chosen card flies into its slot. "Found it. Fire Noodles from Wok & Fire, smoky, spicy and seriously filling." rises in, followed by "Want me to order it for you?" Then show two pills: "Order now" in black and "More options" outlined. The cursor clicks Order now → spinner → "✓ Ordered".

Beats 21-32, outro: the black button expands into the page, staying pill-shaped as it reaches the edges while the camera pushes into it. Its label grows to headline size, then slides away. Bring in "You were craving noodles." and "Now it's on the way." word by word (92px, white on black). A courier dot follows a route to a pin. The pin becomes the brand mark, and the wordmark wipes out from behind it, with "made with" above and the product name below.
</structure>

<build>
1. One HTML file, 1920x1080. Compute every style from time inside seek(t): no CSS transitions, timers or state carried between frames.
2. Use one camera transform on a container, keyed by [time, zoom, x, y] with eased segments and zoom interpolated in log space.
3. Use closed-form step-response springs for every pop and settle.
4. Make every handoff a shared element: the lime flood carries a copy of the bubble's words, and the button carries its label into the page.
5. Sound: use a downloaded Mixkit SFX for each event - typing, send pop, each toss, drop impact, card swoosh, click, success tone, page-fill whoosh and mark sparkle. Place each by its measured peak and loudnorm to -14 LUFS.
6. Render with Playwright at 60fps using 8 subframes per frame, blended with ffmpeg tmix. Review every fast moment frame by frame and scan the full video frame by frame.
</build>
```

### Source rights / 来源许可

```text
许可未知 · 仅出处链接（不本地再托管）· MIT 只覆盖源码
```

<a id="en"></a>
## English

AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.

```text
<inputs> Ask me for: my product, the exact request a user types into it, 6 to 8 photos for
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
<inputs>
Ask me for: my product, the exact request a user types into it, 6 to 8 photos for the result cards, a royalty-free song around 130 BPM with a clear drop (Mixkit, free for commercial use), and my brand mark for the end card. If I skip anything, use the defaults: the food-ordering story below, food photos from Pexels (fire noodles, birria tacos, hot chicken, buffalo wings, smash burger, spicy ramen), and Mixkit "Cat Walk".
</inputs>

<direction>
A 15-second product launch film, 1920x1080 at 60fps. 2D only, one continuous take. No fades, blurs or cuts: each scene grows from the last. Text rises from a mask line, buttons expand into pages, and color floods from one object before shrinking into another. Give the camera one eased move per scene, and never zoom in and out consecutively.

Look: warm white canvas (#f5f5f2), black UI (#0e0e10), lime accent (#cdf24f), orange (#ff6a2a), and a blue send button (#2f6bff). Add an Apple Intelligence-style iridescent glow around the input: a blurred conic gradient rotating through pink, orange, lime, cyan and violet. Use real food photography on dark cards, Geist for UI and a serif for the product name on the end card.

Banned: crossfades, blur-ins, 3D, particles, camera moves that reverse direction, holds longer than 1s, anything that feels like a template.
</direction>

<structure>
130 BPM, 32 beats (14.8s). Start the song 12 beats before its drop.

Beats 0-6, ask: push slowly into the glowing composer, about 3x zoom. Type the request over three fixed lines with a natural keystroke rhythm:
"I'm really hungry, I don't know
what I want but something
spicy, crispy and filling"

Beat 6, send: press the send button. A lime ripple spreads from it and transforms the message into a chat bubble. Pull back once to reveal the phone around it (428x900 screen, 11px black bezel, 9:41 status bar).

Beats 6-12, think: the send button grows into an orange wok, a half-disc with a thin handle. It tosses 6 colorful ingredients on beats 8, 9, 10 and 11 beneath the shimmering text "Finding something for you…".

Beat 12, the drop: a lime circle expands from the wok to fill the frame in about 0.35s. Dark food cards (330x440, radius 28, photo on top, name, one-line description, price and rating) burst in from the center. Slide the strip across three cards and land on "Fire Noodles", which lifts with a "Best match" pill.

Beats 16-21, chat: the lime contracts back into the user's bubble, carrying its words as the chosen card flies into its slot. "Found it. Fire Noodles from Wok & Fire, smoky, spicy and seriously filling." rises in, followed by "Want me to order it for you?" Then show two pills: "Order now" in black and "More options" outlined. The cursor clicks Order now → spinner → "✓ Ordered".

Beats 21-32, outro: the black button expands into the page, staying pill-shaped as it reaches the edges while the camera pushes into it. Its label grows to headline size, then slides away. Bring in "You were craving noodles." and "Now it's on the way." word by word (92px, white on black). A courier dot follows a route to a pin. The pin becomes the brand mark, and the wordmark wipes out from behind it, with "made with" above and the product name below.
</structure>

<build>
1. One HTML file, 1920x1080. Compute every style from time inside seek(t): no CSS transitions, timers or state carried between frames.
2. Use one camera transform on a container, keyed by [time, zoom, x, y] with eased segments and zoom interpolated in log space.
3. Use closed-form step-response springs for every pop and settle.
4. Make every handoff a shared element: the lime flood carries a copy of the bubble's words, and the button carries its label into the page.
5. Sound: use a downloaded Mixkit SFX for each event - typing, send pop, each toss, drop impact, card swoosh, click, success tone, page-fill whoosh and mark sparkle. Place each by its measured peak and loudnorm to -14 LUFS.
6. Render with Playwright at 60fps using 8 subframes per frame, blended with ffmpeg tmix. Review every fast moment frame by frame and scan the full video frame by frame.
</build>
```

<a id="zh-cn"></a>
## 简体中文

AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。

```text
<inputs> 向我询问：我的产品、用户输入其中的确切请求、6 至 8 张照片，用于…
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
<inputs>
请向我询问：我的产品、用户在其中输入的确切请求、结果卡片所用的 6 到 8 张照片、一首约 130 BPM 且有清晰 drop 的免版税歌曲（Mixkit，可免费商用），以及结束卡片上的品牌标识。如果我跳过任何项目，使用默认值：下文的点餐故事、Pexels 美食照片（火辣面、birria tacos、辣鸡、布法罗鸡翅、压肉汉堡、辣拉面），以及 Mixkit 的 “Cat Walk”。
</inputs>

<direction>
一部 15 秒的产品发布短片，1920x1080，60fps。仅用 2D，一个连续长镜头。不要淡入淡出、模糊或切镜：每个场景都从上一个场景生长出来。文字从遮罩线升起，按钮扩展成页面，颜色从一个物体涌出，再收缩到另一个物体中。每个场景给镜头安排一次带缓动的移动，绝不要连续先推近再拉远或反之。

外观：暖白画布（#f5f5f2）、黑色 UI（#0e0e10）、青柠强调色（#cdf24f）、橙色（#ff6a2a），以及蓝色发送按钮（#2f6bff）。在输入框周围添加 Apple Intelligence 风格的虹彩辉光：一个经过模糊的锥形渐变，在粉色、橙色、青柠色、青色和紫色之间旋转。深色卡片上使用真实美食摄影，UI 使用 Geist，结束卡片上的产品名使用衬线字体。

禁止：交叉淡化、模糊入场、3D、粒子、反向折返的镜头运动、超过 1s 的停留，以及任何让人觉得像模板的东西。
</direction>

<structure>
130 BPM，32 拍（14.8s）。歌曲从 drop 前 12 拍开始。

第 0–6 拍，提问：缓慢推近发光的输入框，约 3x 缩放。以自然的敲键节奏在固定的三行中输入请求：
"I'm really hungry, I don't know
what I want but something
spicy, crispy and filling"

第 6 拍，发送：按下发送按钮。青柠色涟漪从按钮扩散，把消息变成聊天气泡。镜头只拉远一次，显露外围的手机（428x900 屏幕、11px 黑色边框、9:41 状态栏）。

第 6–12 拍，思考：发送按钮长成一口橙色炒锅，是带细把手的半圆盘。它在第 8、9、10 和 11 拍抛起 6 种彩色食材，上方是闪烁的文字 “Finding something for you…”。

第 12 拍，drop：一个青柠色圆从炒锅中扩张，约 0.35s 填满画面。深色美食卡片（330x440、圆角半径 28、顶部照片、名称、一行描述、价格与评分）从中央迸入。横向滑动卡片条，经过三张卡片后停在 “Fire Noodles”，它向上抬起并带有 “Best match” 胶囊标签。

第 16–21 拍，聊天：青柠色收缩回用户气泡中，并携带气泡里的文字，同时选中的卡片飞入自己的位置。“Found it. Fire Noodles from Wok & Fire, smoky, spicy and seriously filling.” 升起，随后是 “Want me to order it for you?”。然后显示两个胶囊按钮：黑色 “Order now” 和描边 “More options”。光标点击 Order now → 加载旋转图标 → “✓ Ordered”。

第 21–32 拍，收尾：黑色按钮扩展成整个页面，扩展到边缘时仍保持胶囊形，同时镜头推近。按钮标签长到标题大小，再滑走。逐词引入 “You were craving noodles.” 和 “Now it's on the way.”（92px，黑底白字）。一个配送员圆点沿路线走向定位图钉。图钉变成品牌标识，字标从它后面擦出，上方写 “made with”，下方写产品名。
</structure>

<build>
1. 一个 HTML 文件，1920x1080。在 seek(t) 内根据时间计算每项样式：不要 CSS transitions、计时器或跨帧传递的状态。
2. 对一个容器使用单一镜头变换，关键值为 [time, zoom, x, y]，各段带缓动，缩放在对数空间插值。
3. 每次弹出与稳定都使用闭式阶跃响应弹簧函数。
4. 每次交接都使用共享元素：青柠色铺屏区域携带气泡文字的副本，按钮将自己的标签带入页面。
5. 声音：每个事件使用下载的 Mixkit 音效，包括打字、发送弹出、每次颠锅、drop 冲击、卡片掠过、点击、成功提示、页面铺满呼啸声和标识闪亮声。按测得的峰值定位各音效，用 loudnorm 归一化至 -14 LUFS。
6. 使用 Playwright 以 60fps 渲染，每帧使用 8 个子帧，用 ffmpeg tmix 混合。逐帧检查每个快速动作，并逐帧扫描整段视频。
</build>
```

<a id="zh-tw"></a>
## 繁體中文

AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。

```text
<inputs> 向我詢問：我的產品、用戶輸入其中的確切請求、6 至 8 張照片，用於…
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
<inputs>
請向我詢問：我的產品、用戶在其中輸入的確切請求、結果卡片所用的 6 到 8 張照片、一首約 130 BPM 且有清晰 drop 的免版稅歌曲（Mixkit，可免費商用），以及結束卡片上的品牌標識。如果我跳過任何項目，使用默認值：下文的點餐故事、Pexels 美食照片（火辣面、birria tacos、辣雞、布法羅雞翅、壓肉漢堡、辣拉麵），以及 Mixkit 的 “Cat Walk”。
</inputs>

<direction>
一部 15 秒的產品發佈短片，1920x1080，60fps。僅用 2D，一個連續長鏡頭。不要淡入淡出、模糊或切鏡：每個場景都從上一個場景生長出來。文字從遮罩線升起，按鈕擴展成頁面，顏色從一個物體湧出，再收縮到另一個物體中。每個場景給鏡頭安排一次帶緩動的移動，絕不要連續先推近再拉遠或反之。

外觀：暖白畫布（#f5f5f2）、黑色 UI（#0e0e10）、青檸強調色（#cdf24f）、橙色（#ff6a2a），以及藍色發送按鈕（#2f6bff）。在輸入框周圍添加 Apple Intelligence 風格的虹彩輝光：一個經過模糊的錐形漸變，在粉色、橙色、青檸色、青色和紫色之間旋轉。深色卡片上使用真實美食攝影，UI 使用 Geist，結束卡片上的產品名使用襯線字體。

禁止：交叉淡化、模糊入場、3D、粒子、反向折返的鏡頭運動、超過 1s 的停留，以及任何讓人覺得像模板的東西。
</direction>

<structure>
130 BPM，32 拍（14.8s）。歌曲從 drop 前 12 拍開始。

第 0–6 拍，提問：緩慢推近發光的輸入框，約 3x 縮放。以自然的敲鍵節奏在固定的三行中輸入請求：
"I'm really hungry, I don't know
what I want but something
spicy, crispy and filling"

第 6 拍，發送：按下發送按鈕。青檸色漣漪從按鈕擴散，把消息變成聊天氣泡。鏡頭只拉遠一次，顯露外圍的手機（428x900 屏幕、11px 黑色邊框、9:41 狀態欄）。

第 6–12 拍，思考：發送按鈕長成一口橙色炒鍋，是帶細把手的半圓盤。它在第 8、9、10 和 11 拍拋起 6 種彩色食材，上方是閃爍的文字 “Finding something for you…”。

第 12 拍，drop：一個青檸色圓從炒鍋中擴張，約 0.35s 填滿畫面。深色美食卡片（330x440、圓角半徑 28、頂部照片、名稱、一行描述、價格與評分）從中央迸入。橫向滑動卡片條，經過三張卡片後停在 “Fire Noodles”，它向上抬起並帶有 “Best match” 膠囊標籤。

第 16–21 拍，聊天：青檸色收縮回用戶氣泡中，並攜帶氣泡里的文字，同時選中的卡片飛入自己的位置。“Found it. Fire Noodles from Wok & Fire, smoky, spicy and seriously filling.” 升起，隨後是 “Want me to order it for you?”。然後顯示兩個膠囊按鈕：黑色 “Order now” 和描邊 “More options”。光標點擊 Order now → 加載旋轉圖標 → “✓ Ordered”。

第 21–32 拍，收尾：黑色按鈕擴展成整個頁面，擴展到邊緣時仍保持膠囊形，同時鏡頭推近。按鈕標籤長到標題大小，再滑走。逐詞引入 “You were craving noodles.” 和 “Now it's on the way.”（92px，黑底白字）。一個配送員圓點沿路線走向定位圖釘。圖釘變成品牌標識，字標從它後面擦出，上方寫 “made with”，下方寫產品名。
</structure>

<build>
1. 一個 HTML 文件，1920x1080。在 seek(t) 內根據時間計算每項樣式：不要 CSS transitions、計時器或跨幀傳遞的狀態。
2. 對一個容器使用單一鏡頭變換，關鍵值為 [time, zoom, x, y]，各段帶緩動，縮放在對數空間插值。
3. 每次彈出與穩定都使用閉式階躍響應彈簧函數。
4. 每次交接都使用共享元素：青檸色鋪屏區域攜帶氣泡文字的副本，按鈕將自己的標籤帶入頁面。
5. 聲音：每個事件使用下載的 Mixkit 音效，包括打字、發送彈出、每次顛鍋、drop 衝擊、卡片掠過、點擊、成功提示、頁面鋪滿呼嘯聲和標識閃亮聲。按測得的峰值定位各音效，用 loudnorm 歸一化至 -14 LUFS。
6. 使用 Playwright 以 60fps 渲染，每幀使用 8 個子幀，用 ffmpeg tmix 混合。逐幀檢查每個快速動作，並逐幀掃描整段視頻。
</build>
```

<a id="ja"></a>
## 日本語

AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。

```text
<inputs> 私に尋ねること：製品、ユーザーが入力する正確なリクエスト、…用の写真6〜8枚
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
<inputs>
次の項目を私に尋ねてください：私の製品、ユーザーがそこに入力する正確なリクエスト、結果カード用の写真 6～8 枚、明確なドロップがある約 130 BPM のロイヤリティフリー楽曲（Mixkit、商用利用無料）、エンドカード用のブランドマーク。省略した項目には、次のデフォルトを使ってください：下記の料理注文ストーリー、Pexels の料理写真（激辛麺、ビリアタコス、ホットチキン、バッファローウィング、スマッシュバーガー、辛いラーメン）、Mixkit の “Cat Walk”。
</inputs>

<direction>
15 秒の製品ローンチ映像、1920x1080、60fps。2D のみ、ひと続きのワンテイク。フェード、ぼかし、カットはなし。各シーンは直前のシーンから成長させます。文字がマスクの線からせり上がり、ボタンがページへ広がり、ある物体から色が画面を満たした後、別の物体へ縮みます。各シーンにイージング付きのカメラ移動を 1 回与え、ズームインとズームアウトを連続させないでください。

見た目：暖かい白のキャンバス（#f5f5f2）、黒い UI（#0e0e10）、ライムのアクセント（#cdf24f）、オレンジ（#ff6a2a）、青い送信ボタン（#2f6bff）。入力欄の周囲に Apple Intelligence 風の虹色のグローを加えます。ピンク、オレンジ、ライム、シアン、バイオレットを巡って回転する、ぼかした円錐グラデーションです。暗いカードには実際の料理写真を使い、UI は Geist、エンドカードの製品名はセリフ体にします。

禁止：クロスフェード、ぼかしながらの出現、3D、粒子、途中で逆方向に戻るカメラ移動、1s を超える静止、テンプレートのように感じるもの。
</direction>

<structure>
130 BPM、32 拍（14.8s）。曲はドロップの 12 拍前から始めます。

0～6 拍、質問：発光する入力欄へゆっくり寄り、約 3x にズームします。自然なキー入力のリズムで、固定した 3 行にリクエストを入力します：
"I'm really hungry, I don't know
what I want but something
spicy, crispy and filling"

6 拍、送信：送信ボタンを押します。そこからライム色の波紋が広がり、メッセージをチャットの吹き出しに変えます。1 回だけ引いて、周囲のスマートフォンを見せます（428x900 の画面、11px の黒いベゼル、9:41 のステータスバー）。

6～12 拍、思考：送信ボタンがオレンジの中華鍋に成長します。細い柄のある半円盤です。きらめく “Finding something for you…” の文字の下で、8、9、10、11 拍に 6 種のカラフルな食材をあおります。

12 拍、ドロップ：鍋からライム色の円が広がり、約 0.35s で画面を満たします。暗い料理カード（330x440、半径 28、上部に写真、名前、1 行の説明、価格、評価）が中央から勢いよく入ります。カード列を 3 枚分スライドさせ、“Fire Noodles” で止めます。そのカードは “Best match” のピル型ラベルとともに持ち上がります。

16～21 拍、チャット：選ばれたカードが所定の位置へ飛ぶ間に、ライム色が文字を運びながらユーザーの吹き出しへ戻るように縮みます。“Found it. Fire Noodles from Wok & Fire, smoky, spicy and seriously filling.” がせり上がり、続いて “Want me to order it for you?” が現れます。次に、黒い “Order now” と輪郭線の “More options” の 2 つのピル型ボタンを表示します。カーソルが Order now をクリック → スピナー → “✓ Ordered”。

21～32 拍、アウトロ：黒いボタンがページに広がります。縁に届くまでピル形を保ち、カメラはそこへ寄ります。ラベルが見出しの大きさになり、その後スライドして去ります。“You were craving noodles.” と “Now it's on the way.” を単語ごとに登場させます（92px、黒地に白）。配達員を示す点がルートに沿ってピンへ向かいます。ピンがブランドマークになり、その後ろからワードマークがワイプで現れ、上に “made with”、下に製品名が入ります。
</structure>

<build>
1. HTML ファイル 1 つ、1920x1080。seek(t) 内で時間からすべてのスタイルを計算します。CSS transitions、タイマー、フレーム間で引き継ぐ状態は使いません。
2. コンテナーに単一のカメラ変換を適用し、[time, zoom, x, y] をキーにして各区間をイージングさせます。ズームは対数空間で補間します。
3. すべての飛び出しと収束には、閉形式のステップ応答ばねを使います。
4. すべての受け渡しを共有要素で行います。画面を満たすライム色には吹き出しの文字のコピーを載せ、ボタンはラベルをページへ運びます。
5. 音：タイピング、送信のポップ音、各あおり、ドロップの衝撃、カードのスウッシュ、クリック、成功音、ページを満たす風切り音、マークのきらめきの各イベントに、ダウンロードした Mixkit SFX を使用します。測定したピークに合わせて配置し、loudnorm で -14 LUFS に正規化します。
6. Playwright で 60fps、1 フレームにつき 8 サブフレームでレンダリングし、ffmpeg tmix で合成します。速い瞬間をすべてコマ送りで確認し、動画全体も 1 フレームずつ走査します。
</build>
```
