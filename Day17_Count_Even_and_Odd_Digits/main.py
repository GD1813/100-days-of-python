#Day 17 – Count Even and Odd Digits
"""
Write a Python program that accepts an integer from the user and counts how many even digits and odd digits are present in the number.

Examples:

Input: 123456
Output:
Even digits: 3
Odd digits: 3

For:

Input: 2468
Output:
Even digits: 4
Odd digits: 0

Also handle:

Input: 0
Output:
Even digits: 1
Odd digits: 0

For negative numbers, consider only the digits:

Input: -1234
Output:
Even digits: 2
Odd digits: 2
📚 Concepts You'll Practice
while loop
% 10 to extract digits
// 10 to remove digits
abs()
if-else
Counter variables
Modulus operator (%)

Challenge: Don't convert the number to a string.
"""

num = abs(int(input("Enter the number: ")))

even = 0
odd = 0


if num == 0 :
    even = 1
else:
    while num > 0:
        digit = num % 10
        if digit % 2 == 0 :
            even += 1
        else:
            odd += 1
        num = num // 10

print(f"Odd number = {odd}")
print(f"Even number = {even}")


