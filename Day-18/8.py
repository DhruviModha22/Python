def count_file_content(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        print(f"Lines: {len(lines)}, Words: {word_count}, Characters: {char_count}")

count_file_content("sample.txt")