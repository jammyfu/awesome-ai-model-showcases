#!/usr/bin/env python3
"""Append independently verified 2D game-sequence playbooks. Not generic stickers."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDEAS = ROOT / "docs/data/ideas.json"

SSSS_PROMPT = """このキャラクターを参照して、ゲーム用の2Dアニメーションスプライトシートを作成して。
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
・各フレームの描き込み密度、線、塗り、陰影を統一する"""

VARG_PROMPT = """Using this character as the reference, create a 2D animation sprite sheet for a game.
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
- The same detail, line, colour and shading in every frame"""

COMMON = {
    "category": "游戏动作序列",
    "emoji": "🎮",
    "priority": "P1",
    "preview": "",
    "preview_kind": "link_only",
    "tested_here": False,
    "generation_verified": False,
    "game_sequence": True,
    "media_storage": "external",
    "media_rights": "unknown_link_only",
}


def item(**kwargs):
    out = dict(COMMON)
    out.update(kwargs)
    return out


ITEMS = [
    item(
        id="game-ssss-4x4-spec",
        title_zh="游戏 4×4 分镜表（脚底对齐规格）",
        title_en="Game 4×4 sheet with locked ground line",
        origin="community",
        source_url="https://x.com/SSSS_CRYPTOMAN/status/2097797456117539136",
        source_label="SSSS.CRYPTOMAN @SSSS_CRYPTOMAN · 原帖写明 GPT Image 2.5 · X animated_gif→MP4 · 未视觉复核",
        model="GPT Image 2.5（原帖；早于 2.6 原生 GIF）",
        frames=16,
        frame_duration_ms=0,
        frames_basis="author_prompt_spec",
        aspect="1:1",
        description_zh="原作者 2026-09-09 公开的游戏用 4×4/16 帧规格：等大格子、10px 边距、固定倍率与脚底基准线、禁止出格。第二步再切帧对齐做 GIF。这是游戏序列规格，不是表情包。原帖模型是 2.5，不能写成 2.6 成品。X 附件为 animated_gif→MP4 加三张静图；本仓未观看、未转载。",
        prompt=SSSS_PROMPT,
        prompt_adaptation="""用我上传的原创角色全身图生成一张游戏用 2D 分镜表（本站改写，不是 SSSS.CRYPTOMAN 原文）。动作栏只填一个动作，例如待机呼吸、侧面跑、跳跃起落、或一次攻击。

正方形、严格 4 列×4 行共 16 格，格子一样大，每格四周至少 10px 空白。不要框线、数字、文字。背景用统一白底（这不是真 alpha；若接口支持 transparent 再改这一句）。从左到右、从上到下按时间排。

全帧同一角色、同一服装、同一镜头距离、同一脚底高度。不要缩放角色来迁就大动作。头发、武器、特效不得画出格子。

切帧后按阅读顺序播：先对齐脚底再合成循环。待机/走/攻击可用自动对齐；跑跳腾空帧不要把脚硬拉回地面。""",
        prompt_status="verbatim",
        prompt_source_url="https://x.com/SSSS_CRYPTOMAN/status/2097797456117539136",
        output_kind="sprite_sheet",
        evidence_date="2026-09-09",
        tags=["game", "sprite-sheet", "idle-run-attack", "ground-line", "x-mp4"],
        example_is_image26=False,
        example_run_model="GPT Image 2.5（原帖）",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        visual_review_status="unwatched",
        pipeline="sheet_then_slice",
        action_kind="spec_fill_in",
        needs_reference_image=True,
        alpha_status="solid_white_then_key_not_true_alpha",
        engine_import_status="none",
        cell_spec="4×4 · 16 equal cells · ≥10px inset",
        media_id="x-ssss-4x4-gif-mp4",
        media_url="https://video.twimg.com/tweet_video/HRzfplxaYAAEzX5.mp4",
        media_poster_url="https://pbs.twimg.com/tweet_video_thumb/HRzfplxaYAAEzX5.jpg",
        media_kind="mp4",
        reference_image_url="https://pbs.twimg.com/media/HRzfqLqaMAAvrqF.jpg",
        acceptance="格子等大；脚底基准线不跳；无出格；白底不是透明通道；第二步才是 GIF，分镜表本身是静图。",
    ),
    item(
        id="game-varg-knight-run",
        title_zh="骑士跑循环：2.6 出表再切帧",
        title_en="Knight run cycle: 2.6 sheet then slice",
        origin="tested",
        source_url="https://github.com/vargHQ/skills/blob/main/gpt-image-sprite-sheet/SKILL.md",
        source_label="vargHQ gpt-image-sprite-sheet · 声明 gpt_image_2_6 · PNG 分镜+切帧演示 · Phaser/Godot 步骤未实机跑",
        model="gpt-image-2.6 / varg `gpt_image_2_6`（作者声明；本仓未复测）",
        frames=16,
        frame_duration_ms=0,
        frames_basis="author_prompt_spec",
        aspect="1:1",
        description_zh="varg 把上条日文规格译成英文，在 2026-11-04/05 用 gpt_image_2_6 出骑士跑循环 4×4 PNG（1024²→256² 格），再 slice 成循环。这是 Sprite 表切帧，不是原生 GIF。白底抠色后约 79% 透明，可能有白边，不是 API true alpha。技能写了 Phaser atlas / Godot SpriteFrames，但作者写明未跑引擎，故不能说已经用于游戏。本仓 HEAD 核到 PNG 签名与 MP4；未观看、未转载。",
        prompt=VARG_PROMPT,
        prompt_adaptation="""用我上传的原创角色全身侧面图，按同一规格各出一张表，不要混在一张里（本站策划，不是 varg 原文）：

