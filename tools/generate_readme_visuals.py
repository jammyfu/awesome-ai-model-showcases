#!/usr/bin/env python3
"""Generate README hero/icon PNGs from the real stack. No SVG fallback. No paid API."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/readme-assets"
W, H = 1500, 500


def font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).is_file():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (W, H), "#10131a")
    draw = ImageDraw.Draw(img)
    for i in range(H):
        mix = int(16 + (36 - 16) * (i / H))
        draw.line([(0, i), (W, i)], fill=(mix, mix + 4, mix + 14))
    draw.rectangle((36, 36, W - 36, H - 36), outline="#c2ff67", width=3)
    draw.text((72, 86), "AWESOME GPT IMAGE GIFS", font=font(28, True), fill="#c2ff67")
    draw.text((72, 150), "Community case archive", font=font(52, True), fill="#eff3f8")
    draw.text((72, 230), "Real cases  ·  Local media  ·  Original prompts  ·  Sources", font=font(26), fill="#d7deea")
    draw.text((72, 286), "真实案例 · 本地素材 · 原文 prompt · 出处", font=font(24), fill="#a9b2c1")
    chips = ["43 cases", "HTML/CSS/JS", "Python validators", "GitHub Pages", "Pillow"]
    x = 72
    for chip in chips:
        box = draw.textbbox((0, 0), chip, font=font(18, True))
        w = box[2] - box[0] + 28
        draw.rounded_rectangle((x, 360, x + w, 408), radius=8, outline="#c2ff67", width=2)
        draw.text((x + 14, 372), chip, font=font(18, True), fill="#c2ff67")
        x += w + 14
    img.save(OUT / "hero-wide.png", "PNG")

    icon = Image.new("RGB", (256, 256), "#0d1018")
    d = ImageDraw.Draw(icon)
    d.rounded_rectangle((10, 10, 246, 246), radius=40, outline="#c2ff67", width=6)
    d.text((78, 62), "G", font=font(140, True), fill="#c2ff67")
    icon.save(OUT / "project-icon.png", "PNG")
    print("wrote", OUT / "hero-wide.png", OUT / "project-icon.png")


if __name__ == "__main__":
    main()
