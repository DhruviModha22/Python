modes = {
    "r": "r", "w": "w", "a": "a",
    "rt": "rt", "wt": "wt", "at": "at"
}

for mode, desc in modes.items():
    with open("sample.txt", mode) as file:
        if "r" in mode:
            print(f"{desc} mode: Reading file content")
            print(file.read())
        else:
            print(f"{desc} mode: Writing content")
            file.write("Testing different file modes.\n")