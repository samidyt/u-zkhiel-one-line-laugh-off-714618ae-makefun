#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
The line: a single joke that lands on a cold read, no setup notes,
no explanation. The twist sits in the last word: "proposed" does
double duty -- the AI was asked to draft wording, and instead it
made a marriage proposal to the fiancee. Setup, turn and punch
all inside one sentence.
"""

JOKE = "I asked AI to write my wedding vows. It proposed to my fiancée instead."


def main() -> None:
    import os

    # Gate check, mirroring the scorer: 1-200 UTF-8 chars, not only
    # whitespace, exactly one line. Fail loudly instead of shipping
    # an entry the gate would refuse.
    text = JOKE.strip()
    assert text and "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
