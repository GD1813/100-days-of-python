# Day 28 — Sum of All Factors

num1 = abs(int(input("Enter the number: ")))

total = 0

if num1 == 0:
    total = 0
else:
    for i in range(1,num1 + 1):
        if num1 % i == 0:
            total += i

print(f"The sum of all factors is {total}")