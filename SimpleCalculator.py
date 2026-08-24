def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Error: You cannot divide by zero.")
        return a
    return a / b


def power(a, b):
    return a ** b


def remainder(a, b):
    if b == 0:
        print("Error: You cannot divide by zero.")
        return a
    return a % b


def square_root(a):
    if a < 0:
        print("Error: You cannot find the square root of a negative number.")
        return a
    return a ** 0.5


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def show_history(history):
    if len(history) == 0:
        print("No calculations yet.")
    else:
        print("\n--- History ---")
        for item in history:
            print(item)


history = []

while True:
    print("\n--- Advanced Calculator ---")
    print("Enter 'q' to quit.")
    print("Enter 'h' to view history.")

    first_input = input("Enter your first number: ")

    if first_input.lower() == "q":
        print("Goodbye!")
        break

    if first_input.lower() == "h":
        show_history(history)
        continue

    try:
        answer = float(first_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    while True:
        print("\nOperations: +  -  *  /  **  %  sqrt")
        print("Commands: = finish | c clear | h history | q quit")

        operation = input("Choose an operation: ").lower()

        if operation == "=":
            print("Final answer:", answer)
            break

        if operation == "c":
            print("Calculation cleared.")
            break

        if operation == "h":
            show_history(history)
            continue

        if operation == "q":
            print("Goodbye!")
            quit()

        if operation == "sqrt":
            old_answer = answer
            answer = square_root(answer)
            history.append(f"√{old_answer} = {answer}")
            print("Current answer:", answer)
            continue

        if operation not in ["+", "-", "*", "/", "**", "%"]:
            print("That is not a valid operation.")
            continue

        next_number = get_number("Enter the next number: ")
        old_answer = answer

        if operation == "+":
            answer = add(answer, next_number)
        elif operation == "-":
            answer = subtract(answer, next_number)
        elif operation == "*":
            answer = multiply(answer, next_number)
        elif operation == "/":
            answer = divide(answer, next_number)
        elif operation == "**":
            answer = power(answer, next_number)
        elif operation == "%":
            answer = remainder(answer, next_number)

        history.append(f"{old_answer} {operation} {next_number} = {answer}")
        print("Current answer:", answer)