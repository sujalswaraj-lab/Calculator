"""A simple calculator for the terminal."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: you can't divide by zero"
    return a / b


def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        first = input("Enter first number: ")
        if first.lower() == "q":
            break

        operation = input("Enter operation (+, -, *, /): ")
        if operation.lower() == "q":
            break

        second = input("Enter second number: ")
        if second.lower() == "q":
            break

        try:
            a = float(first)
            b = float(second)
        except ValueError:
            print("Please enter valid numbers.\n")
            continue

        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            print("Unknown operation. Use +, -, * or /.\n")
            continue

        print(f"Result: {result}\n")

    print("Goodbye!")


if __name__ == "__main__":
    calculator()