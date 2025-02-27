# Set the number of rows for the upper part of the pattern
n = 3  # You can change this value to adjust the size of the pattern

# Print the upper part of the pattern
for i in range(1, n + 1):
    print('* ' * i)

# Print the lower part of the pattern
for i in range(n - 1, 0, -1):
    print('* ' * i)