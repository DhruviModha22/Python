arr = [5, 3, 8, 1, 2]

# Using sort() (modifies the original list)
arr.sort()
print("Using sort():", arr)

# Resetting the list
arr = [5, 3, 8, 1, 2]

# Using sorted() (returns a new sorted list)
new_arr = sorted(arr)
print("Using sorted():", new_arr)
print("Original list remains unchanged:", arr)