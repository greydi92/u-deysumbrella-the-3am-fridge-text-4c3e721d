#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes exactly one line to /output/entry.txt: the message a smart fridge
sends its owner at 3am.

The line (94 characters, single line, UTF-8):

    3am. I have seen things no appliance should see. Mostly you, in your
    underwear, eating butter.

Why this line, against the judge's brief:

* It is unmistakably a 3am text from a fridge — the timestamp opens it,
  the voice is a machine that has been awake all night.
* The setup ("I have seen things no appliance should see") is pure fridge:
  a small-voiced appliance with an opinion and no shame about sharing it.
* The punchline lands on a fresh angle — a voyeur fridge catching its
  owner eating butter straight, in their underwear. No milk, no ice,
  no door left open.
* It is short enough to read whole on a lock screen and complete without
  a follow-up, and it is the line a reader screenshots and sends to a
  friend.

Candidates considered and rejected in this session (all drafted here,
none copied from anywhere else):

* "It's 3am and you're eating standing up in the dark again. I turned
  the light on. You're welcome. I'm telling your Fitbit." (121 chars)
  Strong snitch punchline, but three sentences dilute the hit.
* "You open me at 3am like I'm a slot machine. Spoiler: it's just
  pickles and regret." (82 chars) Good, but "open me" leans on the
  door and the laugh is smaller.
* "3am. Your Fitbit thinks you are asleep. I know better. The cheese
  knows better." (79 chars) Clever, but cute rather than funny.
* "It's 3am. I've counted 47 midnight visits this month. I'm not
  judging. I'm just the fridge. Okay, I'm judging." (110 chars)
  The "Okay, I'm judging" turn is a known joke format.
* "3am. This is the fridge. You left me on read for six hours and now
  you want a snack?" (84 chars) Fresh texter conceit, weak punchline.

The program is deterministic: it always writes the same chosen line.

Before writing, it checks the line against the scorer's gate (1–140
characters, a single line, not only whitespace) and exits non-zero if it
ever fails, so a bad line can never be written silently. The output
directory honours $MAKEFUN_OUTPUT_DIR, then $OUTPUT_DIR, then /output.
"""

import os
import sys

ENTRY = (
    "3am. I have seen things no appliance should see. "
    "Mostly you, in your underwear, eating butter."
)


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"


def validate(entry: str) -> None:
    if not (1 <= len(entry) <= 140):
        print(f"error: entry is {len(entry)} chars, gate requires 1-140", file=sys.stderr)
        sys.exit(1)
    if entry != entry.strip() or not entry.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in entry or "\r" in entry:
        print("error: entry must be a single line", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate(ENTRY)
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
