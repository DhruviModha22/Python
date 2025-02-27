# Input list of words
words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi", "elephant"]

# Define vowels
vowels = "AEIOUaeiou"

# Use list comprehension to filter words starting with a vowel
filtered_words = [word for word in words if word[0] in vowels]

# Print the result
print(filtered_words)
