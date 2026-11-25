#!/usr/bin/env python3
"""Write the one funny line to /output/entry.txt.

The entry is a single line of 69 characters, no trailing newline,
inside the competition's 1-140 character gate.
"""

import os

ENTRY = "The on-call phone rang at 3 a.m. It was my own code, asking for help."
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> None:
    # Gate: entry must be a single non-blank line of 1-140 characters.
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"ENTRY must be 1-{MAX_CHARS} chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "ENTRY must be a single line"
    assert ENTRY.strip(), "ENTRY must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verification: the bytes on disk must be exactly ENTRY,
    # with no trailing newline added by the write.
    data = open(OUTPUT_PATH, "rb").read()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match ENTRY"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
