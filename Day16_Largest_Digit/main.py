#Day 16 – Find the Largest Digit
"""
Write a Python program that accepts an integer from the user and finds the largest digit present in that number.

Examples:

Input: 58321
Output: 8
Input: 4079
Output: 9

Also handle:

Input: 0
Output: 0

For negative numbers, consider only the digits:

Input: -583
Output: 8

Challenge: Don't convert the number to a string and don't use max().
"""

num = abs(int(input("Enter the num:")))

largest = 0

while num != 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num = num // 10

print(f"{largest} is is the largest digit.")

