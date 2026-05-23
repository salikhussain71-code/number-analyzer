def is_even(n):
    return n % 2 == 0


def number_sign(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"


def square(n):
    return n * n


def main():
    print("=== Number Analyzer ===")

    x = int(input("Enter a number: "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

    print(number_sign(x))

    print(f"Square: {square(x)}")


if __name__ == "__main__":
    main()