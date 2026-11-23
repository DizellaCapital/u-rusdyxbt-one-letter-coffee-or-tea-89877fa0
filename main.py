"""One Letter: Coffee or Tea entry program.

Writes exactly one letter, ``A`` (coffee), to
MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only. The letter is a single
uppercase character, no newline, no punctuation, no explanation.
The entry file is exactly one byte long.
"""

import os
import sys

LETTER = "A"


def main():
    if len(LETTER) != 1 or not LETTER.isalpha() or not LETTER.isupper():
        print(f"entry must be exactly one uppercase letter, got {LETTER!r}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LETTER:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
