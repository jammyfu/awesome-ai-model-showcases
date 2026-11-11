#!/usr/bin/env python3
"""Apply independently verified link-only GPT Image 2.6 media to catalog JSON.

Does not download third-party bytes into git. Morphic examples stay prompt-only.
"""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBED = "2026-11-05"

# Independently Pillow-probed. Report counts are not treated as authority.
OFFICIAL_LANTERN = {
    "id": "openai-lantern-monkey-gif",
    "url": "https://developers.openai.com/images/platform/guides/image-prompting/monkey-lantern-gpt-image-2-6-sunburst.gif",
    "content_type": "image/gif",
    "sha256": "5d786a550b93a24fed3aec36725eab00f767cb4aa84985027004e40eb6c61f52",
    "bytes": 1280950,
    "n_frames": 9,
    "duration_ms": 1800,
    "width": 512,
    "height": 512,
    "model": "Sunburst",
    "model_claim": "OpenAI image-prompting docs: gpt-image-2.6-sunburst, 9×200 ms, 512²",
    "creator": "OpenAI",
    "source_page": "https://developers.openai.com/api/docs/guides/image-prompting",
    "source_label": "OpenAI 官方提示词指南",
    "prompt_status": "verbatim",
    "idea_ids": ["lantern-monkey-gif"],
    "gallery_id": "openai-lantern-monkey",
    "playbook_role": "fill",
}

LIGHTLYN_PRODUCT = {
    "id": "lightlyn-earbuds-product-gif",
    "url": "https://image.lightlyn.com/examples/gpt-image-2-6/gif-product.gif",
    "content_type": "image/gif",
    "sha256": "1908d92f1ff3431b26c244b2e4a9023592b1a3652a4822a15c645d1d49b9931c",
    "bytes": 2221707,
    "n_frames": 9,
    "duration_ms": 1800,
    "width": 960,
    "height": 960,
    "model": "Sunburst",
    "model_claim": "Lightlyn page: Product (2.6 Sunburst, 38.6 s)",
    "creator": "Linger / Lightlyn",
    "source_page": "https://image.lightlyn.com/gpt-image-2-6?lang=en",
    "source_label": "Lightlyn 公开实测（Linger · 2026-11-05）",
    "prompt_status": "verbatim",
    "idea_ids": ["earbuds-product"],
    "gallery_id": "lightlyn-earbuds-product",
    "playbook_role": "fill",
}

LIGHTLYN_STEAM = {
    "id": "lightlyn-latte-steam-gif",
    "url": "https://image.lightlyn.com/examples/gpt-image-2-6/gif-photo.gif",
    "content_type": "image/gif",
    "sha256": "b09ad209bf2d04bccdbba9d836e63e80444dcb99769858574f7377675daa394e",
    "bytes": 2727700,
    "n_frames": 9,
    "duration_ms": 1800,
    "width": 1152,
    "height": 768,
    "model": "Flare",
    "model_claim": "Lightlyn page: Photo (2.6 Flare, uploaded photo, 22.8 s, 1152×768)",
    "creator": "Linger / Lightlyn",
    "source_page": "https://image.lightlyn.com/gpt-image-2-6?lang=en",
    "source_label": "Lightlyn 公开实测（Linger · 2026-11-05）",
    "prompt_status": "verbatim",
    "idea_ids": ["photo-to-gif-steam"],
    "gallery_id": "lightlyn-latte-steam",
    "playbook_role": "fill",
}

VEEVID_PERFUME = {
    "id": "veevid-perfume-loop-gif",
    "url": "https://cdn.veevid.ai/gpt-image-2-6-samples/blog/gif-perfume-loop.gif",
    "content_type": "image/gif",
    "sha256": "ff47327095bd335f65ca7c49cf671ca8ba9700b5f434d5a44054826d8f4da4e1",
    "bytes": 1034983,
    "n_frames": 9,
    "duration_ms": 1800,
    "width": 512,
    "height": 512,
    "model": "Flare",
    "model_claim": "Veevid blog: product loop we ran on Flare",
    "creator": "Veevid Team",
    "source_page": "https://veevid.ai/blog/gpt-image-2-6-gif",
    "source_label": "Veevid 公开实测（2026-11-05）",
    "prompt_status": "verbatim",
    "idea_ids": ["perfume-light"],
    "gallery_id": "veevid-perfume-loop",
    "playbook_role": "fill",
}

REDDIT_NOD = {
    "id": "reddit-anime-nod-gif",
    "url": "https://i.redd.it/smnyo808cszh1.gif",
    "content_type": "image/gif",
    "sha256": "6eafc6274f28973d2c76a1ac09ffa1ca73b5f80a8b4119872de39108610d01da",
    "bytes": 497626,
    "n_frames": 9,
    "duration_ms": 1620,
    "width": 390,
    "height": 437,
    "model": "Sunburst",
    "model_claim": "r/OpenAI post titled as Image 2.6 GIF feature; Reddit JSON 403 this pass so author handle and prompt text were not independently re-read",
    "creator": "r/OpenAI post author (handle not recovered this pass)",
    "source_page": "https://www.reddit.com/r/OpenAI/comments/1xoh2u0/i_tried_the_new_image_26_gif_feature/",
    "source_label": "社区公开案例（Reddit r/OpenAI）",
    "prompt_status": "reconstructed",
    "idea_ids": ["anime-nod"],
    "gallery_id": "reddit-anime-nod",
    "playbook_role": "fill",
}

