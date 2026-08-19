# Day 18 – Find the Smallest Digit
"""
Write a Python program that accepts an integer from the user and finds the smallest digit present in that number.

Examples:

Input: 58321
Output: 1
Input: 4079
Output: 0

For a negative number, consider only its digits:

Input: -583
Output: 3

For 0:

Input: 0
Output: 0
"""

num = abs(int(input("Enter the number: ")))

smallest = 10

if num == 0:
    smallest = 0
else:
    while num != 0:
        digit = num % 10
        if smallest > digit:
            smallest = digit
        num = num // 10

print(f"{smallest} is the smallest digit!")

