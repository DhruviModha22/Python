'''Create a program that:
   -Accepts a user's age as input.
   -Uses nested `if-else` statements to categorize the user into age groups:
      child(0-12)
      Teenager(13-19)
      Adult(20-59)
      Senior(60+)'''

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age. Please enter a positive integer.")

elif age <= 12:
    print("You are a child.")

elif age <= 19:
    print("You are a teenager.")

elif age <= 59:
    print("You are an adult.")
else:
    print("You are a senior.")