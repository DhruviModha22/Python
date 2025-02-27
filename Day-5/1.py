'''Write a python program to :
  - Take a number as input from the user.
  -use an 'if-else' statement to check if the number is even or odd and print the result.'''


# Take input from the user

user_input = int(input("Enter a number: "))

# Check if the number is even or odd

if user_input % 2 == 0:
    print(f"{user_input} is an even number.")
else:
    print(f"{user_input} is an odd number.")

