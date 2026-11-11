# Source post

https://x.com/ericmaskfr/status/2119910195325481026

Model claim: Feishu AIGCreative wiki lists this under Claude Fable 5.2. The linked X post is the original page. Not independently re-run.

Discovery: via 飞书 AIGCreative wiki
https://aigcreative.feishu.cn/wiki/ZB58w4kilimVTPkIosFcN2N4nnd
Wiki section: 游戏、交互与实时模拟｜38 例 / 04｜有明确操作或机制的游戏样机（12 例）

## Wiki titles

- 80 年代迈阿密风格的开放城市和任务系统

## Wiki summary (paraphrase, not the original post)

简介　作者让 Fable 5.2 做一个开放世界犯罪游戏原型。约两分钟录屏覆盖步行和开车，贴文还列出车辆改装、通缉、比赛与送货任务。

证据与边界　作者称单提示用时 2 小时 14 分钟，并用代码合成车辆和警报等声音。计划价格与实际单次模型费用是两种口径。

## Original post text

GTA 6 isn't out yet. Anthropic's new Fable 5.2 already built me one

one prompt. I was not ready for how close it got to the real thing

an indie studio quotes $90,000 and 8 months for a playable prototype like this. Fable 5.2 did it in 2 hours 14 minutes on a $200 plan

what's in there:

→ on foot: sprint, jump, kick, fists, a pistol with real ammo and reloads
→ crime: a witness calls the cops, the stars stack up to 5, police shoot back
→ cars: jack any car, 3 gears, handbrake, headlights, live traffic and crashes
→ garage: 10 paint jobs, bumpers, 5 wheel sets, rim colors and neon underglow, all paid from your balance
→ missions: a 9-checkpoint race on a timer and a courier run that pays $600
→ the city: 9 districts, sunny day into neon night, a minimap, hidden cash that glows green and a pelican on the pier

even the sound is code. every gunshot, engine and siren is generated in python, zero audio files

the prompt:

"you're a senior game dev. build a third-person open-world crime game in a sunny 80s miami-style city. make the loop tight: walk, fight, steal a car, get chased, earn money, spend it. every system feeds the next: crimes bring heat, heat brings cops, missions pay, money unlocks the garage. cars need weight: gears, skids, real crashes. the city has to feel alive with traffic, people and day into night. no audio files, generate every sound in code. after each system, play it yourself, screenshot it and fix what looks wrong. don't stop until a stranger could play for 10 minutes without hitting a bug"

here's what it built ↓
