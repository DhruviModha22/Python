import re

text = "This is a test string"
words = re.split(r'\s+', text)
print("Words:", words)
