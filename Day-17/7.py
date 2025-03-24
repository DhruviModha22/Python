class InvalidGradeError(Exception):
    pass

def validate_grade(grade):
    if not grade:
        raise AssertionError("Grade cannot be empty.")
    if not (0 <= grade <= 100):
        raise ValueError("Grade must be between 0 and 100.")
    if grade < 40:
        raise InvalidGradeError("Failing grade detected!")

    print("Grade is valid.")

validate_grade(85)  # Valid
# validate_grade(-5)  # Raises ValueError
# validate_grade(35)  # Raises InvalidGradeError
