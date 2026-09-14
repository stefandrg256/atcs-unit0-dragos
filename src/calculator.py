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

def divide(a, b):
    """Return a divided by b"""

    if (b==0):
        return "Cannot divide by 0"
    return round(float(a) / b, 4)


def main():
    print("Engineering Calculator")
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))

    print("5 / 3 =", divide(5, 3))
    print("-5 / 3 =", divide(-5, 3))
    print("5 / 2 =", divide(5, 2))
    print("15 / -3 =", divide(15, -3))
    print("-5 / -3 =", divide(-5, -3))
    print("5 / 0 =", divide(5, 0))
    print("0 / 5 =", divide(0, 5))


if __name__ == "__main__":
    main()
