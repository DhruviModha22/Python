import sys
user_input = input("Enter something: ")
if user_input.lower() == "exit":
    sys.exit("Exiting the program. Goodbye!")
else:
    print("You entered:", user_input)
