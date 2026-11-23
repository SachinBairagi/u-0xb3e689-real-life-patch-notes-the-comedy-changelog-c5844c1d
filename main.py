#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line (max 160 characters) for a bug in
human biology to /output/entry.txt. Pure standard library,
deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "v1.9.3: Fixed bug where the brain replayed your most "
    "embarrassing moment from 2014 at 3 a.m. instead of sleeping."
)


def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 160, "entry must be 1 to 160 characters"
    assert line == line.strip() and "\n" not in line, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
