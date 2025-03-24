try:
    filename = input("Enter filename to open: ")
    file = open(filename, "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("No file to close.")