#!/usr/bin/env python3
"""One-line roast of the gadget I use every day: my robot vacuum.

Writes a single original roast (one line, at most 200 characters) to
/output/entry.txt, or to the path given as the first argument.
Deterministic, standard library only, no network, no randomness.
"""

import sys
from pathlib import Path

MAX_CHARS = 200

ROAST = (
    "My robot vacuum has mapped every inch of my flat, yet it still "
    "hunts down the one charging cable on the floor and slurps it "
    "like spaghetti."
)


def validate(line: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not line or not line.strip():
        raise ValueError("roast must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"roast is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main(argv: list[str]) -> int:
    output = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    validate(ROAST)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ROAST + "\n", encoding="utf-8")
    print(f"Wrote {len(ROAST)}-character roast to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
