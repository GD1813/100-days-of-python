# Day 26 – Find the LCM of Two Numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
divisor = 0

if num1 == 0 or num2 == 0:
    divisor =0
else:
    for i in range(1,num1 * num2 + 1):
        if i % num1 == 0 and i % num2 == 0:
            divisor = i
            break

print(divisor)