def search_word(filename, word):
    with open(filename, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            if word in line:
                print(f"Word found in line {i}: {line.strip()}")

search_word("sample.txt", "Python")


with open("sample.txt", "r") as src, open("backup.txt", "w") as dest:
    dest.write(src.read())
