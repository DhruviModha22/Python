def outer_rectangle_area(length, width):
    def inner_square_area(side):
        return side ** 2
    return length * width, inner_square_area(length)

rect_area, square_area = outer_rectangle_area(5, 4)
print(f"Rectangle Area: {rect_area}, Square Area: {square_area}")
