# Develop a program using recursion to reverse a string

def reverse_string(input_string):
    # Base case: if the string is empty, return it
    if len(input_string) == 0:
        return input_string
    else:
        # Recursive case: reverse the rest of the string and concatenate the first character
        return reverse_string(input_string[1:]) + input_string[0]
    
# Test the function with some inputs

print(reverse_string("Hello, World!"))  

print(reverse_string("Python"))  

print(reverse_string(""))  

print(reverse_string("1234567890")) 