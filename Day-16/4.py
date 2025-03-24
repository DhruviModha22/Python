try:
    text = input("Enter a string: ")
    index = int(input("Enter index: "))
    char = text[index]
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
else:
    print("Character at index:", char)