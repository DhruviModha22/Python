# Create a program that takes a user-defined function as an argument to calculate the cube of a list of numbers.

def cube_numbers(numbers, function):
    """Calculate the cube of a list of numbers using a provided function."""
    return [function(n) ** 3 for n in numbers]

# Test the function

numbers = [1, 2, 3, 4, 5]
result = cube_numbers(numbers, lambda x: x)
print("Cube of each number in the list:", result)
