def outer_length(s):
    def inner_length():
        print("Length of string:", len(s))
    inner_length()

outer_length("Hello World")
