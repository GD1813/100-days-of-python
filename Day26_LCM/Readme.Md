# Day 26 - LCM of Two Numbers

## 📖 Description

This is my **Day 26** program for the **100 Days of Python** challenge.

The program accepts two integers from the user and finds their **Least Common Multiple (LCM)**.

The LCM is the smallest positive integer that is divisible by both numbers without leaving a remainder.

For example:

12 → 12, 24, 36, 48, ...

18 → 18, 36, 54, 72, ...

The common multiples are:

36, 72, ...

Therefore:

LCM = 36

---

## 💻 Program

```
# Day 26 - LCM of Two Numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

divisor = 0

if num1 == 0 or num2 == 0:
    divisor = 0
else:
    for i in range(1, num1 * num2 + 1):
        if i % num1 == 0 and i % num2 == 0:
            divisor = i
            break

print(divisor)
```

---

## ▶️ Sample Output

![Program Output](output.png)

---

## 📚 Concepts Practiced

* Variables
* User Input
* Type Conversion (`int()`)
* `for` Loop
* `range()` Function
* Modulus Operator (`%`)
* Divisibility
* Conditional Statements
* `if` and `else`
* Comparison Operators
* Logical Operator (`or`)
* Logical Operator (`and`)
* Finding Common Multiples
* Finding the Smallest Value
* `break` Statement
* `print()` Function

---

## 🎯 What I Learned

* What LCM means.
* How to find common multiples of two numbers.
* How to check whether a number is divisible by another number using `%`.
* How to find the smallest common multiple.
* How to use `break` to stop the loop after finding the first common multiple.
* How to handle zero as an input.
* How to use `if` and `else` to handle different cases.
* How to solve the problem without using `math.lcm()`.

---

## 🔑 Important Technique

```
for i in range(1, num1 * num2 + 1):
    if i % num1 == 0 and i % num2 == 0:
        divisor = i
        break
```

The loop checks possible multiples starting from `1` and determines whether they are divisible by both numbers.

Because the loop checks the values from smallest to largest, the first common multiple found is the **Least Common Multiple**.

The `break` statement stops the loop immediately after finding the LCM.

---

## 🚀 Future Improvement

A more efficient approach for finding the LCM is to use the relationship between **LCM and GCD**:

```
LCM(a, b) = |a × b| / GCD(a, b)
```

This program intentionally uses the basic common-multiple approach to strengthen understanding of loops, divisibility, conditional logic, and the `break` statement.

---

**Challenge:** 100 Days of Python
**Day:** 26/100 ✅
