#Day 5 – Largest of Three Numbers

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

if num1 > num2 and num1 > num3 :
    print(f"{num1} is greater than {num2} and {num3}.")
elif num2 > num1 and num2 > num3 :
    print(f"{num2} is greater than {num1} and {num3}.")
elif num3 > num1 and num3 > num2 :
    print(f"{num3} is greater than {num1} and {num2}.")
elif num1 == num2 and num1 > num3:
    print(f"{num1} and {num2} are greater than {num3}")
elif num1 == num3 and num1 > num2:
    print(f"{num1} and {num3} are greater than {num2}")
elif num2 == num3 and num2 > num1:
    print(f"{num2} and {num3} are greater than {num1}")
else:
    print("The three numbers are equal!")
