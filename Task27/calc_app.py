def write_to_file(equation, answer):
    try:
        with open("equations.txt", "a") as f:
            f.write(f"{equation} = {answer}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def read_from_file():
    try:
        with open("equations.txt", "r") as f:
            equations = f.readlines()
            print("Previous Calculations:")
            for equation in equations:
                print(equation.strip())
    except FileNotFoundError:
        print("No previous calculations found.")


def perform_calculation():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation (+, -, *, /): ")

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        elif operation == "*":
            answer = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            answer = num1 / num2
        else:
            print("Invalid operation.")
            return

        equation = f"{num1} {operation} {num2}"
        print(f"The answer is: {answer}")
        write_to_file(equation, answer)
    except ValueError:
        print("Invalid input, please enter numerical values.")


if __name__ == "__main__":
    while True:
        choice = input(
            "Do you want to perform a calculation or print previous calculations? (calc/print/exit): "
        )
        if choice == "calc":
            perform_calculation()
        elif choice == "print":
            read_from_file()
        elif choice == "exit":
            break
        else:
            print("Invalid choice, please enter 'calc', 'print', or 'exit'.")
