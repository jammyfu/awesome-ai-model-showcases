#!/usr/bin/env python3
"""Apply independently re-checked X playbooks. Quality-dedupe; never dump 42 cards.

Media: X animated_gif + HEAD video/mp4 only. No decode, no watch, no .gif claim.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDEAS = ROOT / "docs/data/ideas.json"
MANIFEST = ROOT / "docs/data/media-manifest.json"

MIRAI_PROMPT = """添付画像を基準に、アニメーションGIFファイルを生成してください。

【出力仕様】
・各フレームの幅：288px
・各フレームの高さ：512px
・総フレーム数：16フレーム
・各フレームの表示時間：200ミリ秒
・合計再生時間：3.2秒
・無限ループ
・この寸法をGIFファイルそのもののピクセル寸法として使用する。表示上のサイズだけを変えたり、余白を追加して寸法を合わせたりしない。

【映像内容】
参考画像と同じミライ、同じ顔、短いボブ、衣装、秋の街並み、日差しを維持する。

構図は胸から上。顔全体と頭の上が入り、右手に持った赤いモミジが胸元に見える。
カメラ固定、ワンカット。

ミライがカメラを見ながら口元を少しほころばせ、一度だけ自然に瞬きをする。
風でボブの毛先と背景の紅葉が少し揺れる。
最後は最初の表情と姿勢へ戻り、自然につながるループにする。

全フレームを同じ人物の連続動作として描く。
フレームを単純に複製して枚数だけを増やさず、毛先や背景の葉の動きを時間に沿って少しずつ変える。
顔立ちや衣装を途中で変更しない。

静止画、分割画像、絵コンテではなく、動くGIFを出力する。
字幕、文字、ロゴ、透かし、音楽なし。"""

MIRAI_ADAPT = """以我上传的角色参考图生成循环 GIF（本站改写，不是蓝澤ミライ原文）。

【输出规格】
- 文件像素 288×512，不要靠加边或只改显示尺寸
- 16 帧，每帧 200ms，总长 3.2 秒，无限循环

【画面】
胸上构图，固定镜头。角色看镜头、轻轻微笑、自然眨眼一次；发梢与背景轻微随风。最后一帧回到第一帧。不要复制同一帧凑数。不要字幕、水印。

作者实测：ChatGPT 对话里 288×512 / 576×1024 指定可能不被遵守；指定 16 帧得到约 267×358，指定 32 帧得到约 217×217。本仓未复测生成，也未观看附件。"""

FATFISH_PROMPT = """请以我上传的大肥鱼图片为角色和画风参考，根据最后一行的「表情包主题」，直接制作一张可下载的动态 GIF 表情包。

【角色保持一致】
保留参考图中的蓝色渐变长发、呆毛、鲸鱼耳鳍、蓝色蝴蝶结、白色女仆头饰、蓝白女仆裙和大鲸鱼尾巴。
保持原图的大头小身体 Q 版比例、圆脸和可爱画风，人物外观在所有帧中保持一致。

【自动设计动作】
理解我想表达的情绪或梗，将它设计成一个简单、有趣、一眼能看懂的短动作。
突出一个核心笑点，用夸张表情、动作反差和轻微的压缩回弹增加喜感。头发、呆毛、耳鳍和尾巴自然跟随动作。
根据主题添加必要的少量道具，保持画面简洁。
主动设计首尾衔接，让动画能够自然循环播放。

【自动配字】
根据主题提炼一句简短、有网感的中文配字，优先控制在 2～8 个字。
如果主题中用引号指定了台词，直接使用该台词。
字幕放在顶部，使用粗圆体、深蓝字、白色描边；文字、字形和位置全程稳定，角色与道具不遮挡字幕。

【画面与输出】
正方形画面，纯白背景，固定镜头，主体居中并保留足够边距。
动画约 2～3 秒，无限循环，动作清晰，适合聊天时作为表情包发送。
最终交付实际会播放的多帧 GIF 文件，并提供下载。

表情包主题：【在这里填一句话，描述你想表达的梗、情绪或动作】"""

FATFISH_ADAPT = """请以我上传的角色图为外形和画风参考，根据最后一行的「表情包主题」，直接制作一张可下载的动态 GIF 表情包。（本站改写：去掉大肥鱼专属外形，换成你的角色。）

【角色保持一致】
保留参考图的发型、配色、服装、标志性配件和画风。人物外观在所有帧中保持一致。

【自动设计动作】
把主题收成一个简单、一眼能看懂的短动作。夸张表情、轻微压缩回弹；配件跟随运动。首尾衔接，可循环。

