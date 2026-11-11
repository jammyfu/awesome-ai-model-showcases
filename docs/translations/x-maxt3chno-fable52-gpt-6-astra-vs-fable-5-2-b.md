# x-maxt3chno-fable52-gpt-6-astra-vs-fable-5-2-b

Author / 作者 / 作者 / 作者: @maxt3chno

[Original source / 原帖 / 原帖 / 原投稿](https://x.com/maxt3chno/status/2119896698281467952)
[Archived case / 归档案例 / 歸檔案例 / 収録事例](../cases/x-maxt3chno-fable52-gpt-6-astra-vs-fable-5-2-b/README.md)


[English](#en) · [简体中文](#zh-cn) · [繁體中文](#zh-tw) · [日本語](#ja)

## Original / 原文

```text
GPT-6 Astra vs Fable 5.2 building a zombie eagle creature in Blender
```

### Model evidence / 模型依据

```text
Citing repo lists this under Claude Fable 5.2 and links the original post. Not independently re-run.
```

### Original prompt / 原始提示词

```text
You are building a game-ready 3D creature in Blender through Blender MCP (execute_blender_code for actions, renders and viewport screenshots to check your work). The attached image is the reference. Goal: an outstanding, realistic, production-quality model that matches the reference as closely as possible. Work like a senior creature artist: plan, build, look at your renders critically, fix, and only move on when a stage really looks right. Never ask me questions; if something is unclear, choose the option closest to the reference and continue.

WORK_DIR = C:\Users\Max\Documents\Claude\Fablr (create subfolders textures, renders, export). Save after every stage as WORK_DIR\eagle_stage#.blend. Work only inside WORK_DIR. If Blender is not running, start "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --online-mode yourself; the MCP add-on starts on port 9876.

========================================
WHAT IT IS
A zombie war eagle from a dark, gritty survival island game: a huge, ragged, half-dead bird of prey standing on the ground, hunched forward, wings half-open and drooping, screaming, ready to attack. Realistic, heavy, dirty, dangerous. Never cartoon, never toy-like.
Size: about 1.6 m tall hunched (top of the head about 1.45 m), wingspan about 4.2 m in this pose.
Metres. Faces -Y, Z up, feet on the ground at Z = 0, origin between the feet.
Static model in the pose of the reference. No rig, no animation.
========================================
THE REFERENCE, PART BY PART
HEAD AND SKULLReal eagle/vulture skull shape: flat top, heavy bony brow ridge, long face running into the beak, cheek and jaw lines readable under the feathers. Pushed forward and slightly down, angry.
Head and neck feathers: pale grey-beige, shaggy, messy, spiky on top and at the back of the head, darker and dirtier toward the neck.

BEAK AND MOUTHBig raptor beak: deep at the base, curving down into a sharp hook that overhangs the lower beak, sharp cutting edges, cere with nostril at the base. Grey-yellow horn, darker and dirty toward the tip, small chips and cracks.
Separate lower beak, mouth wide open (about 35-40 degrees), pink-red tongue, dark wet throat.

EYESSet deep in the sockets under the brow ridge, only part of the eyeball visible, real eyelids around them.
Its RIGHT eye (left side of the image): blind, milky white with a faint grey iris shadow. A deep diagonal scar runs through it from the forehead to the cheek: a real cut in the geometry, feathers missing along it, dried dark red blood.
Its LEFT eye (right side of the image): amber-orange iris with a darker outer ring, round black pupil, glossy cornea, faint glow.

BODYThick, heavy chest and shoulders, dark brown-black feathers, wet and clumped, layered down the body.
Long shaggy feathers hang from the belly and thighs like a torn skirt, uneven, some broken.

WOUNDOn its LEFT shoulder (right side of the image), where the wing meets the body: a torn hole in the skin. Ragged skin edge with feathers pulled out around it, lumpy wet dark-red flesh going inward.
Two broken bones coming out of the flesh (one pointing up, one sideways), off-white to yellow, jagged splintered ends, a bit of blood on them.

WINGSHalf-open and drooping: shoulders high, elbows out and slightly forward, wrists low, long primaries hanging down and outward, tips almost on the ground. Real wing anatomy: shoulder, elbow, wrist.
Layered feathers: small and medium coverts over the top, secondaries along the arm, long primaries at the hand.
Colours: black, dark brown, rust-orange, with light/dark bars across many feathers. Many feathers are torn, split, broken or missing, leaving gaps.

NATURAL LEG: its right leg (left side of the image)Thigh hidden in feathers, then a thick scaly tarsus: big overlapping scutes on the front, small pebbly scales on the sides, yellow-brown, dirty, cracked.
Foot: 3 toes forward, 1 back, thick toe pads, long black curved talons with sharp tips.

MECHANICAL LEG: its left leg (right side of the image)A crude, heavy prosthetic of rusty dark iron, as thick as the real leg or thicker, hand-made from scrap.
Upper part: thick pipe with bolted plates, round knee hub with a big bolt, a rod or piston along the back.
Lower part wrapped in dirty leather straps and rags with blood stains, wire or rope tied around them.
Iron foot with 3 forward and 1 back hinged claw blades: thick, hooked, chipped, rusty, dried blood.
The top is strapped into the torn, bloody flesh of the thigh.

========================================
HOW TO BUILD IT
BLOCKOUT. Simple shapes in the exact hunched pose. Front camera (orthographic) with the reference as background; also side and 3/4 cameras. Match proportions and pose to the reference before any detail. This is the most important check.
BODY MESH. One clean, subdivision-ready quad mesh for body, neck, head and natural leg, with edge loops around eyes, beak, shoulders, wing roots and joints. Sculpt the skull, brow, cheeks, beak base and leg scales (multires or a displacement map from your own height map).
FEATHERS. This decides the whole look, so give it the most care.Feather atlas, 2048 px: draw 10-16 different feathers yourself in numpy. Each one has a vane outline (tapered, slightly asymmetric), a central shaft (rachis), fine barb lines angled off the shaft, a few splits and gaps in the vane, a broken or ragged tip on some. Colour variants: black, dark brown, rust, barred (light/dark stripes), pale beige for the head. Alpha mask, plus a normal map from the barb lines and roughness.
Cards: every card shows exactly ONE whole feather from ONE atlas cell, with UVs fitted to that cell. Never tile the atlas across a card. Material with alpha (Alpha Clip about 0.5, or Alpha Hashed), backface culling off, light passing slightly through (translucency or a little subsurface).
Each card is curved: a slight bend along the shaft and across the vane, never a flat plane.
Placement: scatter by script along the surface, oriented to a flow direction (from head toward tail and down the limbs), in overlapping rows like roof tiles. Random size, rotation, curl and colour within limits. Clumps of 3-5 feathers stuck together where it is wet. Head and neck feathers short and spiky, chest feathers medium and layered, belly and thigh fringe long and hanging.
Wings: primaries and secondaries are real thin meshes (vane with slight thickness and a raised shaft), fanned from the wrist and the arm, each with its own angle and droop, some torn or missing. Coverts as layered cards over them.
Under the feather cards, the body mesh is dark brown so gaps never show bright skin.

WOUND. Cut a real hole in the body mesh at the shoulder, model the ragged skin edge as a thin flap, fill the hole with lumpy flesh going inward, add the two broken bones from cylinders with splintered, displaced ends.
NATURAL LEG. Scutes and scales as real relief, toe pads, 4 talons as separate curved hard meshes.
MECHANICAL LEG. Hard-surface modelling: pipes, plates, bolts, knee hub, piston, straps, rag wraps (cloth with thickness and folds), wire, hinged claw blades. Bevel all metal edges so they catch the light.
MATERIALS (PBR, own textures, 2048 px max per set):Feathers: from the atlas, darker and wet at the roots, slightly lighter worn edges, dirt.
Beak: grey-yellow horn, darker tip, dirt in the cracks. Mouth and tongue wet pink-red, throat dark.
Eyes: glossy cornea; one milky blind, one amber with a faint glow.
Flesh: wet dark red with lighter and darker patches. Dried blood dark brown-red, matte. Bones off-white to yellow, slightly glossy.
Natural leg: yellow-brown scales, dark dirt in the gaps, black glossy talons.
Prosthetic: dark rusty iron, bright worn metal on edges and bolt heads, orange-brown rust in recesses, brown leather, dirty grey-brown bloody rags.

========================================
CHECKS
After each build step render front, 3/4 and side views (EEVEE, studio light from the upper left, neutral grey background). Put the front render next to the reference and look critically. Fix what is clearly off before moving on.
At the end also render: head close-up, both feet close-up, wound close-up, one wing from behind.
Final self-check, all must be true:
Silhouette and pose match the reference.
Feathers read as soft, individual, layered feathers with barbs and ragged edges, never as hard plates, combs or a repeating pattern.
The beak is a hooked raptor beak, wide open, tongue visible.
The eyes sit deep under the brow; one blind and scarred, one amber.
Wound and bones read clearly; prosthetic is heavy, rusty and crude.
No holes, no floating parts, no feather card seen edge-on as a thin line, no bad intersections.
========================================
GAME LIMITS
At most 80,000 triangles total, feather cards included.
At most 4 texture sets, each at most 2048 x 2048. In the GLB use JPEG for colour maps and PNG only where alpha is needed; the GLB should be under 30 MB.
Object names: eagle_body, eagle_feathers, eagle_wings, eagle_beak, eagle_eyes, eagle_wound, eagle_prosthetic.
========================================
OUTPUT
WORK_DIR\export\eagle.glb (textures embedded) and WORK_DIR\export\eagle.blend.
WORK_DIR\export\final_front.png, final_34.png, final_side.png, final_head.png, final_feet.png, final_compare.png (reference next to final front).
A short report: triangle count, texture sets and sizes, GLB size.
```

### Source rights / 来源许可

```text
许可未知 · 仅出处链接（不本地再托管）· MIT 只覆盖源码
```

<a id="en"></a>
## English

AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.

```text
GPT-6 Astra vs Fable 5.2 building a zombie eagle creature in Blender
```

### Method

Three.js / HTML or Blender scene captured as video on X

### Verification

Primary X URL listed by yihui-dev/awesome-fable5-2-videos · not independently re-run

### Model evidence (translation)

```text
Citing repo lists this under Claude Fable 5.2 and links the original post. Not independently re-run.
```

### Published prompt (translation)

```text
You are building a game-ready 3D creature in Blender through Blender MCP (execute_blender_code for actions, renders and viewport screenshots to check your work). The attached image is the reference. Goal: an outstanding, realistic, production-quality model that matches the reference as closely as possible. Work like a senior creature artist: plan, build, look at your renders critically, fix, and only move on when a stage really looks right. Never ask me questions; if something is unclear, choose the option closest to the reference and continue.

WORK_DIR = C:\Users\Max\Documents\Claude\Fablr (create subfolders textures, renders, export). Save after every stage as WORK_DIR\eagle_stage#.blend. Work only inside WORK_DIR. If Blender is not running, start "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --online-mode yourself; the MCP add-on starts on port 9876.

========================================
WHAT IT IS
A zombie war eagle from a dark, gritty survival island game: a huge, ragged, half-dead bird of prey standing on the ground, hunched forward, wings half-open and drooping, screaming, ready to attack. Realistic, heavy, dirty, dangerous. Never cartoon, never toy-like.
Size: about 1.6 m tall hunched (top of the head about 1.45 m), wingspan about 4.2 m in this pose.
Metres. Faces -Y, Z up, feet on the ground at Z = 0, origin between the feet.
Static model in the pose of the reference. No rig, no animation.
========================================
THE REFERENCE, PART BY PART
HEAD AND SKULLReal eagle/vulture skull shape: flat top, heavy bony brow ridge, long face running into the beak, cheek and jaw lines readable under the feathers. Pushed forward and slightly down, angry.
Head and neck feathers: pale grey-beige, shaggy, messy, spiky on top and at the back of the head, darker and dirtier toward the neck.

BEAK AND MOUTHBig raptor beak: deep at the base, curving down into a sharp hook that overhangs the lower beak, sharp cutting edges, cere with nostril at the base. Grey-yellow horn, darker and dirty toward the tip, small chips and cracks.
Separate lower beak, mouth wide open (about 35-40 degrees), pink-red tongue, dark wet throat.

EYESSet deep in the sockets under the brow ridge, only part of the eyeball visible, real eyelids around them.
Its RIGHT eye (left side of the image): blind, milky white with a faint grey iris shadow. A deep diagonal scar runs through it from the forehead to the cheek: a real cut in the geometry, feathers missing along it, dried dark red blood.
Its LEFT eye (right side of the image): amber-orange iris with a darker outer ring, round black pupil, glossy cornea, faint glow.

BODYThick, heavy chest and shoulders, dark brown-black feathers, wet and clumped, layered down the body.
Long shaggy feathers hang from the belly and thighs like a torn skirt, uneven, some broken.

WOUNDOn its LEFT shoulder (right side of the image), where the wing meets the body: a torn hole in the skin. Ragged skin edge with feathers pulled out around it, lumpy wet dark-red flesh going inward.
Two broken bones coming out of the flesh (one pointing up, one sideways), off-white to yellow, jagged splintered ends, a bit of blood on them.

WINGSHalf-open and drooping: shoulders high, elbows out and slightly forward, wrists low, long primaries hanging down and outward, tips almost on the ground. Real wing anatomy: shoulder, elbow, wrist.
Layered feathers: small and medium coverts over the top, secondaries along the arm, long primaries at the hand.
Colours: black, dark brown, rust-orange, with light/dark bars across many feathers. Many feathers are torn, split, broken or missing, leaving gaps.

NATURAL LEG: its right leg (left side of the image)Thigh hidden in feathers, then a thick scaly tarsus: big overlapping scutes on the front, small pebbly scales on the sides, yellow-brown, dirty, cracked.
Foot: 3 toes forward, 1 back, thick toe pads, long black curved talons with sharp tips.

MECHANICAL LEG: its left leg (right side of the image)A crude, heavy prosthetic of rusty dark iron, as thick as the real leg or thicker, hand-made from scrap.
Upper part: thick pipe with bolted plates, round knee hub with a big bolt, a rod or piston along the back.
Lower part wrapped in dirty leather straps and rags with blood stains, wire or rope tied around them.
Iron foot with 3 forward and 1 back hinged claw blades: thick, hooked, chipped, rusty, dried blood.
The top is strapped into the torn, bloody flesh of the thigh.

========================================
HOW TO BUILD IT
BLOCKOUT. Simple shapes in the exact hunched pose. Front camera (orthographic) with the reference as background; also side and 3/4 cameras. Match proportions and pose to the reference before any detail. This is the most important check.
BODY MESH. One clean, subdivision-ready quad mesh for body, neck, head and natural leg, with edge loops around eyes, beak, shoulders, wing roots and joints. Sculpt the skull, brow, cheeks, beak base and leg scales (multires or a displacement map from your own height map).
FEATHERS. This decides the whole look, so give it the most care.Feather atlas, 2048 px: draw 10-16 different feathers yourself in numpy. Each one has a vane outline (tapered, slightly asymmetric), a central shaft (rachis), fine barb lines angled off the shaft, a few splits and gaps in the vane, a broken or ragged tip on some. Colour variants: black, dark brown, rust, barred (light/dark stripes), pale beige for the head. Alpha mask, plus a normal map from the barb lines and roughness.
Cards: every card shows exactly ONE whole feather from ONE atlas cell, with UVs fitted to that cell. Never tile the atlas across a card. Material with alpha (Alpha Clip about 0.5, or Alpha Hashed), backface culling off, light passing slightly through (translucency or a little subsurface).
Each card is curved: a slight bend along the shaft and across the vane, never a flat plane.
Placement: scatter by script along the surface, oriented to a flow direction (from head toward tail and down the limbs), in overlapping rows like roof tiles. Random size, rotation, curl and colour within limits. Clumps of 3-5 feathers stuck together where it is wet. Head and neck feathers short and spiky, chest feathers medium and layered, belly and thigh fringe long and hanging.
Wings: primaries and secondaries are real thin meshes (vane with slight thickness and a raised shaft), fanned from the wrist and the arm, each with its own angle and droop, some torn or missing. Coverts as layered cards over them.
Under the feather cards, the body mesh is dark brown so gaps never show bright skin.

WOUND. Cut a real hole in the body mesh at the shoulder, model the ragged skin edge as a thin flap, fill the hole with lumpy flesh going inward, add the two broken bones from cylinders with splintered, displaced ends.
NATURAL LEG. Scutes and scales as real relief, toe pads, 4 talons as separate curved hard meshes.
MECHANICAL LEG. Hard-surface modelling: pipes, plates, bolts, knee hub, piston, straps, rag wraps (cloth with thickness and folds), wire, hinged claw blades. Bevel all metal edges so they catch the light.
MATERIALS (PBR, own textures, 2048 px max per set):Feathers: from the atlas, darker and wet at the roots, slightly lighter worn edges, dirt.
Beak: grey-yellow horn, darker tip, dirt in the cracks. Mouth and tongue wet pink-red, throat dark.
Eyes: glossy cornea; one milky blind, one amber with a faint glow.
Flesh: wet dark red with lighter and darker patches. Dried blood dark brown-red, matte. Bones off-white to yellow, slightly glossy.
Natural leg: yellow-brown scales, dark dirt in the gaps, black glossy talons.
Prosthetic: dark rusty iron, bright worn metal on edges and bolt heads, orange-brown rust in recesses, brown leather, dirty grey-brown bloody rags.

========================================
CHECKS
After each build step render front, 3/4 and side views (EEVEE, studio light from the upper left, neutral grey background). Put the front render next to the reference and look critically. Fix what is clearly off before moving on.
At the end also render: head close-up, both feet close-up, wound close-up, one wing from behind.
Final self-check, all must be true:
Silhouette and pose match the reference.
Feathers read as soft, individual, layered feathers with barbs and ragged edges, never as hard plates, combs or a repeating pattern.
The beak is a hooked raptor beak, wide open, tongue visible.
The eyes sit deep under the brow; one blind and scarred, one amber.
Wound and bones read clearly; prosthetic is heavy, rusty and crude.
No holes, no floating parts, no feather card seen edge-on as a thin line, no bad intersections.
========================================
GAME LIMITS
At most 80,000 triangles total, feather cards included.
At most 4 texture sets, each at most 2048 x 2048. In the GLB use JPEG for colour maps and PNG only where alpha is needed; the GLB should be under 30 MB.
Object names: eagle_body, eagle_feathers, eagle_wings, eagle_beak, eagle_eyes, eagle_wound, eagle_prosthetic.
========================================
OUTPUT
WORK_DIR\export\eagle.glb (textures embedded) and WORK_DIR\export\eagle.blend.
WORK_DIR\export\final_front.png, final_34.png, final_side.png, final_head.png, final_feet.png, final_compare.png (reference next to final front).
A short report: triangle count, texture sets and sizes, GLB size.
```

<a id="zh-cn"></a>
## 简体中文

AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。

```text
GPT-6 Astra 与 Fable 5.2 在 Blender 中制作僵尸鹰怪物的对照
```

### 做法

Three.js／HTML 或 Blender 场景，录制为 X 视频

### 核验状态

由 yihui-dev/awesome-fable5-2-videos 收录的原始 X URL · 未独立复测

### 模型依据（译文）

```text
引用仓库将此列于 Claude Fable 5.2 下，并链接原帖。未独立复跑。
```

### 公开提示词（译文）

```text
你正在通过 Blender MCP 在 Blender 中构建一个可用于游戏的 3D 生物（用 execute_blender_code 执行动作，用渲染图和视口截图检查成果）。附图就是参考。目标：制作一个出色、写实、达到生产质量，并尽可能贴近参考的模型。像资深生物艺术家一样工作：规划、构建、批判性地查看渲染、修正，只有某一阶段真正看起来正确时才进入下一阶段。不要向我提问；如有不明确之处，选择最贴近参考的方案继续。

WORK_DIR = C:\Users\Max\Documents\Claude\Fablr（创建 textures、renders、export 子文件夹）。每个阶段完成后保存为 WORK_DIR\eagle_stage#.blend。只在 WORK_DIR 内工作。如果 Blender 没有运行，自行启动 "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --online-mode；MCP 插件会在端口 9876 启动。

========================================
它是什么
来自黑暗、粗粝的生存岛游戏的一只丧尸战鹰：巨大、破败、半死不活的猛禽，站在地上，身体向前佝偻，翅膀半张下垂，嘶叫着准备攻击。写实、沉重、肮脏、危险。绝不做成卡通或玩具感。
尺寸：佝偻姿态约 1.6 m 高（头顶约 1.45 m），此姿势的翼展约 4.2 m。
单位为米。朝向 -Y，Z 向上，双脚落在 Z = 0 的地面，原点在双脚之间。
按参考姿势制作静态模型。不要骨架绑定，不要动画。
========================================
逐部分解析参考
头部与头骨
真实的鹰／秃鹫头骨形状：平坦的头顶，厚重的骨性眉脊，长脸延伸到喙，羽毛下能辨认出面颊与下颌轮廓。头向前探，略向下压，显得愤怒。
头颈羽毛：浅灰米色，蓬乱、杂乱，头顶和后脑呈尖刺状，越靠近颈部越暗、越脏。

喙与口腔
大型猛禽喙：根部厚深，向下弯成锋利钩形并伸出下喙之外，切缘锋利，基部有带鼻孔的蜡膜。灰黄色角质，越向尖端越暗、越脏，带细小缺口和裂纹。
下喙独立，嘴大张（约 35–40 度），粉红偏红的舌头，阴暗湿润的咽喉。

眼睛
深嵌于眉脊下的眼窝，只露出部分眼球，周围有真实眼睑。
它的右眼（图像左侧）：失明，乳白色，隐约有灰色虹膜阴影。一道深深的斜向疤痕从额头穿过眼睛延伸到脸颊：必须是几何上的真实切口，沿线羽毛缺失，带干涸的暗红血迹。
它的左眼（图像右侧）：琥珀橙色虹膜，外圈更暗，圆形黑瞳孔，光亮角膜，微弱发光。

身体
厚重的胸部与肩部，深棕至黑色羽毛，湿润结团，顺着身体层层向下覆盖。
腹部和大腿垂下长而蓬乱的羽毛，像撕破的裙摆，参差不齐，部分折断。

伤口
在左肩（图像右侧），翅膀与身体连接处：皮肤上有一个撕裂的洞。皮肤边缘破烂，周围羽毛被拔掉，湿润的暗红色肉块向内部延伸。
两根断骨从血肉中伸出（一根朝上，一根朝侧面），灰白至黄色，断端尖锐劈裂，带少量血迹。

翅膀
半张且下垂：肩部高，肘部向外且略向前，腕部低，长初级飞羽向下、向外垂，尖端几乎触地。真实翅膀解剖结构：肩、肘、腕。
羽毛分层：上层为小型和中型覆羽，沿臂部为次级飞羽，手部为长初级飞羽。
颜色：黑色、深棕色、锈橙色，许多羽毛横跨明暗条纹。很多羽毛撕裂、分叉、折断或缺失，留下空隙。

自然腿：它的右腿（图像左侧）
大腿藏在羽毛中，往下是一段粗壮、覆鳞的跗部：正面为大型重叠鳞甲，两侧为细小卵石状鳞片，黄棕色，肮脏、开裂。
脚：3 趾向前、1 趾向后，趾垫厚，长而黑的弯爪，尖端锋利。

机械腿：它的左腿（图像右侧）
一条由生锈暗铁制作的粗陋沉重义肢，与真腿一样粗或更粗，由废料手工拼成。
上部：粗管配螺栓固定板，圆形膝关节毂带一个大螺栓，后侧有一根杆或活塞。
下部缠着脏皮带和带血渍的破布，外面绑着铁丝或绳索。
铁脚有 3 个向前、1 个向后的铰接爪刃：厚重、钩状、有缺口、生锈、带干血。
顶部用带子固定在大腿撕裂流血的血肉中。

========================================
制作方法
粗模。用简单形体摆出完全相同的佝偻姿势。设置正面相机（正交），将参考图作为背景；另设侧面和 3/4 相机。添加任何细节前，先让比例和姿态与参考一致。这是最重要的检查。
身体网格。身体、颈部、头部和自然腿使用一个干净、适合细分的四边形网格，在眼睛、喙、肩部、翼根和关节周围布置边循环。雕刻头骨、眉脊、面颊、喙基部和腿部鳞片（使用多级细分或由自制高度图生成的置换贴图）。
羽毛。它决定整体外观，因此要投入最多心力。
羽毛图集，2048 px：自行用 numpy 绘制 10–16 种不同羽毛。每根都有羽片轮廓（逐渐收尖、略不对称）、中央羽轴（rachis）、从羽轴斜向伸出的细密羽枝线、羽片中少量裂隙与空缺，部分具有折断或参差的尖端。配色变体：黑色、深棕、锈色、条斑（明暗条纹）、头部用的浅米色。制作 alpha 蒙版，以及根据羽枝线生成的法线贴图和粗糙度。
羽毛卡片：每张卡片准确显示一个图集单元中的一根完整羽毛，UV 贴合该单元。绝不要在单张卡片上平铺图集。材质带 alpha（Alpha Clip 约 0.5，或 Alpha Hashed），关闭背面剔除，允许少量光线穿过（透光或少量次表面散射）。
每张卡片都要弯曲：沿羽轴和横跨羽片方向都略弯，绝不能是平面。
放置：通过脚本沿表面散布，朝向顺应流向（从头部向尾部，并沿四肢向下），像屋瓦一样逐排重叠。在合理范围内随机变化大小、旋转、卷曲和颜色。湿处让 3–5 根羽毛粘成一簇。头颈羽毛短而尖，胸羽中等长度且层次分明，腹部和大腿边缘的羽毛长而下垂。
翅膀：初级和次级飞羽用真正的薄网格（羽片略有厚度，羽轴隆起），从腕部和臂部扇形展开，每根有独立的角度与下垂程度，部分撕裂或缺失。上方用分层卡片作为覆羽。
羽毛卡片下的身体网格为深棕色，让间隙绝不露出亮色皮肤。

伤口。在肩部身体网格上切出真实的洞，将参差皮肤边缘建模成薄皮瓣，用向内延伸的肉块填充洞口，添加两根断骨：由圆柱制作，断端劈裂并做置换变形。
自然腿。鳞甲与鳞片要有真实起伏，制作趾垫，将 4 根爪分别建成弯曲的硬质网格。
机械腿。硬表面建模：管、板、螺栓、膝关节毂、活塞、带子、破布缠绕物（有厚度和褶皱的布料）、铁丝、铰接爪刃。所有金属边缘倒角，以捕捉光线。
材质（PBR、自制纹理，每组最高 2048 px）：
羽毛：使用图集，根部更暗且湿，磨损边缘略亮，带污垢。
喙：灰黄色角质，尖端更暗，裂缝内有污垢。口腔和舌头为湿润粉红偏红色，咽喉暗色。
眼睛：光亮角膜；一只乳白失明，一只琥珀色且微微发光。
血肉：湿润暗红色，夹杂更浅与更深的斑块。干血为暗棕红色、哑光。骨头灰白至黄色，略有光泽。
自然腿：黄棕色鳞片，缝隙中有深色污垢，黑色亮爪。
义肢：暗色锈铁，边缘和螺栓头露出明亮磨损金属，凹陷处为橙棕色锈迹，棕色皮革，肮脏的灰棕色血污破布。

========================================
检查
每个制作步骤完成后，渲染正面、3/4 和侧面视图（EEVEE，左上方摄影棚灯光，中性灰背景）。把正面渲染放在参考图旁，批判性地查看。修正明显不对之处后再继续。
最后还要渲染：头部特写、双脚特写、伤口特写、一侧翅膀背面。
最终自检，必须全部满足：
轮廓与姿势匹配参考。
羽毛看起来柔软、独立、层层叠叠，具有羽枝和破损边缘，绝不像硬板、梳子或重复图案。
喙是钩状猛禽喙，大张，能看到舌头。
眼睛深嵌在眉脊下；一只失明带疤，一只琥珀色。
伤口与骨头清晰可辨；义肢沉重、生锈、粗陋。
没有洞、没有悬浮部件、没有以侧边呈现为细线的羽毛卡片、没有不良穿插。
========================================
游戏限制
总计最多 80,000 个三角形，包含羽毛卡片。
最多 4 组纹理，每组最多 2048 x 2048。GLB 中颜色贴图使用 JPEG，只有需要 alpha 的地方使用 PNG；GLB 应小于 30 MB。
对象名：eagle_body、eagle_feathers、eagle_wings、eagle_beak、eagle_eyes、eagle_wound、eagle_prosthetic。
========================================
输出
WORK_DIR\export\eagle.glb（嵌入纹理）和 WORK_DIR\export\eagle.blend。
WORK_DIR\export\final_front.png、final_34.png、final_side.png、final_head.png、final_feet.png、final_compare.png（参考图与最终正面图并排）。
简短报告：三角形数、纹理组数及尺寸、GLB 大小。
```

<a id="zh-tw"></a>
## 繁體中文

AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。

```text
GPT-6 Astra 與 Fable 5.2 在 Blender 中製作僵屍鷹怪物的對照
```

### 做法

Three.js／HTML 或 Blender 場景，錄製為 X 影片

### 核驗狀態

由 yihui-dev/awesome-fable5-2-videos 收錄的原始 X URL · 未獨立重現

### 模型依據（譯文）

```text
引用倉庫將此列於 Claude Fable 5.2 下，並鏈接原帖。未獨立復跑。
```

### 公開提示詞（譯文）

```text
你正在通過 Blender MCP 在 Blender 中構建一個可用於遊戲的 3D 生物（用 execute_blender_code 執行動作，用渲染圖和視口截圖檢查成果）。附圖就是參考。目標：製作一個出色、寫實、達到生產質量，並盡可能貼近參考的模型。像資深生物藝術家一樣工作：規劃、構建、批判性地查看渲染、修正，只有某一階段真正看起來正確時才進入下一階段。不要向我提問；如有不明確之處，選擇最貼近參考的方案繼續。

WORK_DIR = C:\Users\Max\Documents\Claude\Fablr（創建 textures、renders、export 子文件夾）。每個階段完成後保存為 WORK_DIR\eagle_stage#.blend。只在 WORK_DIR 內工作。如果 Blender 沒有運行，自行啓動 "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --online-mode；MCP 插件會在端口 9876 啓動。

========================================
它是甚麼
來自黑暗、粗糲的生存島遊戲的一隻喪屍戰鷹：巨大、破敗、半死不活的猛禽，站在地上，身體向前佝僂，翅膀半張下垂，嘶叫著準備攻擊。寫實、沈重、骯髒、危險。絕不做成卡通或玩具感。
尺寸：佝僂姿態約 1.6 m 高（頭頂約 1.45 m），此姿勢的翼展約 4.2 m。
單位為米。朝向 -Y，Z 向上，雙腳落在 Z = 0 的地面，原點在雙腳之間。
按參考姿勢製作靜態模型。不要骨架綁定，不要動畫。
========================================
逐部分解析參考
頭部與頭骨
真實的鷹／禿鷲頭骨形狀：平坦的頭頂，厚重的骨性眉脊，長臉延伸到喙，羽毛下能辨認出面頰與下頜輪廓。頭向前探，略向下壓，顯得憤怒。
頭頸羽毛：淺灰米色，蓬亂、雜亂，頭頂和後腦呈尖刺狀，越靠近頸部越暗、越髒。

喙與口腔
大型猛禽喙：根部厚深，向下彎成鋒利鈎形並伸出下喙之外，切緣鋒利，基部有帶鼻孔的蠟膜。灰黃色角質，越向尖端越暗、越髒，帶細小缺口和裂紋。
下喙獨立，嘴大張（約 35–40 度），粉紅偏紅的舌頭，陰暗濕潤的咽喉。

眼睛
深嵌於眉脊下的眼窩，只露出部分眼球，周圍有真實眼瞼。
它的右眼（圖像左側）：失明，乳白色，隱約有灰色虹膜陰影。一道深深的斜向疤痕從額頭穿過眼睛延伸到臉頰：必須是幾何上的真實切口，沿線羽毛缺失，帶乾涸的暗紅血跡。
它的左眼（圖像右側）：琥珀橙色虹膜，外圈更暗，圓形黑瞳孔，光亮角膜，微弱發光。

身體
厚重的胸部與肩部，深棕至黑色羽毛，濕潤結團，順著身體層層向下覆蓋。
腹部和大腿垂下長而蓬亂的羽毛，像撕破的裙擺，參差不齊，部分折斷。

傷口
在左肩（圖像右側），翅膀與身體連接處：皮膚上有一個撕裂的洞。皮膚邊緣破爛，周圍羽毛被拔掉，濕潤的暗紅色肉塊向內部延伸。
兩根斷骨從血肉中伸出（一根朝上，一根朝側面），灰白至黃色，斷端尖銳劈裂，帶少量血跡。

翅膀
半張且下垂：肩部高，肘部向外且略向前，腕部低，長初級飛羽向下、向外垂，尖端幾乎觸地。真實翅膀解剖結構：肩、肘、腕。
羽毛分層：上層為小型和中型覆羽，沿臂部為次級飛羽，手部為長初級飛羽。
顏色：黑色、深棕色、鏽橙色，許多羽毛橫跨明暗條紋。很多羽毛撕裂、分叉、折斷或缺失，留下空隙。

自然腿：它的右腿（圖像左側）
大腿藏在羽毛中，往下是一段粗壯、覆鱗的跗部：正面為大型重疊鱗甲，兩側為細小卵石狀鱗片，黃棕色，骯髒、開裂。
腳：3 趾向前、1 趾向後，趾墊厚，長而黑的彎爪，尖端鋒利。

機械腿：它的左腿（圖像右側）
一條由生鏽暗鐵製作的粗陋沈重義肢，與真腿一樣粗或更粗，由廢料手工拼成。
上部：粗管配螺栓固定板，圓形膝關節轂帶一個大螺栓，後側有一根桿或活塞。
下部纏著髒皮帶和帶血漬的破布，外面綁著鐵絲或繩索。
鐵腳有 3 個向前、1 個向後的鉸接爪刃：厚重、鈎狀、有缺口、生鏽、帶乾血。
頂部用帶子固定在大腿撕裂流血的血肉中。

========================================
製作方法
粗模。用簡單形體擺出完全相同的佝僂姿勢。設置正面相機（正交），將參考圖作為背景；另設側面和 3/4 相機。添加任何細節前，先讓比例和姿態與參考一致。這是最重要的檢查。
身體網格。身體、頸部、頭部和自然腿使用一個乾淨、適合細分的四邊形網格，在眼睛、喙、肩部、翼根和關節周圍佈置邊循環。雕刻頭骨、眉脊、面頰、喙基部和腿部鱗片（使用多級細分或由自制高度圖生成的置換貼圖）。
羽毛。它決定整體外觀，因此要投入最多心力。
羽毛圖集，2048 px：自行用 numpy 繪制 10–16 種不同羽毛。每根都有羽片輪廓（逐漸收尖、略不對稱）、中央羽軸（rachis）、從羽軸斜向伸出的細密羽枝線、羽片中少量裂隙與空缺，部分具有折斷或參差的尖端。配色變體：黑色、深棕、鏽色、條斑（明暗條紋）、頭部用的淺米色。製作 alpha 蒙版，以及根據羽枝線生成的法線貼圖和粗糙度。
羽毛卡片：每張卡片準確顯示一個圖集單元中的一根完整羽毛，UV 貼合該單元。絕不要在單張卡片上平鋪圖集。材質帶 alpha（Alpha Clip 約 0.5，或 Alpha Hashed），關閉背面剔除，允許少量光線穿過（透光或少量次表面散射）。
每張卡片都要彎曲：沿羽軸和橫跨羽片方向都略彎，絕不能是平面。
放置：通過腳本沿表面散布，朝向順應流向（從頭部向尾部，並沿四肢向下），像屋瓦一樣逐排重疊。在合理範圍內隨機變化大小、旋轉、捲曲和顏色。濕處讓 3–5 根羽毛粘成一簇。頭頸羽毛短而尖，胸羽中等長度且層次分明，腹部和大腿邊緣的羽毛長而下垂。
翅膀：初級和次級飛羽用真正的薄網格（羽片略有厚度，羽軸隆起），從腕部和臂部扇形展開，每根有獨立的角度與下垂程度，部分撕裂或缺失。上方用分層卡片作為覆羽。
羽毛卡片下的身體網格為深棕色，讓間隙絕不露出亮色皮膚。

傷口。在肩部身體網格上切出真實的洞，將參差皮膚邊緣建模成薄皮瓣，用向內延伸的肉塊填充洞口，添加兩根斷骨：由圓柱製作，斷端劈裂並做置換變形。
自然腿。鱗甲與鱗片要有真實起伏，製作趾墊，將 4 根爪分別建成彎曲的硬質網格。
機械腿。硬表面建模：管、板、螺栓、膝關節轂、活塞、帶子、破布纏繞物（有厚度和褶皺的布料）、鐵絲、鉸接爪刃。所有金屬邊緣倒角，以捕捉光線。
材質（PBR、自制紋理，每組最高 2048 px）：
羽毛：使用圖集，根部更暗且濕，磨損邊緣略亮，帶污垢。
喙：灰黃色角質，尖端更暗，裂縫內有污垢。口腔和舌頭為濕潤粉紅偏紅色，咽喉暗色。
眼睛：光亮角膜；一隻乳白失明，一隻琥珀色且微微發光。
血肉：濕潤暗紅色，夾雜更淺與更深的斑塊。乾血為暗棕紅色、啞光。骨頭灰白至黃色，略有光澤。
自然腿：黃棕色鱗片，縫隙中有深色污垢，黑色亮爪。
義肢：暗色鏽鐵，邊緣和螺栓頭露出明亮磨損金屬，凹陷處為橙棕色鏽跡，棕色皮革，骯髒的灰棕色血污破布。

========================================
檢查
每個製作步驟完成後，渲染正面、3/4 和側面視圖（EEVEE，左上方攝影棚燈光，中性灰背景）。把正面渲染放在參考圖旁，批判性地查看。修正明顯不對之處後再繼續。
最後還要渲染：頭部特寫、雙腳特寫、傷口特寫、一側翅膀背面。
最終自檢，必須全部滿足：
輪廓與姿勢匹配參考。
羽毛看起來柔軟、獨立、層層疊疊，具有羽枝和破損邊緣，絕不像硬板、梳子或重復圖案。
喙是鈎狀猛禽喙，大張，能看到舌頭。
眼睛深嵌在眉脊下；一隻失明帶疤，一隻琥珀色。
傷口與骨頭清晰可辨；義肢沈重、生鏽、粗陋。
沒有洞、沒有懸浮部件、沒有以側邊呈現為細線的羽毛卡片、沒有不良穿插。
========================================
遊戲限制
總計最多 80,000 個三角形，包含羽毛卡片。
最多 4 組紋理，每組最多 2048 x 2048。GLB 中顏色貼圖使用 JPEG，只有需要 alpha 的地方使用 PNG；GLB 應小於 30 MB。
對象名：eagle_body、eagle_feathers、eagle_wings、eagle_beak、eagle_eyes、eagle_wound、eagle_prosthetic。
========================================
輸出
WORK_DIR\export\eagle.glb（嵌入紋理）和 WORK_DIR\export\eagle.blend。
WORK_DIR\export\final_front.png、final_34.png、final_side.png、final_head.png、final_feet.png、final_compare.png（參考圖與最終正面圖並排）。
簡短報告：三角形數、紋理組數及尺寸、GLB 大小。
```

<a id="ja"></a>
## 日本語

AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。

```text
GPT-6 AstraとFable 5.2でBlenderのゾンビワシを制作して比較
```

### 制作方法

Three.js／HTML または Blender のシーンを X の動画として収録

### 検証状況

yihui-dev/awesome-fable5-2-videos に掲載された原投稿の X URL · 独立した再実行なし

### モデルの根拠（翻訳）

```text
引用元リポジトリではClaude Fable 5.2に分類し、元投稿へリンク。独立した再実行は未実施。
```

### 公開プロンプト（翻訳）

```text
Blender MCP を通じて Blender でゲーム対応の 3D クリーチャーを制作してください（操作には execute_blender_code、確認にはレンダリングとビューポートのスクリーンショットを使用）。添付画像がリファレンスです。目標は、参考に可能な限り忠実な、優れた写実的で本制作に耐える品質のモデルです。シニアのクリーチャーアーティストのように、計画し、作り、レンダリングを批判的に見て修正し、その段階が本当に良く見えてから次へ進んでください。質問はしないでください。不明な点は参考に最も近い選択肢を選び、そのまま進めてください。

WORK_DIR = C:\Users\Max\Documents\Claude\Fablr（textures、renders、export のサブフォルダーを作成）。各段階の後に WORK_DIR\eagle_stage#.blend として保存してください。作業は WORK_DIR 内だけで行ってください。Blender が動作していなければ、自分で "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --online-mode を起動してください。MCP アドオンはポート 9876 で起動します。

========================================
どんな生き物か
暗く荒々しいサバイバル島ゲームに登場するゾンビの戦闘ワシ。巨大でぼろぼろの半死の猛禽が地面に立ち、前かがみになり、翼を半開きで垂らし、叫びながら襲いかかろうとしています。写実的、重々しい、汚い、危険。漫画風や玩具風には絶対にしません。
大きさ：かがんだ状態で約 1.6 m（頭頂は約 1.45 m）、この姿勢で翼幅約 4.2 m。
単位はメートル。正面は -Y、上は Z、足は Z = 0 の地面、原点は両足の間です。
参考画像のポーズの静的モデル。リグもアニメーションも不要です。
========================================
参考画像を部位ごとに確認
頭と頭蓋骨
本物のワシ／ハゲワシの頭蓋骨の形。平たい頭頂、重厚な骨性の眉稜、くちばしへ続く長い顔、羽の下から読み取れる頬と顎のライン。頭を前に突き出し、少し下に向け、怒った表情にします。
頭と首の羽：淡いグレーベージュ。毛羽立ち、乱れ、頭頂と後頭部は尖り、首へ向かうほど暗く汚れています。

くちばしと口
大きな猛禽のくちばし。根元は深く厚く、下方へ曲がって鋭い鉤となり、下くちばしより張り出しています。鋭い切断縁、基部には鼻孔のある蝋膜。灰黄色の角質で、先端ほど暗く汚れ、小さな欠けやひびがあります。
下くちばしを別にし、口を大きく開けます（約 35～40 度）。舌はピンクがかった赤、喉は暗く湿っています。

目
眉稜の下の眼窩に深く収まり、眼球は一部だけが見え、周囲には実際のまぶたがあります。
右目（画像左側）：失明して乳白色で、灰色の虹彩の影がかすかに見えます。額から目を通って頬に至る深い斜めの傷跡があります。ジオメトリに実際の切れ目を作り、その沿線の羽を欠落させ、乾いた暗赤色の血を付けます。
左目（画像右側）：琥珀オレンジの虹彩、暗い外周、丸い黒い瞳孔、光沢のある角膜、かすかな発光。

胴体
厚く重い胸と肩。暗褐色から黒の羽が濡れて固まり、胴体を下へ覆うように重なります。
腹と腿から長く乱れた羽が、破れたスカートのように垂れます。不揃いで、一部は折れています。

傷
左肩（画像右側）の、翼と胴体がつながる場所に、皮膚が裂けた穴があります。皮膚の縁はぼろぼろで周りの羽が抜け、湿った暗赤色の塊状の肉が奥へ続きます。
肉から 2 本の折れた骨が突き出ます（1 本は上向き、1 本は横向き）。オフホワイトから黄色で、断端は鋭く砕け、少量の血が付いています。

翼
半開きで垂れています。肩は高く、肘は外側かつ少し前、手首は低く、長い初列風切が下と外へ垂れ、先端がほぼ地面に届きます。肩、肘、手首という本物の翼の解剖構造です。
羽を重ねます。上は小・中サイズの雨覆、腕に沿って次列風切、手の部分に長い初列風切。
色：黒、暗褐色、錆びたオレンジ。多くの羽には明暗の横帯があります。多くの羽が裂け、割れ、折れ、または欠落し、隙間が空いています。

生身の脚：右脚（画像左側）
腿は羽に隠れ、その下に太いうろこ状の跗部があります。前面は大きく重なった鱗板、側面は小石状の細かいうろこ。黄褐色で、汚れ、ひび割れています。
足：前に 3 本、後ろに 1 本の指。厚い指の肉球、長く黒い湾曲した鉤爪、鋭い先端。

機械の脚：左脚（画像右側）
錆びた暗い鉄の粗雑で重い義足。生身の脚と同じかそれ以上の太さで、スクラップから手作りされています。
上部：ボルト留めの板を付けた太いパイプ、大きなボルトのある丸い膝ハブ、後ろに沿うロッドまたはピストン。
下部は血のしみた汚い革ひもとぼろ布で巻かれ、その周囲に針金やロープが結ばれています。
鉄の足には前に 3 本、後ろに 1 本のヒンジ付きの爪刃。厚く、鉤状で、欠け、錆び、乾いた血が付いています。
上端は腿の裂けて血の出た肉にストラップで固定されています。

========================================
作り方
ブロックアウト。単純な形で、正確に同じ前かがみの姿勢を作ります。正面の正投影カメラに参考画像を背景として置き、側面と 3/4 のカメラも用意します。細部の前に、比率と姿勢を参考に合わせます。これが最も重要な確認です。
胴体メッシュ。胴体、首、頭、生身の脚を、きれいで細分化に適した 1 つの四角ポリゴンメッシュにします。目、くちばし、肩、翼の付け根、関節の周囲にはエッジループを作ります。頭蓋骨、眉、頬、くちばしの基部、脚のうろこをスカルプトします（マルチレゾリューション、または自作の高さマップによるディスプレイスメントマップ）。
羽。全体の見た目を左右するため、最も丁寧に取り組んでください。
羽のアトラス、2048 px：numpy で 10～16 種類の羽を自分で描きます。それぞれに羽弁の輪郭（先細りで少し非対称）、中央の羽軸（rachis）、軸から斜めに伸びる細かな羽枝の線、羽弁にいくつかの裂け目と隙間、一部には折れた先端や不揃いの先端を持たせます。色違いは黒、暗褐色、錆色、横帯入り（明暗の縞）、頭用の淡いベージュ。アルファマスクに加え、羽枝の線から作る法線マップとラフネスを用意します。
カード：各カードにはアトラスの 1 セルから完全な羽 1 枚だけを表示し、UV をそのセルに合わせます。カード上にアトラスをタイル状に繰り返してはいけません。アルファ付きのマテリアル（Alpha Clip 約 0.5、または Alpha Hashed）、裏面カリングは無効、光を少し透過させます（透光、または少量のサブサーフェス）。
すべてのカードを曲げます。羽軸方向にも羽弁を横切る方向にも軽い湾曲を付け、平面には絶対にしません。
配置：スクリプトで表面に散布し、流れの方向（頭から尾へ、四肢に沿って下へ）に向け、屋根瓦のように列を重ねます。大きさ、回転、カール、色を範囲内でランダム化します。濡れた部分では羽 3～5 枚をくっついた束にします。頭と首は短く尖った羽、胸は中程度で層状、腹と腿の縁は長く垂れた羽にします。
翼：初列風切と次列風切は本物の薄いメッシュにします（羽弁にわずかな厚み、羽軸に盛り上がり）。手首と腕から扇状に並べ、各羽に固有の角度と垂れ方を与え、一部は裂けや欠損を作ります。その上にカードを重ねて雨覆を作ります。
羽のカードの下の胴体メッシュは暗褐色にし、隙間から明るい皮膚が見えないようにします。

傷。肩の胴体メッシュに実際の穴を開け、ぼろぼろの皮膚の縁を薄い皮弁として作り、奥へ続く塊状の肉で穴を埋めます。円柱から、砕けて変位した端を持つ 2 本の折れた骨を加えます。
生身の脚。鱗板とうろこは実際の凹凸にし、指の肉球を作り、4 本の鉤爪は個別の湾曲した硬質メッシュにします。
機械の脚。ハードサーフェスモデリングで、パイプ、板、ボルト、膝ハブ、ピストン、ストラップ、ぼろ布の巻き（厚みと折り目のある布）、針金、ヒンジ付きの爪刃を作ります。金属のすべての縁をベベルし、光を拾うようにします。
マテリアル（PBR、自作テクスチャ、各セット最大 2048 px）：
羽：アトラスを使い、根元は暗く濡れ、擦れた縁は少し明るくし、汚れを加えます。
くちばし：灰黄色の角質、暗い先端、ひびの中に汚れ。口と舌は濡れたピンクがかった赤、喉は暗くします。
目：光沢のある角膜。片方は乳白色の盲目、もう片方はかすかに発光する琥珀色。
肉：濡れた暗赤色に、明暗の斑。乾いた血は暗い赤褐色でつや消し。骨はオフホワイトから黄色、わずかに光沢。
生身の脚：黄褐色のうろこ、隙間に暗い汚れ、黒く光沢のある鉤爪。
義足：暗い錆鉄。縁とボルト頭には明るく擦れた金属、くぼみにはオレンジ褐色の錆。茶色の革、汚れた灰褐色の血まみれのぼろ布。

========================================
確認
各制作工程の後に正面、3/4、側面をレンダリングします（EEVEE、左上からのスタジオ照明、中間的な灰色の背景）。正面レンダリングを参考画像の横に並べ、批判的に見てください。明らかに違う部分は次へ進む前に修正します。
最後にはさらに、頭のクローズアップ、両足のクローズアップ、傷のクローズアップ、片翼の背面をレンダリングします。
最終セルフチェック。すべて満たすこと：
シルエットと姿勢が参考に一致する。
羽が柔らかく、個々に分かれて重なり、羽枝とぼろぼろの縁を持つ羽として見え、硬い板、くし、反復模様には決して見えない。
くちばしは猛禽の鉤状のくちばしで、大きく開き、舌が見える。
目は眉の下に深く収まり、片方は傷のある盲目、もう片方は琥珀色。
傷と骨がはっきり読み取れ、義足は重く、錆び、粗雑。
穴がない、浮いたパーツがない、羽カードが真横から見えて細線になっていない、不適切な交差がない。
========================================
ゲーム用の制限
羽カードを含めて合計最大 80,000 三角形。
テクスチャは最大 4 セット、各セット最大 2048 x 2048。GLB のカラーマップは JPEG とし、アルファが必要な部分だけ PNG を使います。GLB は 30 MB 未満にします。
オブジェクト名：eagle_body、eagle_feathers、eagle_wings、eagle_beak、eagle_eyes、eagle_wound、eagle_prosthetic。
========================================
出力
WORK_DIR\export\eagle.glb（テクスチャ埋め込み）および WORK_DIR\export\eagle.blend。
WORK_DIR\export\final_front.png、final_34.png、final_side.png、final_head.png、final_feet.png、final_compare.png（参考画像と最終正面図を横に並べる）。
短いレポート：三角形数、テクスチャのセット数とサイズ、GLB のサイズ。
```
