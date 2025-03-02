#Wrute a program to filter out odd numbers from a list using a lamba function and the filter() method.
nums = list(map(int, input("Enter numbers separated by space: ").split()))
odd_numbers = list(filter(lambda x: x % 2 != 0, nums))
print("Odd numbers:", odd_numbers)