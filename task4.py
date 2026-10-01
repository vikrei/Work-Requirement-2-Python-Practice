# Task 4:Math Quiz with Exception Handling
# Create a simple math quiz that generates two random numbers and asks the user to add them. 
# Use native random module.

import random

def MathQuiz():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)

    print(f"What is {number1} + {number2}?")

    try:
        answer = int(input("Your answer: "))

        if answer == number1 + number2:
            print("Correct!")
        else:
            print("Wrong answer.")

    except ValueError:
        print("Invalid input!")


MathQuiz()