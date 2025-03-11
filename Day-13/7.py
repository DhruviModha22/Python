a = 10
b = 10
c = 20

print("Memory address of a:", id(a))
print("Memory address of b:", id(b))  # Same as 'a' due to Python's integer caching
print("Memory address of c:", id(c))  # Different from 'a' and 'b'
