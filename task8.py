# Task 8: Simple Calculator Module
# Create a simple calculator module with functions for addition, subtraction, multiplication, and division.
# Then, create a script that imports this module and allows the user to perform calculations by entering two numbers and choosing an operation.

import calculator

def task8():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    operation = input("Choose an operation (+, -, *, /): ")

    try:
        if operation == "+":
            result = calculator.add(number1, number2)

        elif operation == "-":
            result = calculator.subtract(number1, number2)

        elif operation == "*":
            result = calculator.multiply(number1, number2)

        elif operation == "/":
            result = calculator.divide(number1, number2)

        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


task8()