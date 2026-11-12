# x-twoclipping-opus55-inputs-ask-me-for-my-produ

Author / 作者 / 作者 / 作者 / 제작자: @twoclipping

[Original source / 原帖 / 原帖 / 原投稿 / 원문](https://x.com/twoclipping/status/2106101258834551116)
[Archived case / 归档案例 / 歸檔案例 / 収録事例 / 보관 사례](../cases/x-twoclipping-opus55-inputs-ask-me-for-my-produ/README.md)


[English](#en) · [简体中文](#zh-cn) · [繁體中文](#zh-tw) · [日本語](#ja) · [한국어](#ko)

## Original / 原文

```text
<inputs> Ask me for: my product's name (one lowercase word), a 4-word tagline, the 3-step
```

### Model evidence / 模型依据

```text
Citing repo lists this under Claude Opus 5.5 and links the original post. Previous mainstream generation. Not independently re-run.
```

### Original prompt / 原始提示词

```text
<inputs>
Ask me for: my product's name (one lowercase word), a 4-word tagline, the 3-step story of what it does, a launch date and domain, a royalty-free song with a clear drop, 4 vertical talking-to-camera clips and 12 portrait photos. If I skip any, use the defaults: "castr", "ugc ads, cast by ai", write a brief → scan 1,000 creators → cast 4, Mixkit "Cat Walk" (129.6 BPM, drop at 29.7s), free Pexels clips and portraits, and transparent stickers from Pixabay (serum, mic, megaphone, vintage camera, spotlight, lips).
</inputs>

<direction>
A 25 second square launch trailer, 1440x1440 at 60fps, loud poster style. Cobalt #2B3BFF, ink #0E0F1F, cream #F6E4C6, pink #FF7DC7, tangerine #FF5A1F. Archivo 900 extra-condensed for names, expanded for headlines, Geist and Geist Mono for labels. Op-art sunburst, scrolling waves, film grain. Real media only: the clips play inside the design, and the stickers get a white die-cut border and a soft shadow.
Motion rules: the camera never stops (a slow 1.03-1.07 push on every scene), nothing pops in (letters rise through a mask line one by one), nothing snaps to the beat (patterns rotate continuously), swaps are carousel glides of about 0.55s, colour changes fade over about 0.35s, stickers ease in and then keep a slow sway. No full stops after the wordmark or any headline.
Banned: beat-snapped rotations, pop-in slams, white flashes, crossfades between scenes, hard cuts, templates.
</direction>

<structure>
54 beats. The song starts 8 beats before its drop.
Beats 0-8: a cobalt sunburst turns around a breathing cream disc. The wordmark types in with a gliding caret and the tagline pill rises. The disc floods the frame into the drop.
Beat 8, the drop: the cream becomes the face of a 3D box and "ONE BRIEF" rises letter by letter. The camera pulls back to the box floating on waves. On beat 12 it turns to "1,000 CREATORS" (stacked, with outlined echoes), on beat 14 to "ZERO DMs".
Beats 16-22: a whip to a dark desk. A tangerine "BRIEF #042" ticket types its rows (product, vibe, cast, due), stickers drift on, a polaroid of a real clip drops onto the corner, and a "NOW CASTING" stamp presses down on beat 20.
Beats 22-34: the casting stage. A crowd of black and white portraits in an arc, a 3D stage block, and the creators gliding through like a carousel. Each plays live in a big disc in black and white, with their name in pink on the stage, their followers, and a MATCH % that counts up. One beat later a "CAST ✓" stamp lands and the clip fades to colour. A counter rolls 1/4 to 4/4.
Beats 34-39: pink floods out of the last disc. The disc morphs into a phone screen (the clip keeps playing) and fans into 4 phones playing all 4 creators, with views counting up. "4 ADS" and "BY FRIDAY" rise.
Beats 39-44, the music's break: the pink floor drops away and a cream "JOIN THE WAITLIST" ticket glides down onto the sunburst. On the pickup its stub tears off.
Beats 44-54: the ticket body morphs into a poster arch. The wordmark rises in, then the tagline, then an info bar slides up in 3 blocks (date, numbers, domain) and a ticker runs round the frame edge. Then it all folds back into the opening disc, so the last frame is the first.
</structure>

<build>
1. One HTML canvas. Every frame is a pure function of time inside seek(t).
2. A beat map in beats, B = 60/BPM, with the song placed so its drop lands on beat 8.
3. The 3D box is an orthographic projection: each face is a 1440px offscreen canvas drawn with an affine transform and shaded by its normal.
4. Cut the clips to 30fps JPEG sequences with ffmpeg, draw frame floor(t*30), and do the black and white with ctx.filter.
5. Trim the sticker PNGs and add the die-cut border by dilating their alpha.
6. Sound: a downloaded SFX for every event (a shutter on every cast, whooshes on the glides, key clicks on the typing), each placed by its measured peak. Loudnorm to -14 LUFS.
7. Render with Playwright at 60fps with 8 motion-blur subframes. Scan for single-frame pops, then compare its motion against a reference video (hard jumps per second, share of still frames).
</build>

<gotchas>
A pattern that rotates one notch per beat reads as stutter: rotate it continuously, and pick each ring's speed so it lands on the same pattern at the last frame. 4 subframes ghost on fast whips, so use 8. A layer whose background is a huge flood circle still covers the screen after sliding down one frame height, so switch it to a full-frame rect once it has flooded. Counters read the frame's time, not the subframe's. The disc must morph inside the same camera transform as the scene it leaves, or it jumps.
</gotchas>

<start>
Ask me for the inputs, then show me the beat map and 6 stills (open, box, brief, casting, phones, poster) before you render.
</start>
```

### Source rights / 来源许可

```text
许可未知 · 仅出处链接（不本地再托管）· MIT 只覆盖源码
```

<a id="en"></a>
## English

AI translation, not human-reviewed. Read the original alongside it; translation does not verify the source or grant reuse rights.

```text
<inputs> Ask me for: my product's name (one lowercase word), a 4-word tagline, the 3-step
```

### Method

Code-made animation captured as video on X

### Verification

Primary X URL listed by yihui-dev/awesome-opus5-5-videos · not independently re-run

### Model evidence (translation)

```text
Citing repo lists this under Claude Opus 5.5 and links the original post. Previous mainstream generation. Not independently re-run.
```

### Published prompt (translation)

```text
<inputs>
Ask me for: my product's name (one lowercase word), a 4-word tagline, the 3-step story of what it does, a launch date and domain, a royalty-free song with a clear drop, 4 vertical talking-to-camera clips and 12 portrait photos. If I skip any, use the defaults: "castr", "ugc ads, cast by ai", write a brief → scan 1,000 creators → cast 4, Mixkit "Cat Walk" (129.6 BPM, drop at 29.7s), free Pexels clips and portraits, and transparent stickers from Pixabay (serum, mic, megaphone, vintage camera, spotlight, lips).
</inputs>

<direction>
A 25 second square launch trailer, 1440x1440 at 60fps, loud poster style. Cobalt #2B3BFF, ink #0E0F1F, cream #F6E4C6, pink #FF7DC7, tangerine #FF5A1F. Archivo 900 extra-condensed for names, expanded for headlines, Geist and Geist Mono for labels. Op-art sunburst, scrolling waves, film grain. Real media only: the clips play inside the design, and the stickers get a white die-cut border and a soft shadow.
Motion rules: the camera never stops (a slow 1.03-1.07 push on every scene), nothing pops in (letters rise through a mask line one by one), nothing snaps to the beat (patterns rotate continuously), swaps are carousel glides of about 0.55s, colour changes fade over about 0.35s, stickers ease in and then keep a slow sway. No full stops after the wordmark or any headline.
Banned: beat-snapped rotations, pop-in slams, white flashes, crossfades between scenes, hard cuts, templates.
</direction>

<structure>
54 beats. The song starts 8 beats before its drop.
Beats 0-8: a cobalt sunburst turns around a breathing cream disc. The wordmark types in with a gliding caret and the tagline pill rises. The disc floods the frame into the drop.
Beat 8, the drop: the cream becomes the face of a 3D box and "ONE BRIEF" rises letter by letter. The camera pulls back to the box floating on waves. On beat 12 it turns to "1,000 CREATORS" (stacked, with outlined echoes), on beat 14 to "ZERO DMs".
Beats 16-22: a whip to a dark desk. A tangerine "BRIEF #042" ticket types its rows (product, vibe, cast, due), stickers drift on, a polaroid of a real clip drops onto the corner, and a "NOW CASTING" stamp presses down on beat 20.
Beats 22-34: the casting stage. A crowd of black and white portraits in an arc, a 3D stage block, and the creators gliding through like a carousel. Each plays live in a big disc in black and white, with their name in pink on the stage, their followers, and a MATCH % that counts up. One beat later a "CAST ✓" stamp lands and the clip fades to colour. A counter rolls 1/4 to 4/4.
Beats 34-39: pink floods out of the last disc. The disc morphs into a phone screen (the clip keeps playing) and fans into 4 phones playing all 4 creators, with views counting up. "4 ADS" and "BY FRIDAY" rise.
Beats 39-44, the music's break: the pink floor drops away and a cream "JOIN THE WAITLIST" ticket glides down onto the sunburst. On the pickup its stub tears off.
Beats 44-54: the ticket body morphs into a poster arch. The wordmark rises in, then the tagline, then an info bar slides up in 3 blocks (date, numbers, domain) and a ticker runs round the frame edge. Then it all folds back into the opening disc, so the last frame is the first.
</structure>

<build>
1. One HTML canvas. Every frame is a pure function of time inside seek(t).
2. A beat map in beats, B = 60/BPM, with the song placed so its drop lands on beat 8.
3. The 3D box is an orthographic projection: each face is a 1440px offscreen canvas drawn with an affine transform and shaded by its normal.
4. Cut the clips to 30fps JPEG sequences with ffmpeg, draw frame floor(t*30), and do the black and white with ctx.filter.
5. Trim the sticker PNGs and add the die-cut border by dilating their alpha.
6. Sound: a downloaded SFX for every event (a shutter on every cast, whooshes on the glides, key clicks on the typing), each placed by its measured peak. Loudnorm to -14 LUFS.
7. Render with Playwright at 60fps with 8 motion-blur subframes. Scan for single-frame pops, then compare its motion against a reference video (hard jumps per second, share of still frames).
</build>

<gotchas>
A pattern that rotates one notch per beat reads as stutter: rotate it continuously, and pick each ring's speed so it lands on the same pattern at the last frame. 4 subframes ghost on fast whips, so use 8. A layer whose background is a huge flood circle still covers the screen after sliding down one frame height, so switch it to a full-frame rect once it has flooded. Counters read the frame's time, not the subframe's. The disc must morph inside the same camera transform as the scene it leaves, or it jumps.
</gotchas>

<start>
Ask me for the inputs, then show me the beat map and 6 stills (open, box, brief, casting, phones, poster) before you render.
</start>
```

<a id="zh-cn"></a>
## 简体中文

AI 译文，未经人工审校。请对照原文阅读；翻译不等于核实来源，也不授予再利用许可。

```text
<inputs> 向我询问：我的产品名（一个小写单词）、一句 4 词标语、3 步…
```

### 做法

代码制作的动画，录制为 X 视频

### 核验状态

由 yihui-dev/awesome-opus5-5-videos 收录的原始 X URL · 未独立复测

### 模型依据（译文）

```text
引用仓库将此列于 Claude Opus 5.5 下，并链接原帖。属于上一代主流模型。未独立复跑。
```

### 公开提示词（译文）

```text
<inputs>
请向我询问：我的产品名（一个小写单词）、一条 4 个词的标语、说明产品作用的 3 步故事、发布日期和域名、一首有清晰 drop 的免版税歌曲、4 段竖屏对镜讲话视频，以及 12 张人像照片。如果我跳过任何项目，使用默认值：“castr”、“ugc ads, cast by ai”、写一份简报 → 扫描 1,000 位创作者 → 选定 4 位、Mixkit 的 “Cat Walk”（129.6 BPM，drop 在 29.7s）、免费的 Pexels 视频与人像，以及 Pixabay 的透明贴纸（精华液、麦克风、扩音器、复古相机、聚光灯、嘴唇）。
</inputs>

<direction>
一部 25 秒的正方形发布预告片，1440x1440，60fps，醒目张扬的海报风格。钴蓝 #2B3BFF、墨色 #0E0F1F、奶油色 #F6E4C6、粉色 #FF7DC7、橘红色 #FF5A1F。名称使用 Archivo 900 的特窄字宽，标题使用加宽字宽，标签使用 Geist 和 Geist Mono。欧普艺术放射纹、滚动波浪、胶片颗粒。只用真实媒体：视频在设计中播放，贴纸带白色模切边框与柔和阴影。
运动规则：镜头永不停止（每个场景都缓慢推近 1.03–1.07）；任何元素都不突然弹出（字母逐个从遮罩线升起）；任何运动都不按节拍突跳（图案持续旋转）；切换采用约 0.55s 的轮播式滑动；颜色变化在约 0.35s 内渐变；贴纸缓动入场后继续缓慢摇摆。字标或任何标题出现后，都不要完全停住。
禁止：按节拍跳变的旋转、突然弹入砸落、白色闪光、场景之间的交叉淡化、硬切、模板。
</direction>

<structure>
54 拍。歌曲从 drop 前 8 拍开始。
第 0–8 拍：钴蓝放射纹围绕一个呼吸起伏的奶油色圆盘旋转。字标伴随滑动的输入光标逐字出现，标语胶囊标签升起。圆盘扩张铺满画面，进入 drop。
第 8 拍，drop：奶油色变成 3D 盒子的一个面，“ONE BRIEF” 逐字母升起。镜头拉远，显示漂浮在波浪上的盒子。第 12 拍，盒子转向 “1,000 CREATORS”（堆叠排版，带描边重影）；第 14 拍转向 “ZERO DMs”。
第 16–22 拍：快速甩向深色桌面。橘红色 “BRIEF #042” 票据逐行打出内容（product、vibe、cast、due），贴纸漂入，一个真实视频的拍立得画面落在角上，第 20 拍压下 “NOW CASTING” 印章。
第 22–34 拍：选角舞台。一群黑白人像呈弧形排列，一个 3D 舞台块，创作者像轮播一样滑过。每个人都在一个大圆盘中播放黑白实时视频，舞台上用粉色显示名字、粉丝数，以及递增的 MATCH %。一拍之后，“CAST ✓” 印章落下，视频逐渐恢复彩色。计数器从 1/4 滚动到 4/4。
第 34–39 拍：粉色从最后一个圆盘涌出。圆盘变成手机屏幕（视频继续播放），再呈扇形展开为 4 台手机，播放全部 4 位创作者，观看数不断增加。“4 ADS” 和 “BY FRIDAY” 升起。
第 39–44 拍，音乐间奏：粉色地面落下消失，一张奶油色 “JOIN THE WAITLIST” 票据滑落到放射纹上。在弱起拍处，票根被撕掉。
第 44–54 拍：票据主体变成拱形海报。字标升起，接着是标语，然后信息栏以 3 个区块滑上来（日期、数字、域名），跑马灯沿画面边缘滚动。最后所有内容折回开场圆盘，使最后一帧与第一帧相同。
</structure>

<build>
1. 一个 HTML canvas。每一帧都是 seek(t) 内时间的纯函数。
2. 以拍为单位的节拍图，B = 60/BPM，放置歌曲时让它的 drop 落在第 8 拍。
3. 3D 盒子使用正交投影：每个面都是一个 1440px 的离屏 canvas，通过仿射变换绘制，按其法线着色。
4. 用 ffmpeg 将视频切成 30fps 的 JPEG 序列，绘制 floor(t*30) 帧，用 ctx.filter 实现黑白效果。
5. 裁去贴纸 PNG 的多余区域，通过膨胀 alpha 通道添加模切边框。
6. 声音：每个事件使用下载的音效（每次选角时的快门声、滑动时的呼啸声、打字时的按键声），按其测得的峰值放置。用 Loudnorm 归一化至 -14 LUFS。
7. 使用 Playwright 以 60fps 渲染，使用 8 个运动模糊子帧。检查单帧闪跳，再与参考视频比较运动表现（每秒硬跳次数、静止帧比例）。
</build>

<gotchas>
每拍只转动一格的图案看起来会卡顿：让它持续旋转，并选择每个圆环的速度，使其在最后一帧回到相同图案。4 个子帧在快速甩镜时会产生重影，因此使用 8 个。以巨大铺屏圆为背景的图层，即使向下滑动一个画面高度仍会覆盖屏幕，所以圆铺满画面后要将其切换成全画面矩形。计数器读取整帧时间，而非子帧时间。圆盘必须在它离开的场景所使用的同一个镜头变换中变形，否则会跳动。
</gotchas>

<start>
先向我询问输入资料，再在渲染前向我展示节拍图和 6 张静帧（开场、盒子、简报、选角、手机、海报）。
</start>
```

<a id="zh-tw"></a>
## 繁體中文

AI 譯文，未經人工審校。請對照原文閱讀；翻譯不等於核實來源，也不授予再利用許可。

```text
<inputs> 向我詢問：我的產品名（一個小寫單詞）、一句 4 詞標語、3 步…
```

### 做法

程式碼製作的動畫，錄製為 X 影片

### 核驗狀態

由 yihui-dev/awesome-opus5-5-videos 收錄的原始 X URL · 未獨立重現

### 模型依據（譯文）

```text
引用倉庫將此列於 Claude Opus 5.5 下，並鏈接原帖。屬於上一代主流模型。未獨立復跑。
```

### 公開提示詞（譯文）

```text
<inputs>
請向我詢問：我的產品名（一個小寫單詞）、一條 4 個詞的標語、說明產品作用的 3 步故事、發佈日期和域名、一首有清晰 drop 的免版稅歌曲、4 段竪屏對鏡講話視頻，以及 12 張人像照片。如果我跳過任何項目，使用默認值：“castr”、“ugc ads, cast by ai”、寫一份簡報 → 掃描 1,000 位創作者 → 選定 4 位、Mixkit 的 “Cat Walk”（129.6 BPM，drop 在 29.7s）、免費的 Pexels 視頻與人像，以及 Pixabay 的透明貼紙（精華液、麥克風、擴音器、復古相機、聚光燈、嘴唇）。
</inputs>

<direction>
一部 25 秒的正方形發佈預告片，1440x1440，60fps，醒目張揚的海報風格。鈷藍 #2B3BFF、墨色 #0E0F1F、奶油色 #F6E4C6、粉色 #FF7DC7、橘紅色 #FF5A1F。名稱使用 Archivo 900 的特窄字寬，標題使用加寬字寬，標籤使用 Geist 和 Geist Mono。歐普藝術放射紋、滾動波浪、膠片顆粒。只用真實媒體：視頻在設計中播放，貼紙帶白色模切邊框與柔和陰影。
運動規則：鏡頭永不停止（每個場景都緩慢推近 1.03–1.07）；任何元素都不突然彈出（字母逐個從遮罩線升起）；任何運動都不按節拍突跳（圖案持續旋轉）；切換採用約 0.55s 的輪播式滑動；顏色變化在約 0.35s 內漸變；貼紙緩動入場後繼續緩慢搖擺。字標或任何標題出現後，都不要完全停住。
禁止：按節拍跳變的旋轉、突然彈入砸落、白色閃光、場景之間的交叉淡化、硬切、模板。
</direction>

<structure>
54 拍。歌曲從 drop 前 8 拍開始。
第 0–8 拍：鈷藍放射紋圍繞一個呼吸起伏的奶油色圓盤旋轉。字標伴隨滑動的輸入光標逐字出現，標語膠囊標籤升起。圓盤擴張鋪滿畫面，進入 drop。
第 8 拍，drop：奶油色變成 3D 盒子的一個面，“ONE BRIEF” 逐字母升起。鏡頭拉遠，顯示漂浮在波浪上的盒子。第 12 拍，盒子轉向 “1,000 CREATORS”（堆疊排版，帶描邊重影）；第 14 拍轉向 “ZERO DMs”。
第 16–22 拍：快速甩向深色桌面。橘紅色 “BRIEF #042” 票據逐行打出內容（product、vibe、cast、due），貼紙漂入，一個真實視頻的拍立得畫面落在角上，第 20 拍壓下 “NOW CASTING” 印章。
第 22–34 拍：選角舞台。一群黑白人像呈弧形排列，一個 3D 舞台塊，創作者像輪播一樣滑過。每個人都在一個大圓盤中播放黑白實時視頻，舞台上用粉色顯示名字、粉絲數，以及遞增的 MATCH %。一拍之後，“CAST ✓” 印章落下，視頻逐漸恢復彩色。計數器從 1/4 滾動到 4/4。
第 34–39 拍：粉色從最後一個圓盤湧出。圓盤變成手機屏幕（視頻繼續播放），再呈扇形展開為 4 台手機，播放全部 4 位創作者，觀看數不斷增加。“4 ADS” 和 “BY FRIDAY” 升起。
第 39–44 拍，音樂間奏：粉色地面落下消失，一張奶油色 “JOIN THE WAITLIST” 票據滑落到放射紋上。在弱起拍處，票根被撕掉。
第 44–54 拍：票據主體變成拱形海報。字標升起，接著是標語，然後信息欄以 3 個區塊滑上來（日期、數字、域名），跑馬燈沿畫面邊緣滾動。最後所有內容折回開場圓盤，使最後一幀與第一幀相同。
</structure>

<build>
1. 一個 HTML canvas。每一幀都是 seek(t) 內時間的純函數。
2. 以拍為單位的節拍圖，B = 60/BPM，放置歌曲時讓它的 drop 落在第 8 拍。
3. 3D 盒子使用正交投影：每個面都是一個 1440px 的離屏 canvas，通過仿射變換繪制，按其法線著色。
4. 用 ffmpeg 將視頻切成 30fps 的 JPEG 序列，繪制 floor(t*30) 幀，用 ctx.filter 實現黑白效果。
5. 裁去貼紙 PNG 的多餘區域，通過膨脹 alpha 通道添加模切邊框。
6. 聲音：每個事件使用下載的音效（每次選角時的快門聲、滑動時的呼嘯聲、打字時的按鍵聲），按其測得的峰值放置。用 Loudnorm 歸一化至 -14 LUFS。
7. 使用 Playwright 以 60fps 渲染，使用 8 個運動模糊子幀。檢查單幀閃跳，再與參考視頻比較運動表現（每秒硬跳次數、靜止幀比例）。
</build>

<gotchas>
每拍只轉動一格的圖案看起來會卡頓：讓它持續旋轉，並選擇每個圓環的速度，使其在最後一幀回到相同圖案。4 個子幀在快速甩鏡時會產生重影，因此使用 8 個。以巨大鋪屏圓為背景的圖層，即使向下滑動一個畫面高度仍會覆蓋屏幕，所以圓鋪滿畫面後要將其切換成全畫面矩形。計數器讀取整幀時間，而非子幀時間。圓盤必須在它離開的場景所使用的同一個鏡頭變換中變形，否則會跳動。
</gotchas>

<start>
先向我詢問輸入資料，再在渲染前向我展示節拍圖和 6 張靜幀（開場、盒子、簡報、選角、手機、海報）。
</start>
```

<a id="ja"></a>
## 日本語

AI 翻訳であり、人による校閲は未実施です。原文と併せてお読みください。翻訳は出典の検証や再利用の許諾を意味しません。

```text
<inputs> 私に尋ねること：製品名（小文字の1語）、4語のキャッチコピー、3段階の…
```

### 制作方法

コードで制作したアニメーションを X の動画として収録

### 検証状況

yihui-dev/awesome-opus5-5-videos に掲載された原投稿の X URL · 独立した再実行なし

### モデルの根拠（翻訳）

```text
引用元リポジトリではClaude Opus 5.5に分類し、元投稿へリンク。前世代の主流モデル。独立した再実行は未実施。
```

### 公開プロンプト（翻訳）

```text
<inputs>
次の項目を私に尋ねてください：製品名（小文字の単語 1 つ）、4 語のタグライン、製品の働きを示す 3 ステップのストーリー、公開日とドメイン、明確なドロップのあるロイヤリティフリー楽曲、カメラに向かって話す縦動画 4 本、ポートレート写真 12 枚。省略した項目には次のデフォルトを使ってください：“castr”、“ugc ads, cast by ai”、ブリーフを書く → 1,000 人のクリエイターをスキャン → 4 人をキャスティング、Mixkit の “Cat Walk”（129.6 BPM、29.7s にドロップ）、無料の Pexels 動画とポートレート、Pixabay の透過ステッカー（美容液、マイク、メガホン、ビンテージカメラ、スポットライト、唇）。
</inputs>

<direction>
25 秒の正方形ローンチトレーラー。1440x1440、60fps、強烈なポスタースタイル。コバルト #2B3BFF、インク #0E0F1F、クリーム #F6E4C6、ピンク #FF7DC7、タンジェリン #FF5A1F。名前は Archivo 900 の極端に狭い字幅、見出しは広い字幅、ラベルは Geist と Geist Mono。オプアートのサンバースト、スクロールする波、フィルムグレイン。実写素材のみを使い、動画はデザインの中で再生し、ステッカーには白いダイカットの縁と柔らかな影を付けます。
動きのルール：カメラは止めない（各シーンでゆっくり 1.03～1.07 の寄り）。突然ポップインさせない（文字をマスクの線から 1 つずつせり上げる）。ビートに合わせて瞬間的に動かさない（模様は連続回転）。入れ替えは約 0.55s のカルーセル状の滑り。色の変化は約 0.35s のフェード。ステッカーはイーズインした後もゆっくり揺れ続けます。ワードマークやどの見出しの後にも完全な停止を入れません。
禁止：ビートごとに跳ぶ回転、突然飛び込む叩きつけ、白いフラッシュ、シーン間のクロスフェード、ハードカット、テンプレート。
</direction>

<structure>
54 拍。曲はドロップの 8 拍前から始めます。
0～8 拍：呼吸するクリーム色の円盤を中心に、コバルト色のサンバーストが回転します。滑るキャレットとともにワードマークがタイプされ、タグラインのピルがせり上がります。円盤が画面を満たしてドロップへつなぎます。
8 拍、ドロップ：クリーム色が 3D ボックスの面となり、“ONE BRIEF” が 1 文字ずつせり上がります。カメラが引くと、波の上に浮かぶボックスが見えます。12 拍で “1,000 CREATORS”（積み重ねた組版と輪郭線の残響）へ、14 拍で “ZERO DMs” へ回転します。
16～22 拍：暗いデスクへ素早く振ります。タンジェリン色の “BRIEF #042” チケットに各行（product、vibe、cast、due）がタイプされ、ステッカーが漂って入り、実写クリップのポラロイドが角に落ちます。20 拍で “NOW CASTING” スタンプが押されます。
22～34 拍：キャスティングのステージ。白黒のポートレート群を弧状に並べ、3D のステージブロックを置き、クリエイターたちがカルーセルのように滑って通ります。各人が大きな円盤の中で白黒の動画として再生され、ステージにはピンクの名前、フォロワー数、数値が上がる MATCH % を表示します。1 拍後に “CAST ✓” スタンプが着地し、動画がカラーへフェードします。カウンターが 1/4 から 4/4 へ回ります。
34～39 拍：最後の円盤からピンクがあふれ出します。円盤がスマートフォンの画面に変形し（動画は再生を継続）、扇状に 4 台のスマートフォンへ広がります。4 人全員の動画が再生され、再生回数が増えていきます。“4 ADS” と “BY FRIDAY” がせり上がります。
39～44 拍、曲のブレイク：ピンクの床が落ちて消え、クリーム色の “JOIN THE WAITLIST” チケットがサンバーストの上へ滑り下ります。ピックアップで半券がちぎれます。
44～54 拍：チケット本体がアーチ状のポスターに変形します。ワードマーク、タグラインの順にせり上がり、次に情報バーが 3 ブロック（日付、数字、ドメイン）で滑り上がり、ティッカーが画面の縁を巡ります。最後にすべてが冒頭の円盤へ折りたたまれ、最終フレームが最初のフレームと一致します。
</structure>

<build>
1. HTML canvas を 1 つ。各フレームは seek(t) 内の時間の純粋関数です。
2. 拍単位のビートマップ。B = 60/BPM とし、曲のドロップが 8 拍目に来るように配置します。
3. 3D ボックスは正投影。各面を 1440px のオフスクリーン canvas として、アフィン変換で描き、法線に基づいて陰影を付けます。
4. ffmpeg で動画を 30fps の JPEG シーケンスに切り出し、floor(t*30) フレームを描画します。白黒化は ctx.filter で行います。
5. ステッカー PNG をトリミングし、アルファを膨張させてダイカットの縁を加えます。
6. 音：各イベントにダウンロードした SFX を使います（キャスティングごとにシャッター、滑りに風切り音、入力にキーのクリック）。それぞれ測定したピークを基準に配置します。Loudnorm で -14 LUFS にします。
7. Playwright で 60fps、モーションブラー用の 8 サブフレームを使ってレンダリングします。単一フレームの飛び出しを走査し、参考動画と動きを比較します（1 秒あたりの急な飛びの数、静止フレームの割合）。
</build>

<gotchas>
1 拍ごとに 1 目盛りずつ回る模様はカクついて見えます。連続回転させ、各リングの速度を、最後のフレームで同じ模様に戻るように選んでください。4 サブフレームでは速い振りに残像が出るため、8 を使います。背景が巨大な塗りつぶし円のレイヤーは、画面 1 枚分の高さだけ下へ動かしても画面を覆い続けます。円が画面を満たしたら全画面の矩形へ切り替えてください。カウンターはサブフレームではなくフレームの時刻を読みます。円盤は去るシーンと同じカメラ変換の中で変形させなければ、位置が跳びます。
</gotchas>

<start>
入力資料を私に尋ね、その後、レンダリングの前にビートマップと 6 枚の静止画（冒頭、ボックス、ブリーフ、キャスティング、スマートフォン、ポスター）を見せてください。
</start>
```

<a id="ko"></a>
## 한국어

사람의 검수를 거치지 않은 AI 번역입니다. 원문과 함께 읽어 주세요. 번역은 출처 검증이나 재사용 허가를 의미하지 않습니다.

```text
<inputs> 제품 이름(소문자 단어 하나), 4단어 태그라인, 3단계…를 물어봐(원문 잘림)
```

### 제작 방법

코드로 만든 애니메이션을 X 영상으로 캡처

### 검증 상태

yihui-dev/awesome-opus5-5-videos에 기재된 1차 X URL, 독립적으로 다시 실행하지 않음

### 모델 근거 (번역)

```text
인용 저장소는 Claude Opus 5.5 항목에 수록하고 원 게시물로 연결. 이전 주류 세대. 독립적으로 다시 실행하지 않음
```

### 공개 프롬프트 (번역)

```text
<inputs>
제품명(소문자 한 단어), 네 단어 슬로건, 기능을 설명하는 3단계 이야기, 출시일과 도메인, 드롭이 뚜렷한 로열티 프리 곡, 카메라를 보며 말하는 세로 클립 4개, 인물 세로 사진 12장을 요청하세요. 생략된 항목은 기본값을 사용하세요. “castr”, “ugc ads, cast by ai”, 브리프 작성 → 크리에이터 1,000명 탐색 → 4명 캐스팅, Mixkit “Cat Walk”(129.6 BPM, 드롭 29.7초), 무료 Pexels 클립과 인물 사진, Pixabay의 투명 스티커(세럼, 마이크, 메가폰, 빈티지 카메라, 스포트라이트, 입술).
</inputs>

<direction>
25초 정사각형 출시 예고편, 1440x1440, 60fps, 강렬한 포스터 스타일. 코발트 #2B3BFF, 잉크 #0E0F1F, 크림 #F6E4C6, 분홍 #FF7DC7, 탠저린 #FF5A1F. 이름은 Archivo 900 extra-condensed, 헤드라인은 폭을 넓히고 라벨은 Geist와 Geist Mono를 사용하세요. 옵아트 방사형 무늬, 스크롤하는 물결, 필름 그레인. 실제 미디어만 사용하세요. 클립은 디자인 안에서 재생되며 스티커에는 흰 다이컷 테두리와 부드러운 그림자를 추가합니다.
움직임 규칙: 카메라는 멈추지 않습니다(모든 장면에서 느린 1.03~1.07배 전진). 갑자기 나타나는 것은 없습니다(글자가 마스크 선을 통해 하나씩 올라옵니다). 박자에 맞춰 뚝뚝 바뀌지 않습니다(패턴은 계속 회전). 교체는 약 0.55초의 캐러셀 미끄러짐이며 색 변화는 약 0.35초에 걸쳐 페이드합니다. 스티커는 부드럽게 들어온 뒤 천천히 계속 흔들립니다. 워드마크나 헤드라인 뒤에도 완전히 멈추지 않습니다.
금지: 박자에 맞춰 끊기는 회전, 갑자기 튀어나와 부딪히는 등장, 흰 플래시, 장면 사이 크로스페이드, 하드 컷, 템플릿.
</direction>

<structure>
54박. 곡은 드롭 8박 전에 시작합니다.
0~8박: 호흡하듯 움직이는 크림색 원판 주위로 코발트 방사형 무늬가 돕니다. 미끄러지는 캐럿과 함께 워드마크가 타이핑되고 슬로건 알약이 올라옵니다. 원판이 화면을 채우며 드롭으로 이어집니다.
8박, 드롭: 크림색이 3D 상자의 면이 되고 “ONE BRIEF”가 한 글자씩 올라옵니다. 카메라가 물러나 물결 위에 떠 있는 상자를 보여 줍니다. 12박에 “1,000 CREATORS”(겹쳐 쌓인 글자, 외곽선 잔상)로, 14박에 “ZERO DMs”로 회전합니다.
16~22박: 어두운 책상으로 빠르게 이동합니다. 탠저린색 “BRIEF #042” 티켓이 행(product, vibe, cast, due)을 타이핑하고 스티커가 떠들어오며, 실제 클립의 폴라로이드가 모서리에 떨어집니다. 20박에 “NOW CASTING” 도장이 찍힙니다.
22~34박: 캐스팅 무대. 호 모양의 흑백 인물 사진 군중, 3D 무대 블록, 캐러셀처럼 미끄러져 지나가는 크리에이터. 각자의 영상이 커다란 원판 안에서 흑백으로 재생되고 무대에는 분홍색 이름, 팔로워 수, 올라가는 MATCH %가 표시됩니다. 한 박 뒤 “CAST ✓” 도장이 찍히고 클립이 컬러로 바뀝니다. 카운터는 1/4에서 4/4로 넘어갑니다.
34~39박: 마지막 원판에서 분홍색이 퍼집니다. 원판은 휴대폰 화면으로 변하고(클립은 계속 재생), 부채꼴의 휴대폰 4개로 펼쳐져 크리에이터 4명의 영상이 모두 재생되고 조회 수가 올라갑니다. “4 ADS”와 “BY FRIDAY”가 올라옵니다.
39~44박, 음악의 브레이크: 분홍 바닥이 내려가 사라지고 크림색 “JOIN THE WAITLIST” 티켓이 방사형 무늬 위로 미끄러져 내려옵니다. 음악이 다시 들어오는 타이밍에 티켓의 절취 부분이 뜯어집니다.
44~54박: 티켓 본체가 포스터 아치로 변합니다. 워드마크와 슬로건이 차례로 올라오고, 정보 바가 3개 블록(날짜, 숫자, 도메인)으로 미끄러져 올라오며 티커가 화면 가장자리를 돕니다. 이후 모두 처음의 원판으로 접혀 마지막 프레임이 첫 프레임이 됩니다.
</structure>

<build>
1. HTML canvas 하나. 모든 프레임은 seek(t) 안에서 시간의 순수 함수로 계산합니다.
2. 박자 단위 비트 맵, B = 60/BPM. 곡의 드롭이 8박에 맞도록 배치합니다.
3. 3D 상자는 직교 투영입니다. 각 면은 1440px 오프스크린 canvas로, 아핀 변환으로 그리고 법선에 따라 음영 처리합니다.
4. ffmpeg로 클립을 30fps JPEG 시퀀스로 자르고 floor(t*30) 프레임을 그리며 ctx.filter로 흑백 처리합니다.
5. 스티커 PNG의 여백을 자르고 알파를 팽창시켜 다이컷 테두리를 추가합니다.
6. 사운드: 이벤트마다 다운로드한 SFX를 사용하고(캐스팅마다 셔터, 미끄러짐에 휙 소리, 타이핑에 키 클릭), 측정한 피크에 맞춰 배치합니다. Loudnorm으로 -14 LUFS에 맞춥니다.
7. Playwright로 60fps, 모션 블러 하위 프레임 8개로 렌더링합니다. 한 프레임만 튀는 현상을 검사한 다음 참고 영상과 움직임을 비교합니다(초당 급격한 점프, 정지 프레임 비율).
</build>

<gotchas>
매 박 한 칸씩 회전하는 패턴은 끊겨 보입니다. 연속 회전시키고 각 링의 속도를 마지막 프레임에서 같은 패턴에 도달하도록 정하세요. 하위 프레임 4개는 빠른 휩에서 잔상이 생기므로 8개를 사용하세요. 배경이 거대한 확장 원인 레이어는 화면 높이만큼 내려가도 화면을 덮으므로, 화면을 채운 뒤에는 전체 화면 사각형으로 바꾸세요. 카운터는 하위 프레임이 아닌 해당 프레임의 시간을 읽습니다. 원판은 떠나는 장면과 같은 카메라 변환 안에서 변형해야 합니다. 그렇지 않으면 튑니다.
</gotchas>

<start>
입력을 요청한 다음, 렌더링 전에 비트 맵과 정지 이미지 6장(시작, 상자, 브리프, 캐스팅, 휴대폰, 포스터)을 보여 주세요.
</start>
```
