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

ITEMS = [
    item(
        id="game-daft-pixel-combo",
        title_zh="像素三连击 / 翻滚 / 法术（作者称直出 GIF）",
        title_en="Pixel combo, roll and spell — author says straight to GIF",
        category="游戏动作序列",
        origin="community",
        source_url="https://x.com/Daft_Trade/status/2118283025498906800",
        source_label="Daft_Trade @Daft_Trade · 作者声明 GPT Image 2.6 straight to GIF · 4 条 MP4=1 案例 · 未观看",
        model="作者声明 GPT Image 2.6（非官方验证；本仓未观看、未复测）",
        default_hidden=False,
        include_in_image26_list=True,
        image26_status="author_claim_unverified",
        frames=16,
        frame_duration_ms=40,
        frames_basis="author_prompt_spec",
        aspect="1:1",
        description_zh="原作者游戏动画原型：像素三连击带刀光、同线程蓄力法环、跳跃翻滚、火花。作者写 One prompt in GPT Image 2.6 … straight to GIF。完整 prompt 缺失；回复只给设置（512²、opaque、连招 16×40ms、法术 12×80ms、跳跃 16×80ms）。四条 X animated_gif 对外都是 video/mp4，计 1 案例。未见引擎工程。未观看、未转载。",
        prompt="",
        prompt_excerpt="Lock the camera and give each action a frame range. I used 512×512, high quality, and an opaque background. The sword combo uses 16 frames × 40 ms. … For a looping spell… 12 frames × 80 ms… For a jump… Run → push off → tuck → flip → land… 16 frames × 80 ms.",
        prompt_adaptation="""用原创像素角色做游戏动作循环（本站策划，不是 Daft_Trade 原文；原帖没有完整 prompt）。

固定镜头，不透明背景，正方形。一次只做一个动作：
- 三连击：预备→第一刀（拖尾）→第二刀→第三刀→回收，约 16 帧。
- 法术环：中心不动，末帧接回首帧，约 12 帧。
- 跳跃翻滚：助跑→起跳→团身→翻转→落地，约 16 帧。腾空帧不要把脚拉回地面。

作者声明直出 GIF；X 附件实际是 MP4。本仓未观看、未复测。""",
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
        source_label="maker_evan @maker_evan · 作者声明 2.6 出 sprite sheet · GPT-6.1 Sol 切帧组装 · 未观看 MP4",
        model="作者声明 GPT Image 2.6 出表（切帧/游戏是另一 agent；非官方验证）",
        default_hidden=False,
        include_in_image26_list=True,
        image26_status="author_claim_unverified",
        frames=8,
        frame_duration_ms=0,
        frames_basis="editorial_recommendation",
        aspect="16:9",
        description_zh="可玩网页街机：狐浪人夜市。作者：GPT Image 2.6 made the sprite sheets and the background；GPT-6.1 Sol cut them into frames and built the rest。绝非原生 GIF 直出。完整 one-shot prompt 在回复帖。附件是游戏录像 MP4 + hero sheet 静图，不是 .gif。作者给了 evals.ag 链接；本仓未观看、未运行，不宣称游戏可用。",
        prompt=FOX_PROMPT,
        prompt_adaptation="""做一页可玩的小街机（本站中文改写，不是 maker_evan 原文）：狐浪人守夜市，方向键移动、空格攻击。

图像模型只负责美术：主角待机/跑/攻击/受伤分镜表、三名敌人、一个 boss、一张背景。不要在代码里画角色。

另一个步骤再切帧、组装 HUD/分数/胜负画面。这不是「直接交一张循环 GIF」。本仓未运行作者页面，也未观看录像。""",
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
        acceptance="2.6 只负责 sheet/背景；切帧是另一模型。录像是 MP4。未运行 evals.ag。不要把这张卡当成原生 GIF。",
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
        description_zh="复古 16 位格斗向：出拳、蓄力循环。作者称 Images 2.6 能出人物 GIF / Sprite Sheet，并讨论透明背景拆帧进 Unity/Godot。没有公开 prompt。两条附件是 animated_gif→MP4，另有静图。作者自述连续动作可能形象不一致。未见引擎内运行录像，不能说已经用于游戏。",
        prompt="",
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
        description_zh="硬测 32×32、≤8 色、无缝 8 帧 walk cycle。作者：Two used GPT Image 2.6. One had no image model, so Opus wrote the pixels in code。后续还有 Opus 量化/修头/镜像腿。最终画面不是纯 2.6 一键结果；纯代码那条更不能算 2.6。完整 prompt 未知，只有上述规格摘录。附件是对照录像 MP4，未观看。",
        prompt="",
        prompt_excerpt="Same prompt: 32x32 grid, at most 8 colours, seamless 8-frame loop.",
        prompt_adaptation="""像素 walk cycle 规格（本站策划；原帖只有规格摘录，完整原文未知）：32×32、最多 8 色、无缝 8 帧侧面走循环。

若用 2.6 出表，必须另外标明：调色、修头、镜像腿如果由其他模型完成，交付物就不是纯 2.6。无图像模型、纯代码画像素的对照路径不要标成 2.6 结果。本仓未观看对照录像。""",
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
        acceptance="必须标多模型后处理。纯代码对照不是 2.6。媒体是 MP4。完整 prompt 空。",
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
        title_zh="宣传方宣称的 2.6 拳击游戏视频",
        title_en="Promotional claim: 2.6 boxing-game footage",
        category="游戏动作序列",
        origin="community",
        source_url="https://x.com/higgsfield_ai/status/2118154923070439759",
        source_label="Higgsfield @higgsfield_ai · 宣传方宣称 2.6 · 未观看 MP4 · 无原文 prompt",
        model="宣传方宣称 ChatGPT Images 2.6（未观看；非官方验证）",
        default_hidden=False,
        include_in_image26_list=True,
        image26_status="promo_claim_unwatched",
        frames=9,
        frame_duration_ms=120,
        frames_basis="editorial_recommendation",
        aspect="16:9",
        description_zh="宣传帖称 boxing game was built with GPT Image 2.6 GIF sprite sheets。这是宣传方宣称，不是确认案例：无原文 prompt、附件是 amplify 视频不是 .gif、本仓未观看，不能写成已核引擎导入或已确认 2.6 游戏序列。同账号其他游戏向视频只作相关样本，不拆卡凑数。",
        prompt="",
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
            "https://x.com/higgsfield_ai/status/2118156173618852056",
            "https://x.com/higgsfield_ai/status/2118152221414306226",
            "https://x.com/higgsfield_ai/status/2118149003514913249",
        ],
        acceptance="只有看过游戏画面/引擎工程才能说已经用于游戏。本仓未观看。无原文 prompt。不要把这段宣传视频当成可下载的 GIF 分镜表。",
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