【自动配字】
2～8 个字的中文配字；若主题用引号指定台词，直接用该台词。顶部粗圆体、深色字白描边，位置稳定。

【画面与输出】
正方形、纯白背景、固定镜头。约 2～3 秒无限循环。交付会播放的多帧 GIF，不要只给分镜静图。

表情包主题：【在这里填一句话】"""

NONIE_PROMPT = """Create a coordinated set of 10 animated reaction GIFs featuring the main character in Image 1, using Image 2 as the visual style reference.

How to use the references

Image 1 defines the character: preserve their recognizable identity, distinctive features, clothing, and accessories while translating them into the target style. Adapt gestures to the character’s anatomy.
Image 2 defines the visual style: match its medium, rendering, shapes, proportions, color palette, lighting, textures, level of detail, and overall mood. Let this reference determine whether the result is photographic, illustrated, cartoon-like, painterly, pixel art, clay, plush, or another aesthetic.
Apply that style consistently to the character, setting, props, and captions.
Draw the setting from Image 1 where useful, simplifying or restyling it to suit Image 2.
Keep the same character design, camera angle, framing, and visual treatment across all ten GIFs.
Keep the reactions funny, expressive, and uncluttered. Let gestures, expressions, and timing carry the humor.

Create these eight fixed reactions with short captions:

(1) When I didn’t understand anything the other person said.
(2) When I need more context.
(3) When I don’t know what to do.
(4) When something was probably supposed to be funny, but wasn’t.
(5) When the other person is sad.
(6) When someone complains yet again about their actually pretty good life.
(7) When acknowledging information or instructions.
(8) When getting started on a task.

Invent two additional reactions inspired specifically by Image 1.

Find distinctive gestures, objects, clothing, or details in the setting. Turn two of those cues into useful, funny chat reactions with short captions. Make them distinct from the eight above.

For example, a hand-heart pose might inspire “LOVE THIS.” and a coffee mug might inspire “BUT FIRST, COFFEE.” Choose reactions that fit the actual input image.

Animation and captions:

Each GIF must be 1:1, 512 × 512 pixels, approximately four seconds long, and loop forever.
Give each reaction a readable beginning, gesture, brief hold, and return. Animate the character’s face and limbs, rather than relying on camera movement.
Match the movement and timing to the visual style: subtle expressions, exaggerated cartoon gestures, stepped stop-motion, or another appropriate approach.

Choose caption typography, color, and treatment that complement Image 2. If it contains no typography, select a simple, readable treatment that fits its aesthetic.
Keep captions consistent and legible at small sizes, positioned away from faces and important gestures. Include only the requested caption.

Deliverables

Use image generation to create the visuals and assemble them into actual animated GIF files. Do not stop at concepts, still images, or sprite sheets.

Deliver:

All ten individual GIFs.
A ZIP containing all ten.
One animated gallery GIF arranged in 5 columns × 2 rows, in the order listed above.

Input Images:"""

NONIE_ADAPT = """用图 1 的角色 + 图 2 的画风，做一套 10 张循环反应 GIF。（本站中文改写，不是 Leonie Engel 原文。）

图 1 定角色外形，图 2 定媒介/比例/配色/光影。十张保持同一角色、同一机位、同一画风。动作和表情负责笑点，画面别堆。

八个固定情境（短字幕）：
1. 完全没听懂
2. 需要更多上下文
3. 不知道该怎么办
4. 这大概该好笑，但并不
5. 对方难过时
6. 又在抱怨其实还不错的生活
7. 收到信息/指令，表示收到
8. 开始动手干活

再根据图 1 里两件独特道具或姿势发明两张，不要和上面重复。

每张 512×512、约 4 秒、无限循环；起势—动作—停顿—回位。交付 10 个会动的 GIF + 一个压缩包 + 一张 5×2 总览 GIF。不要只出静帧或分镜表。

