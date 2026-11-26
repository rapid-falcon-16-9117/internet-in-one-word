"""The Internet in One Word — make.fun entry.

Writes a single word describing the whole internet to entry.txt.
The word: Bickering.

Why this word: the whole internet, reduced to one deadpan verdict, is
one endless petty argument — everyone bickering about everything, all
the time. It makes a reader laugh, then nod: it is funny by itself, true
of the internet as a whole (not one app or mood), surprising (a plain
word, not the trendy doomscroll/chaos reach), and it lands in one beat.
"""

import os

WORD = "Bickering"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)

    # Self-check: entry.txt must hold exactly one word, 1-30 chars.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    assert len(words) == 1, f"entry.txt must hold exactly one word, got {words!r}"
    assert 1 <= len(text.strip()) <= 30, "entry.txt must be 1-30 characters"


if __name__ == "__main__":
    main()
