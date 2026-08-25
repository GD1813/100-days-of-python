# Day 24 – Find All Factors of a Number

"""
Today we'll build directly on Day 23 (Perfect Number).

Write a Python program that accepts an integer and prints all factors/divisors of that number.

A factor is a number that divides the given number exactly, leaving remainder 0.

Examples

For 12:

Input: 12

Output:
1
2
3
4
6
12

Because:

12 % 1 = 0
12 % 2 = 0
12 % 3 = 0
12 % 4 = 0
12 % 6 = 0
12 % 12 = 0

For 7:

Input: 7

Output:
1
7
📚 Concepts You'll Practice
for loop
range()
% modulus operator
Divisibility
Conditional statements
Loop control
💡 Hint

You already used almost the same logic in Day 23.

Instead of:

id="day24_hint"
divisor += i

you need to print the divisor when you find one:

if num % i == 0:
    print(i)

This time, however, include the number itself.

For 12, your loop needs to check:

1 → 12

not just:

1 → 11
"""

num = abs(int(input("Enter the number: ")))

for i in range(1,num+1):
    if num % i == 0 :
        print(i)

