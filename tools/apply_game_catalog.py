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
    "emoji": "🎮",
    "priority": "P1",
    "preview": "",
    "preview_kind": "link_only",
    "tested_here": False,
    "generation_verified": False,
    "game_sequence": True,
    "counts_as_image26_game": False,
    "media_storage": "external",
    "media_rights": "unknown_link_only",
}


def item(**kwargs):
    out = dict(COMMON)
    out.update(kwargs)
    return out


FOX_PROMPT = (
    "Make a small arcade action game in one web page: a fox ronin defending a night market "
    "from ink spirits. Arrow keys move, space attacks. All the art must come from the image "
    "model selected for this run: sprite sheets for the hero (idle, run, attack, hurt), three "
    "enemies and a boss, plus a background. Cut the sheets into frames and animate them in the "
    "game. Do not draw characters in code. Add a HUD, a score, and win and game over screens. "
    "It should feel fun the moment it loads."
)

FOX_SHEET_TEMPLATE_RECONSTRUCTED = (
    "A 4x4 sprite sheet of [character], [art style].\n"
    "Rows, top to bottom: idle, run, attack, hurt. 4 frames per row.\n"
    "Same character, same size, same facing in every cell, centered in equal cells.\n"
    "Flat solid magenta background (FF00FF). No grid lines, no borders, no text, no shadows outside the cell."
)

