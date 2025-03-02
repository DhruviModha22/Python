#Create a lambda function to calculate the square of number. 
# -Use it inside a map() function to gererate a list of sqaures from a given list of numbers.
nums = list(map(int, input("Enter numbers separated by space: ").split()))
squares = list(map(lambda x: x ** 2, nums))
print("Squares:", squares)