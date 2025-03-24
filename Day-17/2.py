def check_even(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number % 2 != 0:
        raise ValueError("Number is odd, expected an even number.")
    print(f"{number} is even.")

check_even(4)  # Valid
# check_even("hello")  # Raises TypeError
# check_even(5)  # Raises ValueError
