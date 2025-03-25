lines = [
    "Python is easy to learn.\n",
    "It has numerous libraries.\n",
    "File handling is one of its features.\n"
]
with open("notes.txt", "w") as file:
    file.writelines(lines)