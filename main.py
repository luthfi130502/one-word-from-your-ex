#!/usr/bin/env python3
"""One Word From Your Ex — writes the single word an ex would use."""

import os

WORD = "Nonrefundable"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: UTF-8, 1-24 chars, exactly one word, no spaces.
    assert 1 <= len(WORD) <= 24, "word length out of gate range"
    assert WORD.strip() == WORD and " " not in WORD, "must be a single word"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(WORD + "\n")


if __name__ == "__main__":
    main()
