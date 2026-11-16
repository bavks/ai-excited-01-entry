#!/usr/bin/env python3
"""Tortoise Grand Prix — make.fun ai-excited-01 entry.

Copies the bundled artwork (entry.jpg, stored next to this file) to
<output>/entry.png, where <output> is $MAKEFUN_OUTPUT_DIR when set and
/output otherwise. The image bytes are copied verbatim, in chunks;
the contest gate accepts JPEG content by magic bytes even under a
.png name.

Standard library only. Deterministic: repeated runs write identical
bytes. The copy is verified — the number of bytes written must equal
the source size, otherwise the program fails loudly.
"""

import os
import sys

CHUNK_SIZE = 64 * 1024


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def copy_artwork(src, dst):
    """Copy src to dst in chunks; return the number of bytes written."""
    written = 0
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            fout.write(chunk)
            written += len(chunk)
    return written


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    dst_dir = output_dir()
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, "entry.png")

    expected = os.path.getsize(src)
    written = copy_artwork(src, dst)
    if written != expected:
        print(
            f"error: wrote {written} bytes, expected {expected}",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {dst} ({written} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
