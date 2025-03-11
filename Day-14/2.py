import math

class Shape:
    def area(self):
        pass  # Placeholder method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

c = Circle(5)
r = Rectangle(4, 6)

print(f"Circle Area: {c.area()}")
print(f"Rectangle Area: {r.area()}")
