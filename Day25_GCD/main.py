# Day 25 – Find the GCD (HCF) of Two Numbers

num1 = abs(int(input("Enter the first number: ")))
num2 = abs(int(input("Enter the second number: ")))

gcd = 0

if num1 == 0 :
    gcd = num2
elif num2 == 0:
    gcd = num1
else:
    for i in range(1, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

print(f"{gcd} is the greatest divisor.")

