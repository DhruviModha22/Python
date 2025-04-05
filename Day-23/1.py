import re

text = "Hello everyone in this beautiful World"
if re.match(r"^Hello.*World$", text):
    print("Match found!")
else:
    print("No match.")
