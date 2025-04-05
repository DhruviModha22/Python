import re

text = "Call us at 123-456-7890 or 987-654-3210 for support."
phones = re.findall(r'\b\d{3}-\d{3}-\d{4}\b', text)
print("Phone numbers:", phones)
