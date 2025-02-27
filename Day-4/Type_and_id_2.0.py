
var1 = 50
var2 = 50


print("\nBefore Modification:")
print(f"Memory Address of var1: {id(var1)}")
print(f"Memory Address of var2: {id(var2)}")
print(f"Are var1 and var2 sharing the same memory address? {id(var1) == id(var2)}")


var1 += 10
print("\nvar1 increamnet by 10:",var1)


print("\nAfter Modification:")
print(f"Memory Address of var1: {id(var1)}")
print(f"Memory Address of var2: {id(var2)}")
print(f"Are var1 and var2 sharing the same memory address now? {id(var1) == id(var2)}")
