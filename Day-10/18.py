vowels="aeiouAEIOU"
words = input("Enter words separated by space: ")
vowel_words = [word for word in words if word[0].lower() in vowels]
consonant_words = [word for word in words if word[0].lower() not in vowels]
print("Words starting with vowels:", vowel_words)
print("Words starting with consonants:", consonant_words)