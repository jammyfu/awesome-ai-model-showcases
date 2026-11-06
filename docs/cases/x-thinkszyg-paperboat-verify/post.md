# x-thinkszyg-paperboat-verify

- Author: @thinkszyg
- Source: https://x.com/thinkszyg/status/2118166234495947044
- Model: 作者声明 2.6：ChatGPT 上了 Images 2.6…GIF 是 2.6 才有的能力，老版本只会给你一张静态图。
- Pipeline: 作者称直出 GIF · X 附件实际 MP4
- Verification: 作者声明 + 媒体元数据已核 · 未观看 · 未复测
- Workflow: 复制测试句直接要 GIF；另提供「六宫格分镜」提示词模板（作者说明是从官方示例拆出）——注意六宫格本身是静图工作流，需另合成才成动图，与原生 GIF 直出要区分。

## Play / 玩法

用纸船循环 GIF 验证账号是否已推送 Images 2.6；并附六宫格 sprite sheet 提示词模板

## Original post text

ChatGPT 上了 Images 2.6，出图快了 50%，还能直接做 GIF。可界面里不会告诉你用的是哪个模型，看了一遍官方文档，找到一个最省事的验证办法：让它做一个 GIF。

GIF 是 2.6 才有的能力，老版本只会给你一张静态图。把这句复制进去试试：

Make a looping GIF of a paper boat bobbing on the water.

出来的纸船会动，点开还能调播放速度，就说明你已经在用 2.6 了。如果只拿到一张静态图，说明还没推到你的账号，官方原话是「正在陆续推送」，晚点再试。

还有一个办法也能确认：存参考图。比如把自家狗的照片存成 Pepper，以后新开对话直接写 @ Pepper 就能用，不用再上传一次。这个功能也是这次一起上线的。

用 API 的朋友不用猜，模型名直接写 GPT-Image-2.6 Flare 或 GPT-Image-2.6 Sunburst。Flare 在低质量档最快 6 秒出一张，适合先批量出草图挑方向；Sunburst 用在中高质量档，改好几轮之后，人物衣服和产品细节更不容易走样，适合出终稿。

确认完版本，还有两个地方容易出错。

第一，SVG 导出目前只写在 API 的更新里，ChatGPT 的更新说明没提。在 ChatGPT 里让它出 SVG，大概率拿到的还是 PNG。

第二，ChatGPT 改不了你自己上传的 GIF。想改动画，就回到生成它的那个对话里接着说，把要改的地方讲具体，比如「第三帧的手抬高一点」。

最后送一个从官方示例里拆出来的 GIF 提示词结构，把方括号里的内容换成你自己的就能用：

Create a single animation sprite sheet for a seamless looping GIF. [角色长什么样] [动作从头到尾依次发生什么]. Exactly 6 sequential frames arranged in a precise 3-column by 2-row grid, read left-to-right then top-to-bottom. Every panel has identical dimensions. Fixed camera, same character, same outfit, same background. The sixth frame transitions smoothly toward the first. [画风]. No captions, no words, no borders.

这段的门道在后半截：固定机位、同一个角色、第 6 帧接回第 1 帧。这三条管的是动画不跳、角色不变脸。就像拍定格动画，中途相机挪一下，整段就穿帮了。

先用纸船那句测一下版本，能动的话就把上面这个模板存进备忘录，下次做表情包或者品牌小动画，换个角色描述就能直接出。

## Notes / process

测试句与仓库/社区常见官方示例句相近；六宫格模板与路飞「六帧再合成」玩法同族，需在入库时标注 workflow 差异。
