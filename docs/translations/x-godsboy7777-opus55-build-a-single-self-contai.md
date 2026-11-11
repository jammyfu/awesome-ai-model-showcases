# x-godsboy7777-opus55-build-a-single-self-contai

Author / 作者 / 作者 / 作者: @GodsBoy7777

[Original source / 原帖 / 原帖 / 原投稿](https://x.com/GodsBoy7777/status/2103117450854150194)
[Archived case / 归档案例 / 歸檔案例 / 収録事例](../cases/x-godsboy7777-opus55-build-a-single-self-contai/README.md)


[English](#en) · [简体中文](#zh-cn) · [繁體中文](#zh-tw) · [日本語](#ja)

## Original / 原文

```text
Build a single self-contained HTML file: a 3D marble computer, in the spirit of Wintergata
```

### Model evidence / 模型依据

```text
Citing repo lists this under Claude Opus 5.5 and links the original post. Previous mainstream generation. Not independently re-run.
```

### Original prompt / 原始提示词

```text
Build a single self-contained HTML file: a 3D marble computer, in the spirit of Wintergatan's marble machine and the Digi-Comp II, that adds two 4-bit numbers using nothing but marbles falling through mechanical toggles.

Hard rules:

1. One HTML file. Three.js from https://t.co/KCQbEZLusb via an import map, plus its OrbitControls addon. No other libraries, no physics engine, no external assets.

2. The mechanism is the computer. Each bit of the result is stored in a two-state toggle (flip-flop) that a marble physically flips as it passes. Carries happen because a marble leaving one toggle rolls on to the next. Do not compute the answer in JavaScript arithmetic anywhere. The displayed result must be read from the toggle states after the last marble stops.

3. Marbles move along tracks with believable gravity and timing. Nothing teleports. You may script motion along paths, but every toggle flip must be caused by a marble arriving at it.

4. Input: two rows of four switches (A and B, 0 to 15), set by clicking. A lever labelled RUN releases the marbles. A counter shows how many marbles have fallen.

5. Output: a row of five result toggles, most significant bit on the left, and a readout that shows the binary and decimal value read from those toggles.

6. A DEMO button runs 5+6, then 9+7, then 15+15, resetting between runs, so it can be screen-recorded without touching anything.

7. Looks: a wooden board, brass toggles, glass marbles, warm studio lighting, soft shadows, a slow camera that follows the busiest part of the machine. It should look good in a square 1080x1080 recording.

8. Short click sounds via the Web Audio API when a toggle flips, started only after the first user click.

9. It must run at 60 fps on a normal laptop and have no console errors.

Output only the complete HTML file.
```

### Source rights / 来源许可

```text
许可未知 · 仅出处链接（不本地再托管）· MIT 只覆盖源码
```

<a id="en"></a>
## English

AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.

```text
Build a single self-contained HTML file: a 3D marble computer, in the spirit of Wintergata
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
Build a single self-contained HTML file: a 3D marble computer, in the spirit of Wintergatan's marble machine and the Digi-Comp II, that adds two 4-bit numbers using nothing but marbles falling through mechanical toggles.

Hard rules:

1. One HTML file. Three.js from https://t.co/KCQbEZLusb via an import map, plus its OrbitControls addon. No other libraries, no physics engine, no external assets.

2. The mechanism is the computer. Each bit of the result is stored in a two-state toggle (flip-flop) that a marble physically flips as it passes. Carries happen because a marble leaving one toggle rolls on to the next. Do not compute the answer in JavaScript arithmetic anywhere. The displayed result must be read from the toggle states after the last marble stops.

3. Marbles move along tracks with believable gravity and timing. Nothing teleports. You may script motion along paths, but every toggle flip must be caused by a marble arriving at it.

4. Input: two rows of four switches (A and B, 0 to 15), set by clicking. A lever labelled RUN releases the marbles. A counter shows how many marbles have fallen.

5. Output: a row of five result toggles, most significant bit on the left, and a readout that shows the binary and decimal value read from those toggles.

6. A DEMO button runs 5+6, then 9+7, then 15+15, resetting between runs, so it can be screen-recorded without touching anything.

7. Looks: a wooden board, brass toggles, glass marbles, warm studio lighting, soft shadows, a slow camera that follows the busiest part of the machine. It should look good in a square 1080x1080 recording.

8. Short click sounds via the Web Audio API when a toggle flips, started only after the first user click.

9. It must run at 60 fps on a normal laptop and have no console errors.

Output only the complete HTML file.
```

<a id="zh-cn"></a>
## 简体中文

AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。

```text
制作一个独立完整的 HTML 文件：一台三维弹珠计算机，风格参考 Wintergata…
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
构建一个独立、自包含的 HTML 文件：一台 3D 弹珠计算机，灵感来自 Wintergatan 的弹珠机器和 Digi-Comp II，只用穿过机械翻转开关的下落弹珠来相加两个 4 位数。

硬性规则：

1. 一个 HTML 文件。通过 import map 从 https://t.co/KCQbEZLusb 加载 Three.js，以及它的 OrbitControls 插件。不要其他库、物理引擎或外部素材。

2. 机械装置就是计算机。结果的每一位都存储在一个双状态翻转开关（触发器）中，弹珠经过时会实际将它翻转。进位由离开一个开关的弹珠滚到下一个开关来实现。任何地方都不得用 JavaScript 算术计算答案。显示的结果必须在最后一颗弹珠停下后，从开关状态中读取。

3. 弹珠沿轨道运动，重力与时序要可信。任何东西都不能瞬移。可以用脚本控制沿路径的运动，但每次开关翻转都必须由到达它的弹珠触发。

4. 输入：两排各四个开关（A 和 B，0 到 15），通过点击设置。标有 RUN 的拉杆释放弹珠。计数器显示已有多少颗弹珠落下。

5. 输出：一排五个结果开关，最高有效位在左侧，另有一个读数显示从这些开关读取的二进制值和十进制值。

6. DEMO 按钮依次运行 5+6、9+7、15+15，每次运行之间复位，便于不做任何操作就能录屏。

7. 外观：木板、黄铜开关、玻璃弹珠、温暖的摄影棚灯光、柔和阴影，以及缓慢跟随机器最忙碌部分的镜头。它在正方形 1080x1080 录屏中应当很好看。

8. 开关翻转时，通过 Web Audio API 发出短促的咔嗒声，仅在用户第一次点击后才启动声音。

9. 在普通笔记本电脑上必须以 60 fps 运行，且控制台没有错误。

只输出完整的 HTML 文件。
```

<a id="zh-tw"></a>
## 繁體中文

AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。

```text
製作一個獨立完整的 HTML 文件：一台三維彈珠計算機，風格參考 Wintergata…
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
構建一個獨立、自包含的 HTML 文件：一台 3D 彈珠計算機，靈感來自 Wintergatan 的彈珠機器和 Digi-Comp II，只用穿過機械翻轉開關的下落彈珠來相加兩個 4 位數。

硬性規則：

1. 一個 HTML 文件。通過 import map 從 https://t.co/KCQbEZLusb 加載 Three.js，以及它的 OrbitControls 插件。不要其他庫、物理引擎或外部素材。

2. 機械裝置就是計算機。結果的每一位都存儲在一個雙狀態翻轉開關（觸發器）中，彈珠經過時會實際將它翻轉。進位由離開一個開關的彈珠滾到下一個開關來實現。任何地方都不得用 JavaScript 算術計算答案。顯示的結果必須在最後一顆彈珠停下後，從開關狀態中讀取。

3. 彈珠沿軌道運動，重力與時序要可信。任何東西都不能瞬移。可以用腳本控制沿路徑的運動，但每次開關翻轉都必須由到達它的彈珠觸發。

4. 輸入：兩排各四個開關（A 和 B，0 到 15），通過點擊設置。標有 RUN 的拉桿釋放彈珠。計數器顯示已有多少顆彈珠落下。

5. 輸出：一排五個結果開關，最高有效位在左側，另有一個讀數顯示從這些開關讀取的二進制值和十進制值。

6. DEMO 按鈕依次運行 5+6、9+7、15+15，每次運行之間復位，便於不做任何操作就能錄屏。

7. 外觀：木板、黃銅開關、玻璃彈珠、溫暖的攝影棚燈光、柔和陰影，以及緩慢跟隨機器最忙碌部分的鏡頭。它在正方形 1080x1080 錄屏中應當很好看。

8. 開關翻轉時，通過 Web Audio API 發出短促的咔嗒聲，僅在用戶第一次點擊後才啓動聲音。

9. 在普通筆記本電腦上必須以 60 fps 運行，且控制台沒有錯誤。

只輸出完整的 HTML 文件。
```

<a id="ja"></a>
## 日本語

AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。

```text
単体で完結するHTMLファイルを制作：Wintergata…に着想を得た3Dビー玉コンピューター
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
Wintergatan のマーブルマシンと Digi-Comp II を思わせる 3D のビー玉コンピューターを、単一の自己完結型 HTML ファイルとして作成してください。機械式の切り替え器を通って落下するビー玉だけを使い、2 つの 4 ビット数を加算します。

厳守事項：

1. HTML ファイルは 1 つ。import map を使って https://t.co/KCQbEZLusb から Three.js とその OrbitControls アドオンを読み込むこと。他のライブラリ、物理エンジン、外部アセットは使用しない。

2. 機構そのものがコンピューターです。結果の各ビットは、ビー玉の通過によって物理的に反転する 2 状態の切り替え器（フリップフロップ）に保存されます。桁上がりは、ある切り替え器を出たビー玉が次の切り替え器へ転がることで起こります。JavaScript の算術演算で答えを計算することは、どこでも禁止です。最後のビー玉が停止してから切り替え器の状態を読み取り、その値を結果として表示してください。

3. ビー玉は、重力とタイミングが自然に感じられるように軌道上を動きます。瞬間移動は不可。経路に沿う動きをスクリプト化してもよいですが、切り替え器の反転は必ずビー玉が到達することで起こるようにしてください。

4. 入力：各 4 個のスイッチを 2 列（A と B、0～15）配置し、クリックして設定します。RUN と表示されたレバーでビー玉を放出します。落下したビー玉の個数をカウンターに表示します。

5. 出力：結果用の切り替え器を 5 個横一列に並べ、最上位ビットを左に置きます。それらから読み取った 2 進数と 10 進数の値を表示する読み取り欄も設けます。

6. DEMO ボタンで 5+6、9+7、15+15 を順に実行し、各実行の間でリセットします。何も操作せずに画面録画できるようにします。

7. 外観：木の板、真鍮の切り替え器、ガラスのビー玉、暖かなスタジオ照明、柔らかな影。カメラは機械の最も活発に動く部分をゆっくり追います。正方形の 1080x1080 録画で見栄えがよくなるようにしてください。

8. 切り替え器が反転したときに Web Audio API で短いクリック音を鳴らします。音声の開始はユーザーの最初のクリック後に限ります。

9. 一般的なノートパソコンで 60 fps で動作し、コンソールエラーが出ないこと。

完成した HTML ファイルだけを出力してください。
```
