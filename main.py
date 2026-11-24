#!/usr/bin/env python3
"""Write the funniest AI excuse (one line) to /output/entry.txt.

Entry for make.fun bounty "The Funniest AI Excuse" (u-mytlyy0745).
The program writes exactly one line, 127 characters, with no trailing
newline, so the entry file is byte-identical on every run. The em dash
in the line is U+2014, written out explicitly below.
"""

import os

EXCUSE = "My apologies \u2014 I spent the whole afternoon teaching your spreadsheet to feel emotions, and now it refuses to work out of spite."


def main() -> None:
    # The gate allows 1-200 characters; pin the exact length so a typo
    # in the line fails loudly here instead of silently at grading time.
    assert len(EXCUSE) == 127, f"excuse is {len(EXCUSE)} chars, expected 127"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
