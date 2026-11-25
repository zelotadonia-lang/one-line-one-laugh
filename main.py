#!/usr/bin/env python3
"""Write the one funny line to /output/entry.txt.

The entry is a single line of 69 characters, no trailing newline,
inside the competition's 1-140 character gate.
"""

import os

ENTRY = "The on-call phone rang at 3 a.m. It was my own code, asking for help."
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate_entry(entry: str, max_chars: int = MAX_CHARS) -> str:
    """Check the entry against the competition gate and return it unchanged.

    The gate requires a single non-blank line of 1 to max_chars
    characters. Any violation raises AssertionError with a message
    naming the failed rule, so a bad entry stops the run before
    anything is written to disk. Validation runs first on purpose:
    the write that follows assumes the entry already passed, and
    the read-back check at the end only confirms the bytes on disk.
    """
    assert 1 <= len(entry) <= max_chars, (
        f"ENTRY must be 1-{max_chars} chars, got {len(entry)}"
    )
    assert "\n" not in entry, "ENTRY must be a single line"
    assert entry.strip(), "ENTRY must not be only whitespace"
    return entry


def main() -> None:
    # Gate: entry must be a single non-blank line of 1-140 characters.
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        # No trailing newline: the gate counts characters, so a newline
        # would push the file past the entry itself and break the
        # single-line requirement.
        f.write(ENTRY)
    # Read-back verification: the bytes on disk must be exactly ENTRY,
    # with no trailing newline added by the write.
    data = open(OUTPUT_PATH, "rb").read()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match ENTRY"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
