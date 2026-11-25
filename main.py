 
import math


class Calculator:

    def __init__(self):
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, first_number, operation, second_number):

        if not isinstance(first_number, (int, float)):
            raise TypeError("First input must be a number.")

        if not isinstance(second_number, (int, float)):
            raise TypeError("Second input must be a number.")

        if operation not in self.operations:
            raise ValueError("Invalid operation symbol.")

        try:
            if operation == "/" and second_number == 0:
                raise ZeroDivisionError("Cannot divide by zero.")

            return self.operations[operation](first_number, second_number)

        except Exception as error:
            print("Calculation error:", error)
            raise


# Advanced mathematical functions

def exponentiation(a, b):
    return a ** b


def square_root(a, b):
    return math.sqrt(a)


def logarithm(a, b):
    return math.log10(a)


# Main program

calculator = Calculator()

# Add advanced operations

calculator.add_operation("**", exponentiation)
calculator.add_operation("sqrt", square_root)
calculator.add_operation("log", logarithm)


while True:

    print("\n===== PYTHON CALCULATOR =====")
    print("Available operations: +, -, *, /, **, sqrt, log")
    print("Type 'exit' to quit.")

    operation = input("Enter operation: ")

    if operation.lower() == "exit":
        print("Thank you for using the calculator!")
        break

    try:
        first_number = float(input("Enter first number: "))

        if operation in ["sqrt", "log"]:
            second_number = 0
        else:
            second_number = float(input("Enter second number: "))

        answer = calculator.calculate(
            first_number,
            operation,
            second_number
        )

        print("Answer:", answer)

    except (ValueError, TypeError, ZeroDivisionError) as error:
        print("Error:", error)

    except Exception as error:
        print("Something went wrong:", error)

