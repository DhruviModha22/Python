import math
try:
    num = float(input("Enter a number: "))
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    sqrt_result = math.sqrt(num)
except ValueError as e:
    print("Error:", e)
else:
    print("Square root:", sqrt_result)
finally:
    print("Execution complete.")