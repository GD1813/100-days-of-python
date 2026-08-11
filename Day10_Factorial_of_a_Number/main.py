# Day 10 – Factorial of a Number
"""
Problem Statement:

Write a Python program that accepts a non-negative integer from the user and calculates its factorial using a for loop.

Example:

If the user enters 5:

5! = 120

Remember:

5! = 5 × 4 × 3 × 2 × 1 = 120

Also consider the special case:

0! = 1
📚 Concepts You'll Practice
for loop
range()
Accumulator variable
Multiplication
if-else
User input
f-strings
"""

num = int(input("Enter the number to know the factorial of the number: "))

result = 1
if num < 0:
    print(f"{num} is a negative number, so factorial is not defined.")
else:
    for i in range(num,0,-1):
        result *= i
    print(f"Factorial of {num} is {result}.")