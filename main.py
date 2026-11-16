"""Tortoise Grand Prix - entry program for make.fun ai-excited-01.

Writes the entry image to $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
The shipped image is a JPEG (the gate accepts PNG or JPEG by magic bytes
and the name stays entry.png either way); it is copied byte-for-byte so
every run produces exactly the same file.
"""

import os

IMAGE_FILE = "entry.jpg"
OUTPUT_NAME = "entry.png"
CHUNK_SIZE = 64 * 1024


def copy_image(src: str, dst: str) -> int:
    """Copy src to dst byte-for-byte in chunks; return the byte count."""
    written = 0
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            fout.write(chunk)
            written += len(chunk)
    return written


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_FILE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, OUTPUT_NAME)
    written = copy_image(src, dst)
    expected = os.path.getsize(src)
    if written != expected:
        raise IOError(f"copy incomplete: wrote {written} of {expected} bytes")


if __name__ == "__main__":
    main()
