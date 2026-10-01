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