# game-ssss-4x4-spec

Author / 作者 / 作者 / 作者: SSSS.CRYPTOMAN @SSSS_CRYPTOMAN · 原帖写明 GPT Image 2.5 · 不是 2.6 · 默认隐藏 · 未观看 MP4

[Original source / 原帖 / 原帖 / 原投稿](https://x.com/SSSS_CRYPTOMAN/status/2097797456117539136)

[English](#en) · [简体中文](#zh-cn) · [繁體中文](#zh-tw) · [日本語](#ja)

## Original / 原文

```text
【2.5 历史规格】游戏 4×4 分镜表
```

### Model evidence / 模型依据

```text
GPT Image 2.5（原帖写明；不是 Image 2.6）
```

### Original prompt / 原始提示词

```text
このキャラクターを参照して、ゲーム用の2Dアニメーションスプライトシートを作成して。
内容は「🔴アクションを記入」

1つの連続したアクションを、4列×4行の合計16フレームで表現する。

【スプライトシート仕様】
・正方形キャンバス
・4列×4行、合計16フレーム
・16個のセルは完全に同じ大きさ
・各セルの上下左右に最低10pxの余白を確保する
・枠線、グリッド線、数字、文字、記号、UIは一切不要
・背景は全フレームで統一された単色の白
・各フレームは左上から右へ、上段から下段へ、時間順に並べる

【最重要：サイズと位置の固定】
・16フレームすべてでキャラクターの表示倍率を統一する
・カメラのズームイン、ズームアウトは禁止
・足元の接地面の基準線を同じ高さに固定する
・キャラクターの中心位置がフレームの前後で大きく移動しない
・動きに必要な範囲だけポーズを変える

【最重要：セル内に完全に収める】
・髪、服、手足、武器、小物、エフェクト、残光、粒子を含むすべてを各セルの内部だけに収める
・隣のセルにはみ出さない
・余白10pxの安全領域を侵さない
・アクションが大きくなっても、キャラクターを縮小して調整しない
・必要ならエフェクトや腕の振り幅を控えめにして、セル内に収める

【描画方針】
・2Dゲーム用スプライトとして読みやすい、明快なシルエット
・フレーム間で自然につながる動き
・1枚絵ではなく、アニメーション素材として破綻のない連続性を重視
・各フレームの描き込み密度、線、塗り、陰影を統一する
```

### Source rights / 来源许可

```text
无明确再分发授权 · 仅外链
```

<a id="en"></a>
## English

AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.

```text
[Historical 2.5 specification] 4×4 game storyboard sheet
```

### Method

Sprite sheet, then slicing

### Verification

GPT Image 2.5 · not 2.6

### Model evidence (translation)

```text
GPT Image 2.5 (explicitly stated in the original post; not Image 2.6)
```

### Published prompt (translation)

```text
Using this character as reference, create a 2D animation sprite sheet for a game.
The content is “🔴Enter the action”.

Represent 1 continuous action in 4 columns × 4 rows, totaling 16 frames.

[Sprite-sheet specifications]
• Square canvas
• 4 columns × 4 rows, 16 frames total
• All 16 cells must be exactly the same size
• Ensure at least 10px of margin on all four sides of every cell
• No borders, grid lines, numbers, text, symbols, or UI whatsoever
• Uniform solid white background across all frames
• Arrange frames chronologically from the top left to the right, then from the top row downward

[Most important: fixed size and position]
• Keep the character’s display scale identical in all 16 frames
• Camera zooming in or out is prohibited
• Fix the baseline of the ground beneath the feet at the same height
• The character’s center must not move substantially between frames
• Change the pose only as much as the movement requires

[Most important: keep everything fully inside its cell]
• Keep everything, including hair, clothes, limbs, weapons, props, effects, afterglow, and particles, entirely inside each cell
• Do not extend into adjacent cells
• Do not intrude into the 10px safe margin
• Do not shrink the character to compensate for large actions
• If necessary, reduce effects or the arm swing range to keep everything inside the cell

[Drawing approach]
• Clear silhouettes that read well as 2D game sprites
• Movement that connects naturally between frames
• Prioritize coherent continuity as animation material, not 1 illustration
• Keep detail density, linework, coloring, and shading consistent in each frame
```

<a id="zh-cn"></a>
## 简体中文

AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。

```text
【2.5 历史规格】游戏 4×4 分镜表
```

### 做法

精灵图后切分

### 核验状态

GPT Image 2.5 · 不是 2.6

### 模型依据（译文）

```text
GPT Image 2.5（原帖写明；不是 Image 2.6）
```

### 公开提示词（译文）

```text
参考这个角色，制作游戏用的 2D 动画精灵图集。
内容为“🔴填写动作”。

用 4 列×4 行、共 16 帧表现 1 个连续动作。

【精灵图集规格】
・正方形画布
・4 列×4 行，共 16 帧
・16 个单元格尺寸完全相同
・每格上下左右至少留出 10px 边距
・完全不要边框、网格线、数字、文字、符号或 UI
・所有帧使用统一的纯白单色背景
・各帧按时间顺序从左上向右、从上排向下排列

【最重要：固定尺寸与位置】
・全部 16 帧统一角色显示比例
・禁止镜头推近或拉远
・将脚下接地面的基准线固定在同一高度
・角色中心位置在前后帧间不得大幅移动
・仅在动作必要范围内改变姿势

【最重要：完整容纳在单元格内】
・包括头发、衣服、四肢、武器、小物件、特效、余光、粒子在内的所有内容，都必须完全位于各自单元格内
・不得超出到相邻单元格
・不得侵入 10px 留白安全区
・即使动作幅度增大，也不得缩小角色来调整
・必要时收敛特效或手臂摆动幅度，以容纳在单元格内

【绘制方针】
・作为 2D 游戏精灵易于辨识、轮廓清晰
・帧与帧之间动作自然衔接
・重视作为动画素材的完整连续性，而非 1 张插画
・统一每帧的描绘密度、线条、上色与阴影
```

<a id="zh-tw"></a>
## 繁體中文

AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。

```text
【2.5 歷史規格】遊戲 4×4 分鏡表
```

### 做法

精靈圖後切分

### 核驗狀態

GPT Image 2.5 · 不是 2.6

### 模型依據（譯文）

```text
GPT Image 2.5（原帖寫明；不是 Image 2.6）
```

### 公開提示詞（譯文）

```text
參考這個角色，製作遊戲用的 2D 動畫精靈圖集。
內容為「🔴填寫動作」。

用 4 欄×4 列、共 16 影格表現 1 個連續動作。

【精靈圖集規格】
・正方形畫布
・4 欄×4 列，共 16 影格
・16 個儲存格尺寸完全相同
・每格上下左右至少留出 10px 邊距
・完全不要邊框、格線、數字、文字、符號或 UI
・所有影格使用統一的純白單色背景
・各影格按時間順序從左上向右、從上排向下排列

【最重要：固定尺寸與位置】
・全部 16 影格統一角色顯示比例
・禁止鏡頭推近或拉遠
・將腳下接地面的基準線固定在同一高度
・角色中心位置在前後影格間不得大幅移動
・僅在動作必要範圍內改變姿勢

【最重要：完整容納在儲存格內】
・包括頭髮、衣服、四肢、武器、小物件、特效、餘光、粒子在內的所有內容，都必須完全位於各自儲存格內
・不得超出到相鄰儲存格
・不得侵入 10px 留白安全區
・即使動作幅度增大，也不得縮小角色來調整
・必要時收斂特效或手臂擺動幅度，以容納在儲存格內

【繪製方針】
・作為 2D 遊戲精靈易於辨識、輪廓清晰
・影格與影格之間動作自然銜接
・重視作為動畫素材的完整連續性，而非 1 張插畫
・統一每影格的描繪密度、線條、上色與陰影
```

<a id="ja"></a>
## 日本語

AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。

```text
【2.5の過去仕様】ゲーム用4×4絵コンテシート
```

### 制作方法

スプライトシートを作成後に分割

### 検証状況

GPT Image 2.5 · 2.6 ではない

### モデルの根拠（翻訳）

```text
GPT Image 2.5（元投稿に明記。Image 2.6ではない）
```

### 公開プロンプト（翻訳）

```text
このキャラクターを参照して、ゲーム用の2Dアニメーションスプライトシートを作成して。
内容は「🔴アクションを記入」

1つの連続したアクションを、4列×4行の合計16フレームで表現する。

【スプライトシート仕様】
・正方形キャンバス
・4列×4行、合計16フレーム
・16個のセルは完全に同じ大きさ
・各セルの上下左右に最低10pxの余白を確保する
・枠線、グリッド線、数字、文字、記号、UIは一切不要
・背景は全フレームで統一された単色の白
・各フレームは左上から右へ、上段から下段へ、時間順に並べる

【最重要：サイズと位置の固定】
・16フレームすべてでキャラクターの表示倍率を統一する
・カメラのズームイン、ズームアウトは禁止
・足元の接地面の基準線を同じ高さに固定する
・キャラクターの中心位置がフレームの前後で大きく移動しない
・動きに必要な範囲だけポーズを変える

【最重要：セル内に完全に収める】
・髪、服、手足、武器、小物、エフェクト、残光、粒子を含むすべてを各セルの内部だけに収める
・隣のセルにはみ出さない
・余白10pxの安全領域を侵さない
・アクションが大きくなっても、キャラクターを縮小して調整しない
・必要ならエフェクトや腕の振り幅を控えめにして、セル内に収める

【描画方針】
・2Dゲーム用スプライトとして読みやすい、明快なシルエット
・フレーム間で自然につながる動き
・1枚絵ではなく、アニメーション素材として破綻のない連続性を重視
・各フレームの描き込み密度、線、塗り、陰影を統一する
```
