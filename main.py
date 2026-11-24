"""Say What Actually Broke — one brutally honest error line.

Writes a single line of software error copy to the path in the
OUTPUT_PATH environment variable (default /output/entry.txt).
"""

import os

ENTRY = (
    "The database crashed mid-save and took your file with it. "
    "It's gone. Upload it again \u2014 we'll hold its hand this time."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