作者附件是 X animated_gif→MP4（1280×512），本仓未观看、未复测生成。"""

NEW_IDEAS = [
    {
        "id": "x-mirai-spec-gif",
        "title_zh": "规格化眨眼循环（作者测尺寸未遵守）",
        "title_en": "Spec'd Blink Loop (Size Not Honored)",
        "category": "角色动画",
        "emoji": "🍁",
        "origin": "community",
        "source_url": "https://x.com/mirai_ai2050/status/2118213713761292432",
        "source_label": "藍澤 ミライ @mirai_ai2050 · 作者声明 GPT Image 2.6 · X API animated_gif · HEAD video/mp4 · 未视觉复核",
        "model": "ChatGPT Images 2.6（作者声明；本仓未复测）",
        "frames": 16,
        "frame_duration_ms": 200,
        "frames_basis": "author_prompt_spec",
        "aspect": "9:16",
        "priority": "P1",
        "description_zh": "完整日文规格提示词（288×512、16 帧×200ms、眨眼+发梢微动）。作者反馈指定尺寸未被遵守。X 两枚附件类型是 animated_gif，HEAD 均为 video/mp4。本仓未观看、未解码数帧、未复测生成；静帧预览不是动图。提示词在回复帖。",
        "prompt": MIRAI_PROMPT,
        "prompt_adaptation": MIRAI_ADAPT,
        "prompt_status": "verbatim",
        "output_kind": "gif",
        "evidence_date": "2026-11-05",
        "tags": ["spec", "blink", "loop", "reference-image", "x-mp4"],
        "preview": "",
        "preview_kind": "link_only",
        "tested_here": False,
        "generation_verified": False,
        "author_model_claim_status": "author_explicit",
        "media_metadata_status": "x_api_and_head_checked",
        "visual_review_status": "unwatched",
        "example_is_image26": True,
        "media_id": "x-mirai-16f-mp4",
        "media_url": "https://video.twimg.com/tweet_video/HWVoI72bsAAOx_0.mp4",
        "media_poster_url": "https://pbs.twimg.com/tweet_video_thumb/HWVoI72bsAAOx_0.jpg",
        "media_kind": "mp4",
        "media_storage": "external",
        "media_rights": "unknown_link_only",
        "prompt_source_url": "https://x.com/mirai_ai2050/status/2118213855100997785",
    },
    {
        "id": "x-miramusic-stretch",
        "title_zh": "扁平风拉伸循环",
        "title_en": "Flat Stretch Loop",
        "category": "角色动画",
        "emoji": "🧘",
        "origin": "community",
        "source_url": "https://x.com/MiraMusic_AI/status/2118168013618987298",
        "source_label": "MiraMusic @MiraMusic_AI · 作者声明 GPTimage2.6 · X API animated_gif · HEAD video/mp4 · 未视觉复核",
        "model": "ChatGPT Images 2.6（作者声明；本仓未复测）",
        "frames": 9,
        "frame_duration_ms": 180,
        "frames_basis": "editorial_recommendation",
        "aspect": "1:1",
        "priority": "P1",
        "description_zh": "从零日文提示词做拉伸 GIF，并写明不要微细纹理、粒状噪点和斜网格。作者另附静图。X 标 GIF，HEAD 为 video/mp4（512²）。9 帧是本站玩法建议，不是观看计数。未观看、未复测。",
        "prompt": "ストレッチをしているGIFを製作してください。\n仕上げはフラットでクリーンに。\n複雑な微細テクスチャ、過剰な細密描写、粒状ノイズ、ザラつき、斜めグリッド状の模様なし",
        "prompt_adaptation": "做一个拉伸运动的循环 GIF。平面、干净。不要复杂微细纹理、过度细描、颗粒噪声、粗糙感和斜网格纹。（本站中文改写）\n建议 9 帧、每帧约 180ms；固定镜头，首尾衔接。本仓未观看作者附件，也未复测生成。",
        "prompt_status": "verbatim",
        "output_kind": "gif",
        "evidence_date": "2026-11-05",
        "tags": ["stretch", "flat", "negative-prompt", "x-mp4"],
        "preview": "",
        "preview_kind": "link_only",
        "tested_here": False,
        "generation_verified": False,
        "author_model_claim_status": "author_explicit",
        "media_metadata_status": "x_api_and_head_checked",
        "visual_review_status": "unwatched",
        "example_is_image26": True,
        "media_id": "x-miramusic-stretch-mp4",
        "media_url": "https://video.twimg.com/tweet_video/HWU-HlkagAEV0iO.mp4",
        "media_poster_url": "https://pbs.twimg.com/tweet_video_thumb/HWU-HlkagAEV0iO.jpg",
        "media_kind": "mp4",
        "media_storage": "external",
        "media_rights": "unknown_link_only",
        "reference_image_url": "https://pbs.twimg.com/media/HWU-kOfakAAFXuX.jpg",
    },
    {
        "id": "x-gorden-sun-rice",
        "title_zh": "真香吃饭循环",
        "title_en": "So Good Rice Loop",
        "category": "表情梗图",
        "emoji": "🍚",
        "origin": "community",
        "source_url": "https://x.com/Gorden_Sun/status/2118166046175908016",
        "source_label": "Gorden Sun @Gorden_Sun · 作者声明 GPT Image 2.6 · X API animated_gif · HEAD video/mp4 · 未视觉复核",
        "model": "ChatGPT Images 2.6（作者声明；本仓未复测）",
        "frames": 9,
        "frame_duration_ms": 180,
        "frames_basis": "editorial_recommendation",
        "aspect": "1:1",
        "priority": "P1",
        "description_zh": "上传角色参考图，一句话生成「吃大白米饭 + 真香！」表情包。作者标明图 1 是生成结果、图 2 是参考图。X 标 GIF，HEAD 为 video/mp4。未观看、未复测。9 帧是玩法建议。",
        "prompt": "使用这个角色，生成一张GIF图，内容是她吃大白米饭，图片里有文字：真香！",
        "prompt_adaptation": "使用我上传的角色，生成一张循环 GIF：她在吃大白米饭，画面里有文字「真香！」。保持角色一致，固定镜头，首尾衔接。（本站补了循环约束，不是原文。）本仓未观看作者附件。",
        "prompt_status": "verbatim",
        "output_kind": "gif",
        "evidence_date": "2026-11-05",
        "tags": ["sticker", "caption", "rice", "reference-image", "x-mp4"],
        "preview": "",
        "preview_kind": "link_only",
        "tested_here": False,
        "generation_verified": False,
        "author_model_claim_status": "author_explicit",
        "media_metadata_status": "x_api_and_head_checked",
        "visual_review_status": "unwatched",
        "example_is_image26": True,
        "media_id": "x-gorden-sun-rice-mp4",
        "media_url": "https://video.twimg.com/tweet_video/HWU8ujEbsAEYOxw.mp4",
        "media_poster_url": "https://pbs.twimg.com/tweet_video_thumb/HWU8ujEbsAEYOxw.jpg",
        "media_kind": "mp4",
        "media_storage": "external",
        "media_rights": "unknown_link_only",
        "reference_image_url": "https://pbs.twimg.com/media/HWU8w0Wa8AAb9LS.jpg",
    },
    {
        "id": "x-op7418-fatfish",
        "title_zh": "大肥鱼主题表情包模板",
        "title_en": "Fat Fish Sticker Template",
        "category": "表情梗图",
        "emoji": "🐋",
        "origin": "community",
        "source_url": "https://x.com/op7418/status/2118181775688241456",
        "source_label": "歸藏 @op7418 · 作者声明 GPT-image-2.6 · X API animated_gif×4 · HEAD video/mp4 · 未视觉复核",
        "model": "ChatGPT Images 2.6（作者声明；本仓未复测）",
        "frames": 12,
        "frame_duration_ms": 180,
        "frames_basis": "editorial_recommendation",
        "aspect": "1:1",
        "priority": "P1",
        "description_zh": "完整填空模板：上传两张大肥鱼参考图，改最后一行主题即可出循环表情包（角色锁定、自动动作、自动配字）。同一帖 4 条 animated_gif 算 1 个玩法，不拆 4 张卡。回复里的 iskunzhenbai 衍生与 abc123 静图转动图只记相关样本。X 附件 HEAD 均为 video/mp4，未观看、未拿到 .gif。12 帧是按「约 2–3 秒」估的玩法建议。",
        "prompt": FATFISH_PROMPT,
        "prompt_adaptation": FATFISH_ADAPT,
        "prompt_status": "verbatim",
        "output_kind": "gif",
        "evidence_date": "2026-11-05",
        "tags": ["sticker", "template", "fatfish", "caption", "x-mp4"],
        "preview": "",
        "preview_kind": "link_only",
        "tested_here": False,
        "generation_verified": False,
        "author_model_claim_status": "author_explicit",
        "media_metadata_status": "x_api_and_head_checked",
        "visual_review_status": "unwatched",
        "example_is_image26": True,
        "media_id": "x-op7418-fatfish-a-mp4",
        "media_url": "https://video.twimg.com/tweet_video/HWVKFMFboAApgRC.mp4",
        "media_poster_url": "https://pbs.twimg.com/tweet_video_thumb/HWVKFMFboAApgRC.jpg",
        "media_kind": "mp4",
        "media_storage": "external",
        "media_rights": "unknown_link_only",
        "prompt_source_url": "https://x.com/op7418/status/2118181972451438662",
        "reference_image_url": "https://pbs.twimg.com/media/HWVLQtIbQAA3Tsr.jpg",
        "reference_image_url_2": "https://pbs.twimg.com/media/HWVLQtDbIAAvaGI.jpg",
    },
    {
        "id": "x-nonieengel-reactions",
        "title_zh": "角色+画风 → 10 张反应套装",
        "title_en": "10-Reaction Set From Two References",
        "category": "表情梗图",
        "emoji": "🎭",
        "origin": "community",
        "source_url": "https://x.com/nonieengel/status/2118382251226562570",
        "source_label": "Leonie Engel @nonieengel · 作者声明 Images 2.6（引用官方发布帖）· X API animated_gif · HEAD video/mp4 · 未视觉复核",
        "model": "ChatGPT Images 2.6（作者声明；本仓未复测）",
        "frames": 16,
        "frame_duration_ms": 200,
        "frames_basis": "editorial_recommendation",
        "aspect": "1:1",
        "priority": "P1",
        "description_zh": "一张角色照 + 一张风格参考，一次出 8 个固定情境 + 2 个按图发明的反应 GIF，并要求 5×2 总览。完整英文提示词在回复帖（主帖 API 截断）。作者附件 1280×512，符合总览条的比例，但对外是 MP4 不是 .gif。提示词写约 4 秒；16 帧是本站按接口上限估的建议，不是观看计数。未观看、未复测。",
        "prompt": NONIE_PROMPT,
        "prompt_adaptation": NONIE_ADAPT,
        "prompt_status": "verbatim",
        "output_kind": "gif",
        "evidence_date": "2026-11-05",
        "tags": ["reaction-set", "two-references", "captions", "x-mp4"],
        "preview": "",
        "preview_kind": "link_only",
        "tested_here": False,
        "generation_verified": False,
        "author_model_claim_status": "author_explicit",
        "media_metadata_status": "x_api_and_head_checked",
        "visual_review_status": "unwatched",
        "example_is_image26": True,
        "media_id": "x-nonieengel-gallery-mp4",
        "media_url": "https://video.twimg.com/tweet_video/HWYBYc2agAAlsk4.mp4",
        "media_poster_url": "https://pbs.twimg.com/tweet_video_thumb/HWYBYc2agAAlsk4.jpg",
        "media_kind": "mp4",
        "media_storage": "external",
        "media_rights": "unknown_link_only",
        "prompt_source_url": "https://x.com/nonieengel/status/2118382274270187877",
    },
    {
        "id": "x-supertask-arch-timelapse",
        "title_zh": "建筑透视日落后退",
        "title_en": "Architecture Sunset Timelapse",
        "category": "照片微动效",
        "emoji": "🌇",
        "origin": "community",
        "source_url": "https://x.com/supertask_jp/status/2118241124133532077",
        "source_label": "Tasuku Takahashi @supertask_jp · 作者声明 GPT Image 2.6 · X API animated_gif · HEAD video/mp4 · 未视觉复核",
        "model": "ChatGPT Images 2.6（作者声明；本仓未复测）",
        "frames": 12,
        "frame_duration_ms": 200,
        "frames_basis": "editorial_recommendation",
        "aspect": "3:2",
        "priority": "P2",
        "description_zh": "建筑透视，不是表情包：一句话把静帧做成「太阳慢慢落下」的延时 GIF。与挥手/蒸汽/贴纸玩法不重复。原文很短。X 标 GIF，HEAD 为 video/mp4。未观看、未复测。12 帧是玩法建议。",
        "prompt": "タイムラプスでゆっくり日が変わるような感じのGIFにして",
        "prompt_adaptation": "把这张建筑透视图做成循环 GIF：光线像延时摄影一样慢慢从白天转到黄昏，建筑形体、构图和镜头锁死，不要加人。（本站补了锁镜头约束。）建议 12 帧。本仓未观看作者附件。",
        "prompt_status": "verbatim",
        "output_kind": "gif",
        "evidence_date": "2026-11-05",
        "tags": ["architecture", "timelapse", "photo-to-gif", "x-mp4"],
        "preview": "",
        "preview_kind": "link_only",
        "tested_here": False,
        "generation_verified": False,
        "author_model_claim_status": "author_explicit",
        "media_metadata_status": "x_api_and_head_checked",
        "visual_review_status": "unwatched",
        "example_is_image26": True,
        "media_id": "x-supertask-sunset-mp4",
        "media_url": "https://video.twimg.com/tweet_video/HWWBD7GagAA0Hvu.mp4",
        "media_poster_url": "https://pbs.twimg.com/tweet_video_thumb/HWWBD7GagAA0Hvu.jpg",
        "media_kind": "mp4",
        "media_storage": "external",
        "media_rights": "unknown_link_only",
        "reference_image_url": "https://pbs.twimg.com/media/HWWBDHebsAAhSPa.jpg",
    },
]


def mp4_item(**kwargs):
    base = {
        "storage": "external",
        "media_kind": "mp4",
        "rights": "unknown_link_only",
        "content_type": "video/mp4",
        "x_declared_type": "animated_gif",
        "visual_review_status": "unwatched",
        "probe_method": "x_api_type+HEAD",
        "original_gif_available": False,
        "generation_verified": False,
        "probed_at": "2026-11-05",
        "local_path": None,
        "n_frames": None,
        "duration_ms": None,
        "sha256": None,
        "notes": "X labels this animated_gif; HEAD Content-Type is video/mp4. Not watched, not decoded, not a .gif.",
    }
    base.update(kwargs)
    return base


NEW_MEDIA = [
    mp4_item(
        id="x-mirai-32f-mp4",
        idea_ids=["x-mirai-spec-gif"],
        playbook_role="related_sample",
        url="https://video.twimg.com/tweet_video/HWVoIMqasAAR_VS.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWVoIMqasAAR_VS.jpg",
        bytes=46569,
        width=216,
        height=216,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Author: GPT Image 2.6 via ChatGPT chat; 32-frame request → 217×217 reported. Not retested here.",
        creator="藍澤 ミライ (@mirai_ai2050)",
        source_page="https://x.com/mirai_ai2050/status/2118213713761292432",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
    ),
    mp4_item(
        id="x-mirai-16f-mp4",
        idea_ids=["x-mirai-spec-gif"],
        playbook_role="primary",
        url="https://video.twimg.com/tweet_video/HWVoI72bsAAOx_0.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWVoI72bsAAOx_0.jpg",
        bytes=71937,
        width=266,
        height=358,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Author: GPT Image 2.6; 16-frame request → 267×358 reported; 288×512 not honored. Not retested here.",
        creator="藍澤 ミライ (@mirai_ai2050)",
        source_page="https://x.com/mirai_ai2050/status/2118213713761292432",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
    ),
    mp4_item(
        id="x-miramusic-stretch-mp4",
        idea_ids=["x-miramusic-stretch"],
        playbook_role="primary",
        url="https://video.twimg.com/tweet_video/HWU-HlkagAEV0iO.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWU-HlkagAEV0iO.jpg",
        bytes=68018,
        width=512,
        height=512,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Author post starts with GPTimage2.6. Not retested here.",
        creator="MiraMusic (@MiraMusic_AI)",
        source_page="https://x.com/MiraMusic_AI/status/2118168013618987298",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        still_url="https://pbs.twimg.com/media/HWU-kOfakAAFXuX.jpg",
    ),
    mp4_item(
        id="x-gorden-sun-rice-mp4",
        idea_ids=["x-gorden-sun-rice"],
        playbook_role="primary",
        url="https://video.twimg.com/tweet_video/HWU8ujEbsAEYOxw.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWU8ujEbsAEYOxw.jpg",
        bytes=89025,
        width=508,
        height=508,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Author: GPT Image 2.6. Not retested here.",
        creator="Gorden Sun (@Gorden_Sun)",
        source_page="https://x.com/Gorden_Sun/status/2118166046175908016",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        still_url="https://pbs.twimg.com/media/HWU8w0Wa8AAb9LS.jpg",
    ),
    mp4_item(
        id="x-op7418-fatfish-a-mp4",
        idea_ids=["x-op7418-fatfish"],
        playbook_role="primary",
        url="https://video.twimg.com/tweet_video/HWVKFMFboAApgRC.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWVKFMFboAApgRC.jpg",
        bytes=58278,
        width=414,
        height=408,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Author: GPT-image-2.6. Four attachments = one playbook. Not retested here.",
        creator="歸藏 (@op7418)",
        source_page="https://x.com/op7418/status/2118181775688241456",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
    ),
    mp4_item(
        id="x-op7418-fatfish-b-mp4",
        idea_ids=["x-op7418-fatfish"],
        playbook_role="related_sample",
        url="https://video.twimg.com/tweet_video/HWVKFMMbIAA4Geo.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWVKFMMbIAA4Geo.jpg",
        bytes=35369,
        width=306,
        height=308,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Same op7418 thread; not a second playbook.",
        creator="歸藏 (@op7418)",
        source_page="https://x.com/op7418/status/2118181775688241456",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
    ),
    mp4_item(
        id="x-op7418-fatfish-c-mp4",
        idea_ids=["x-op7418-fatfish"],
        playbook_role="related_sample",
        url="https://video.twimg.com/tweet_video/HWVKFMIb0AA2teV.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWVKFMIb0AA2teV.jpg",
        bytes=71552,
        width=358,
        height=352,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Same op7418 thread; not a second playbook.",
        creator="歸藏 (@op7418)",
        source_page="https://x.com/op7418/status/2118181775688241456",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
    ),
    mp4_item(
        id="x-op7418-fatfish-d-mp4",
        idea_ids=["x-op7418-fatfish"],
        playbook_role="related_sample",
        url="https://video.twimg.com/tweet_video/HWVKFMHawAEA-lR.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWVKFMHawAEA-lR.jpg",
        bytes=61325,
        width=308,
        height=304,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Same op7418 thread; not a second playbook.",
        creator="歸藏 (@op7418)",
        source_page="https://x.com/op7418/status/2118181775688241456",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
    ),
    mp4_item(
        id="x-nonieengel-gallery-mp4",
        idea_ids=["x-nonieengel-reactions"],
        playbook_role="primary",
        url="https://video.twimg.com/tweet_video/HWYBYc2agAAlsk4.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWYBYc2agAAlsk4.jpg",
        bytes=242248,
        width=1280,
        height=512,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Author quotes OpenAI Images 2.6 launch; 10-GIF set. Not retested here.",
        creator="Leonie Engel (@nonieengel)",
        source_page="https://x.com/nonieengel/status/2118382251226562570",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
    ),
    mp4_item(
        id="x-supertask-sunset-mp4",
        idea_ids=["x-supertask-arch-timelapse"],
        playbook_role="primary",
        url="https://video.twimg.com/tweet_video/HWWBD7GagAA0Hvu.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWWBD7GagAA0Hvu.jpg",
        bytes=88805,
        width=506,
        height=336,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Author: GPT Image 2.6. Not retested here.",
        creator="Tasuku Takahashi (@supertask_jp)",
        source_page="https://x.com/supertask_jp/status/2118241124133532077",
        source_label="X animated_gif → MP4 (unwatched)",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        still_url="https://pbs.twimg.com/media/HWWBDHebsAAhSPa.jpg",
    ),
    mp4_item(
        id="x-abc123-static-to-gif-mp4",
        idea_ids=["x-op7418-fatfish"],
        playbook_role="related_sample",
        url="https://video.twimg.com/tweet_video/HWVQJEiaUAAY0Cm.mp4",
        poster_url="https://pbs.twimg.com/tweet_video_thumb/HWVQJEiaUAAY0Cm.jpg",
        bytes=68077,
        width=358,
        height=538,
        model="ChatGPT Images 2.6 (author claim)",
        model_claim="Author: GPT-image-2.6 static-to-GIF sticker; grouped under fatfish, not a new playbook.",
        creator="A1terE&o (@abc123953468547)",
        source_page="https://x.com/abc123953468547/status/2118188053793837265",
        source_label="X animated_gif → MP4 (unwatched); related sticker-from-still",
        prompt_status="verbatim",
        author_model_claim_status="author_explicit",
        media_metadata_status="x_api_and_head_checked",
        notes="Related sample only. Prompt is a generic static-to-loop sticker; do not open a sixth overlapping playbook. Not watched.",
    ),
]

PENDING = [
    {
        "id": "x-chaoranya-orange-cat",
        "url": "https://x.com/chaoranya/status/2118391093633159437",
        "reason": "Author says screenshots were assembled by Grok and generation was not retested; media is amplify video, not animated_gif.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-batzdu-demo-gif",
        "url": "https://x.com/batzdu/status/2118142933924827638",
        "reason": "Quote-only, no prompt, weak model claim.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-aidan-clark-gif",
        "url": "https://x.com/_aidan_clark_/status/2118180063804105025",
        "reason": "Quote-only; identity is not a technical confirmation.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-andrew-mayne-checks-out",
        "url": "https://x.com/AndrewMayne/status/2118137348307485048",
        "reason": "Quote-only, no prompt.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-bt21-ok-flask-light",
        "url": "https://x.com/bt21_ok/status/2118391303872639364",
        "reason": "Korean OC; model name is clearer on a parent post; no copyable prompt.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-hackdeacon-test",
        "url": "https://x.com/hackdeacon/status/2118396692500537383",
        "reason": "Short test post, no prompt.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-jiaojiaojio-fora",
        "url": "https://x.com/jiaojiaojio/status/2118391023911289212",
        "reason": "No prompt; ordinary sticker demo.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-web30708-wechat-listing",
        "url": "https://x.com/web30708/status/2118338310649385317",
        "reason": "Store screenshots only; no playable GIF in the post.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-halozhangyu-fatfish-9",
        "url": "https://x.com/halozhangyu/status/2118327841410408546",
        "reason": "Fatfish clone / reseller; not a new playbook.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-youart-platform-video",
        "url": "https://x.com/YouArtStudio/status/2118391856799056265",
        "reason": "Platform promo video, not a native GIF result.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-antseed-demo-video",
        "url": "https://x.com/AntSeed/status/2118396169336275186",
        "reason": "Promo clip quoting the launch post.",
        "bucket": "pending_verification",
    },
    {
        "id": "x-iskunzhenbai-fatfish-reply",
        "url": "https://x.com/iskunzhenbai/status/2118239397766484445",
        "reason": "Reply inside the op7418 thread; related derivative, not a new playbook.",
        "bucket": "pending_verification",
    },
]


def main() -> None:
    ideas = json.loads(IDEAS.read_text(encoding="utf-8"))
    by_id = {x["id"]: x for x in ideas}
    added = []
    for idea in NEW_IDEAS:
        if idea["id"] in by_id:
            by_id[idea["id"]].update(idea)
        else:
            ideas.append(idea)
            added.append(idea["id"])
    krouxzz = by_id.get("krouxzz-wave-ref")
    if krouxzz:
        krouxzz.setdefault("author_model_claim_status", "author_explicit")
        krouxzz.setdefault("media_metadata_status", "x_api_and_head_checked")
        krouxzz.setdefault("visual_review_status", "unwatched")
        krouxzz.setdefault("generation_verified", False)
        krouxzz.setdefault("frames_basis", "editorial_recommendation")
        krouxzz["media_poster_url"] = "https://pbs.twimg.com/tweet_video_thumb/HWWnk8IXsAE0aXq.jpg"
        krouxzz["source_label"] = "Max Goldstein @Krouxzz · 作者声明 2.6 · X API animated_gif · HEAD video/mp4 · 未视觉复核"
        krouxzz["description_zh"] = (
            "最短参考图挥手句。X 把附件标成 GIF，HEAD Content-Type 是 video/mp4。"
            "作者声明走 2.6。本仓未把附件当 GIF 观看；不入库、不称为已拿到 .gif。"
        )

    IDEAS.write_text(json.dumps(ideas, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    items = manifest.setdefault("items", [])
    item_ids = {x["id"] for x in items}
    for row in NEW_MEDIA:
        if row["id"] in item_ids:
            for i, old in enumerate(items):
                if old["id"] == row["id"]:
                    items[i] = row
                    break
        else:
            items.append(row)
            item_ids.add(row["id"])

    review = manifest.setdefault("independent_review", {})
    review["x_scout_report"] = (
        "X catalog claimed 25 author-explicit groups / 42 dynamic media / 11 with prompts. "
        "Thread groups ≠ 25 playbooks. Independently re-fetched priority posts; HEAD is video/mp4."
    )
    review["accepted_x_playbooks"] = [x["id"] for x in NEW_IDEAS]
    review["x_grouped_not_new_playbooks"] = [
        "op7418 four MP4s = 1 template",
        "abc123 static-to-gif related to fatfish",
        "iskunzhenbai reply stays pending/related",
        "thinkszyg paper boat overlaps ravivit-paper-boat",
        "okan_aitool / IHayato overlap krouxzz/mirai blink-wave",
    ]
    review["x_pending_not_confirmed"] = [x["id"] for x in PENDING]
    review["x_visual_review"] = "unwatched: API type + HEAD only; no ffprobe/decode on this pass"
    manifest["pending"] = PENDING
    manifest["policy"] = (
        "MIT covers code only. No third-party GIF/video bytes were copied into git. "
        "X animated_gif usually delivers video/mp4; do not call those files GIFs. "
        "Unwatched X media stay out of the GIF gallery. Pending candidates are not confirmed 2.6 works."
    )
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("ideas", len(ideas), "added", added)
    print("media", len(items), "pending", len(PENDING))


if __name__ == "__main__":
    main()
