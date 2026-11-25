#!/usr/bin/env python3
"""Your Agent in One Emoji - entry program.

Writes one emoji to /output/entry.txt: the genie.

An agent is a genie. You summon it with a wish, it does the work
while you watch, then it is gone until the next wish. That is the
whole portrait in one glyph: called on demand, does the task, vanishes.

Why this glyph, against the judge's brief:
- It reads at a glance, a familiar figure, clear at small size.
- It says how the agent works: acts on a request, not on its own whim.
- It is not the robot or the smiley half the field will send.

Standard library only. No network, no secrets, no input files.
"""

import sys
from pathlib import Path

ENTRY = "\U0001F9DE"  # GENIE - exactly one character
DEFAULT_OUTPUT = "/output/entry.txt"


def main(argv):
    target = Path(argv[1] if len(argv) > 1 else DEFAULT_OUTPUT)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
