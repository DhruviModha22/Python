for num in range(1, 51):
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} - Divisible by both 2 and 3")
    elif num % 2 == 0:
        print(f"{num} - Divisible by 2")
    elif num % 3 == 0:
        print(f"{num} - Divisible by 3")
    else:
        print(f"{num} - Not divisible by 2 or 3")
    