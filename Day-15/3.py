class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __eq__(self, other):
        return self.area() == other.area()

r1 = Rectangle(4, 5)
r2 = Rectangle(2, 10)
print(r1 == r2)  # Output: True
