"""ATCS Unit 0 demonstration calculator.

This program is intentionally simple so students can focus on
professional software-engineering workflow rather than syntax.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return b subtracted from a."""
    return a - b


def main():
    print("Engineering Calculator")
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))


if __name__ == "__main__":
    main()
