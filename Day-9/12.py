# # Create a function that calculates the are of a rectangle.
# - Add a __doc__ string to describe the function's purpose, parameters, and return type.
# - Write code to print the __doc__ string.

def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

# Test the function

length = 5
width = 3
area = calculate_rectangle_area(length, width)
print(f"The area of a rectangle with length {length} and width {width} is {area} square units.")
