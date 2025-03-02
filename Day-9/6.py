# Write a python function that accepts an arbitrary number of integer arguments and return their sum and product.

def sum_and_product(*args):
    """
    Accepts an arbitrary number of integer arguments and returns their sum and product.

    Args:
        *args (int): Variable number of integer arguments.

    Returns:
        tuple: A tuple containing the sum and product of the arguments.
    """
    # Initialize sum and product variables
    sum_val = 0
    product_val = 1
    # Iterate through the arguments
    for arg in args:
        # Add the argument to the sum
        sum_val += arg
        # Multiply the argument with the current product
        product_val *= arg
    # Return the sum and product as a tuple
    return sum_val, product_val

# Test the function

print(sum_and_product(1, 2, 3, 4, 5))  
print(sum_and_product(-1, -2, -3, -4, -5)) 
print(sum_and_product(0, 1, 2, 3, 4)) 
print(sum_and_product(5))  
print(sum_and_product()) 
