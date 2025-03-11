def outer_square(n):
    def inner_cube(n):
        return n ** 3
    return n ** 2, inner_cube(n)

sq, cb = outer_square(4)
print(f"Square: {sq}, Cube: {cb}")
