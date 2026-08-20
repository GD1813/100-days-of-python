# Day 19 – Product of Digits
"""
Write a Python program that accepts an integer from the user and calculates the product of all its digits.

Examples
Input: 1234
Output: 24

Because:

1 × 2 × 3 × 4 = 24

Another example:

Input: 305
Output: 0

Because:

3 × 0 × 5 = 0

Also handle negative numbers:

Input: -123
Output: 6

And:

Input: 0
Output: 0
"""

num = abs(int(input("Enter the number:")))

product = 1

if num == 0:
    product = 0
else:
    while num != 0:
        digit =  num % 10
        product *= digit
        num = num // 10

print(f"The product of the digit is {product}")


