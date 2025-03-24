class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email or not (email.endswith(".com") or email.endswith(".org")):
        raise InvalidEmailError("Invalid email format.")
    print("Email is valid.")

validate_email("test@example.com")  # Valid
# validate_email("invalid-email")  # Raises InvalidEmailError
