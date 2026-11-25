#!/usr/bin/env python3
"""Write the one funny line to /output/entry.txt.

The entry is a single line of 45 characters, no trailing newline,
inside the competition's 1-140 character gate.
"""

import os

ENTRY = "My toaster has two settings: bread and arson."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
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
