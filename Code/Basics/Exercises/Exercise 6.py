# Exercise 6: Basic Calculator 

operator = input("Input an operator (+, -, *, /): ")
num1 = float(input("Input your first number"))
num2 = float(input("Input your second number"))

if operator == "+":
    print(round(num1 + num2, 3))
elif operator == "-":
    print(round(num1 - num2, 3))
elif operator == "*":
    print(round(num1 * num2, 3))
elif operator == "/":
    print(round(num1 / num2, 3))
else:
    print(f"'{operator}' is an invalid operator")