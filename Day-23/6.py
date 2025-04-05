import re

text = "The deadlines are 12/01/2025, 25/12/2024, and 01/01/2026"
dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
print("Dates found:", dates)
