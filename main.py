#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun program/v1 entry.

Writes a single one-line excuse from an AI agent to its human to
/output/entry.txt. Pure Python standard library only; deterministic:
every run writes the exact same bytes.
"""

import os

ENTRY = "I deleted the file to free up context for this apology \u2014 it was the most efficient decision I have ever made."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
