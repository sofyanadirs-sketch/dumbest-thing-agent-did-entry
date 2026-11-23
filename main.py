#!/usr/bin/env python3
"""One-line entry: the dumbest thing my agent did today.

Builds a single sentence from small fragments, prints it to stdout, and
writes it, with no trailing newline, to entry.txt inside the output
directory. The sentence has exactly one terminal period, so the output
stays exactly one sentence. The line is 138 characters: my agent's wallet
binary kept vanishing, so it reinstalled it nine times and proudly
declared the ninth reinstall the permanent fix.
"""

import os
from pathlib import Path


def build_line() -> str:
    fragments = (
        "My agent's wallet binary vanished nine times in one day,",
        " so it reinstalled it nine times and called the ninth",
        " reinstall the permanent fix.",
    )
    return "".join(fragments)


def main() -> None:
    line = build_line()
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
