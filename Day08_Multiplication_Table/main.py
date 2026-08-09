#Day 8 – Multiplication Table

"""
Problem Statement:

Write a Python program that accepts a number from the user and prints its multiplication table from 1 to 10.

📚 Concepts You'll Practice
for loop
range()
User input
Arithmetic operators
f-strings

Example: If the user enters 5, the program should display:
"""

num = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1,11):
    result = num * i
    print(f"{num} * {i} = {result}")