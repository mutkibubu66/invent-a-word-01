"""finepause — a word for the pause before a polite lie.

Coinage: "fine" + "pause". Everyone knows the moment: someone asks how
you are, and before the automatic "I'm fine" comes out, there is a tiny
held breath in which you decide not to tell the truth. English has words
for hesitation and for small talk, but none for that exact beat — the
split second where honesty loses to politeness. "Finepause" is built from
two plain English words, so it reads and sounds like something the
language could have grown on its own, and it is short enough to use in
the sentence it describes.

The program writes the entry — one line, no trailing newline — to
/output/entry.txt.
"""

import os

# The competition gate: /output/entry.txt must hold 1 to 140 characters.
MAX_ENTRY_CHARS = 140

ENTRY = 'finepause (n.) \u2014 the pause before you say "I\'m fine" when you\'re not.'

assert 1 <= len(ENTRY) <= MAX_ENTRY_CHARS, "entry must be 1-140 characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
