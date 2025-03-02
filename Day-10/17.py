s = input("Enter a string: ")
vowels = "aeiouAEIOU"
v_str = "".join([ch for ch in s if ch in vowels])
c_str = "".join([ch for ch in s if ch not in vowels])
print("Vowels:", v_str, "Consonants:", c_str)