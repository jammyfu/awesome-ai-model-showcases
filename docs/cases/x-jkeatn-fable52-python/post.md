# Source post

https://x.com/jkeatn/status/2119874007382299087

Model claim: Feishu AIGCreative wiki lists this under Claude Fable 5.2. The linked X post is the original page. Not independently re-run.

Discovery: via 飞书 AIGCreative wiki
https://aigcreative.feishu.cn/wiki/ZB58w4kilimVTPkIosFcN2N4nnd
Wiki section: 影像叙事、音乐与视觉实验｜23 例 / 02｜程序化图形（1 例）

## Wiki titles

- 用 Python 模拟画笔，按虚构画家风格作画

## Wiki summary (paraphrase, not the original post)

简介　Anthropic 的 Jake Eaton 让 Fable 5.2 为虚构画家设定背景和一贯的风格，再用 Python 逐笔落色。不同画笔的笔触由模拟画笔引擎生成，他会给反馈让模型继续修订。

证据与边界　Eaton 称没有调用图像生成模型，也没有预先渲染或描摹。约 70 万笔来自同一系列的一次拟摄影实验，属于该幅作品的自述数字。

## Original post text

for the past few weeks, I’ve been exploring painting with Fable 5.2 in code. one of the most common critiques I heard about Opus 5.5’s paintings was that it was only emulating real art. I thought that was fair, so i’ve been asking Fable 5.2 to develop personas—artists with some sort of a back story and a consistent style roughly identifiable in time

not knowing what to expect, i’ve watched this project evolve in directions i never predicted. I give comments or steers, and Claude updates or revises the engines that power the brushes and paint. where paintings come up i like or find intriguing, i ask it to go deeper. these are some favorites.

each of these is a python program, some one to two thousand lines of code, that places every stroke through a simulated paint engine with different bristles. most take a few thousand strokes, but i’ve pushed much higher with varying results. Claude does not use an image model, nor render or trace in advance