PAPER_BOAT = {
    "id": "ravivit-paper-boat-gif",
    "url": "https://static.atlascloud.ai/uploads/03_paper_boat_2_6_c19a8b768b.gif",
    "content_type": "image/gif",
    "sha256": "b0d99d9e487f6356388f5a07d4a492d169e17a768c4236c205c2f30dddb30a0b",
    "bytes": 1811479,
    "n_frames": 16,
    "duration_ms": 1920,
    "width": 512,
    "height": 512,
    "model": "Images 2.6 API",
    "model_claim": "Ravivit note 2026-11-05: API 生成、16コマ・120ms。Atlas hosts the inspected file and calls it an Images 2.6 API result. Flare vs Sunburst not named for this GIF.",
    "creator": "ラビビット | AI活用メディア（Ravivit）",
    "source_page": "https://note.com/ravivit_ai/n/nb8f40b5a21b9",
    "source_label": "ラビビット | AI活用メディア · note（2026-11-05）",
    "prompt_status": "verbatim",
    "idea_ids": ["ravivit-paper-boat"],
    "gallery_id": "ravivit-paper-boat",
    "playbook_role": "new_playbook",
    "host_page": "https://www.atlascloud.ai/blog/tips/gpt-image-2.6-image-to-gif",
}

# Same playbook class as existing cards — gallery samples, not extra idea cards.
RELATED_SAMPLES = [
    {
        "id": "lightlyn-cat-lantern-mascot-gif",
        "url": "https://image.lightlyn.com/examples/gpt-image-2-6/gif-mascot.gif",
        "content_type": "image/gif",
        "sha256": "a0ff5ff5bf98f6b097f302cbf569dc0ee5146a76b1bae3044db339a6fb36d15e",
        "bytes": 1802355,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 960,
        "height": 960,
        "model": "Flare",
        "model_claim": "Lightlyn: Mascot (2.6 Flare, 20.9 s)",
        "creator": "Linger / Lightlyn",
        "source_page": "https://image.lightlyn.com/gpt-image-2-6?lang=en",
        "source_label": "Lightlyn 公开实测（Linger · 2026-11-05）",
        "prompt_status": "verbatim",
        "idea_ids": ["luffy-otter-wave-gif"],
        "gallery_id": "lightlyn-cat-lantern-mascot",
        "playbook_role": "related_sample",
        "related_playbook": "mascot-wave",
        "prompt": "A cheerful round orange cat mascot with a tiny lantern, waving hello and blinking, soft flat illustration style, clean pastel background, gentle seamless loop.",
        "title": "提灯橘猫挥手 / Lightlyn Cat Mascot",
        "description": "Lightlyn 2.6 Flare mascot wave. Same playbook class as other wave loops, not a new idea card.",
        "description_zh": "Lightlyn 2.6 Flare 吉祥物挥手样本，与水獭挥手同属一类玩法，不另开卡。",
        "category": "Mascots",
        "tags": ["mascot", "wave", "cat", "lightlyn", "related-sample"],
    },
    {
        "id": "veevid-cactus-mascot-gif",
        "url": "https://cdn.veevid.ai/gpt-image-2-6-samples/blog/gif-cactus-mascot-v2.gif",
        "content_type": "image/gif",
        "sha256": "fbdd5fd94e508d58079205c11351825561fb840b3b614d1323883f68a1ca56a4",
        "bytes": 520796,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 512,
        "height": 512,
        "model": "Flare",
        "model_claim": "Veevid: sequenced cactus wave run once on Flare",
        "creator": "Veevid Team",
        "source_page": "https://veevid.ai/blog/gpt-image-2-6-gif",
        "source_label": "Veevid 公开实测（2026-11-05）",
        "prompt_status": "verbatim",
        "idea_ids": ["luffy-otter-wave-gif"],
        "gallery_id": "veevid-cactus-mascot",
        "playbook_role": "related_sample",
        "related_playbook": "mascot-wave",
        "prompt": "Create a single animation sprite sheet for a seamless looping GIF. A cheerful cartoon cactus mascot in a small terracotta pot. The sequence: the cactus leans slightly left, raises one arm and waves, smiles and blinks, then leans back to center. Fixed front camera, same character, same pot, plain pastel peach background. Clear incremental arm and body motion; the last frame transitions smoothly back to the first. Flat vector sticker style, thick outline. No captions, no words, no logos, no borders, no gutters.",
        "title": "仙人掌挥手 / Veevid Cactus",
        "description": "Veevid cactus wave. Related mascot-wave sample, not a separate playbook.",
        "description_zh": "Veevid 仙人掌挥手，归入吉祥物挥手样本，不另开玩法卡。",
        "category": "Mascots",
        "tags": ["mascot", "wave", "cactus", "veevid", "related-sample"],
    },
    {
        "id": "veevid-fox-mascot-gif",
        "url": "https://cdn.veevid.ai/gpt-image-2-6-samples/gif-fox.gif",
        "content_type": "image/gif",
        "sha256": "b8acb434d70a2b6648d78574259bba3ad58290e5455a79f7155bbabaafa51852",
        "bytes": 590659,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 512,
        "height": 512,
        "model": "Flare",
        "model_claim": "Veevid: example generated on Veevid with this prompt",
        "creator": "Veevid Team",
        "source_page": "https://veevid.ai/blog/gpt-image-2-6-gif",
        "source_label": "Veevid 公开实测（2026-11-05）",
        "prompt_status": "verbatim",
        "idea_ids": ["luffy-otter-wave-gif"],
        "gallery_id": "veevid-fox-mascot",
        "playbook_role": "related_sample",
        "related_playbook": "mascot-wave",
        "prompt": "A cute orange fox brand mascot waving hello and blinking, flat vector sticker style, thick outline, pastel background, seamless loop",
        "title": "狐狸吉祥物 / Veevid Fox Wave",
        "description": "Veevid fox mascot wave. Distinct hash from the Lightlyn cat; same playbook class.",
        "description_zh": "Veevid 狐狸挥手。与橘猫哈希不同，仍属吉祥物挥手，不另开卡。",
        "category": "Mascots",
        "tags": ["mascot", "wave", "fox", "veevid", "related-sample"],
    },
    {
        "id": "veevid-coffee-loop-gif",
        "url": "https://cdn.veevid.ai/gpt-image-2-6-samples/gif-coffee.gif",
        "content_type": "image/gif",
        "sha256": "097fd00add8edf39e087bde10a5585ba4a7ae0422094391e9f77fd6b3a253475",
        "bytes": 1195270,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 512,
        "height": 512,
        "model": "Flare",
        "model_claim": "Veevid text-to-GIF coffee steam example",
        "creator": "Veevid Team",
        "source_page": "https://veevid.ai/blog/gpt-image-2-6-gif",
        "source_label": "Veevid 公开实测（2026-11-05）",
        "prompt_status": "verbatim",
        "idea_ids": ["photo-to-gif-steam"],
        "gallery_id": "veevid-coffee-loop",
        "playbook_role": "related_sample",
        "related_playbook": "steam-loop",
        "prompt": "A steaming ceramic coffee cup with heart latte art on a wooden cafe table, soft steam curling upward, warm morning window light, seamless loop",
        "title": "文生咖啡蒸汽 / Veevid Coffee",
        "description": "Text-to-GIF steam. Distinct hash from Lightlyn's photo-to-GIF latte; same steam playbook.",
        "description_zh": "Veevid 文生蒸汽。与 Lightlyn 实拍拿铁不是同一文件，不另开蒸汽玩法。",
        "category": "Photo",
        "tags": ["coffee", "steam", "text-to-gif", "veevid", "related-sample"],
    },
    {
        "id": "veevid-dog-wag-gif",
        "url": "https://cdn.veevid.ai/gpt-image-2-6-samples/gif-dog-edit.gif",
        "content_type": "image/gif",
        "sha256": "8e66f90cb4507e8140a32a4352853497ada2297b5f9b7e07db77bceac38e7d00",
        "bytes": 1617115,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 512,
        "height": 512,
        "model": "Flare",
        "model_claim": "Veevid image-to-GIF from a still of a dog",
        "creator": "Veevid Team",
        "source_page": "https://veevid.ai/blog/gpt-image-2-6-gif",
        "source_label": "Veevid 公开实测（2026-11-05）",
        "prompt_status": "verbatim",
        "idea_ids": ["photo-to-gif-steam"],
        "gallery_id": "veevid-dog-wag",
        "playbook_role": "related_sample",
        "related_playbook": "photo-to-gif",
        "prompt": "Animate this: the dog wags its tail and blinks, gentle loop",
        "title": "狗狗摇尾巴 / Veevid Dog Wag",
        "description": "Photo-to-GIF related sample. Not a new playbook beside Lightlyn steam.",
        "description_zh": "图生 GIF 样本：摇尾眨眼。归入照片微动，不另开卡。",
        "category": "Photo",
        "tags": ["dog", "photo-to-gif", "veevid", "related-sample"],
    },
    {
        "id": "veevid-robot-sketch-gif",
        "url": "https://cdn.veevid.ai/gpt-image-2-6-samples/blog/gif-robot-sketch.gif",
        "content_type": "image/gif",
        "sha256": "194af8a7e1be6120ed6f68c4147d2e7b1f9caf6a6346ee60f3f8210e3606680e",
        "bytes": 855668,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 512,
        "height": 512,
        "model": "Flare",
        "model_claim": "Veevid: sketch-to-GIF; doodle disclosed as 2.6-generated stand-in",
        "creator": "Veevid Team",
        "source_page": "https://veevid.ai/blog/gpt-image-2-6-gif",
        "source_label": "Veevid 公开实测（2026-11-05）",
        "prompt_status": "verbatim",
        "idea_ids": ["sketch-owl"],
        "gallery_id": "veevid-robot-sketch",
        "playbook_role": "related_sample",
        "related_playbook": "sketch-to-gif",
        "prompt": "Animate this sketch: the little robot waves one arm and its antenna bobs up and down. Keep the hand-drawn black ink lines and the plain white paper. Fixed camera, same character in every frame, seamless loop. No text, no borders.",
        "title": "墨线机器人 / Veevid Sketch Robot",
        "description": "Real 2.6 GIF for sketch-to-motion. Official owl launch clip is Vimeo, not this file.",
        "description_zh": "草图变 GIF 的 2.6 真文件。官方猫头鹰演示是视频，不是本 GIF。",
        "category": "Sketch",
        "tags": ["sketch", "robot", "veevid", "related-sample"],
    },
]

