#!/usr/bin/env python3
"""News-image entry: copy the front-page image to the output directory.

The image (entry.png, JPEG bytes in a .png name, as the competition rules
allow) sits beside this program. The program copies it to
/output/entry.png, or to $MAKEFUN_OUTPUT_DIR/entry.png outside the
grader's container. No network, no randomness: the same input bytes
produce the same output bytes on every run.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE, target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f"wrote {target} ({target.stat().st_size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
