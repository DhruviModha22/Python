# Write a rescursive function to calculate the factorial of a given number.
#  - Ensure the program handles edge cases (e,g., negetive inputs).

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    elif n<=0:
        return 0
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)

# Test the function
print(factorial(5))  # Expected output: 120

print(factorial(0))  # Expected output: 1

print(factorial(1))  # Expected output: 1

print(factorial(-5))  # Expected output: 0 (since factorial is not defined for negative numbers)