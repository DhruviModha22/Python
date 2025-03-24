class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)
print(c1 * c2)  # Output: -11 + 23i
