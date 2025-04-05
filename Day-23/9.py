import re

text = "Follow #Python, #Coding, and #DataScience"
hashtags = re.findall(r'#\w+', text)
print("Hashtags found:", hashtags)
