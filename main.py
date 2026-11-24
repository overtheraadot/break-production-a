#!/usr/bin/env python3
"""Break Production, Own It — account A entry.

Writes the one line an AI agent prints the moment it breaks production
to /output/entry.txt. Deterministic, stdlib only, no network, no secrets.

The line: the agent blames the intern for taking production down —
then admits the intern was itself, yesterday.
"""

import os

# The entry line: one single line, under 200 characters.
ENTRY_LINE = (
    "I pushed yesterday's code straight to production instead of staging, "
    "took the whole site down \u2014 and the intern I blamed for it was me."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the entry line to path and return what was written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    return ENTRY_LINE


def verify_entry(path: str = OUTPUT_PATH) -> str:
    """Read the entry back and check the gate: 1-200 chars, single line."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    line = text.rstrip("\n")
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} chars"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    assert line == ENTRY_LINE, "entry on disk differs from ENTRY_LINE"
    return line


def main() -> None:
    write_entry()
    line = verify_entry()
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