ITEMS = [
    item(
        id="game-daft-pixel-combo",
        title_zh="像素三连击 / 翻滚 / 法术（跳跃事后压背景）",
        title_en="Pixel combo, roll and spell — jump flattened afterward",
        category="游戏动作序列",
        origin="community",
        source_url="https://x.com/Daft_Trade/status/2118283025498906800",
        source_label="Daft_Trade @Daft_Trade · 作者声明 2.6；跳跃承认 flatten 去闪烁 · 4 条 MP4=1 案例 · 未观看",
        model="作者声明 GPT Image 2.6（非官方验证；跳跃有事后修帧；本仓未观看）",
        default_hidden=False,
        include_in_image26_list=True,
        image26_status="author_claim_unverified",
        frames=16,
        frame_duration_ms=40,
        frames_basis="author_prompt_spec",
        aspect="1:1",
        description_zh="像素三连击、法环、跳跃翻滚。作者写 straight to GIF，但跳跃回复原文：I flattened the background color afterward to remove flicker。不能写成所有动作无需后处理。完整 prompt 仍空；只有设置（512²、opaque、16×40 / 12×80 / 16×80ms）。四条 MP4 计 1 案。演示站 gameslash.app 本仓未运行。未见引擎工程。",
        prompt="",
        prompt_audience="image_model",
        prompt_excerpt="Lock the camera… 512×512, high quality, opaque background. Sword combo 16×40 ms. Looping spell 12×80 ms. Jump: Run → push off → tuck → flip → land, 16×80 ms. I flattened the background color afterward to remove flicker.",
        production_notes="真实制作至少还要：跳跃循环压背景去闪烁；完整图像 prompt 仍未公开；不能假设直出即可进引擎。",
        demo_site_url="https://gameslash.app/",
        prompt_adaptation="""用原创像素角色做游戏动作循环（本站策划，不是 Daft_Trade 原文；原帖没有完整 prompt）。

固定镜头，不透明背景，正方形。一次只做一个动作。
跳跃如果出现背景闪烁，需要事后统一底色——作者自己就做了这一步，不要写成「全部动作无需后处理」。

X 附件是 MP4。本仓未观看、未运行 gameslash.app。""",
        prompt_status="empty",
        prompt_source_url="https://x.com/Daft_Trade/status/2118283168071684292",
        output_kind="gif",
        evidence_date="2026-11-05",
        tags=["game", "pixel", "combo", "native-gif-claimed", "x-mp4", "x-original-author"],
        example_is_image26=False,
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        visual_review_status="unwatched",
        pipeline="native_gif_direct_claimed",
        action_kind="attack",
        needs_reference_image=False,
        alpha_status="opaque_author_setting_not_true_alpha",
        engine_import_status="none",
        cell_spec="作者设置 512×512；不是切帧表",
        media_id="x-daft-combo-mp4",
        media_url="https://video.twimg.com/tweet_video/HWWlW3HaEAAxdLe.mp4",
        media_poster_url="https://pbs.twimg.com/tweet_video_thumb/HWWlW3HaEAAxdLe.jpg",
        media_kind="mp4",
        related_media_urls=[
            "https://video.twimg.com/tweet_video/HWWnTgiakAAJIF-.mp4",
            "https://video.twimg.com/tweet_video/HWWnb6KacAA5032.mp4",
            "https://video.twimg.com/tweet_video/HWWnhl0bYAAofEi.mp4",
        ],
        acceptance="四附件算一案。媒体是 MP4 不是 .gif。opaque 背景不是真 alpha。无完整原文 prompt。未见引擎导入。",
    ),
    item(
        id="game-maker-evan-fox-ronin",
        title_zh="狐浪人网页游戏：2.6 出表、另一 agent 切帧",
        title_en="Fox ronin web game: 2.6 sheets, another agent slices",
        category="游戏动作序列",
        origin="community",
        source_url="https://x.com/maker_evan/status/2118222694345040253",
        source_label="maker_evan @maker_evan · 游戏 agent one-shot 已公开；图像 prompt 未公开 · 未观看 MP4",
        model="作者声明 GPT Image 2.6 出表（切帧/游戏是 GPT-6.1 Sol；非官方验证）",
        default_hidden=False,
        include_in_image26_list=True,
        image26_status="author_claim_unverified",
        frames=8,
        frame_duration_ms=0,
        frames_basis="editorial_recommendation",
        aspect="16:9",
        description_zh="狐浪人夜市网页街机。2.6 出 sheet/背景，Sol 切帧组装，绝非原生 GIF。公开全文是给游戏 agent 的 one-shot（Do not draw characters in code），不是发给图像模型的 sprite prompt；Sol 每次自写图像 prompt，原文未公开。evals 文章 4×4 品红底模板是据干净 sheet 共性重建，不是实发原文。同团队 @evals_ag 44 游戏场报是旧工作流补证，不计新案例。演示站本仓未运行。",
        prompt=FOX_PROMPT,
        prompt_audience="game_agent",
        prompt_reconstruction=FOX_SHEET_TEMPLATE_RECONSTRUCTED,
        production_notes="真实制作还要：让游戏 agent 自写图像 prompt（原文未公开）；品红键色→去边→切格→缩放→图集→canvas；切帧不是 2.6 完成的。文章模板只能当重建规格。",
        demo_site_url="https://evals.ag/runs/run_5XGCQ6DH4CMSS4B3D0AXJ65FN3",
        prompt_adaptation="""做一页可玩的小街机（本站中文改写，受众是游戏 agent，不是图像模型原文）：狐浪人守夜市，方向键移动、空格攻击。

图像模型只负责美术表。不要在代码里画角色。另一个步骤再切帧。

发给 2.6 的逐次 sprite prompt 原作者未公开，本站不编造。下面重建模板来自同团队文章共性，不是实发原文。本仓未运行演示站。""",
        prompt_status="verbatim",
        prompt_source_url="https://x.com/maker_evan/status/2118218896167886861",
        output_kind="sprite_sheet",
        evidence_date="2026-11-05",
        tags=["game", "idle-run-attack", "sprite-sheet", "web-arcade", "x-mp4", "x-original-author"],
        example_is_image26=False,
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        visual_review_status="unwatched",
        pipeline="sheet_then_agent_cut",
        action_kind="in_game_demo",
        needs_reference_image=False,
        alpha_status="unknown_sheet_then_agent",
        engine_import_status="author_claim_unwatched",
        cell_spec="idle/run/attack/hurt 多表；格尺寸作者未公开",
        media_id="x-evan-fox-game-mp4",
        media_url="https://video.twimg.com/amplify_video/2118222620546289665/vid/avc1/1280x776/5_45DZtOxtMThnXz.mp4",
        media_poster_url="https://pbs.twimg.com/amplify_video_thumb/2118222620546289665/img/2BIV9HEKZJFQwBm8.jpg",
        media_kind="mp4",
        reference_image_url="https://pbs.twimg.com/media/HWVswCLbgAACxKN.jpg",
        related_media_urls=[
            "https://video.twimg.com/amplify_video/2118218561596588032/vid/avc1/1440x874/tc9MlAOH2s42gwUo.mp4",
        ],
        related_source_urls=[
            "https://x.com/evals_ag/status/2118336675697090607",
            "https://x.com/maker_evan/status/2118218896167886861",
            "https://x.com/maker_evan/status/2118218636725027037",
        ],
        acceptance="prompt 字段是游戏 agent 原文，不是图像模型原文。重建模板不得标成 verbatim。未运行 evals.ag。同团队场报不计新案例。",
    ),
    item(
        id="game-xiaomovps-fighter",
        title_zh="复古格斗出拳 / 蓄力循环",
        title_en="Retro fighter punch and charge loops",
        category="游戏动作序列",
        origin="community",
        source_url="https://x.com/xiaomovps/status/2118274032227471705",
        source_label="小墨同学 @xiaomovps · 作者声明 Images 2.6 · X animated_gif→MP4 · 未见引擎内运行",
        model="作者声明 GPT Images 2.6（非官方验证；本仓未观看、未复测）",
        default_hidden=False,
        include_in_image26_list=True,
        image26_status="author_claim_unverified",
        frames=12,
        frame_duration_ms=120,
        frames_basis="editorial_recommendation",
        aspect="1:1",
        description_zh="复古格斗出拳/蓄力。深挖后会话 7 条回复作者未补 prompt；from:xiaomovps 后续为 ESP32/Grok，无新 2.6 游戏动作。仍无原文 prompt，仍无 Unity/Godot 实机画面。两条 MP4 + 静图。不能说已经用于游戏。",
        prompt="",
        prompt_audience="image_model",
        production_notes="真实制作缺口：完整图像 prompt；引擎导入与碰撞区；连续动作形象一致性。深挖未补上这些。",
        prompt_adaptation="""用原创复古 16 位格斗角色各做一张循环（本站策划，原帖无完整 prompt）：出拳、蓄力。

固定中景，全身入画，脚底对齐。一次一个动作。循环回到第一帧。

若走分镜表：等大格、透明或声明非真 alpha 的底。作者提到可拆进 Unity/Godot，但本仓未见引擎内运行证据。X 附件是 MP4。未观看、未复测。""",
        prompt_status="empty",
        output_kind="gif",
        evidence_date="2026-11-05",
        tags=["game", "fighter", "punch", "charge", "x-mp4", "x-original-author"],
        example_is_image26=False,
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        visual_review_status="unwatched",
        pipeline="native_gif_and_or_sprite_claimed",
        action_kind="attack",
        needs_reference_image=False,
        alpha_status="author_mentions_transparent_unverified",
        engine_import_status="discussed_not_shown",
        cell_spec="未公开格子尺寸",
        media_id="x-xiaomo-punch-mp4",
        media_url="https://video.twimg.com/tweet_video/HWWcoNDawAALRaJ.mp4",
        media_poster_url="https://pbs.twimg.com/tweet_video_thumb/HWWcoNDawAALRaJ.jpg",
        media_kind="mp4",
        reference_image_url="https://pbs.twimg.com/media/HWWcoNLbkAAxgxF.jpg",
        related_media_urls=["https://video.twimg.com/tweet_video/HWWcoNBbMAATJjY.mp4"],
        acceptance="出拳/蓄力是动作序列不是表情包。媒体是 MP4。Unity/Godot 只是作者讨论，未见运行画面。无原文 prompt。",
    ),
    item(
        id="game-maker-evan-walk-cycle",
        title_zh="像素 walk cycle 对照（含其他模型修帧）",
        title_en="Pixel walk-cycle comparison — multi-model postprocess",
        category="游戏动作序列",
        origin="community",
        source_url="https://x.com/maker_evan/status/2118235403430027495",
        source_label="maker_evan @maker_evan · 多模型后处理 walk cycle · 纯代码对照不算 2.6 · 未观看 MP4",
        model="作者声明两条 GPT Image 2.6 + Claude Opus 5.5 后处理；一条无图像模型",
        default_hidden=False,
        include_in_image26_list=True,
        image26_status="multimodel_postprocess",
        frames=8,
        frame_duration_ms=0,
        frames_basis="author_prompt_spec",
        aspect="16:9",
        description_zh="32×32 / 8 帧 walk。作者：Neither image model got there alone。sheet 看似像素却含 130,647 与 81,053 色；Opus 量化到 7 色、锁头、镜像第 5–8 帧腿、手修 14 个头部像素。像素质量失败局限要保留：2.6 在像素上是在假象。纯代码对照和 @tuzhenzhao Pocketworld（最终 idle/attack 由代码画）都不是纯 2.6 动画。完整 prompt 空。",
        prompt="",
        prompt_audience="unpublished",
        prompt_excerpt="Same prompt: 32x32 grid, at most 8 colours, seamless 8-frame loop.",
        production_notes="真实制作还要：量化到网格与 7 色、锁头、镜像腿、手修像素。2.6 单独交不出合格像素循环。Pocketworld 最终循环是代码绘制，只作混合参考。",
        demo_site_url="https://evals.ag/runs/run_52B3CEGJ9WW16WPDQNWKMXPWB1",
        prompt_adaptation="""像素 walk cycle 规格（本站策划；原帖只有规格摘录）：32×32、最多 8 色、无缝 8 帧。

2.6 出表后必须另做：量化、锁头、镜像腿、手修。不要把纯代码对照或 Pocketworld 代码循环标成 2.6 结果。本仓未观看、未运行演示站。""",
        prompt_status="empty",
        output_kind="sprite_sheet",
        evidence_date="2026-11-05",
        tags=["game", "walk-cycle", "multimodel", "not-pure-26", "x-mp4"],
        example_is_image26=False,
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        visual_review_status="unwatched",
        pipeline="sheet_then_agent_postprocess",
        action_kind="run",
        needs_reference_image=False,
        alpha_status="unknown_pixel_grid",
        engine_import_status="none",
        cell_spec="32×32 · ≤8 colours · 8 frames",
        media_id="x-evan-walk-mp4",
        media_url="https://video.twimg.com/amplify_video/2118232769663025152/vid/avc1/1920x724/ayooWwkfOTLQNASb.mp4",
        media_poster_url="https://pbs.twimg.com/amplify_video_thumb/2118232769663025152/img/6IwejEyatKbS3iw5.jpg",
        media_kind="mp4",
        reference_image_url="https://pbs.twimg.com/media/HWWBvlWakAAEYS-.jpg",
        related_source_urls=[
            "https://x.com/maker_evan/status/2118241905477898501",
            "https://x.com/tuzhenzhao/status/2118286041719423146",
            "https://github.com/Tu-Zhenzhao/pocketworld",
        ],
        acceptance="必须标 Opus 量化/锁头/镜像腿/手修。纯代码与 Pocketworld 代码循环不是纯 2.6。媒体是 MP4。完整 prompt 空。",
    ),
    item(
        id="game-ssss-4x4-spec",
        title_zh="【2.5 历史规格】游戏 4×4 分镜表",
        title_en="Historical 2.5 spec: 4×4 game sheet",
        category="其他模型参考",
        origin="community",
        source_url="https://x.com/SSSS_CRYPTOMAN/status/2097797456117539136",
        source_label="SSSS.CRYPTOMAN @SSSS_CRYPTOMAN · 原帖写明 GPT Image 2.5 · 不是 2.6 · 默认隐藏 · 未观看 MP4",
        model="GPT Image 2.5（原帖写明；不是 Image 2.6）",
        default_hidden=True,
        include_in_image26_list=False,
        image26_status="not_26",
        frames=16,
        frame_duration_ms=0,
        frames_basis="author_prompt_spec",
        aspect="1:1",
        description_zh="历史参考，默认不出现在 Image 2.6 玩法列表。原作者 2026-09-09 公开的游戏用 4×4/16 帧规格：等大格子、10px 边距、固定倍率与脚底基准线。原帖写明 GPT Image 2.5，不能计入 2.6 游戏案例。规格仍可供 2.6 出表时对照。X 附件 animated_gif→MP4，未观看、未转载。",
        prompt=SSSS_PROMPT,
        prompt_adaptation="""用我上传的原创角色全身图生成一张游戏用 2D 分镜表（本站改写，不是 SSSS.CRYPTOMAN 原文）。动作栏只填一个动作，例如待机呼吸、侧面跑、跳跃起落、或一次攻击。

正方形、严格 4 列×4 行共 16 格，格子一样大，每格四周至少 10px 空白。不要框线、数字、文字。背景用统一白底（这不是真 alpha；若接口支持 transparent 再改这一句）。从左到右、从上到下按时间排。

全帧同一角色、同一服装、同一镜头距离、同一脚底高度。不要缩放角色来迁就大动作。头发、武器、特效不得画出格子。

切帧后按阅读顺序播：先对齐脚底再合成循环。待机/走/攻击可用自动对齐；跑跳腾空帧不要把脚硬拉回地面。""",
        prompt_status="verbatim",
        prompt_source_url="https://x.com/SSSS_CRYPTOMAN/status/2097797456117539136",
        output_kind="sprite_sheet",
        evidence_date="2026-09-09",
        tags=["game", "sprite-sheet", "history-2-5", "not-image26", "x-mp4"],
        example_is_image26=False,
        example_run_model="GPT Image 2.5（原帖写明）",
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
        title_zh="骑士跑循环：作者声明 2.6 出表再切帧",
        title_en="Knight run cycle: author-claimed 2.6 sheet",
        category="游戏动作序列",
        origin="community",
        source_url="https://github.com/vargHQ/skills/blob/main/gpt-image-sprite-sheet/SKILL.md",
        source_label="vargHQ gpt-image-sprite-sheet · 作者声明 gpt_image_2_6 · 非 OpenAI 官方验证 · 未复测",
        model="作者声明 gpt_image_2_6（非官方验证；本仓未复测）",
        default_hidden=False,
        include_in_image26_list=True,
        image26_status="author_claim_unverified",
        frames=16,
        frame_duration_ms=0,
        frames_basis="author_prompt_spec",
        aspect="1:1",
        description_zh="工作流作者声明用 gpt_image_2_6 把 4×4 规格跑成骑士跑循环 PNG 再切帧。这是作者声明，不是 OpenAI 官方验证的 2.6 游戏成品，本仓未复测生成。白底抠色不是真 alpha。技能写了 Phaser/Godot 步骤但写明未跑引擎，不能说已经用于游戏。HEAD 核到 PNG 签名与短 MP4；未观看、未转载。",
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
        tags=["game", "run-cycle", "sprite-sheet", "author-claim"],
        example_is_image26=False,
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
        title_zh="宣传方 9 帖游戏演示（1 组，非 9 案）",
        title_en="Higgsfield promo series — 9 posts, one group",
        category="游戏动作序列",
        origin="community",
        source_url="https://x.com/higgsfield_ai/status/2118154923070439759",
        source_label="Higgsfield @higgsfield_ai · 9 帖=1 组宣传演示 · 未观看 MP4 · 无原文 prompt",
        model="宣传方宣称 ChatGPT Images 2.6（未观看；非官方验证）",
        default_hidden=False,
        include_in_image26_list=True,
        image26_status="promo_claim_unwatched",
        frames=9,
        frame_duration_ms=120,
        frames_basis="editorial_recommendation",
        aspect="16:9",
        description_zh="Higgsfield 9 帖游戏向视频（废料场变色龙、花灯、僵尸猎人、太空射击、武士对决、剪影对打、角色一致性、平底锅打鸡、第一人称拳击）计 1 组宣传演示，不拆成 9 案。引用链无独立原作者。无原文 prompt。附件是 amplify MP4。本仓未观看。",
        prompt="",
        prompt_audience="unpublished",
        production_notes="宣传组没有可复制图像 prompt，也没有已观看的引擎工程。不要按帖数加案例。",
        prompt_status="empty",
        output_kind="gif",
        evidence_date="2026-11-05",
        tags=["game", "promo-claim", "unwatched", "x-mp4"],
        example_is_image26=False,
        author_model_claim_status="promo_claim",
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
            "https://x.com/higgsfield_ai/status/2118153557551743154",
            "https://x.com/higgsfield_ai/status/2118154233556201504",
            "https://x.com/higgsfield_ai/status/2118156173618852056",
            "https://x.com/higgsfield_ai/status/2118154729633337599",
            "https://x.com/higgsfield_ai/status/2118152221414306226",
            "https://x.com/higgsfield_ai/status/2118155412130406905",
            "https://x.com/higgsfield_ai/status/2118154923070439759",
        ],
        acceptance="9 帖=1 组。本仓未观看。无原文 prompt。引用链镜像不算独立成功工作流。",
    ),
    item(
        id="game-am09-sprite-failure",
        title_zh="失败样本：动态+静态同帧会崩",
        title_en="Failure: mixed static/dynamic GIF collapses",
        category="失败与注意事项",
        origin="community",
        source_url="https://x.com/AM09_21/status/2118143217434800219",
        source_label="AM09:21 @AM09_21 · 作者声明 2.6 GIF 失败验证 · 未观看 MP4",
        model="作者声明 GPT Image 2.6 GIF（失败/注意事项；非成功落地）",
        default_hidden=True,
        include_in_image26_list=False,
        image26_status="failure_sample",
        frames=8,
        frame_duration_ms=120,
        frames_basis="editorial_recommendation",
        aspect="1:1",
        description_zh="独立失败样本，不计入成功游戏。作者：动态与静态同帧的 GIF 易崩；ゲームとかに応用するならスプライトごとに生成。约 2 分钟出图。无原文 prompt。媒体 MP4 未观看。",
        prompt="",
        prompt_audience="unpublished",
        production_notes="游戏向不要把待机和动作画进同一张会动的 GIF；按动作分开出 sprite。这不是成功案例。",
        prompt_status="empty",
        output_kind="gif",
        evidence_date="2026-11-05",
        tags=["game", "failure", "notes", "x-mp4"],
        example_is_image26=False,
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        visual_review_status="unwatched",
        pipeline="native_gif_claimed",
        action_kind="spec_fill_in",
        needs_reference_image=False,
        alpha_status="gif_1bit_if_native_gif_unknown_here",
        engine_import_status="none",
        cell_spec="作者建议按 sprite 分开生成",
        media_id="x-am09-collapse-mp4",
        media_url="https://video.twimg.com/tweet_video/HWUoBnhaUAALYln.mp4",
        media_poster_url="https://pbs.twimg.com/tweet_video_thumb/HWUoBnhaUAALYln.jpg",
        media_kind="mp4",
        acceptance="失败样本。不计成功卡。无 prompt。媒体是 MP4。",
    ),
    item(
        id="game-wrongnebula-pixel-failure",
        title_zh="失败样本：像素动画 not there yet",
        title_en="Failure: pixel-art animation not there yet",
        category="失败与注意事项",
        origin="community",
        source_url="https://x.com/WrongNebula/status/2118164394400182755",
        source_label="WrongNebula · Sunburst/Flare 像素动画失败 · 未观看 MP4",
        model="作者声明 GPT Image 2.6 Sunburst/Flare（失败结论：不适合 pixel art）",
        default_hidden=True,
        include_in_image26_list=False,
        image26_status="failure_sample",
        frames=8,
        frame_duration_ms=120,
        frames_basis="editorial_recommendation",
        aspect="16:9",
        description_zh="独立失败样本，不计入成功游戏。作者测 Sunburst/Flare 做 pixel art animation，结论 not there yet；后写 GPT 2.6 image isn't fit for pixel art，建议 pixeldiffusion。无原文 prompt。与 maker walk 的像素假象相互印证，不是新成功工作流。",
        prompt="",
        prompt_audience="unpublished",
        production_notes="严格像素循环不要指望 2.6 直出。作者建议 pixeldiffusion。evals 回复只说 painted sprite 更干净，不能把失败帖改写成成功。",
        prompt_status="empty",
        output_kind="gif",
        evidence_date="2026-11-05",
        tags=["game", "failure", "pixel", "notes", "x-mp4"],
        example_is_image26=False,
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        visual_review_status="unwatched",
        pipeline="native_gif_or_sheet_tests",
        action_kind="run",
        needs_reference_image=False,
        alpha_status="unknown_pixel_grid",
        engine_import_status="none",
        cell_spec="未公开；作者判定失败",
        media_id="x-wrongnebula-pixel-mp4",
        media_url="https://video.twimg.com/tweet_video/HWU7Qt2a4AARF_K.mp4",
        media_poster_url="https://pbs.twimg.com/tweet_video_thumb/HWU7Qt2a4AARF_K.jpg",
        media_kind="mp4",
        related_media_urls=["https://video.twimg.com/tweet_video/HWU9CZza8AAHW2s.mp4"],
        related_source_urls=[
            "https://x.com/WrongNebula/status/2118207074438148591",
            "https://x.com/evals_ag/status/2118345170022433142",
        ],
        acceptance="失败样本。不计成功卡。无 prompt。媒体是 MP4。",
    ),
]


def main() -> None:
    data = json.loads(IDEAS.read_text(encoding="utf-8"))
    keep_ids = {it["id"] for it in ITEMS}
    data = [x for x in data if x.get("id") not in keep_ids]
    before = len(data)
    data.extend(ITEMS)
    IDEAS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"game catalog: {len(ITEMS)} playbooks, {len(data) - before} appended after replace, total ideas {len(data)}")


if __name__ == "__main__":
    main()
