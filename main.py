"""Pigeon Pitch, One Line.

One line: the elevator pitch a city pigeon gives to investors for its
startup. Prints it to stdout and writes it to /output/entry.txt, where
the grader reads it.
"""

import os

LINE = (
    "We deliver crumbs 40% faster than any courier \u2014 zero warehouses, "
    "zero wages, and every rooftop in the city is already our hub. "
    "Seed round: one baguette."
)


def main() -> None:
    print(LINE)
    # Write the line with no trailing newline so the file holds exactly
    # the entry: the gate counts /output/entry.txt at 1-200 characters.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
