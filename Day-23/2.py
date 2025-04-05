import re

text = "Python123"
if re.fullmatch(r"[A-Za-z0-9]+", text):
    print("String is alphanumeric.")
else:
    print("String is not alphanumeric.")
