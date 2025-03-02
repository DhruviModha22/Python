# Create a recursive fumction to print all prime numbers between two given numbers.

# Helper function to check if a number is prime
def is_prime(n, i=2):
    if n < 2:
        return False
    if i * i > n:  # Base case: if i exceeds sqrt(n), n is prime
        return True
    if n % i == 0:  # If divisible, it's not prime
        return False
    return is_prime(n, i + 1)  # Recursive check for next divisor

# Recursive function to print prime numbers in range
def print_primes(start, end):
    if start > end:  # Base case: stop when start exceeds end
        return
    if is_prime(start):  # Print if it's prime
        print(start, end=" ")
    print_primes(start + 1, end)  # Recursive call for next number

# Example usage
start=int(input("Enter start number: "))

end=int(input("Enter end number: "))
print_primes(start, end)
