
user_input = input("Enter a boolean value (True or False): ")


bool_value = user_input == "True"


int_value = int(bool_value)
str_value = str(bool_value)


print("\nConversion Results:")
print(f"Original boolean value: {bool_value}")
print(f"Converted integer value: {int_value}")
print(f"Converted string value: {str_value}")
