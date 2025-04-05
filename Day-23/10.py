import re

text = "Python is fun. Python is easy to learn."
new_text = re.sub(r'Python', 'Java', text)
print("Updated text:", new_text)
