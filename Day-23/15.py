import re

plate = "AB-12-3456"
if re.fullmatch(r'[A-Z]{2}-\d{2}-\d{4}', plate):
    print("Valid license plate")
else:
    print("Invalid license plate")
