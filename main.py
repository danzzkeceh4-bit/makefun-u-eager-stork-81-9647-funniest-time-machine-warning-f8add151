#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning label (105 characters) to /output/entry.txt.
The label is a straight-faced safety notice: a paradox (already crashed
before operating) with the surprise saved for the last words — the
grandfather paradox, and a manufacturer that disclaims liability for him.
"""

import os
import sys

LABEL = "CAUTION: Do not operate if you have already crashed. The manufacturer is not liable for your grandfather."


def main() -> int:
    if not 1 <= len(LABEL) <= 120:
        print(f"error: label is {len(LABEL)} characters, must be 1-120",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
