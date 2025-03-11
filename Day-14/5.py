class Calculator:
    def multiply(self, a, b, c=1):  # Default argument for third parameter
        return a * b * c

calc = Calculator()
print(calc.multiply(2, 3))       # 6
print(calc.multiply(2, 3, 4))    # 24
