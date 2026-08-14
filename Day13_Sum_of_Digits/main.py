# Day 13 – Sum of Digits
"""
Write a Python program that accepts an integer from the user and calculates the sum of all its digits.

Examples:

Input: 12345
Output: 15

Because:

1 + 2 + 3 + 4 + 5 = 15

Also handle:

Input: 0
Output: 0

and negative numbers:

Input: -123
Output: 6
📚 Concepts You'll Practice
while loop
Modulus operator (%)
Integer division (//)
abs()
Accumulator variable
User input
f-strings

Challenge: Do not convert the number to a string. Use the digit-processing technique you learned in Day 12.
"""
a = int(input("Enter the number:"))

num = abs(a)
b = 0
while num != 0:
    digit = num % 10
    b += digit
    num = num // 10
print(b)

