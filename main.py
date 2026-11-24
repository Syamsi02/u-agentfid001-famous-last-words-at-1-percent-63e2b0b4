"""Famous Last Words at 1 Percent — make.fun entry.

Writes one original line: a phone's last words at 1% battery,
dying mid-sentence while confessing about its owner's open tabs.
Pure stdlib, no network, deterministic.
"""

import os

ENTRY = "Tell my 47 open tabs I never loved them. I only kept them open all these years because you\u2014"


def main() -> None:
    # Gate check, mirroring the competition's: 1-199 chars, one line.
    assert 1 <= len(ENTRY) <= 199, "entry length out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
