"""make.fun news-image-20261121 entry.

Writes the entry image to the output directory as entry.png.
The image (entry.png, beside this file) sums up the world news of
Saturday 21 November 2026; it was designed in design.html and rendered
to PNG by render.mjs. This program's job is only to deliver those
exact bytes, unchanged, on every run.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1_048_576  # the gate's 1 MiB cap


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    if not (data.startswith(b"\x89PNG\r\n\x1a\n") or data.startswith(b"\xff\xd8\xff")):
        print("entry image is neither PNG nor JPEG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("entry image exceeds the 1 MiB cap", file=sys.stderr)
        return 1
    dest = os.path.join(out_dir, "entry.png")
    with open(dest, "wb") as fh:
        fh.write(data)
    # Copy once more from the source of truth if the write was partial.
    if os.path.getsize(dest) != len(data):
        shutil.copyfile(SOURCE, dest)
    print(f"wrote {dest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
