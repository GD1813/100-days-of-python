# Day 25 - GCD of Two Numbers

## 📖 Description

This is my **Day 25** program for the **100 Days of Python** challenge.

The program accepts two integers from the user and finds their **Greatest Common Divisor (GCD)**, also known as the **Highest Common Factor (HCF)**.

The GCD is the largest positive integer that divides both numbers without leaving a remainder.

For example:

12 → 1, 2, 3, 4, 6, 12

18 → 1, 2, 3, 6, 9, 18

The common divisors are:

1, 2, 3, 6

Therefore:

GCD = 6

---

## 💻 Program

    # Day 25 - GCD of Two Numbers

    num1 = abs(int(input("Enter the first number: ")))
    num2 = abs(int(input("Enter the second number: ")))

    gcd = 0

    if num1 == 0:
        gcd = num2
    elif num2 == 0:
        gcd = num1
    else:
        for i in range(1, num1 + 1):
            if num1 % i == 0 and num2 % i == 0:
                gcd = i

    print(f"{gcd} is the greatest divisor.")

---

## ▶️ Sample Output

![Program Output](output.png)

---

## 📚 Concepts Practiced

- Variables
- User Input
- Type Conversion (`int()`)
- `abs()` Function
- `for` Loop
- `range()` Function
- Modulus Operator (`%`)
- Divisibility
- Conditional Statements
- `if`, `elif`, and `else`
- Comparison Operators
- Logical Operator (`and`)
- Finding Common Divisors
- Tracking the Largest Value
- f-Strings
- `print()` Function

---

## 🎯 What I Learned

- What GCD/HCF means.
- How to find common divisors of two numbers.
- How to check whether a number divides another number using `%`.
- How to find the largest common divisor.
- How to use a variable to keep track of the latest common divisor.
- How to handle zero as an input.
- How to use `if`, `elif`, and `else` to organize different cases.
- How to solve the problem without using `math.gcd()`.

---

## 🔑 Important Technique

    for i in range(1, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

The loop checks possible divisors of the first number and determines whether they also divide the second number.

Because the loop checks the values from smallest to largest, the final common divisor stored in `gcd` is the greatest common divisor.

---

## 🚀 Future Improvement

A more efficient approach for finding the GCD is the **Euclidean Algorithm**.

This program intentionally uses the basic divisor-checking approach to strengthen understanding of loops, divisibility, and conditional logic.

---

**Challenge:** 100 Days of Python  
**Day:** 25/100 ✅