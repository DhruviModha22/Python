string = input("Enter a string: ")
frequency = {char: string.count(char) for char in string}
print("Character frequency:", frequency)