#Day 11 – Prime Number Checker
"""
Problem Statement:


Write a Python program that accepts a positive integer from the user and determines whether the number is prime or not prime.

A prime number is a number greater than 1 that has only two factors: 1 and itself.

Examples:

2 → Prime
7 → Prime
10 → Not Prime
1 → Not Prime
📚 Concepts You'll Practice
for loop
range()
if-else
Modulus operator (%)
Boolean/flag variable
break
User input
"""

num = int(input("Enter the number to know if the number is a prime or not: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for n in range(2,num):
        if num % n == 0:
            is_prime = False

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

