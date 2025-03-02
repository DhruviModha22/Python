# Develop a program where a UDF accepts *agrs and filters out the string from the arguments.
# - Return a tuple of filered values (e.g,. strings in one tuple, numbers in another).

def filter_string_args(*args):
    string_args = ()
    number_args = ()
    for arg in args:
        if isinstance(arg, str):
            string_args += (arg,)
            continue
        if isinstance(arg, (int, float)):
            number_args += (arg,)
            continue
    return string_args, number_args

# Test the function

args = [1, 'Hello', 2.5, 'World', 3, '!', 4.7]
filtered_strings, filtered_numbers = filter_string_args(*args)
print(f"Filtered strings: {filtered_strings}")
print(f"Filtered numbers: {filtered_numbers}")