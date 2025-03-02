# Create a user-defined fumction (UDF) that calculates the factorial of a given number.


def factorial(n):
    """Calculate the factorial of a number using recursion."""
    return 1 if n == 0 else n * factorial(n - 1)

# Test the function

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}") 



