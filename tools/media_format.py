#!/usr/bin/env python3
"""Detect real image/video formats. Prefer ffprobe for MP4; fall back to ISO-BMFF."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

IMAGE_EXTS = {"gif", "png", "jpg", "jpeg", "webp"}
VIDEO_EXTS = {"mp4"}
ANIMATED_ROLES = {"gif", "x-dynamic", "dynamic"}
STILL_ROLES = {"still", "poster", "reference", "sheet", "ref"}


def ffprobe_bin() -> str | None:
    return shutil.which("ffprobe")


def looks_like_html(data: bytes) -> bool:
    head = data[:1024].lstrip().lower()
    return (
        head.startswith(b"<!doctype")
        or head.startswith(b"<html")
        or head.startswith(b"<head")
        or (head.startswith(b"<") and b"<html" in head)
    )


def _u32(data: bytes, off: int) -> int:
    return int.from_bytes(data[off : off + 4], "big")


def _iter_boxes(data: bytes, start: int = 0, end: int | None = None):
    if end is None:
        end = len(data)
    off = start
    while off + 8 <= end:
        size = _u32(data, off)
        typ = data[off + 4 : off + 8]
        if size == 1:
            if off + 16 > end:
                break
            size = int.from_bytes(data[off + 8 : off + 16], "big")
            hdr = 16
        elif size == 0:
            yield typ, off + 8, end
            break
        else:
            hdr = 8
        if size < 8:
            break
        box_end = off + size
        if box_end > end or box_end <= off:
            break
        yield typ, off + hdr, box_end
        off = box_end


def _trak_is_video(data: bytes, start: int, end: int) -> bool:
    for typ, payload, box_end in _iter_boxes(data, start, end):
        if typ == b"mdia":
            for t2, p2, e2 in _iter_boxes(data, payload, box_end):
                if t2 == b"hdlr" and e2 - p2 >= 12:
                    handler = data[p2 + 8 : p2 + 12]
                    if handler == b"vide":
                        return True
    return False


def _scan_moov(data: bytes, start: int, end: int) -> tuple[bool, float]:
    video = False
    duration = 0.0
    for typ, payload, box_end in _iter_boxes(data, start, end):
        if typ == b"mvhd" and box_end - payload >= 20:
            ver = data[payload]
            if ver == 0 and box_end - payload >= 20:
                timescale = _u32(data, payload + 12)
                dur = _u32(data, payload + 16)
                if timescale:
                    duration = dur / timescale
            elif ver == 1 and box_end - payload >= 32:
                timescale = _u32(data, payload + 20)
                dur = int.from_bytes(data[payload + 24 : payload + 32], "big")
                if timescale:
                    duration = dur / timescale
        elif typ == b"trak" and _trak_is_video(data, payload, box_end):
            video = True
    return video, duration


def parse_iso_bmff(path: Path) -> dict:
    data = path.read_bytes()
    if len(data) < 16:
        raise ValueError(f"{path}: too short to be MP4")
    if looks_like_html(data):
        raise ValueError(f"{path}: HTML payload, not MP4")
    if data.lstrip().startswith(b"{") or data.lstrip()[:5].lower() == b"<?xml":
        raise ValueError(f"{path}: text/JSON/XML payload, not MP4")
    has_ftyp = False
    has_moov = False
    has_mdat = False
    video = False
    duration = 0.0
    brands: list[str] = []
    for typ, payload, box_end in _iter_boxes(data):
        if typ == b"ftyp":
            has_ftyp = True
            if box_end - payload >= 4:
                brands.append(data[payload : payload + 4].decode("latin1", "replace"))
        elif typ == b"moov":
            has_moov = True
            video, duration = _scan_moov(data, payload, box_end)
        elif typ == b"mdat":
            has_mdat = True
    if not has_ftyp:
        raise ValueError(f"{path}: missing ISO-BMFF ftyp box")
    if not has_moov and not has_mdat:
        raise ValueError(f"{path}: missing moov/mdat")
    if has_moov and not video:
        raise ValueError(f"{path}: no vide track in moov")
    return {
        "container": "iso-bmff",
        "has_video": bool(video or has_mdat),
        "duration": duration,
        "brands": brands,
        "via": "iso-bmff",
    }


def probe_mp4_ffprobe(path: Path) -> dict:
    exe = ffprobe_bin()
    if not exe:
        raise FileNotFoundError("ffprobe not on PATH")
    cmd = [
        exe,
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=codec_type,codec_name,duration,width,height",
        "-show_entries",
        "format=duration,format_name",
        "-of",
        "json",
        str(path),
    ]
    raw = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=45)
    info = json.loads(raw.decode("utf-8", "replace") or "{}")
    streams = info.get("streams") or []
    if not streams:
        raise ValueError(f"{path}: ffprobe found no video stream")
    st = streams[0]
    if st.get("codec_type") != "video":
        raise ValueError(f"{path}: ffprobe stream is {st.get('codec_type')!r}, not video")
    fmt = info.get("format") or {}
    dur_s = st.get("duration") or fmt.get("duration") or 0
    try:
        duration = float(dur_s)
    except (TypeError, ValueError):
        duration = 0.0
    width = int(st.get("width") or 0)
    height = int(st.get("height") or 0)
    if duration <= 0 and (width <= 0 or height <= 0):
        raise ValueError(f"{path}: ffprobe video has no duration or frame size")
    return {
        "container": fmt.get("format_name") or "mp4",
        "codec": st.get("codec_name") or "",
        "has_video": True,
        "duration": duration,
        "width": width,
        "height": height,
        "via": "ffprobe",
    }


def probe_mp4(path: Path) -> dict:
    data = path.read_bytes()
    if looks_like_html(data):
        raise ValueError(f"{path}: HTML payload, not MP4")
    if ffprobe_bin():
        return probe_mp4_ffprobe(path)
    return parse_iso_bmff(path)


def probe_image(path: Path, *, require_animated: bool = False) -> dict:
    from PIL import Image

    data = path.read_bytes()
    if looks_like_html(data):
        raise ValueError(f"{path}: HTML payload, not an image")
    with Image.open(path) as im:
        fmt = (im.format or "").upper()
        n_frames = int(getattr(im, "n_frames", 1) or 1)
        animated = bool(getattr(im, "is_animated", False) or n_frames > 1)
        im.load()
        size = im.size
    if require_animated and not animated:
        raise ValueError(f"{path}: GIF/role requires multiple frames, got {n_frames}")
    return {
        "format": fmt,
        "n_frames": n_frames,
        "animated": animated,
        "size": size,
        "via": "pillow",
    }


def probe_media(path: Path, *, ext: str = "", role: str = "") -> dict:
    """Validate that *path* is a real media file matching ext/role semantics."""
    ext = (ext or path.suffix.lstrip(".")).lower()
    role = (role or "").lower()
    if ext == "mp4" or role in {"x-dynamic", "dynamic"} and ext in VIDEO_EXTS:
        return probe_mp4(path)
    if ext == "gif" or role == "gif":
        return probe_image(path, require_animated=True)
    if ext in IMAGE_EXTS:
        return probe_image(path, require_animated=False)
    if ext in VIDEO_EXTS:
        return probe_mp4(path)
    raise ValueError(f"{path}: unsupported media ext {ext!r} role {role!r}")
