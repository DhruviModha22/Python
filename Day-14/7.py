import math

class Shape:
    @staticmethod
    def area(radius=None, length=None, width=None):
        if radius:
            return math.pi * radius ** 2
        elif length and width:
            return length * width
        else:
            return None

print(Shape.area(radius=5))        # Circle area
print(Shape.area(length=4, width=6))  # Rectangle area
