#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf"]
# ///
"""Render one PDF page to a PNG, optionally cropped to the part the scene needs.

Pages start at 1. The crop box is x,y,w,h in PDF points (1/72 inch) from the page's
top-left corner; the page size is printed so you can render the whole page first.
Usage: uv run pdf_page.py <pdf> <page> <out.png> [--crop x,y,w,h] [--scale 2]
"""

import argparse
import sys

import pymupdf


def main() -> None:
    """Render the page and print its size."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("page", type=int)
    ap.add_argument("out")
    ap.add_argument("--crop", help="x,y,w,h in PDF points from the top-left")
    ap.add_argument("--scale", type=float, default=2.0, help="pixels per point (default 2)")
    a = ap.parse_args()
    with pymupdf.open(a.pdf) as doc:
        if not 1 <= a.page <= doc.page_count:
            sys.exit(f"page {a.page} is out of range (1..{doc.page_count})")
        page = doc[a.page - 1]
        clip = None
        if a.crop:
            x, y, w, h = (float(v) for v in a.crop.split(","))
            clip = pymupdf.Rect(x, y, x + w, y + h)
        pix = page.get_pixmap(matrix=pymupdf.Matrix(a.scale, a.scale), clip=clip)
        pix.save(a.out)
        r = page.rect
        print(f"{a.out}: {pix.width}x{pix.height}px from page {a.page}/{doc.page_count} ({r.width:.0f}x{r.height:.0f} pt)")


if __name__ == "__main__":
    main()
