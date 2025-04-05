import re

text = "Contact us at support@company.com or sales@company.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print("Email addresses:", emails)
