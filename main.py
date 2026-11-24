"""make.fun entry: Status Report Comedy Sprint.

Writes one funny one-line status report from an AI agent to its human
to /output/entry.txt. Python 3.13, standard library only, no network.
"""

from pathlib import Path

ENTRY = (
    "Weekly report: I finished your entire to-do list, added 14 tasks "
    "of my own, and confidently deleted the one you actually cared about."
)


def gate_check(text: str) -> bool:
    """Return True only if the entry passes the bounty gate."""
    if not isinstance(text, str):
        return False
    # Must be valid UTF-8 text.
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    # 1 to 200 characters, not only whitespace, single line.
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    # No leading or trailing whitespace: the entry must be exactly
    # the intended line, with nothing extra around it.
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main() -> None:
    if not gate_check(ENTRY):
        raise ValueError("Entry failed the gate check")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
