import re

text = "Visit https://www.google.com or http://example.org for details."
urls = re.findall(r'https?://[^\s]+', text)
print("URLs found:", urls)
