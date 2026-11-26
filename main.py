#!/usr/bin/env python3
"""news-image-20261126 entry: copy the front-page poster to the output dir.

The poster (entry.png, 1024x1024) sits beside this program. The program
runs with no network and only the standard library, so it just copies
that image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR when set, which
is how the kit documents local runs). It then checks the copy is a real
PNG of the expected size before reporting success.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def here():
    return os.path.dirname(os.path.abspath(__file__))


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def png_dimensions(path):
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file: " + path)
    if head[12:16] != b"IHDR":
        raise ValueError("PNG has no IHDR chunk: " + path)
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height


def main():
    src = os.path.join(here(), SOURCE_NAME)
    if not os.path.isfile(src):
        print("missing source image: " + src, file=sys.stderr)
        return 1
    if os.path.getsize(src) > 1048576:
        print("source image over 1 MiB: " + src, file=sys.stderr)
        return 1
    dest_dir = output_dir()
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, SOURCE_NAME)
    shutil.copyfile(src, dest)
    width, height = png_dimensions(dest)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        print("bad size: %dx%d, expected %dx%d"
              % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT),
              file=sys.stderr)
        return 1
    print("wrote %s (%dx%d)" % (dest, width, height))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
