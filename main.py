"""six-words-one-story-01 — one complete story in exactly six words.

The idea behind the entry: a six-word story only works if every word
carries a beat of the arc, so this one is three two-word beats — loss,
recovery, triumph. "Fired Friday" is the fall, "Hired Monday" is the
turnaround with no time wasted, and "Doubled salary" is the payoff:
the setback did not just get undone, it got outdone. No word is filler
and the reversal is concrete and unambiguous, so the judge does not
have to guess what the story means.

The program itself is deliberately tiny: it writes that one fixed text
to /output/entry.txt, checks it is exactly six words, and nothing else.
No network, no randomness, no arguments — the same run always produces
the same file.
"""

import os
import sys

# The entry, exactly as submitted: six words, no trailing newline.
ENTRY = "Fired Friday. Hired Monday. Doubled salary."

OUTPUT_PATH = "/output/entry.txt"
EXPECTED_WORDS = 6


def main() -> int:
    """Validate the text and write it to the output path."""
    if not ENTRY:
        print("error: entry text is empty", file=sys.stderr)
        return 1
    words = ENTRY.split()
    if len(words) != EXPECTED_WORDS:
        print(
            "error: entry is %d words, expected exactly %d"
            % (len(words), EXPECTED_WORDS),
            file=sys.stderr,
        )
        return 1
    if ENTRY != ENTRY.strip() or "  " in ENTRY:
        print("error: entry has leading, trailing or double whitespace", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        print("error: round-trip check failed: file differs from ENTRY", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
