#!/usr/bin/env python3
"""The Printer Apology — entrypoint.

Reads entry.txt (the one-line apology) and writes it verbatim to
<output>/entry.txt, where <output> is MAKEFUN_OUTPUT_DIR or /output.
The output directory is created if missing and never deleted: the
grader mounts it, so this program only ever makes it.
"""

import os
import sys


def main() -> int:
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR")
    if input_dir:
        entry_path = os.path.join(input_dir, "entry.txt")
    else:
        entry_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    with open(entry_path, "r", encoding="utf-8") as f:
        text = f.read()

    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
