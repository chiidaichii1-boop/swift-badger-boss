"""One Word for the Boss — entry program.

Writes exactly one word describing the boss to /output/entry.txt.

The word: "Lurker" — the boss who never announces himself, just
materialises silently behind your desk to watch your screen, then
vanishes before you can turn around. A word colleagues actually use,
funny on its own, true of a real boss habit, and fresher than the
first word anyone reaches for.
"""

import os

WORD = "Lurker"  # verified: 6 characters, single word, within the 1-30 gate


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Gate: exactly one word, 1-30 characters, not only whitespace.
    assert 1 <= len(WORD) <= 30, "word outside 1-30 char gate"
    assert WORD.strip() and " " not in WORD, "entry must be a single word"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
