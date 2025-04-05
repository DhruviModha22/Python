import re

text = "Python is Amazing. Regular Expressions are Powerful."
matches = re.findall(r'\b[A-Z][a-z]*\b', text)
print("Capitalized words:", matches)
