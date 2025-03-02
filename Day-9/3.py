# Implement a program where a UDF accepts a list of interger and returns the square of each interger in a new list using a list comprehension.

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

# Test the function

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print("Squared numbers:", squared_numbers)
