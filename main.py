#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single line (under 200 characters) to /output/entry.txt:
a sick-day excuse that a boss might half believe and a coworker
would laugh at. Pure Python standard library, no network, no input.

The line: a believable everyday mishap (car keys in the freezer)
with the laugh landing at the end (the fridge holding them hostage).
Fresh idea — no fever, no dog, no dead grandmother — written the
way a real person would text their boss.
"""

import os

ENTRY = (
    "Sorry, can't come in today \u2014 my car keys ended up in the freezer "
    "and my fridge is holding them hostage until I apologize."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip() == text and text, "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back verification: the file on disk must hold exactly the entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the entry"
    print(f"wrote {len(text)} characters to {OUTPUT_PATH} (verified)")


if __name__ == "__main__":
    main()
