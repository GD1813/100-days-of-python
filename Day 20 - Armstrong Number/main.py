#Day 20 – Check Armstrong Number

num = abs(int(input("Enter the number: ")))

armstrong = 0
original = num
real = num
number_of_digit = 0

while num != 0:
    num = num // 10
    number_of_digit += 1

if real == 0:
    number_of_digit = 1

while original != 0 :
    digit = original % 10
    armstrong = armstrong + digit ** number_of_digit
    original = original // 10

if real == armstrong :
    print(f"{armstrong} is armstrong number.")
else:
    print(f"{armstrong} it is not an armstrong number.")