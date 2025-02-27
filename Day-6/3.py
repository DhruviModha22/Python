string = "PYTHON"
vowels = "AEIOU"

for char in string:
    if char in vowels:
        continue
    print(char, end="")
