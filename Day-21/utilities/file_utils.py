# utilities/file_utils.py

def write_to_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)

def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()
