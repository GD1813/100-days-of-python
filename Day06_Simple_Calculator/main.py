# Day 6 – Simple Calculator
"""
📝 Problem Statement

Write a Python program that:

Accepts two numbers from the user.
Asks the user to choose an operation:
+ Addition
- Subtraction
* Multiplication
/ Division
Performs the selected operation.
Displays the result.
If the user enters an invalid operator, display an appropriate error message.
"""

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

choice = input("Enter the operation (+, -, *, /): ")

if choice == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Cannot divide by zero")
else:
    print("The operation choice entered is invalid.")