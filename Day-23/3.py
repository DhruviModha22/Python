import re

text = "Learning Java first, then Python and Pythonic stuff"
match = re.search(r"\bPython\b", text)
if match:
    print("First 'Python' found at position:", match.start())
else:
    print("'Python' not found.")