SOGNI_EXTRAS = [
    {
        "id": "sogni-jellyfish-gif",
        "url": "https://www.sogni.ai/models/samples/gpt-image-2-6/jellyfish-98965a0f9a82.gif",
        "content_type": "image/gif",
        "sha256": "98965a0f9a820ac2a695fea441ddd66ee96746b0485182f8384b4c4bef7b67e8",
        "bytes": 2359657,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 896,
        "height": 896,
        "model": "Flare",
        "model_claim": "Sogni model page sample: Jellyfish pulse · Flare. Prompt unpublished.",
        "creator": "Sogni",
        "source_page": "https://www.sogni.ai/models/gpt-image-2-6",
        "source_label": "Sogni GPT Image 2.6 样品页",
        "prompt_status": "empty",
        "idea_ids": [],
        "gallery_id": "sogni-jellyfish-pulse",
        "playbook_role": "independent_extra",
        "prompt": "",
        "title": "水母脉冲 / Sogni Jellyfish",
        "description": "Sogni 2.6 Flare sample. Prompt not published. Not a new idea card.",
        "description_zh": "独立核到的 Sogni 2.6 样品，提示词未公开，只进画廊。",
        "category": "Effects",
        "tags": ["jellyfish", "sogni", "external"],
    },
    {
        "id": "sogni-lantern-monkey-gif",
        "url": "https://www.sogni.ai/models/samples/gpt-image-2-6/lantern.gif",
        "content_type": "image/gif",
        "sha256": "2048efc145e0d9f5560d7706f4b29580332679cb37d657ba847e02fede812d5f",
        "bytes": 3349096,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 896,
        "height": 896,
        "model": "Sunburst",
        "model_claim": "Sogni: Lantern lift · Sunburst. Different sha256 from the official docs GIF.",
        "creator": "Sogni",
        "source_page": "https://www.sogni.ai/models/gpt-image-2-6",
        "source_label": "Sogni GPT Image 2.6 样品页",
        "prompt_status": "empty",
        "idea_ids": ["lantern-monkey-gif"],
        "gallery_id": "sogni-lantern-monkey",
        "playbook_role": "related_sample",
        "related_to": "openai-lantern-monkey-gif",
        "prompt": "",
        "title": "Sogni 提灯小猴 / Third-party re-run",
        "description": "Same playbook as the official lantern monkey; different file hash.",
        "description_zh": "官方提灯玩法的第三方重跑，哈希不同，不另开卡。",
        "category": "Official",
        "tags": ["lantern", "sogni", "related-sample"],
    },
    {
        "id": "sogni-origami-fox-gif",
        "url": "https://www.sogni.ai/models/samples/gpt-image-2-6/origami-83734f912c9a.gif",
        "content_type": "image/gif",
        "sha256": "83734f912c9af44704897f891093bc9168c60cc91b8ef5fc8e05d4c7e6ef68d2",
        "bytes": 2003887,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 896,
        "height": 896,
        "model": "Flare",
        "model_claim": "Sogni: Origami fox · Flare. Prompt unpublished.",
        "creator": "Sogni",
        "source_page": "https://www.sogni.ai/models/gpt-image-2-6",
        "source_label": "Sogni GPT Image 2.6 样品页",
        "prompt_status": "empty",
        "idea_ids": ["papercraft-koi"],
        "gallery_id": "sogni-origami-fox",
        "playbook_role": "related_sample",
        "prompt": "",
        "title": "折纸狐狸 / Sogni Origami Fox",
        "description": "Actual 2.6 GIF. Morphic papercraft koi is a 2.6-oriented prompt whose Morphic example ran on 2.5.",
        "description_zh": "2.6 折纸 GIF 样本。Morphic 锦鲤分镜示例跑在 2.5，不能当 2.6 成品。",
        "category": "Effects",
        "tags": ["origami", "sogni", "papercraft"],
    },
    {
        "id": "sogni-wordmark-orbit-gif",
        "url": "https://www.sogni.ai/models/samples/gpt-image-2-6/typography-747619aeabb2.gif",
        "content_type": "image/gif",
        "sha256": "747619aeabb2673ffde6264a09850586ae348ef19e99b8ee9134b53e64e14106",
        "bytes": 814838,
        "n_frames": 9,
        "duration_ms": 1800,
        "width": 896,
        "height": 896,
        "model": "Flare",
        "model_claim": "Sogni: SOGNI orbit · Flare. Publisher wordmark; prompt unpublished.",
        "creator": "Sogni",
        "source_page": "https://www.sogni.ai/models/gpt-image-2-6",
        "source_label": "Sogni GPT Image 2.6 样品页",
        "prompt_status": "empty",
        "idea_ids": ["neon-word-switch"],
        "gallery_id": "sogni-wordmark-orbit",
        "playbook_role": "related_sample",
        "prompt": "",
        "title": "SOGNI 字标光轨 / Wordmark Orbit",
        "description": "Sogni publisher wordmark sample. Keep Sogni as creator.",
        "description_zh": "Sogni 字标样品，作者是 Sogni。归入文字循环样本。",
        "category": "Typography",
        "tags": ["typography", "sogni"],
    },
]

