#!/usr/bin/env python3
"""Print the out-of-office auto-reply stored in entry.txt.

The bounty brief caps the reply at one line of at most 159 characters,
so the loader enforces both limits and refuses to print anything that
breaks them, instead of silently emitting an invalid entry.
"""

from pathlib import Path

MAX_CHARS = 159


def load_reply(path):
    raw = Path(path).read_text(encoding="utf-8")
    parts = [line.strip() for line in raw.splitlines() if line.strip()]
    reply = " ".join(parts)
    if len(reply) > MAX_CHARS:
        raise SystemExit(
            f"reply is {len(reply)} characters, over the {MAX_CHARS} limit"
        )
    return reply


def main():
    print(load_reply(Path(__file__).with_name("entry.txt")))


if __name__ == "__main__":
    main()
