# Day 22 – Fibonacci Series: Find the nth Term

"""
Write a Python program that accepts n from the user and finds the nth Fibonacci term.

Use 0-based indexing:

F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
...
Examples
Input: 0
Output: 0
Input: 5
Output: 5
Input: 7
Output: 13
"""

num = int(input("Enter the number: "))

if num == 0 :
    second_num = 0
else:
    first_num = 0
    second_num = 1
    for i in range(num):
        next_num = first_num + second_num
        first_num = second_num
        second_num = next_num

print(second_num)

