# Write a UDF that takes a String as input and returns the frequency of each character in the string as a dictonary.

def char_frequency(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

# Test the function

input_string = "Hello, World!"
frequency_dict = char_frequency(input_string)
print(frequency_dict)

