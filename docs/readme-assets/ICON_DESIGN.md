# AI Model Showcases icon

## Direction

The repository is an independent, source-first collection of AI production cases across model families, not an image generator and not a single vendor's product. The new mark uses two exhibit cards to suggest a curated collection. The play-shaped aperture keeps the collection's animation and interactive-demo focus. It removes the previous looping arrow and sparkle so the silhouette stays clear at small sizes.

The palette follows the existing gallery: ink navy `#10131a`, chartreuse `#c2ff67`, and lavender `#a69dff`. The generated raster has slight tonal variation rather than perfectly uniform swatches. No vendor logos or model names are used. This is project branding artwork, not a cataloged model-output case.

## Files

- `project-icon.png`: original generated 1254 × 1254 RGBA PNG.
- `project-icon-512.png`: recommended README/project image, 512 × 512 PNG.
- `project-icon-256.png`: compact general-purpose web image.
- `project-icon-180.png`: Apple touch icon size.
- `project-icon-112.png`: README display-size reference.
- `project-icon-64.png`, `project-icon-48.png`, `project-icon-32.png`, `project-icon-16.png`: mechanical downscaled exports.
- `favicon.ico`: 16, 32, 48, 64, 128 and 256 pixel icon frames.
- `icon-size-check.png`: visual QA sheet, light background above and dark below. Columns are 16, 32, 48, 64 and 112 pixels at native display size.
- `generation-prompt.txt`: full image-generation brief.

All exported PNGs preserve transparency outside the rounded navy tile. ImageMagick was used only to export sizes and make the inspection sheet; the artwork itself was generated with the built-in image generation tool.

## QA result

Visually inspected the original and the 16–112px comparison sheet. The chartreuse card and dark triangular aperture remain recognizable even at 16px. The lavender offset is subtle at 16px and becomes distinct at 32px and larger. White and dark-page backgrounds both retain strong central contrast. There is no small text or thin decoration to disappear.

## Integration

Copy `project-icon-512.png` to `docs/readme-assets/project-icon.png` to replace the existing shared README asset without changing all references. Suggested alt text: `AI Model Showcases: layered exhibit cards with a play aperture`.

Use 32px PNG or the ICO as a website favicon, and the 180px PNG for Apple touch if desired. Keep this branding out of the real-case media inventory.

## Reviewed sources

- https://github.com/jammyfu/awesome-ai-model-showcases/blob/main/PROJECT_BRIEF.md
- https://github.com/jammyfu/awesome-ai-model-showcases/blob/main/README.md
- https://github.com/jammyfu/awesome-ai-model-showcases/blob/main/docs/styles.css
- https://github.com/jammyfu/awesome-ai-model-showcases/blob/main/docs/brand-artwork.md
- https://github.com/jammyfu/awesome-ai-model-showcases/blob/main/docs/readme-assets/project-icon.png
