import sys
if len(sys.argv) == 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("The sum is:", num1 + num2)
else:
    print("Usage: python script.py <num1> <num2>")
