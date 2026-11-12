# game-varg-knight-run

Author / 作者 / 作者 / 作者 / 제작자: vargHQ gpt-image-sprite-sheet · 作者声明 gpt_image_2_6 · 非 OpenAI 官方验证 · 未复测

[Original source / 原帖 / 原帖 / 原投稿 / 원문](https://github.com/vargHQ/skills/blob/main/gpt-image-sprite-sheet/SKILL.md)
[Archived case / 归档案例 / 歸檔案例 / 収録事例 / 보관 사례](../cases/game-varg-knight-run/README.md)


[English](#en) · [简体中文](#zh-cn) · [繁體中文](#zh-tw) · [日本語](#ja) · [한국어](#ko)

## Original / 原文

```text
骑士跑循环：作者声明 2.6 出表再切帧
```

### Model evidence / 模型依据

```text
作者声明 gpt_image_2_6（非官方验证；本仓未复测）
```

### Original prompt / 原始提示词

```text
Using this character as the reference, create a 2D animation sprite sheet for a game.
Action: "[🔴 write the action here]"

Show one continuous action in 4 columns × 4 rows, 16 frames in total.

[Sprite sheet spec]
- Square canvas
- 4 columns × 4 rows, 16 frames in total
- All 16 cells exactly the same size
- At least 10 px of margin on every side of each cell
- No borders, grid lines, numbers, letters, symbols or UI at all
- One plain white background, the same in every frame
- Frames in time order: left to right, top row to bottom row

[Most important: fixed size and position]
- The same character scale in all 16 frames
- No camera zoom in or out
- The ground line under the feet fixed at the same height
- The character's centre does not move much from one frame to the next
- Change the pose only as much as the motion needs

[Most important: everything inside its cell]
- Hair, clothes, arms and legs, weapons, props, effects, afterimages and particles all stay inside their own cell
- Nothing spills into the next cell
- Nothing enters the 10 px safety margin
- Even when the action gets bigger, do not shrink the character to make it fit
- If needed, tone down effects and arm swings so they stay in the cell

[Drawing]
- A clear silhouette that reads well as a 2D game sprite
- Motion that flows naturally from frame to frame
- Not a single illustration: unbroken continuity as animation material comes first
- The same detail, line, colour and shading in every frame
```

### Source rights / 来源许可

```text
许可未知 · 本地归档（非作者授权、非 CC0）。MIT 只覆盖源码。
```

<a id="en"></a>
## English

AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.

```text
Knight running loop: author says 2.6 generated the sheet, then frames were extracted
```

### Method

Sprite sheet, then slicing

### Verification

Author claims 2.6 · not officially verified · not watched

### Model evidence (translation)

```text
Author claims gpt_image_2_6 (not officially verified; not retested by this repository)
```

### Published prompt (translation)

```text
Using this character as the reference, create a 2D animation sprite sheet for a game.
Action: "[🔴 write the action here]"

Show one continuous action in 4 columns × 4 rows, 16 frames in total.

[Sprite sheet spec]
- Square canvas
- 4 columns × 4 rows, 16 frames in total
- All 16 cells exactly the same size
- At least 10 px of margin on every side of each cell
- No borders, grid lines, numbers, letters, symbols or UI at all
- One plain white background, the same in every frame
- Frames in time order: left to right, top row to bottom row

[Most important: fixed size and position]
- The same character scale in all 16 frames
- No camera zoom in or out
- The ground line under the feet fixed at the same height
- The character's centre does not move much from one frame to the next
- Change the pose only as much as the motion needs

[Most important: everything inside its cell]
- Hair, clothes, arms and legs, weapons, props, effects, afterimages and particles all stay inside their own cell
- Nothing spills into the next cell
- Nothing enters the 10 px safety margin
- Even when the action gets bigger, do not shrink the character to make it fit
- If needed, tone down effects and arm swings so they stay in the cell

[Drawing]
- A clear silhouette that reads well as a 2D game sprite
- Motion that flows naturally from frame to frame
- Not a single illustration: unbroken continuity as animation material comes first
- The same detail, line, colour and shading in every frame
```

<a id="zh-cn"></a>
## 简体中文

AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。

```text
骑士跑循环：作者声明 2.6 出表再切帧
```

### 做法

精灵图后切分

### 核验状态

作者声明 2.6 · 非官方验证 · 未观看

### 模型依据（译文）

```text
作者声明 gpt_image_2_6（非官方验证；本仓未复测）
```

### 公开提示词（译文）

```text
以这个角色为参考，为游戏制作一张 2D 动画精灵图集。
动作：“[🔴 write the action here]”

以 4 列 × 4 行、共 16 帧展现一个连续动作。

[精灵图集规格]
- 正方形画布
- 4 列 × 4 行，共 16 帧
- 全部 16 个格子的尺寸完全一致
- 每个格子的四边至少留出 10 px 边距
- 完全不要边框、网格线、数字、字母、符号或 UI
- 统一的纯白背景，每一帧都相同
- 帧按时间顺序排列：从左到右、从最上行到最下行

[最重要：固定尺寸与位置]
- 全部 16 帧中的角色比例相同
- 镜头不得拉近或拉远
- 脚下的地面线固定在同一高度
- 相邻帧之间角色的中心位置不要有明显移动
- 仅根据动作需要改变姿势

[最重要：所有内容都留在自己的格子内]
- 头发、衣服、手臂与腿、武器、道具、特效、残影和粒子都必须留在各自的格子内
- 任何内容都不得溢出到下一个格子
- 任何内容都不得进入 10 px 安全边距
- 即使动作幅度变大，也不要缩小角色来适应格子
- 必要时减弱特效和手臂摆动，让它们留在格子内

[绘制]
- 轮廓清晰，作为 2D 游戏精灵时易于辨认
- 帧与帧之间的动作自然流畅
- 不是单张插画：作为动画素材，连续无间断的动作最重要
- 每一帧的细节、线条、颜色和明暗处理保持一致
```

<a id="zh-tw"></a>
## 繁體中文

AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。

```text
騎士跑循環：作者聲明 2.6 出表再切幀
```

### 做法

精靈圖後切分

### 核驗狀態

作者聲明 2.6 · 非官方驗證 · 未觀看

### 模型依據（譯文）

```text
作者聲明 gpt_image_2_6（非官方驗證；本倉未復測）
```

### 公開提示詞（譯文）

```text
以這個角色為參考，為遊戲製作一張 2D 動畫精靈圖集。
動作：“[🔴 write the action here]”

以 4 列 × 4 行、共 16 幀展現一個連續動作。

[精靈圖集規格]
- 正方形畫布
- 4 列 × 4 行，共 16 幀
- 全部 16 個格子的尺寸完全一致
- 每個格子的四邊至少留出 10 px 邊距
- 完全不要邊框、網格線、數字、字母、符號或 UI
- 統一的純白背景，每一幀都相同
- 幀按時間順序排列：從左到右、從最上行到最下行

[最重要：固定尺寸與位置]
- 全部 16 幀中的角色比例相同
- 鏡頭不得拉近或拉遠
- 腳下的地面線固定在同一高度
- 相鄰幀之間角色的中心位置不要有明顯移動
- 僅根據動作需要改變姿勢

[最重要：所有內容都留在自己的格子內]
- 頭髮、衣服、手臂與腿、武器、道具、特效、殘影和粒子都必須留在各自的格子內
- 任何內容都不得溢出到下一個格子
- 任何內容都不得進入 10 px 安全邊距
- 即使動作幅度變大，也不要縮小角色來適應格子
- 必要時減弱特效和手臂擺動，讓它們留在格子內

[繪制]
- 輪廓清晰，作為 2D 遊戲精靈時易於辨認
- 幀與幀之間的動作自然流暢
- 不是單張插畫：作為動畫素材，連續無間斷的動作最重要
- 每一幀的細節、線條、顏色和明暗處理保持一致
```

<a id="ja"></a>
## 日本語

AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。

```text
騎士の走行ループ：作者によると2.6でシートを生成後、フレームを切り出した
```

### 制作方法

スプライトシートを作成後に分割

### 検証状況

作者は 2.6 と主張 · 公式な検証ではない · 未視聴

### モデルの根拠（翻訳）

```text
作者はgpt_image_2_6と主張（公式検証なし。当リポジトリでは未再検証）
```

### 公開プロンプト（翻訳）

```text
このキャラクターを参考に、ゲーム用の 2D アニメーションスプライトシートを作成してください。
アクション：「[🔴 write the action here]」

4 列 × 4 行、合計 16 フレームで、ひと続きの動作を表現してください。

[スプライトシートの仕様]
- 正方形のキャンバス
- 4 列 × 4 行、合計 16 フレーム
- 16 個すべてのセルをまったく同じ大きさにする
- 各セルの四辺に少なくとも 10 px の余白を設ける
- 枠線、グリッド線、数字、文字、記号、UI は一切入れない
- 背景は一様な白一色で、すべてのフレームで同じにする
- フレームは時間順に、左から右、上の行から下の行へ並べる

[最重要：サイズと位置を固定する]
- 全 16 フレームでキャラクターの縮尺を統一する
- カメラのズームイン・ズームアウトはしない
- 足元の地面の線を同じ高さに固定する
- 前後のフレームでキャラクターの中心が大きく移動しないようにする
- ポーズは動作に必要な範囲だけ変える

[最重要：すべてをセル内に収める]
- 髪、衣服、手足、武器、小道具、エフェクト、残像、粒子を、それぞれのセル内に収める
- 隣のセルにはみ出さない
- 10 px の安全余白に何も入れない
- 動作が大きくなっても、収めるためにキャラクターを縮小しない
- 必要ならエフェクトや腕の振りを抑え、セル内に収める

[描画]
- 2D ゲームスプライトとして見やすい、明確なシルエット
- フレーム間で自然につながる動作
- 単独のイラストではなく、アニメーション素材として途切れのない連続性を最優先する
- すべてのフレームでディテール、線、色、陰影を統一する
```

<a id="ko"></a>
## 한국어

사람의 검수를 거치지 않은 AI 번역입니다. 원문과 함께 읽어 주세요. 번역은 출처 검증이나 재사용 허가를 의미하지 않습니다.

```text
기사 달리기 루프: 작성자는 2.6으로 시트를 생성한 뒤 프레임을 추출했다고 설명
```

### 제작 방법

스프라이트 시트 생성 후 분할

### 검증 상태

작성자는 2.6이라고 주장, 공식 확인 없음, 미시청

### 모델 근거 (번역)

```text
작성자는 gpt_image_2_6이라고 주장(공식 확인 없음, 이 저장소에서는 재시험하지 않음)
```

### 공개 프롬프트 (번역)

```text
이 캐릭터를 참고해 게임용 2D 애니메이션 스프라이트 시트를 만들어 주세요.
동작: “[🔴 여기에 동작 입력]”

하나의 연속 동작을 가로 4칸 × 세로 4칸, 총 16프레임으로 보여 주세요.

[스프라이트 시트 사양]
- 정사각형 캔버스
- 가로 4칸 × 세로 4칸, 총 16프레임
- 16개 셀의 크기는 완전히 동일
- 각 셀의 사방에 최소 10px의 여백
- 테두리, 격자선, 숫자, 글자, 기호, UI는 일절 금지
- 모든 프레임에서 동일한 단색 흰 배경
- 프레임은 왼쪽에서 오른쪽, 위 행에서 아래 행 순으로 시간순 배치

[가장 중요: 크기와 위치 고정]
- 모든 16프레임에서 캐릭터 배율 동일
- 카메라 줌인·줌아웃 금지
- 발밑 지면 기준선을 같은 높이에 고정
- 프레임 사이에 캐릭터 중심 위치가 크게 움직이지 않도록 유지
- 동작에 필요한 만큼만 자세 변경

[가장 중요: 모든 요소를 셀 안에 배치]
- 머리카락, 의상, 팔다리, 무기, 소품, 효과, 잔상, 입자를 모두 각자의 셀 안에 배치
- 옆 셀로 넘치지 않게 유지
- 10px 안전 여백을 침범하지 않게 유지
- 동작이 커져도 캐릭터를 축소해 맞추지 말 것
- 필요하다면 효과와 팔의 움직임 폭을 줄여 셀 안에 배치

[그리기]
- 2D 게임 스프라이트로 알아보기 쉬운 명확한 실루엣
- 프레임 사이에 자연스럽게 이어지는 움직임
- 단일 일러스트가 아닌 애니메이션 소재로서 끊김 없는 연속성을 우선
- 모든 프레임에서 세부 묘사, 선, 색상, 명암을 동일하게 유지
```
