# Day 23 – Check if a Number is Perfect
"""
Write a Python program that accepts an integer and checks whether it is a Perfect Number.

A perfect number is a positive number whose proper divisors add up exactly to the number itself.

Examples

For 6:

Divisors of 6: 1, 2, 3

1 + 2 + 3 = 6

Therefore:

6 is a perfect number.

For 28:

1 + 2 + 4 + 7 + 14 = 28

So:

28 is a perfect number.

For 12:

1 + 2 + 3 + 4 + 6 = 16

Therefore:

12 is not a perfect number.
"""

num = abs(int(input("Enter the number:")))
a = num

divisor = 0

for i in range(1,num):
    if a % i == 0:
        divisor += i

if divisor == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
