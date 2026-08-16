# Day 15 – Palindrome Number Checker
"""
Write a Python program that accepts an integer from the user and checks whether the number is a palindrome.

A palindrome number reads the same forward and backward.

Examples:

Input: 121
Output: 121 is a palindrome number.
Input: 123
Output: 123 is not a palindrome number.

Also handle:

Input: 0
Output: 0 is a palindrome number.
📚 Concepts You'll Practice
while loop
% 10
// 10
abs()
Number reversal
if-else
Comparison operators
💡 Hint

You already solved almost everything in Day 14.

Think:

Original number → Reverse the number → Compare both
"""

num = abs(int(input("Enter the number:")))

a = num

result = 0
while num != 0:
    digit = num % 10
    result = digit + result * 10
    num = num // 10

if a == result:
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is not a palindrome.")