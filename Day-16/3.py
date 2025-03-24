try:
    filename = input("Enter filename: ")
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Unable to read file.")
else:
    print("File content:\n", content)