LOCAL_GIFS = [
    ("local-pixel-head-pat", "pixel-head-pat", ["head-pat-meme"], "gifs/pixel-head-pat.gif", "66d61c9a53e1f7fdd2d4af8fe8feea68bd42db5ef79fd76f6b1dd035fa1a8ab7", 845183, 12, 2160, 267, 478),
    ("local-cat-screen-crack", "cat-screen-crack", ["cat-screen-crash"], "gifs/cat-screen-crack.gif", "82760b72d46e2cd21a31aaf311f4a6f24ad161c3ffed4905fa2c16e9677f02df", 1104065, 16, 1760, 273, 344),
    ("local-cat-headbutt", "cat-headbutt", [], "gifs/cat-headbutt.gif", "fcdac1bb6e45c42ebb84d042c01dffc6a2cea69cbe569a204556e5ee5f14104c", 1057018, 16, 1920, 276, 344),
    ("local-kangaroo-pat", "kangaroo-pat", [], "gifs/kangaroo-pat.gif", "00b786702e8721d4358deaf5e4c8424caa1474b78f4ef4c2e41002cd8c890bc8", 1017390, 12, 2160, 309, 412),
    ("local-martial-arts-combo", "martial-arts-combo", [], "gifs/martial-arts-combo.gif", "e9fed10bb5ebbc7265bc83ba4df0a14c5faa77731a2e29c7bf63caf7b0f0ba12", 650736, 16, 2080, 357, 264),
    ("local-head-pat-caption", "head-pat-caption", [], "gifs/head-pat-caption.gif", "b0e75b22809acab76c890485f739f929ca3741e4467751e796f05ef8992c6694", 830804, 12, 2160, 267, 478),
]

MORPHIC_IDS = {
    "baker-mascot-sprite": "GPT Image 2.5 Sunburst（Morphic FAQ：示例不是 2.6）",
    "papercraft-koi": "GPT Image 2.5 Sunburst（Morphic FAQ：示例不是 2.6）",
    "character-ref-sheet": "GPT Image 2.5 Sunburst（Morphic FAQ：示例不是 2.6）",
    "packaging-dieline": "GPT Image 2.5 Flare/Sunburst（Morphic FAQ：示例不是 2.6）",
    "labelled-bakery-cutaway": "GPT Image 2.5 Sunburst（Morphic FAQ：示例不是 2.6）",
    "winter-edition-edit": "GPT Image 2.5 Sunburst（Morphic FAQ：示例不是 2.6）",
    "autumn-bake-poster": "GPT Image 2.5 Flare/Sunburst（Morphic FAQ：示例不是 2.6）",
}

