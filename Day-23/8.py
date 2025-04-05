import re

password = "StrongPass1@"
if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'\d', password) and
    re.search(r'[\W_]', password)):
    print("Strong password!")
else:
    print("Weak password.")
