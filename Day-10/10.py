total_sum = 0
def add_to_sum(n):
    global total_sum
    total_sum += n
    print("Updated sum:", total_sum)

nums = list(map(int, input("Enter numbers to add: ").split()))
for num in nums:
    add_to_sum(num)