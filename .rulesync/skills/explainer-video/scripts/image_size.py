#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Read the width-to-height ratio of a PNG, JPEG or SVG file with the standard library only.

build_video.py uses it to pick the split or stack layout for an image.
Run this file directly to self-check the parsers.
"""

import re
import struct
from pathlib import Path

SVG_TAG = re.compile(rb"<svg\b[^>]*>", re.IGNORECASE)
SVG_ATTR = re.compile(rb"""([\w:-]+)\s*=\s*["']([^"']*)["']""")
SVG_LENGTH = re.compile(rb"\s*([\d.]+)\s*(px)?\s*$")


def aspect(data: bytes) -> float | None:
    """Return width / height of the image bytes, or None when the size cannot be read."""
    size = None
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        size = struct.unpack(">II", data[16:24])  # IHDR comes first
    elif data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data) and data[i] == 0xFF:
            marker, seg = data[i + 1], struct.unpack(">H", data[i + 2 : i + 4])[0]
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):  # SOFn
                h, w = struct.unpack(">HH", data[i + 5 : i + 9])
                size = (w, h)
                break
            i += 2 + seg
    elif tag := SVG_TAG.search(data):
        attrs = dict(SVG_ATTR.findall(tag.group(0)))
        w, h = (SVG_LENGTH.match(attrs.get(k, b"")) for k in (b"width", b"height"))
        if w and h:
            size = (float(w.group(1)), float(h.group(1)))
        elif box := attrs.get(b"viewBox"):
            size = tuple(float(v) for v in box.replace(b",", b" ").split()[2:4])
    if not size or len(size) != 2 or not size[1]:
        return None
    return size[0] / size[1]


def image_aspect(path: str | Path) -> float | None:
    """Return width / height of an image file, or None when the size cannot be read."""
    return aspect(Path(path).read_bytes())


if __name__ == "__main__":
    png = b"\x89PNG\r\n\x1a\n" + b"\0\0\0\rIHDR" + struct.pack(">II", 1279, 707)
    jpeg = b"\xff\xd8" + b"\xff\xe0\0\x04xx" + b"\xff\xc0\0\x11\x08" + struct.pack(">HH", 600, 800) + b"\0" * 8
    cases = [
        (png, 1279 / 707),
        (jpeg, 800 / 600),
        (b'<svg xmlns="x" viewBox="0 0 760 404" width="1520" height="808">', 1520 / 808),
        (b"<svg viewBox='0,0,300,600'>", 0.5),
        (b'<svg width="100%" height="100%" viewBox="0 0 400 100">', 4.0),
        (b"not an image", None),
    ]
    for src, want in cases:
        got = aspect(src)
        assert got == want, (src[:40], got, want)  # nosec B101
    print("ok")
