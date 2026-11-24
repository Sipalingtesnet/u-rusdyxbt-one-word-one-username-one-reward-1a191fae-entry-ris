#!/usr/bin/env python3
"""One Word, One Username, One Reward -- entry by @ris.

The entry is the handle itself: "ris", three letters, sent with nothing
attached. The judge reads /output/entry.txt and nothing else, so the job
here is narrow and absolute: put those three characters in the file
unaltered -- no newline, no quotes, no gloss -- because a handle should
arrive exactly the way its owner wears it.
"""

from pathlib import Path

# The entire entry: the entrant's own make.fun handle, lowercase, undecorated.
USERNAME = "ris"

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # The published gate is UTF-8 text of 1 to 30 characters, not only
    # whitespace. Check the word against it here so the entry can never be
    # scored as invalid for a reason this file could have caught itself.
    if not (1 <= len(USERNAME) <= 30) or USERNAME != USERNAME.strip() or " " in USERNAME:
        raise ValueError(f"handle does not fit the gate: {USERNAME!r}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # write_bytes, not write_text: no platform newline translation, so the
    # file is byte-identical on every run and ends without a trailing newline.
    OUTPUT_FILE.write_bytes(USERNAME.encode("utf-8"))


if __name__ == "__main__":
    main()
