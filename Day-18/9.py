with open("sample.txt", "r+") as file:
    content = file.read()
    file.write("\nThis file was last modified by adding this sentence.")
    print("Updated content:\n", content)