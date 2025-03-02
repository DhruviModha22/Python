# Write a function that accepts **kwargs to print out a formatted description of a person (e.g., name, age, city).

def print_person_description(**kwargs):
    """
    Prints a formatted description of a person.

    Args:
        **kwargs (dict): A dictionary containing the person's name, age, and city.

    Returns:
        None
    """
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Test the function

person_info = {
    "name": "Dhruvi",
    "age": 18,
    "city": "Ahmedabad"
}

print_person_description(**person_info)
