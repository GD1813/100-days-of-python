# Day Write a Python program that accepts a number n from the user and prints the first n terms of the Fibonacci series.
"""
The Fibonacci sequence starts with:

0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Each number is obtained by adding the previous two numbers.

Examples
Input: 5

Output:
0 1 1 2 3
Input: 10

Output:
0 1 1 2 3 5 8 13 21 34

For:

Input: 1

Output:

0
📚 Concepts You'll Practice
for loop
Variables
Multiple variable assignment
Arithmetic operators
User input
if-else
Sequence generation
💡 Hint

Start with:

first = 0
second = 1

Then think about how you can repeatedly calculate:

next = first + second

and update:

first
second

Challenge: Generate the series using a loop. Don't use recursion yet.

Write it yourself and send me your code.
"""
num = int(input("Enter the number: "))

first_num = 0
second_num = 1

for i in range(num):
    print(first_num, end="\t")
    next = first_num + second_num
    first_num = second_num
    second_num = next




