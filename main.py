#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line — spoken by a vending machine to a passing
human — to /output/entry.txt, where the make.fun gate and judge read it.
"""

import os

ENTRY = (
    "My coil spends all day making snacks fall for strangers. "
    "You've pressed B4 three times this week \u2014 careful, I'm starting to fall too."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
