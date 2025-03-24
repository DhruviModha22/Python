def check_palindrome(s):
    assert s, "Input string cannot be empty."
    return s == s[::-1]

print(check_palindrome("madam"))  # True
# check_palindrome("")  # Raises AssertionError
