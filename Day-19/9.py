import time

seconds = int(input("Enter the number of seconds: "))

for i in range(seconds, 0, -1):
    print(f"Time remaining: {i} seconds", end="\r")
    time.sleep(1)

print("Time's up!")
