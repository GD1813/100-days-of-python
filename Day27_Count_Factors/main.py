# Day 27 – Count the Number of Factors

num = abs(int(input("Enter the number: ")))

factor = 0
if num == 0:
    factor = 0
else:
    for i in range(1,num + 1):
        if num % i == 0:
            factor += 1

print(f"The number of factor is {factor}.")