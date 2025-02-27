products = {'Laptop': 800, 'Phone': 500, 'Tablet': 300}
max_product = max(products, key=products.get)
print("Product with the highest price:", max_product)