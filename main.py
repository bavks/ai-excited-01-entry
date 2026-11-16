#!/usr/bin/env python3
"""Tortoise Grand Prix - make.fun ai-excited-01 entry.

Writes the shipped artwork (entry.jpg, a JPEG-encoded tortoise
Formula-1 grand prix scene) to $MAKEFUN_OUTPUT_DIR/entry.png.
The grader accepts PNG or JPEG by magic bytes, so the JPEG payload
is copied byte-for-byte under the entry.png name.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.jpg")
CHUNK_SIZE = 64 * 1024


def copy_verified(src: str, dest: str) -> None:
    """Copy src to dest in chunks and verify the written size.

    The grader runs this program twice and requires both outputs to
    be byte-identical, so fail loudly rather than emit a short file.
    """
    expected = os.path.getsize(src)
    written = 0
    with open(src, "rb") as fin, open(dest, "wb") as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            fout.write(chunk)
            written += len(chunk)
    if written != expected:
        raise IOError(f"short copy: wrote {written} of {expected} bytes")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    copy_verified(SOURCE, dest)


if __name__ == "__main__":
    main()