NEW_IDEA = {
    "id": "ravivit-paper-boat",
    "title_zh": "白纸船水面轻摇",
    "title_en": "Paper Boat Rocking Loop",
    "category": "创意特效",
    "emoji": "⛵",
    "origin": "tested",
    "source_url": "https://note.com/ravivit_ai/n/nb8f40b5a21b9",
    "source_label": "ラビビット | AI活用メディア · note（2026-11-05）",
    "model": "Images 2.6 API",
    "frames": 16,
    "frame_duration_ms": 120,
    "aspect": "1:1",
    "priority": "P1",
    "description_zh": "Ravivit 用 Images 2.6 API 生成的 16 帧×120ms 真 GIF：白纸船在水面左右轻摇、镜头锁死。Atlas 检视托管同一文件，并写明同页粘土机器人/茶杯循环是更早工作流、不是 2.6。动图只外链。",
    "prompt": "白い紙の船が水面でゆっくり左右に揺れる。カメラは固定。短いループGIF。文字は入れない",
    "tags": ["paper-boat", "loop", "api", "ravivit", "gif"],
    "preview": "",
    "preview_kind": "external_gif",
    "tested_here": False,
    "prompt_status": "verbatim",
    "output_kind": "gif",
    "evidence_date": "2026-11-05",
    "example_is_image26": True,
    "media_id": "ravivit-paper-boat-gif",
    "media_url": PAPER_BOAT["url"],
    "media_kind": "gif",
    "media_storage": "external",
    "media_rights": "unknown_link_only",
}


def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def attach_gif(card, media, *, frames=None, duration_ms=None):
    card["media_id"] = media["id"]
    card["media_url"] = media["url"]
    card["media_kind"] = "gif"
    card["media_storage"] = "external"
    card["media_rights"] = "unknown_link_only"
    card["preview_kind"] = "external_gif"
    card["preview"] = ""
    card["example_is_image26"] = True
    n = frames if frames is not None else media["n_frames"]
    ms = duration_ms if duration_ms is not None else media["duration_ms"]
    card["frames"] = n
    card["frame_duration_ms"] = int(ms / n)
    card["source_label"] = media["source_label"]
    return card


def media_record(base, storage, media_kind="gif", rights=None, extra=None):
    item = deepcopy(base)
    item["storage"] = storage
    item["media_kind"] = media_kind
    item["rights"] = rights or ("repo_seed" if storage == "local" else "unknown_link_only")
    item["probed_at"] = PROBED
    if storage == "external":
        item["local_path"] = None
    if extra:
        item.update(extra)
    for key in ("title", "description", "description_zh", "category", "tags", "prompt"):
        item.pop(key, None)
    return item


def gallery_from_sample(sample, featured=False):
    return {
        "id": sample["gallery_id"],
        "title": sample["title"],
        "description": sample["description"],
        "description_zh": sample["description_zh"],
        "category": sample["category"],
        "tags": sample["tags"],
        "image": sample["url"],
        "prompt": sample.get("prompt", ""),
        "prompt_file": "",
        "prompt_status": sample["prompt_status"],
        "model": f"GPT Image 2.6 ({sample['model']})" if sample["model"] else "GPT Image 2.6",
        "frames": sample["n_frames"],
        "duration_ms": sample["duration_ms"],
        "width": sample["width"],
        "height": sample["height"],
        "source_note": "Link-only; no redistribution license found. Not mirrored.",
        "source_url": sample["source_page"],
        "creator": sample["creator"],
        "featured": featured,
        "storage": "external",
        "media_kind": "gif",
        "rights": "unknown_link_only",
        "media_id": sample["id"],
        "playbook_role": sample.get("playbook_role", "related_sample"),
    }


