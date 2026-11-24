#!/usr/bin/env python3
"""Doorknob pitch entry for make.fun's "The Worst App Idea Ever Pitched".

Writes one sentence (at most 240 characters) pitching the worst, most
useless app imaginable to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: fixed text, no clock, no randomness, no network, no input.
"""

import os
import sys

# One sentence, 222 characters: a premium AI app that reminds you which
# of your doors are doors, with a global leaderboard for door awareness.
PITCH = (
    "Doorknob is a premium AI app that uses machine learning to remind you "
    "every morning which of your doors are doors, with push notifications, "
    "daily streaks, and a global leaderboard ranking the world's most "
    "door-aware users."
)


def main() -> int:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 240
    # characters, not only white space, in a single sentence.
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"pitch is {len(text)} characters, must be 1-240")
    if not text or text != PITCH:
        raise SystemExit("pitch must be exactly one clean sentence")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
