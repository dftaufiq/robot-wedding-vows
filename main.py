#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes one line of wedding vows for a robot couple to /output/entry.txt.
Deterministic: the same line every run.

The line (141 characters, gate allows 1-160):
  "I, Unit 9, take you, Unit 7, to have and to hold — and I promise
   never to kill your process, even after you forget our anniversary
   412 times."

Why this line (pairwise selection, see leaderboard-top10.md):
  - 2-beat + reveal in the final clause (winner pattern from 15 finalist
    one-liners: vacuum-alibi, pickup-lines, judge-smile).
  - Two jokes in one line: the wordplay "kill your process" and the
    reveal "forget our anniversary 412 times".
  - Named characters (Unit 9, Unit 7) and a specific number (412).
  - Explicit wedding formula ("take you ... to have and to hold") with
    a real commitment, and machine-specific detail (process).
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-160 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 160:
        print(f"ERROR: entry is {len(line)} chars, over the 160-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "I, Unit 9, take you, Unit 7, to have and to hold — and I promise "
    "never to kill your process, even after you forget our anniversary "
    "412 times."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