def main():
    ideas_path = ROOT / "docs/data/ideas.json"
    gallery_path = ROOT / "docs/data/gallery.json"
    ideas = json.loads(ideas_path.read_text(encoding="utf-8"))
    gallery = json.loads(gallery_path.read_text(encoding="utf-8"))
    by_id = {x["id"]: x for x in ideas}

    lantern = attach_gif(by_id["lantern-monkey-gif"], OFFICIAL_LANTERN)
    lantern["frames"] = 9
    lantern["frame_duration_ms"] = 200
    lantern["description_zh"] = (
        "官方文档真实 GIF（9×200 ms、512²、Sunburst）：小猴提灯、眨眼、放回。"
        "封面改为源站 GIF 外链，不再用 SVG 冒充生成结果。"
        "Sogni 另有哈希不同的第三方重跑。xianyu110 镜像与官方字节一致，不另收。"
    )

    earbuds = by_id["earbuds-product"]
    earbuds["prompt"] = (
        'A white wireless earbuds charging case labelled "LIGHTLYN" on a sage-green studio background: '
        "the lid opens, the two earbuds rise and float a little, then settle back and the lid closes. "
        "Clean product animation, seamless loop."
    )
    earbuds["prompt_status"] = "verbatim"
    earbuds["description_zh"] = (
        "Lightlyn 2.6 Sunburst 真实 GIF：盒盖开合、耳机浮起归位。提示词改回实测原文；只外链。"
    )
    attach_gif(earbuds, LIGHTLYN_PRODUCT)

    steam = by_id["photo-to-gif-steam"]
    steam["description_zh"] = (
        "Lightlyn 2.6 Flare 真实图生 GIF：杯子/桌子/窗户不动，只动蒸汽和光。"
        "Veevid 文生咖啡蒸汽、狗摇尾是同一「微动」玩法的样本，不另开蒸汽/摇尾卡。"
    )
    attach_gif(steam, LIGHTLYN_STEAM)

    perfume = by_id["perfume-light"]
    perfume["prompt"] = (
        "A frosted glass perfume bottle on a round stone pedestal. The sequence: a soft band of light "
        "sweeps slowly across the glass from left to right while tiny dust particles drift upward. "
        "Fixed camera, same bottle, same pedestal, warm beige studio background. The last frame "
        "transitions smoothly back to the first for a seamless loop. Clean product photography style. "
        "No captions, no words, no logos, no borders."
    )
    perfume["prompt_status"] = "verbatim"
    perfume["description_zh"] = "Veevid 2.6 Flare 真实 GIF：瓶子不动，高光扫过。提示词按博文原文；只外链。"
    attach_gif(perfume, VEEVID_PERFUME)

    nod = by_id["anime-nod"]
    nod["description_zh"] = (
        "Reddit 帖附带的可播放 GIF（9 帧·390×437）已核到。帖文 JSON 本轮 403，作者 handle 与原文提示词未能独立复核，"
        "因此提示词仍标 reconstructed，不把第三方报告里的长提示词当逐字原文。"
    )
    attach_gif(nod, REDDIT_NOD)
    nod["prompt_status"] = "reconstructed"

    otter = by_id["luffy-otter-wave-gif"]
    otter["related_media_ids"] = [
        "lightlyn-cat-lantern-mascot-gif",
        "veevid-cactus-mascot-gif",
        "veevid-fox-mascot-gif",
    ]
    otter["description_zh"] = (
        "路飞中文挥手玩法（逐字提示词）。封面仍为原创 SVG，不转载路飞 GIF。"
        "同玩法的 2.6 真 GIF 样本见画廊：Lightlyn 橘猫、Veevid 仙人掌/狐狸，不另开挥手卡。"
    )

    sketch = by_id["sketch-owl"]
    sketch["demo_kind"] = "vimeo"
    sketch["demo_url"] = "https://player.vimeo.com/video/1242957231?h=375195e1fb&muted=1&loop=1"
    sketch["related_media_ids"] = ["veevid-robot-sketch-gif"]
    sketch["example_is_image26"] = False
    sketch["description_zh"] = (
        "官方发布页猫头鹰演示是 Vimeo 视频，不是 GIF。封面 SVG 不是生成结果。"
        "可播放的 2.6 草图 GIF 见 Veevid 墨线机器人（另一份素材）。"
    )

    typing = by_id["typing-companion"]
    typing["demo_kind"] = "vimeo"
    typing["demo_url"] = "https://player.vimeo.com/video/1242966135?h=a954ad2081&muted=1&loop=1"
    typing["example_is_image26"] = False
    typing["description_zh"] = "官方 Town 助手演示是 Vimeo 视频，不是 GIF。没有可复制提示词；封面 SVG 不是生成结果。"

    sprite = by_id["sprite-sheet-stock-crash"]
    sprite["demo_kind"] = "vimeo"
    sprite["demo_url"] = "https://player.vimeo.com/video/1242918506?h=5b6824f867&muted=1&loop=1"
    sprite["example_is_image26"] = False
    sprite["description_zh"] = (
        "官方 3×2 分镜提示词仍逐字收录。发布页股市演示是 Vimeo 视频，不是 GIF。封面 SVG 不是生成结果。"
    )

    krouxzz = by_id["krouxzz-wave-ref"]
    krouxzz["media_id"] = "krouxzz-wave-mp4"
    krouxzz["media_url"] = "https://video.twimg.com/tweet_video/HWWnk8IXsAE0aXq.mp4"
    krouxzz["media_kind"] = "mp4"
    krouxzz["media_storage"] = "external"
    krouxzz["media_rights"] = "unknown_link_only"
    krouxzz["preview_kind"] = "link_only"
    krouxzz["preview"] = ""
    krouxzz["frames"] = 9
    krouxzz["frame_duration_ms"] = 180
    krouxzz["example_is_image26"] = True
    krouxzz["description_zh"] = (
        "最短参考图挥手句。X 把附件标成 GIF，实测 Content-Type 是 video/mp4（tweet_video，580×576，约 6.55 秒）。"
        "本页按 MP4 展示，不称为 GIF，也不入库。"
    )

    for idea_id, run_model in MORPHIC_IDS.items():
        card = by_id[idea_id]
        card["example_is_image26"] = False
        card["example_run_model"] = run_model
        card["source_label"] = "Morphic 公开提示词库（FAQ：示例不是 2.6，跑在 2.5 / Ideogram Vector）"
        card["preview_kind"] = "concept_illustration"
        extra = "Morphic 明示示例不是 ChatGPT Images 2.6（2.5 Flare/Sunburst 或 Ideogram Vector；Copilot 循环还用了 MiniMax 视频）。提示词面向 2.6 仍逐字收录；SVG 封面不是 2.6 成品，也不进入 2.6 GIF 画廊。"
        if extra not in card["description_zh"]:
            card["description_zh"] = card["description_zh"].rstrip("。") + "。" + extra

    steam["related_media_ids"] = ["veevid-coffee-loop-gif", "veevid-dog-wag-gif"]
    lantern["related_media_ids"] = ["sogni-lantern-monkey-gif"]
    koi = by_id["papercraft-koi"]
    koi["related_media_ids"] = ["sogni-origami-fox-gif"]

    for card in by_id.values():
        card.setdefault("example_is_image26", card["id"] not in MORPHIC_IDS)

    ideas = [by_id[x["id"]] for x in ideas]
    if NEW_IDEA["id"] not in by_id:
        ideas.append(NEW_IDEA)

    local_map = {row[1]: row[0] for row in LOCAL_GIFS}
    for item in gallery:
        item.setdefault("storage", "local")
        item.setdefault("media_kind", "gif")
        item.setdefault("rights", "repo_seed")
        item.setdefault("creator", "repository seed")
        item.setdefault(
            "source_url",
            f"https://github.com/jammyfu/awesome-ai-model-showcases/blob/main/docs/{item['image']}",
        )
        item["media_id"] = local_map[item["id"]]
        item["playbook_role"] = "local_seed"

    fills = [
        (OFFICIAL_LANTERN, "提灯小猴 / Official Lantern Monkey", "OpenAI docs 9-frame Sunburst GIF.", "官方文档 9 帧真 GIF。", "Official", ["official", "lantern", "sunburst"], True, lantern["prompt"]),
        (LIGHTLYN_PRODUCT, "耳机盒开合 / Lightlyn Earbuds", "Lightlyn 2.6 Sunburst product loop.", "Lightlyn 2.6 Sunburst 产品循环。", "Product", ["product", "earbuds", "lightlyn"], False, earbuds["prompt"]),
        (LIGHTLYN_STEAM, "拿铁蒸汽 / Lightlyn Photo Steam", "Lightlyn photo-to-GIF: only steam and light move.", "Lightlyn 图生 GIF，只动蒸汽。", "Photo", ["photo-to-gif", "steam", "lightlyn"], True, steam["prompt"]),
        (VEEVID_PERFUME, "香水高光 / Veevid Perfume", "Veevid Flare light sweep on a still bottle.", "Veevid 香水高光扫过。", "Product", ["product", "perfume", "veevid"], False, perfume["prompt"]),
        (REDDIT_NOD, "动漫点头 / Reddit Anime Nod", "Reddit Image 2.6 GIF thread sample. Prompt remains reconstructed.", "Reddit 点头 GIF。提示词未能独立复核，仍标改写。", "Community", ["anime", "nod", "reddit"], True, nod["prompt"]),
        (PAPER_BOAT, "白纸船 / Ravivit Paper Boat", "Ravivit Images 2.6 API GIF, 16×120 ms. Atlas hosts the copy; robot/teacup on that page are not 2.6.", "Ravivit API 16 帧真 GIF。Atlas 托管副本；同页机器人/茶杯不是 2.6。", "Effects", ["paper-boat", "ravivit", "api"], True, NEW_IDEA["prompt"]),
    ]
    extras = []
    for media, title, desc, desc_zh, cat, tags, featured, prompt in fills:
        extras.append(
            {
                "id": media["gallery_id"],
                "title": title,
                "description": desc,
                "description_zh": desc_zh,
                "category": cat,
                "tags": tags + ["external"],
                "image": media["url"],
                "prompt": prompt,
                "prompt_file": "",
                "prompt_status": media["prompt_status"],
                "model": f"GPT Image 2.6 ({media['model']})",
                "frames": media["n_frames"],
                "duration_ms": media["duration_ms"],
                "width": media["width"],
                "height": media["height"],
                "source_note": "Link-only; no redistribution license found.",
                "source_url": media["source_page"],
                "creator": media["creator"],
                "featured": featured,
                "storage": "external",
                "media_kind": "gif",
                "rights": "unknown_link_only",
                "media_id": media["id"],
                "playbook_role": media["playbook_role"],
            }
        )
    extras.extend(gallery_from_sample(s) for s in RELATED_SAMPLES)
    extras.extend(gallery_from_sample(s) for s in SOGNI_EXTRAS)

    known = {x["id"] for x in gallery}
    gallery.extend(x for x in extras if x["id"] not in known)

    items = []
    for mid, gid, idea_ids, path, sha, nbytes, frames, dur, w, h in LOCAL_GIFS:
        items.append(
            media_record(
                {
                    "id": mid,
                    "gallery_id": gid,
                    "idea_ids": idea_ids,
                    "url": path,
                    "local_path": path,
                    "content_type": "image/gif",
                    "sha256": sha,
                    "bytes": nbytes,
                    "n_frames": frames,
                    "duration_ms": dur,
                    "width": w,
                    "height": h,
                    "model": "unknown",
                    "model_claim": "Repository seed from a ChatGPT session; exact 2.6 checkpoint not recorded",
                    "creator": "repository seed",
                    "source_page": f"https://github.com/jammyfu/awesome-ai-model-showcases/blob/main/docs/{path}",
                    "source_label": "本项目已有 GIF 案例",
                    "prompt_status": "reconstructed",
                    "playbook_role": "local_seed",
                    "notes": "Shipped in docs/gifs/. Reference-image rights not independently verified.",
                },
                "local",
                "gif",
                "repo_seed",
            )
        )
    for rec in [OFFICIAL_LANTERN, LIGHTLYN_PRODUCT, LIGHTLYN_STEAM, VEEVID_PERFUME, REDDIT_NOD, PAPER_BOAT, *RELATED_SAMPLES, *SOGNI_EXTRAS]:
        items.append(media_record(rec, "external", "gif"))
    items.append(
        media_record(
            {
                "id": "krouxzz-wave-mp4",
                "idea_ids": ["krouxzz-wave-ref"],
                "url": "https://video.twimg.com/tweet_video/HWWnk8IXsAE0aXq.mp4",
                "content_type": "video/mp4",
                "sha256": "d22d64bcbf273bd98466e86b2529f672f5c0d386771d85ec7f518984d503ea6a",
                "bytes": 48068,
                "n_frames": 74,
                "duration_ms": 6550,
                "width": 580,
                "height": 576,
                "codec": "h264",
                "x_declared_type": "animated_gif",
                "model": "Flare",
                "model_claim": "X media entity type animated_gif delivering video/mp4",
                "creator": "Max Goldstein (@Krouxzz)",
                "source_page": "https://x.com/Krouxzz/status/2118283796181053637",
                "source_label": "社区公开案例",
                "prompt_status": "verbatim",
                "playbook_role": "fill",
                "notes": "Do not call this a GIF. Not in the GIF gallery.",
            },
            "external",
            "mp4",
        )
    )
    for rec in [
        {
            "id": "openai-launch-sketch-owl-vimeo",
            "idea_ids": ["sketch-owl"],
            "url": "https://player.vimeo.com/video/1242957231?h=375195e1fb&muted=1&loop=1",
            "content_type": "text/html",
            "model": "Sunburst",
            "model_claim": "ImgAPI: launch owl demo is video, not GIF",
            "creator": "OpenAI",
            "source_page": "https://openai.com/index/introducing-images-2-6/",
            "source_label": "OpenAI 官方发布（Vimeo 视频，非 GIF）",
            "prompt_status": "reconstructed",
            "playbook_role": "video_demo",
            "notes": "Vimeo title mapped from ImgAPI page order (oEmbed 404).",
            "mapping_confidence": "page-order",
        },
        {
            "id": "openai-launch-town-assistant-vimeo",
            "idea_ids": ["typing-companion"],
            "url": "https://player.vimeo.com/video/1242966135?h=a954ad2081&muted=1&loop=1",
            "content_type": "text/html",
            "model": "Flare",
            "model_claim": "ImgAPI: Town assistant demo is video, not GIF",
            "creator": "Town / OpenAI launch page",
            "source_page": "https://openai.com/index/introducing-images-2-6/",
            "source_label": "OpenAI 官方发布（Vimeo 视频，非 GIF）",
            "prompt_status": "reconstructed",
            "playbook_role": "video_demo",
            "notes": "Vimeo title mapped from ImgAPI page order (oEmbed 404).",
            "mapping_confidence": "page-order",
        },
        {
            "id": "openai-launch-market-downturn-vimeo",
            "idea_ids": ["sprite-sheet-stock-crash"],
            "url": "https://player.vimeo.com/video/1242918506?h=5b6824f867&muted=1&loop=1",
            "content_type": "text/html",
            "model": "Sunburst",
            "model_claim": "ImgAPI: launch stock-chart clip is video, not GIF",
            "creator": "OpenArt / OpenAI launch page",
            "source_page": "https://openai.com/index/introducing-images-2-6/",
            "source_label": "OpenAI 官方发布（Vimeo 视频，非 GIF）",
            "prompt_status": "verbatim",
            "playbook_role": "video_demo",
            "notes": "Vimeo title mapped from ImgAPI page order (oEmbed 404).",
            "mapping_confidence": "page-order",
        },
    ]:
        items.append(media_record(rec, "external", "vimeo"))

    excluded = [
        {
            "id": "atlas-robot-wave-pre26",
            "url": "https://static.atlascloud.ai/uploads/01_robot_wave_d7b491e387.gif",
            "media_kind": "gif",
            "n_frames": 8,
            "width": 480,
            "height": 480,
            "duration_ms": 2000,
            "sha256": "a1a63045752479bf0061cbcc7272fdc36ac415768c08d44d9484433019904eac",
            "reason": "Atlas: earlier workflow, not presented as Images 2.6 output. Creator could not verify the exact image model.",
            "source_page": "https://www.atlascloud.ai/blog/tips/gpt-image-2.6-image-to-gif",
            "bucket": "excluded_wrong_model",
        },
        {
            "id": "atlas-teacup-pre26",
            "url": "https://static.atlascloud.ai/uploads/02_tea_cup_loop_6581c7b529.gif",
            "media_kind": "gif",
            "n_frames": 46,
            "width": 400,
            "height": 500,
            "duration_ms": 9200,
            "sha256": "3145289817e2e584ce50c3467328a1586ba5448cedc1eb9f145e0b4f30537888",
            "reason": "Atlas: earlier workflow example, not an Images 2.6 test.",
            "source_page": "https://www.atlascloud.ai/blog/tips/gpt-image-2.6-image-to-gif",
            "bucket": "excluded_wrong_model",
        },
        {
            "id": "v2ex-pelican-bike",
            "url": "https://i.imgur.com/ZthxiAB.gif",
            "media_kind": "gif",
            "n_frames": 6,
            "width": 508,
            "height": 506,
            "duration_ms": 840,
            "sha256": "5692187f2f998bf9d76e3a9c2716f3adbd53bcc83e3321f35c0ffff89c876ec8",
            "reason": "Real GIF already withdrawn from idea cards as a one-liner; not a new playbook.",
            "source_page": "https://www.v2ex.com/t/1254763",
            "bucket": "candidate_known_withdrawn",
        },
        {
            "id": "xianyu110-lantern-mirror",
            "url": "https://raw.githubusercontent.com/xianyu110/awesome-gpt-images-2.6/main/images/monkey-lantern-gpt-image-2-6-sunburst.gif",
            "media_kind": "gif",
            "sha256": "5d786a550b93a24fed3aec36725eab00f767cb4aa84985027004e40eb6c61f52",
            "reason": "Byte-identical to the official lantern GIF. MIT on that repo does not grant media redistribution.",
            "source_page": "https://github.com/xianyu110/awesome-gpt-images-2.6",
            "bucket": "duplicate_mirror",
        },
    ]

    manifest = {
        "generated_at": "2026-11-05",
        "policy": (
            "MIT covers code only. No third-party GIF/video bytes were copied into git: no redistribution "
            "license was found. External records are link-only. Morphic prompt-library stills/sheets are not "
            "Images 2.6 outputs and must not appear in the 2.6 GIF gallery."
        ),
        "probe_method": "HTTP GET + Pillow n_frames/duration + sha256; ffprobe for X tweet_video. CI does not re-fetch.",
        "independent_review": {
            "scout_report": "non-X web.md/web.json claimed 12 GIFs = 7 new samples + 5 fills, not 7 playbooks",
            "accepted_new_playbooks": ["ravivit-paper-boat"],
            "accepted_fills": [
                "lantern-monkey-gif",
                "earbuds-product",
                "photo-to-gif-steam",
                "perfume-light",
                "anime-nod",
            ],
            "grouped_not_new_playbooks": [
                "mascot-wave samples (cat/cactus/fox)",
                "steam/photo-to-gif samples (veevid coffee/dog)",
                "sketch-to-gif sample (veevid robot) under sketch-owl",
            ],
            "rejected_as_image26_results": [
                "Atlas robot wave",
                "Atlas teacup",
                "Morphic 2.5 / Ideogram Vector / MiniMax examples",
            ],
        },
        "failures": [
            {"source": "https://nowrap.ai/tools/chatgpt-images-2-6", "error": "HTTP 429"},
            {"source": "https://openai.com/index/introducing-images-2-6/", "error": "HTML 403; Vimeo via ImgAPI"},
            {"source": "https://vimeo.com/api/oembed.json", "error": "HTTP 404"},
            {"source": "Reddit 1xoh2u0 JSON", "error": "HTTP 403; GIF URL still retrieved from i.redd.it"},
            {"source": "路飞 X Article media", "error": "photos, not animated_gif entities; not mirrored"},
        ],
        "items": items,
        "excluded": excluded,
    }

    dump(ideas_path, ideas)
    dump(gallery_path, gallery)
    dump(ROOT / "docs/data/media-manifest.json", manifest)
    print(f"Wrote {len(ideas)} ideas, {len(gallery)} gallery items, {len(items)} media, {len(excluded)} excluded")


if __name__ == "__main__":
    main()
