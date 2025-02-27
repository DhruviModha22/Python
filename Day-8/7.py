def factorial(n):
    """Calculate factorial of a number using recursion."""
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")