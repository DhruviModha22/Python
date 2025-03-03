tuples_list = [(1, 5), (2, 3), (3, 8), (4, 1)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)