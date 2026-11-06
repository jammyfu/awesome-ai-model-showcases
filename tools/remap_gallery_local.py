#!/usr/bin/env python3
"""Point the 12 collected web GIFs at local archived files. Original URLs stay as citations."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "docs/data/local-media-manifest.json").read_text(encoding="utf-8"))
GALLERY = ROOT / "docs/data/gallery.json"
MEDIA = ROOT / "docs/data/media-manifest.json"

by_url = {}
for f in MANIFEST.get("files") or []:
    if f.get("ok") and f.get("ext") == "gif" and f.get("source_url"):
        by_url[f["source_url"]] = f


def to_docs_rel(path: str) -> str:
    return path[len("docs/") :] if path.startswith("docs/") else path


def main() -> None:
    gallery = json.loads(GALLERY.read_text(encoding="utf-8"))
    media = json.loads(MEDIA.read_text(encoding="utf-8"))
    changed = 0
    for item in gallery:
        rec = by_url.get(item.get("image")) or by_url.get(item.get("source_media_url") or "")
        if not rec:
            continue
        item["image"] = to_docs_rel(rec["local_path"])
        item["storage"] = "local"
        item["rights"] = "unknown_archived"
        item["source_media_url"] = rec["source_url"]
        changed += 1
    for item in media.get("items") or []:
        rec = by_url.get(item.get("url"))
        if not rec:
            continue
        item["storage"] = "local"
        item["rights"] = "unknown_archived"
        item["local_path"] = to_docs_rel(rec["local_path"])
        item["sha256"] = rec["sha256"]
        item["bytes"] = rec["bytes"]
        item["content_type"] = "image/gif"
        changed += 1
    GALLERY.write_text(json.dumps(gallery, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    MEDIA.write_text(json.dumps(media, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"remapped {changed} gallery/media records to local archives")


if __name__ == "__main__":
    main()
