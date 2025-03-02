# Implement a function that accepts product detauls like name, price, and quantity using **kwargs.
# -Return a formatted string shoqing the total cost of all products.

def calculate_total_cost(**kwargs):
    """
    Accepts product details like name, price, and quantity using **kwargs.

    Returns:
        str: Formatted string showing the total cost of all products.
    """
    total_cost = 0
    for product, details in kwargs.items():
        name = details['name']
        price = details['price']
        quantity = details['quantity']
        cost = price * quantity
        total_cost += cost
        formatted_cost = f"{name}: {cost:.2f}"
        print(formatted_cost)
    return f"Total cost: {total_cost:.2f}"


# Test the function with named arguments
total_cost = calculate_total_cost(
    product1={'name': 'Product 1', 'price': 10.99, 'quantity': 2},
    product2={'name': 'Product 2', 'price': 5.99, 'quantity': 3},
    product3={'name': 'Product 3', 'price': 8.99, 'quantity': 1}
)

print(total_cost)
