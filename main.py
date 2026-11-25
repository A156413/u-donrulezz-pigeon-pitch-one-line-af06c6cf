"""Pigeon Pitch, One Line.

One line: the elevator pitch a city pigeon gives to investors for its
startup. Prints it to stdout and writes it to entry.txt under the output
directory (``$MAKEFUN_OUTPUT_DIR``, default ``/output``), where the
grader reads it.
"""

import os

ENTRY = (
    "We deliver crumbs 40% faster than any courier \u2014 zero warehouses, "
    "zero wages, and every rooftop in the city is already our hub. "
    "Seed round: one baguette."
)

MIN_LENGTH = 1
MAX_LENGTH = 200
DEFAULT_OUTPUT_DIR = "/output"


def validate_entry(entry: str) -> None:
    """The gate counts entry.txt at 1-200 characters on a single line."""
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not MIN_LENGTH <= len(entry) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(entry)}"
        )


def output_path() -> str:
    return os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR),
        "entry.txt",
    )


def main() -> None:
    validate_entry(ENTRY)
    print(ENTRY)
    # Write the line with no trailing newline so the file holds exactly
    # the entry: the gate counts entry.txt at 1-200 characters.
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader reads entry.txt as a plain file; keep permissions explicit.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
