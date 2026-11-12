# x-rossaxbt-opus55-inputs-ask-me-for-a-short

Author / 作者 / 作者 / 作者 / 제작자: @rossaxbt

[Original source / 原帖 / 原帖 / 原投稿 / 원문](https://x.com/rossaxbt/status/2107121188027707651)
[Archived case / 归档案例 / 歸檔案例 / 収録事例 / 보관 사례](../cases/x-rossaxbt-opus55-inputs-ask-me-for-a-short/README.md)


[English](#en) · [简体中文](#zh-cn) · [繁體中文](#zh-tw) · [日本語](#ja) · [한국어](#ko)

## Original / 原文

```text
<inputs> Ask me for: a short label for the opening toggle, one hero word, a percentage for
```

### Model evidence / 模型依据

```text
Citing repo lists this under Claude Opus 5.5 and links the original post. Previous mainstream generation. Not independently re-run.
```

### Original prompt / 原始提示词

```text
<inputs>
Ask me for: a short label for the opening toggle, one hero word, a percentage for the graph, the text for the final card, one accent color, and a track with a clear beat.
</inputs>

<direction>
A 2D motion design film in 16:9. Use a warm off-white canvas, near-black backgrounds, bold typography and one vivid orange accent. The orange dot connects every scene: it starts in the UI, becomes the dot over a letter, traces a spring graph, grows into a shape and returns on the end card. A cursor makes the opening click feel real. Keep the motion sharp and controlled, with small spring overshoots and no dead time.
Banned: stock footage, gradients, glows, particle bursts, random transitions and motion that isn't connected to an element already on screen.
</direction>

<structure>
Around 15 seconds, with a visual change on every major beat.
Open: a cursor clicks the orange toggle beside "Reduce Motion". The letters bend and move into place until only "Motion" remains, with the orange dot above the "i".
Spring: the dot jumps away from the word and lands on a graph. Its path draws a spring response, overshoots the target and settles beside a "+22%" callout.
Shape: the dot shoots across a line, grows into an orange circle and fills the frame. A black rounded square rotates inside it, then stretches into a pill. The scene contracts to a single orange dot on black.
Type: words like "SPRINGS", "EASING", "KINETIC TYPE", "3D" and "SOUND" orbit the dot. The circle of type opens out into a field of tiny dots.
Reveal: the halftone field expands and flips to black, revealing the final card: "Opus 5.5", "Motion designer." and "0 keyframes".
Return: the orange dot moves back through the halftone, graph and toggle. Match the final frame to the first so the video loops cleanly.
</structure>

<build>
1. One HTML file, 1920x1080 at 60fps. Compute every visual from time inside seek(t): no CSS transitions, timers or state carried between frames.
2. Use closed-form springs for the toggle, bouncing dot and graph. Draw the graph from the same spring function that moves the dot.
3. Animate letters individually for the "Reduce Motion" to "Motion" transformation. Keep the orange dot attached to the "i" until it begins its jump.
4. Make the orange circle, rotating square and pill different states of the same shape. Preserve its position and motion through each transformation.
5. Place the orbiting words along a circular path, then move their letters outward to hand the frame over to the halftone grid.
6. Draw the halftone as a grid of dots whose sizes respond to the orange dot. Let it grow past the frame edges before revealing the end card.
7. Sync the click, dot landing, graph peak, shape changes and final title to measured beats.
```

### Source rights / 来源许可

```text
许可未知 · 仅出处链接（不本地再托管）· MIT 只覆盖源码
```

<a id="en"></a>
## English

AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.

```text
<inputs> Ask me for: a short label for the opening toggle, one hero word, a percentage for
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
Ask me for: a short label for the opening toggle, one hero word, a percentage for the graph, the text for the final card, one accent color, and a track with a clear beat.
</inputs>

<direction>
A 2D motion design film in 16:9. Use a warm off-white canvas, near-black backgrounds, bold typography and one vivid orange accent. The orange dot connects every scene: it starts in the UI, becomes the dot over a letter, traces a spring graph, grows into a shape and returns on the end card. A cursor makes the opening click feel real. Keep the motion sharp and controlled, with small spring overshoots and no dead time.
Banned: stock footage, gradients, glows, particle bursts, random transitions and motion that isn't connected to an element already on screen.
</direction>

<structure>
Around 15 seconds, with a visual change on every major beat.
Open: a cursor clicks the orange toggle beside "Reduce Motion". The letters bend and move into place until only "Motion" remains, with the orange dot above the "i".
Spring: the dot jumps away from the word and lands on a graph. Its path draws a spring response, overshoots the target and settles beside a "+22%" callout.
Shape: the dot shoots across a line, grows into an orange circle and fills the frame. A black rounded square rotates inside it, then stretches into a pill. The scene contracts to a single orange dot on black.
Type: words like "SPRINGS", "EASING", "KINETIC TYPE", "3D" and "SOUND" orbit the dot. The circle of type opens out into a field of tiny dots.
Reveal: the halftone field expands and flips to black, revealing the final card: "Opus 5.5", "Motion designer." and "0 keyframes".
Return: the orange dot moves back through the halftone, graph and toggle. Match the final frame to the first so the video loops cleanly.
</structure>

<build>
1. One HTML file, 1920x1080 at 60fps. Compute every visual from time inside seek(t): no CSS transitions, timers or state carried between frames.
2. Use closed-form springs for the toggle, bouncing dot and graph. Draw the graph from the same spring function that moves the dot.
3. Animate letters individually for the "Reduce Motion" to "Motion" transformation. Keep the orange dot attached to the "i" until it begins its jump.
4. Make the orange circle, rotating square and pill different states of the same shape. Preserve its position and motion through each transformation.
5. Place the orbiting words along a circular path, then move their letters outward to hand the frame over to the halftone grid.
6. Draw the halftone as a grid of dots whose sizes respond to the orange dot. Let it grow past the frame edges before revealing the end card.
7. Sync the click, dot landing, graph peak, shape changes and final title to measured beats.
```

<a id="zh-cn"></a>
## 简体中文

AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。

```text
<inputs> 向我询问：开场切换开关的简短标签、一个主视觉词、一个百分比，用于…
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
请向我询问：开场切换开关的简短标签、一个主打词、图表中的百分比、结束卡片的文字、一种强调色，以及一首节拍清晰的音乐。
</inputs>

<direction>
一部 16:9 的 2D 动态设计短片。使用温暖的米白色画布、近黑色背景、醒目的字体，以及一种鲜艳的橙色强调色。橙色圆点串联每个场景：它从 UI 出发，变成字母上的点，描绘弹簧曲线，长成一个形状，然后回到结束卡片。用光标让开场的点击显得真实。动作要利落而受控，带有小幅弹簧过冲，没有空闲停顿。
禁止：素材库实拍片段、渐变、辉光、粒子爆发、随机转场，以及任何不与屏幕上已有元素相连的运动。
</direction>

<structure>
约 15 秒，每个主要节拍都有视觉变化。
开场：光标点击 “Reduce Motion” 旁边的橙色切换开关。字母弯曲并移入位置，直到只剩下 “Motion”，橙色圆点位于 “i” 上方。
弹簧：圆点从词语上跳开，落到图表上。它的路径画出弹簧响应曲线，越过目标后稳定在 “+22%” 标注旁边。
形状：圆点沿一条线飞过，长成橙色圆形并填满画面。一个黑色圆角正方形在其中旋转，然后拉伸成胶囊形。场景收缩为黑底上的一个橙色圆点。
文字：像 “SPRINGS”、“EASING”、“KINETIC TYPE”、“3D” 和 “SOUND” 这样的词围绕圆点运行。环状文字向外展开，变成一片微小圆点。
揭晓：半色调点阵扩张并翻转为黑色，揭示结束卡片：“Opus 5.5”、“Motion designer.” 和 “0 keyframes”。
返回：橙色圆点穿过半色调点阵、图表和切换开关原路返回。让最后一帧与第一帧匹配，使视频无缝循环。
</structure>

<build>
1. 一个 HTML 文件，1920x1080，60fps。在 seek(t) 内根据时间计算每个视觉元素：不要 CSS transitions、计时器或跨帧传递的状态。
2. 为切换开关、弹跳圆点和图表使用闭式弹簧函数。用驱动圆点的同一个弹簧函数绘制图表。
3. 为 “Reduce Motion” 到 “Motion” 的变换逐个制作字母动画。在圆点开始跳跃前，让橙色圆点始终附着在 “i” 上。
4. 将橙色圆形、旋转正方形和胶囊形作为同一个形状的不同状态。每次变换都保持其位置和运动连续。
5. 沿圆形路径摆放环绕的词语，然后让字母向外移动，将画面交接给半色调网格。
6. 用一张点阵网格绘制半色调效果，各圆点大小响应橙色圆点。让它扩张到画面边缘以外，再揭示结束卡片。
7. 将点击、圆点着陆、图表峰值、形状变化和最终标题同步到测得的节拍。
```

<a id="zh-tw"></a>
## 繁體中文

AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。

```text
<inputs> 向我詢問：開場切換開關的簡短標籤、一個主視覺詞、一個百分比，用於…
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
請向我詢問：開場切換開關的簡短標籤、一個主打詞、圖表中的百分比、結束卡片的文字、一種強調色，以及一首節拍清晰的音樂。
</inputs>

<direction>
一部 16:9 的 2D 動態設計短片。使用溫暖的米白色畫布、近黑色背景、醒目的字體，以及一種鮮艷的橙色強調色。橙色圓點串聯每個場景：它從 UI 出發，變成字母上的點，描繪彈簧曲線，長成一個形狀，然後回到結束卡片。用光標讓開場的點擊顯得真實。動作要利落而受控，帶有小幅彈簧過衝，沒有空閒停頓。
禁止：素材庫實拍片段、漸變、輝光、粒子爆發、隨機轉場，以及任何不與屏幕上已有元素相連的運動。
</direction>

<structure>
約 15 秒，每個主要節拍都有視覺變化。
開場：光標點擊 “Reduce Motion” 旁邊的橙色切換開關。字母彎曲並移入位置，直到只剩下 “Motion”，橙色圓點位於 “i” 上方。
彈簧：圓點從詞語上跳開，落到圖表上。它的路徑畫出彈簧響應曲線，越過目標後穩定在 “+22%” 標注旁邊。
形狀：圓點沿一條線飛過，長成橙色圓形並填滿畫面。一個黑色圓角正方形在其中旋轉，然後拉伸成膠囊形。場景收縮為黑底上的一個橙色圓點。
文字：像 “SPRINGS”、“EASING”、“KINETIC TYPE”、“3D” 和 “SOUND” 這樣的詞圍繞圓點運行。環狀文字向外展開，變成一片微小圓點。
揭曉：半色調點陣擴張並翻轉為黑色，揭示結束卡片：“Opus 5.5”、“Motion designer.” 和 “0 keyframes”。
返回：橙色圓點穿過半色調點陣、圖表和切換開關原路返回。讓最後一幀與第一幀匹配，使視頻無縫循環。
</structure>

<build>
1. 一個 HTML 文件，1920x1080，60fps。在 seek(t) 內根據時間計算每個視覺元素：不要 CSS transitions、計時器或跨幀傳遞的狀態。
2. 為切換開關、彈跳圓點和圖表使用閉式彈簧函數。用驅動圓點的同一個彈簧函數繪製圖表。
3. 為 “Reduce Motion” 到 “Motion” 的變換逐個製作字母動畫。在圓點開始跳躍前，讓橙色圓點始終附著在 “i” 上。
4. 將橙色圓形、旋轉正方形和膠囊形作為同一個形狀的不同狀態。每次變換都保持其位置和運動連續。
5. 沿圓形路徑擺放環繞的詞語，然後讓字母向外移動，將畫面交接給半色調網格。
6. 用一張點陣網格繪制半色調效果，各圓點大小響應橙色圓點。讓它擴張到畫面邊緣以外，再揭示結束卡片。
7. 將點擊、圓點著陸、圖表峰值、形狀變化和最終標題同步到測得的節拍。
```

<a id="ja"></a>
## 日本語

AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。

```text
<inputs> 私に尋ねること：冒頭の切り替えスイッチ用の短いラベル、メインとなる1語、…用のパーセンテージ
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
次の項目を私に尋ねてください：冒頭のトグル用の短いラベル、主役となる単語 1 つ、グラフのパーセンテージ、最終カードの文章、アクセントカラー 1 色、明確なビートのある楽曲。
</inputs>

<direction>
16:9 の 2D モーションデザイン映像。暖かなオフホワイトのキャンバス、ほぼ黒の背景、大胆なタイポグラフィ、鮮やかなオレンジ 1 色のアクセントを使います。オレンジの点が全シーンをつなぎます。UI から始まり、文字の上の点となり、ばねのグラフを描き、図形に成長し、エンドカードに戻ります。カーソルで冒頭のクリックに実感を与えてください。動きは切れ味よく制御し、小さなばねのオーバーシュートを使い、何も起こらない時間を作らないでください。
禁止：ストック映像、グラデーション、グロー、粒子の噴出、無作為なトランジション、画面にすでにある要素とつながらない動き。
</direction>

<structure>
約 15 秒。主要なビートごとに視覚的な変化を起こします。
冒頭：カーソルが “Reduce Motion” の横にあるオレンジのトグルをクリックします。文字が曲がりながら所定の位置に動き、“Motion” だけが残り、オレンジの点が “i” の上に来ます。
ばね：点が単語から飛び離れ、グラフに着地します。その軌跡がばね応答を描き、目標を行き過ぎてから “+22%” の注記の横に落ち着きます。
図形：点が線に沿って飛び、オレンジの円に成長して画面を満たします。その中で黒い角丸四角形が回転し、カプセル形へ伸びます。シーンは黒地のオレンジの点 1 つへと縮みます。
文字：“SPRINGS”、“EASING”、“KINETIC TYPE”、“3D”、“SOUND” といった単語が点を周回します。文字の輪が外へ開き、小さな点が広がる面になります。
リビール：ハーフトーンの面が広がって黒に反転し、最終カード “Opus 5.5”、“Motion designer.”、“0 keyframes” が現れます。
帰還：オレンジの点がハーフトーン、グラフ、トグルを逆にたどります。最後のフレームを最初と一致させ、映像がきれいにループするようにします。
</structure>

<build>
1. HTML ファイル 1 つ、1920x1080、60fps。seek(t) 内で時間からすべての表示を計算します。CSS transitions、タイマー、フレーム間で引き継ぐ状態は使いません。
2. トグル、跳ねる点、グラフには閉形式のばね関数を使います。点を動かすのと同じばね関数でグラフを描画します。
3. “Reduce Motion” から “Motion” への変形は文字ごとにアニメーション化します。オレンジの点は跳び始めるまで “i” に付けたままにします。
4. オレンジの円、回転する四角形、カプセルを、同じ図形の異なる状態にします。各変形の間も位置と動きの連続性を保ちます。
5. 周回する単語を円形の経路に沿って配置し、その後、文字を外へ動かしてハーフトーンのグリッドに画面を引き継ぎます。
6. オレンジの点に反応してサイズが変化する点のグリッドとしてハーフトーンを描画します。画面の縁を越えて広がってからエンドカードを見せます。
7. クリック、点の着地、グラフの頂点、図形の変化、最終タイトルを測定したビートに同期させます。
```

<a id="ko"></a>
## 한국어

사람의 검수를 거치지 않은 AI 번역입니다. 원문과 함께 읽어 주세요. 번역은 출처 검증이나 재사용 허가를 의미하지 않습니다.

```text
<inputs> 시작 토글의 짧은 문구, 대표 단어 하나, 퍼센트 수치를 물어봐…(원문 잘림)
```

### 제작 방법

Three.js / HTML 장면을 X 영상으로 캡처

### 검증 상태

yihui-dev/awesome-opus5-5-videos에 기재된 1차 X URL, 독립적으로 다시 실행하지 않음

### 모델 근거 (번역)

```text
인용 저장소는 Claude Opus 5.5 항목에 수록하고 원 게시물로 연결. 이전 주류 세대. 독립적으로 다시 실행하지 않음
```

### 공개 프롬프트 (번역)

```text
<inputs>
시작 토글의 짧은 라벨, 핵심 단어 하나, 그래프의 백분율, 마지막 카드의 문구, 강조색 하나, 박자가 뚜렷한 트랙을 요청하세요.
</inputs>

<direction>
16:9의 2D 모션 디자인 영상. 따뜻한 미색 캔버스, 검정에 가까운 배경, 굵은 타이포그래피, 선명한 주황색 강조 하나를 사용하세요. 주황색 점이 모든 장면을 연결합니다. UI에서 시작해 글자 위의 점이 되고, 스프링 그래프를 그리고, 도형으로 커졌다가 마지막 카드에 돌아옵니다. 커서로 시작 클릭에 현실감을 줍니다. 작은 스프링 오버슈트와 함께 날카롭고 절제된 움직임을 유지하고 죽은 시간을 두지 마세요.
금지: 스톡 영상, 그라데이션, 글로우, 입자 폭발, 무작위 전환, 이미 화면에 있는 요소와 연결되지 않는 동작.
</direction>

<structure>
약 15초이며 주요 박자마다 시각적 변화가 있습니다.
시작: 커서가 “Reduce Motion” 옆의 주황색 토글을 클릭합니다. 글자들이 휘고 제자리로 이동해 “Motion”만 남으며 “i” 위에는 주황색 점이 있습니다.
스프링: 점이 단어에서 뛰어올라 그래프에 내려앉습니다. 그 경로가 스프링 응답을 그리며 목표를 넘어갔다가 “+22%” 설명 옆에 안정됩니다.
도형: 점이 선을 가로질러 날아가 주황색 원으로 커지며 화면을 채웁니다. 안에서는 검은 둥근 사각형이 회전한 뒤 알약 모양으로 늘어납니다. 장면은 검은 바탕의 주황색 점 하나로 축소됩니다.
타이포: “SPRINGS”, “EASING”, “KINETIC TYPE”, “3D”, “SOUND” 같은 단어가 점 주위를 공전합니다. 원형 글자 배열이 펼쳐져 작은 점들의 장이 됩니다.
공개: 하프톤 영역이 확장되고 검정으로 뒤집히며 마지막 카드 “Opus 5.5”, “Motion designer.”, “0 keyframes”를 드러냅니다.
복귀: 주황색 점이 하프톤, 그래프, 토글을 거슬러 돌아갑니다. 마지막 프레임을 첫 프레임과 맞춰 깔끔하게 반복되게 하세요.
</structure>

<build>
1. HTML 파일 하나, 1920x1080, 60fps. seek(t) 안에서 시간으로 모든 시각 요소를 계산하세요. CSS transition, 타이머, 프레임 간에 이어받는 상태는 쓰지 마세요.
2. 토글, 튀는 점, 그래프에 닫힌 형태의 스프링 함수를 사용하세요. 점을 움직이는 것과 같은 스프링 함수로 그래프를 그리세요.
3. “Reduce Motion”→“Motion” 변환에서는 글자를 개별 애니메이션으로 움직이세요. 점이 점프하기 전까지는 “i”에 붙어 있어야 합니다.
4. 주황색 원, 회전하는 사각형, 알약 모양을 동일 도형의 서로 다른 상태로 만드세요. 변형마다 위치와 움직임을 유지하세요.
5. 공전하는 단어를 원형 경로에 배치한 뒤 글자들을 바깥으로 움직여 하프톤 격자에 화면을 넘기세요.
6. 하프톤은 주황색 점에 반응해 크기가 바뀌는 점 격자로 그리세요. 마지막 카드를 드러내기 전에 화면 경계 밖까지 커지게 하세요.
7. 클릭, 점 착지, 그래프 정점, 도형 변화, 마지막 제목을 측정한 박자에 맞추세요.
```
