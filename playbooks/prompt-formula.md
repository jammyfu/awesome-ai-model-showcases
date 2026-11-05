# Short-loop GIF Prompt Formula / 可复用提示词结构

```
Create a seamless looping GIF of [ORIGINAL SUBJECT], in [STYLE].
Beat 1: [starting pose]. Beat 2: [one primary movement]. Beat 3: [reaction / pause]. Beat 4: [return precisely to original pose].
Fixed camera and lighting. Keep [identity, geometry, clothes, background] exactly the same across all frames.
No additional limbs, object morphing, camera cuts, watermark, text, or logos.
```

Recommended first test: 9 frames × 180–200ms. For a character reaction: 12 × 140–180ms. For product details prefer Sunburst; for simple graphical loops begin with Flare. These are author recommendations, not measured performance benchmarks.

## Failure checklist / 失败诊断

1. **Jump-cut loop:** return the body/object/lighting to the first pose; avoid irreversible movements.
2. **Anatomy drift:** simplify limb count and restrict moving area to one joint.
3. **Background drift:** demand a locked camera and unchanged props.
4. **Text flicker:** use few, short words; inspect every frame; consider adding typography separately in post.
5. **Storyboard mistaken for GIF:** verify actual file extension and frames; a sprite sheet PNG is not a GIF.
6. **GIF large filesize:** reduce canvas size, frame count, colors or timing; verify loop and color banding after compression.
7. **Image reference rights:** have consent / license; an open repository does not grant rights to contributed character likenesses.

## API reference

https://developers.openai.com/api/docs/guides/image-generation

The official documentation currently notes `output_format: gif` for image generation. Do not assume the separate image-edit endpoint can output GIFs. API frame count maximum may differ from guide documentation; test your account's actual validation before batching.
