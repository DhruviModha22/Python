import sys
import math

if len(sys.argv) == 2:
    num = int(sys.argv[1])
    print(f"The factorial of {num} is: {math.factorial(num)}")
else:
    print("Usage: python script.py <number>")
