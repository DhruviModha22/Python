
a, b, c = map(int, input("Enter three numbers: ").split())
largest = (lambda x, y, z: max(x, y, z))(a, b, c)
print("Largest number:", largest)