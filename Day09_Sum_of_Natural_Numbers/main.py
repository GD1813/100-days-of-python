# Day 9 – Sum of Natural Numbers
"""
Problem Statement:

Write a Python program that accepts a positive integer n from the user and calculates the sum of all natural numbers from 1 to n.

Example:

If the user enters 5:

1 + 2 + 3 + 4 + 5 = 15
📚 Concepts You'll Practice
for loop
range()
Variables
User input
Arithmetic operators
Accumulator variable
f-strings

Hint: You'll need a variable to keep track of the running total.
"""

num = int(input("Enter the number for which you want the sum of all natural numbers: "))


result = 0

for n in range(1,num+1):
    result += n
print(f"The sum of natural numbers up to {num} is {result}.")
