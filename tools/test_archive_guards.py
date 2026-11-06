#!/usr/bin/env python3
"""Fault-injection guards: HTML-as-MP4 and WRONG PROMPT must fail."""
from __future__ import annotations

import hashlib
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from ingest_local_media import reject_download_payload  # noqa: E402
from media_format import probe_media  # noqa: E402
from validate_local_media import UNPUBLISHED_MARK, check_prompt_archive  # noqa: E402

HTML_AS_MP4 = b"""<!DOCTYPE html>
<html><head><title>not a video</title></head>
<body><p>WRONG MEDIA pretending to be MP4</p></body></html>
"""


def expect_fail(fn, *args, **kwargs) -> str:
    try:
        fn(*args, **kwargs)
    except Exception as exc:
        return str(exc)
    raise AssertionError(f"{fn.__name__} unexpectedly passed")


def test_html_as_mp4_probe() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "01-dynamic.mp4"
        path.write_bytes(HTML_AS_MP4)
        digest = hashlib.sha256(HTML_AS_MP4).hexdigest()
        # Even with matching hash/size/ext, format probe must reject HTML.
        assert path.stat().st_size == len(HTML_AS_MP4)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest
        msg = expect_fail(probe_media, path, ext="mp4", role="x-dynamic")
        assert "HTML" in msg or "ftyp" in msg or "video" in msg, msg


def test_ingest_rejects_wrong_content_type() -> None:
    err = reject_download_payload("text/html; charset=utf-8", HTML_AS_MP4)
    assert err, "HTML content-type must be rejected"
    err2 = reject_download_payload("video/mp4", HTML_AS_MP4)
    assert err2, "HTML body with video/mp4 content-type must be rejected"
    err3 = reject_download_payload("application/json", b'{"ok":true}')
    assert err3, "JSON content-type must be rejected"
    ok = reject_download_payload("video/mp4", b"\x00\x00\x00\x18ftypiso5" + b"\x00" * 64)
    assert not ok, ok


def test_wrong_prompt_fails() -> None:
    src = "Make a looping GIF of a paper boat bobbing on the water."
    heading_only = "# Original prompt\n\n"
    msg = expect_fail(check_prompt_archive, "web-paper-boat", heading_only, [src])
    assert "heading" in msg.lower() or "missing" in msg.lower(), msg
    wrong = "# Original prompt\n\nWRONG PROMPT\n"
    msg2 = expect_fail(check_prompt_archive, "web-paper-boat", wrong, [src])
    assert "WRONG PROMPT" not in src
    assert "missing" in msg2.lower() or "full source" in msg2.lower(), msg2
    title_bypass = "# Original prompt\n\nOriginal prompt\n"
    expect_fail(check_prompt_archive, "demo", title_bypass, [src])


def test_unpublished_requires_marker() -> None:
    expect_fail(check_prompt_archive, "game-empty", "# Original prompt\n\n", [""])
    check_prompt_archive("game-empty", f"# Original prompt\n\n{UNPUBLISHED_MARK}\n", [""])


def test_full_source_and_ideas_pass() -> None:
    src = "Make a looping GIF of this character waving."
    check_prompt_archive("krouxzz-wave-ref", f"# Original prompt\n\n{src}\n", [src])
    otter = "生成一个约 1 秒、可循环播放的 GIF 聊天表情。"
    check_prompt_archive(
        "luffy-x-article",
        f"# Original prompts from the Luffy article\n\n## 雨衣\n\n{otter}\nmore\n",
        [otter],
    )


def main() -> int:
    test_html_as_mp4_probe()
    test_ingest_rejects_wrong_content_type()
    test_wrong_prompt_fails()
    test_unpublished_requires_marker()
    test_full_source_and_ideas_pass()
    print("archive guards ok: HTML-as-MP4 fails, WRONG PROMPT fails, unpublished marker required")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
