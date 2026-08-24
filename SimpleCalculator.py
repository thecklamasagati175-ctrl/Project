def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("You cannot divide by zero.")
        return a
    return a / b


while True:
    print("\nCalculator")
    print("Type 'q' at the first question to quit.")

    first_number = input("Enter your first number: ")

    if first_number.lower() == "q":
        print("Goodbye!")
        break

    answer = float(first_number)

    while True:
        operation = input("Enter +, -, *, /, or = to finish: ")

        if operation == "=":
            print("Final answer:", answer)
            break

        if operation not in ["+", "-", "*", "/"]:
            print("That is not a valid operation.")
            continue

        next_number = float(input("Enter the next number: "))

        if operation == "+":
            answer = add(answer, next_number)

        elif operation == "-":
            answer = subtract(answer, next_number)

        elif operation == "*":
            answer = multiply(answer, next_number)

        elif operation == "/":
            answer = divide(answer, next_number)

        print("Current answer:", answer)