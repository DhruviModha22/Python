user_input=input("Enter a value: ")

int_value=int(user_input)
float_value=float(user_input)
bool_value=bool(user_input)
str_value=str(user_input)

print("\nType casting Results: ")
print(f"Interger value: {int_value} (Type: {type(int_value)})")

print(f"Float value: {float_value} (Type: {type(float_value)})")

print(f"Boolean value: {bool_value} (Type: {type(bool_value)})")

print(f"String value: {str_value} (Type: {type(str_value)})")
