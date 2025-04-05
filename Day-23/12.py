import re

text = "My PIN code is 12345"
new_text = re.sub(r'\d', '*', text)
print("Modified text:", new_text)
