count = 0
def increment_count():
    global count
    count += 1
    print("Function called", count, "times")

for _ in range(3):  # Calling function multiple times
    increment_count()