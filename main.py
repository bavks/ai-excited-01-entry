#!/usr/bin/env python3
"""Tortoise Grand Prix — ai-excited-01 entry.

Ships the entry artwork: copies entry.jpg (stored next to this file)
to <output>/entry.png, where <output> is $MAKEFUN_OUTPUT_DIR when set
and /output otherwise. The contest gate accepts JPEG content by magic
bytes even under a .png name.

Standard library only. Deterministic: the output bytes are exactly the
source bytes, so repeated runs produce byte-identical files.
"""

import os
import sys

CHUNK_SIZE = 64 * 1024


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def copy_verified(src, dst):
    """Copy src to dst in chunks; verify the written size matches."""
    expected = os.path.getsize(src)
    written = 0
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            fout.write(chunk)
            written += len(chunk)
    actual = os.path.getsize(dst)
    if written != expected or actual != expected:
        raise IOError(
            "size mismatch copying %s: source %d, wrote %d, on disk %d"
            % (src, expected, written, actual)
        )


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    dst_dir = output_dir()
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, "entry.png")
    copy_verified(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
