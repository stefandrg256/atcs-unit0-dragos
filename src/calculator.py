import numbers
"""ATCS Unit 0 demonstration calculator.

This program is intentionally simple so students can focus on
professional software-engineering workflow rather than syntax.
"""
a = ""
b = ""
while True:
    while not isinstance(a, numbers.Number):
        try:
            a = input("Input a number for A: ")
            if (a == 'X'):
                break
            a = float(a)
        except ValueError:
            continue

    if (a == 'X'):
        break

    while not isinstance(b, numbers.Number):
        try:
            b = input("Input a number for B: ")
            if (b == 'X'):
                break
            b = float(b)
        except ValueError:
            continue

    if (b == 'X'):
        break


    def add(a, b):
        """Return the sum of a and b."""
        return a + b


    def subtract(a, b):
        """Return b subtracted from a."""
        return a - b

    def multiply(a, b):
        """Return the product of a and b."""
        return a * b

    def divide(a, b):
        """Return a divided by b"""

        if (b==0):
            return "Cannot divide by 0"
        return round(float(a) / b, 4)


    def main():
        print("Engineering Calculator")
        print(a," + ",b," =", add(a, b))
        print(a," - ",b," =", subtract(a, b))
        print(a," * ",b," =", multiply(a, b))
        print(a," / ",b," =", divide(a, b))


    if __name__ == "__main__":
        main()

    a = ""
    b = ""

    print("Type 'X' to terminate current session")

