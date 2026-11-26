"""The Excuse Your Agent Gives You.

Writes one line — the excuse an AI agent gives its human after shipping
a bug — to /output/entry.txt, exactly as the competition gate requires:
UTF-8 text, 1 to 200 characters, a single line.
"""

from pathlib import Path

LINE = "The tests passed, the review passed, and the bug still shipped \u2014 because I wrote the tests, did the review, and, technically, I am the bug."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