1) 待机：原地呼吸与重心微移，4–6 个有效关键帧即可，其余格重复过渡。
2) 跑：侧面循环跑，接触→下沉→交换→上提，再对侧。腾空帧不要事后把脚拉回地面。
3) 攻击：预备→挥击→命中→回收。武器不得画出格子。

正方形 4×4、等大格、10px 边距、脚底基准线固定、禁止变焦。白底（非真 alpha）或在支持时写 transparent background。一格一个动作，不要待机和跑画在同一张。切帧后对齐脚底，导出循环 GIF 只作预览；游戏导入用图集 PNG+JSON。未实测生成。""",
        prompt_status="verbatim",
        prompt_source_url="https://github.com/vargHQ/skills/blob/main/gpt-image-sprite-sheet/SKILL.md",
        output_kind="sprite_sheet",
        evidence_date="2026-11-05",
        tags=["game", "run-cycle", "sprite-sheet", "phaser", "godot"],
        example_is_image26=True,
        author_model_claim_status="author_explicit",
        media_metadata_status="head_checked",
        visual_review_status="unwatched",
        pipeline="sheet_then_slice",
        action_kind="run",
        needs_reference_image=True,
        alpha_status="keyed_white_not_true_alpha",
        engine_import_status="documented_not_run",
        cell_spec="4×4 on 1024×1024 → 256×256 cells",
        media_id="varg-knight-run-sheet",
        media_url="https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_e80336e6b820.png",
        media_kind="png",
        media_loop_url="https://s3.varg.ai/files/4325c578-378d-4c43-ae53-3cc3218df1ea/file_26db85e9f9b6.mp4",
        acceptance="16 格等大；角色不缩放；跑循环能接回第 1 帧；白底抠色不是真 alpha；有引擎工程/录像才算已用于游戏。本条没有。",
    ),
    item(
        id="game-higgsfield-boxing",
        title_zh="宣称用 2.6 GIF 分镜做的拳击游戏演示",
        title_en="Claimed 2.6 GIF-sheet boxing game footage",
        origin="community",
        source_url="https://x.com/higgsfield_ai/status/2118154923070439759",
        source_label="Higgsfield @higgsfield_ai · 作者声明 GPT Image 2.6 GIF sprite sheets · amplify video · 未视觉复核",
        model="ChatGPT Images 2.6（平台声明；本仓未复测）",
        frames=9,
        frame_duration_ms=120,
        frames_basis="editorial_recommendation",
        aspect="16:9",
        description_zh="平台帖称 first-person boxing game was built with GPT Image 2.6 GIF sprite sheets。附件是 amplify 视频不是 .gif，HEAD 为 video/mp4。本仓未观看，因此只记「作者宣称游戏内演示」，不写成已核引擎导入。提示词未公开，留空。同账号废料场/花灯/武士/对打视频只作相关样本，不拆成多张玩法卡。",
        prompt="",
        prompt_status="empty",
        output_kind="gif",
        evidence_date="2026-11-05",
        tags=["game", "in-engine-claim", "gif-sprite-sheet", "x-mp4"],
        example_is_image26=True,
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        visual_review_status="unwatched",
        pipeline="native_gif_claimed",
        action_kind="in_game_demo",
        needs_reference_image=False,
        alpha_status="gif_1bit_if_native_gif_unknown_here",
        engine_import_status="author_claim_unwatched",
        cell_spec="未公开",
        media_id="x-higgsfield-boxing-mp4",
        media_url="https://video.twimg.com/amplify_video/2118154871027445760/vid/avc1/960x720/Bq_LlhwmfHmeaEya.mp4",
        media_poster_url="https://pbs.twimg.com/amplify_video_thumb/2118154871027445760/img/7_JjxnY3yoz7H7Qe.jpg",
        media_kind="mp4",
        related_source_urls=[
            "https://x.com/higgsfield_ai/status/2118152815625552235",
            "https://x.com/higgsfield_ai/status/2118151978635440250",
            "https://x.com/higgsfield_ai/status/2118156173618852056",
            "https://x.com/higgsfield_ai/status/2118152221414306226",
            "https://x.com/higgsfield_ai/status/2118149003514913249",
        ],
        acceptance="只有看过游戏画面/引擎工程才能说已经用于游戏。本仓未观看。无原文 prompt。不要把这段宣传视频当成可下载的 GIF 分镜表。",
    ),
]


def main() -> None:
    data = json.loads(IDEAS.read_text(encoding="utf-8"))
    by_id = {x["id"]: i for i, x in enumerate(data)}
    added = 0
    for it in ITEMS:
        if it["id"] in by_id:
            data[by_id[it["id"]]] = it
        else:
            data.append(it)
            added += 1
    IDEAS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"game catalog: {len(ITEMS)} playbooks, {added} newly appended, total ideas {len(data)}")


if __name__ == "__main__":
    main()
