'''write a python program using a 'switch case' equivalent to:
-Take an operator(`+`,`-`,`*`,`/`)
-perform the corresponding operator on two numbers entered by the user'''

operator = input("Enter an operator (+, -, *, /): ")

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Error: Invalid operator. Please use (+, -, *, /).")