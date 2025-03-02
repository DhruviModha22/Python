# Develop a program that uses a UDF to return the Fibonacci sequence up to a given number.
# - Include a detailed __doc__ string explaining the function's working, input, and output.

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth number.

    Parameters:
    n (int): The position in the Fibonacci sequence to generate.

    Returns:
    list: A list containing the Fibonacci sequence up to the nth number.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence

# Test the function

n = int(input("Enter a number: "))
print(f"Fibonacci sequence up to the {n}th number is:", fibonacci(n))