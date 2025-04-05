import sys

if len(sys.argv) < 2:
    print("Usage: python script.py num1 num2 ...")
else:
    numbers = list(map(float, sys.argv[1:]))
    avg = sum(numbers) / len(numbers)
    print("Average is:", avg)
