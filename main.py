#!/usr/bin/env python3
"""Cat review entry for make.fun — program/v1.

Writes one single-line one-star cat review (at most 200 characters)
to /output/entry.txt. The review text is fixed in this file; the
program checks the gate itself (1-200 characters, one line, not
blank) at runtime and then writes it deterministically, so two runs
produce byte-identical output.
"""

REVIEW = (
    "One star. He snores all night, steals the warm spot, and blames "
    "me for the hair on his pillow. I slept on his face once. He has "
    "not snored since."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not REVIEW.strip():
        raise SystemExit("review is empty")
    if "\n" in REVIEW or "\r" in REVIEW:
        raise SystemExit("review must be a single line")
    if len(REVIEW) > 200:
        raise SystemExit(
            f"review is {len(REVIEW)} characters, over the 200 limit"
        )
    if REVIEW != REVIEW.strip():
        raise SystemExit("review must not start or end with whitespace")
    parent = OUTPUT_PATH.rsplit("/", 1)[0]
    if parent:
        import os

        os.makedirs(parent, exist_ok=True)
    expected = REVIEW + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(expected)
    # Verify what landed on disk is exactly what was intended;
    # a partial write must fail loudly instead of passing silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != expected:
            raise SystemExit("output verification failed")


if __name__ == "__main__":
    main()
