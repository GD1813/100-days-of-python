# Day 12 – Count the Digits of a Number

"""
Problem Statement:

Write a Python program that accepts an integer from the user and counts how many digits it contains.

Examples:

Input: 12345
Output: 5 digits
Input: 789
Output: 3 digits

Also handle:

Input: 0
Output: 1 digit

And consider negative numbers such as:

Input: -1234
Output: 4 digits
📚 Concepts You'll Practice
"""

a = int(input("Enter the number: "))

num = abs(a)

digit = 0

if num == 0:
    print(f"1 digit")
else:
    while num > 0 :
        b = num // 10
        digit += 1
        num = b
    print(f"{digit} digits")


