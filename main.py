#!/usr/bin/env python3
"""Write the one-line review of a rubber band to /output/entry.txt.

The review: a bag of 500 rubber bands, one used, snapped on the first
stretch, the other 499 drying out in a drawer waiting to do the same.
The joke is the object's own dullness -- rubber bands really do dry-rot in
drawers and snap the moment you stretch them -- and the turn comes early,
with the last words sharpening it.

Deterministic, no network, no input: the entry is a single fixed line.
"""

import os
from pathlib import Path

REVIEW = (
    "Bought 500 rubber bands. Used one. It snapped on the first stretch. "
    "The other 499 are in a drawer, quietly drying out, waiting to do the same."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly unless the line satisfies the competition gate."""
    assert isinstance(line, str)
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    assert line.encode("utf-8").decode("utf-8") == line, "entry must be UTF-8"


def main() -> None:
    validate(REVIEW)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    # No trailing newline: the gate counts the file's characters, so the
    # file holds exactly the line, nothing else.
    target.write_text(REVIEW, encoding="utf-8")
    assert target.read_text(encoding="utf-8") == REVIEW, (
        "entry.txt does not hold exactly the chosen line"
    )


if __name__ == "__main__":
    main()
