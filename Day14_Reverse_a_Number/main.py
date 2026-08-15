# Day 14 – Reverse a Number
"""
Write a Python program that accepts an integer from the user and prints the reverse of that number.

Examples:

Input: 12345
Output: 54321
Input: 1200
Output: 21

Also handle negative numbers:

Input: -123
Output: -321
📚 Concepts You'll Practice
while loop
% 10 to extract the last digit
// 10 to remove the last digit
abs()
Accumulator/result variable
User input
if-else

Challenge: Do not convert the number to a string. Use the digit-processing technique you learned in Days 12 and 13.
"""

a = int(input("Enter the number:"))

num = abs(a)

result = 0

while num != 0:
    digit = num % 10
    result = digit + result * 10
    num = num // 10

if a < 0:
    result = -result
    print(result)
elif a > 0:
    print(result)
else:
    print(0)



