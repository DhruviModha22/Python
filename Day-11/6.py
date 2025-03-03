matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_value = max(max(row) for row in matrix)
min_value = min(min(row) for row in matrix)
print("Max:", max_value, "Min:", min_value)