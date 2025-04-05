import re

text = "172162543.*"
digits = re.findall(r'\d', text)
print("Digits found:", digits)
