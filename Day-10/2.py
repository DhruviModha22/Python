# Implement a recursive function to calculate the nth fibonacci number.
# - test the function with various inputs. 

   
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function with some inputs

print(fibonacci(0))  # Expected output: 0
print(fibonacci(1))  # Expected output: 1
print(fibonacci(2))  # Expected output: 1
print(fibonacci(3))  # Expected output: 2
print(fibonacci(4))  # Expected output: 3