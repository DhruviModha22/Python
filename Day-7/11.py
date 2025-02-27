# Create a tuple of 3 lists
my_tuple = ([1, 2], [3, 4], [5, 6])

# Modify one of the inner lists
my_tuple[1].append(7)
print("Modified tuple:", my_tuple)

# Explanation:
# Tuples are immutable, meaning their structure cannot change (no adding/removing elements).
# However, if a tuple contains mutable elements (like lists), those elements can be modified.
# Here, we modified an inner list, but the tuple itself remains unchanged.