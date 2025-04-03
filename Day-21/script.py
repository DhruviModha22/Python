# script.py

import math_utils

print("Addition:", math_utils.add(5, 3))
print("Subtraction:", math_utils.subtract(10, 4))
print("Multiplication:", math_utils.multiply(6, 7))
print("Division:", math_utils.divide(20, 4))


import string_utils

text = "Hello World"
print("Number of vowels:", string_utils.count_vowels(text))



import greet

greet.greet("Dhruvi")



import helper

helper.helper_function()


from shapes import circle, rectangle

print("Circle Area:", circle.area(5))
print("Circle Circumference:", circle.circumference(5))
print("Rectangle Area:", rectangle.area(4, 6))
print("Rectangle Perimeter:", rectangle.perimeter(4, 6))



from utilities import file_utils, date_utils

# File operations
file_utils.write_to_file("sample.txt", "Hello, Dhruvi!")
print("File Content:", file_utils.read_from_file("sample.txt"))

# Date operations
print("Days Between 2024-01-01 and 2025-01-01:", date_utils.days_between("2024-01-01", "2025-01-01"))


import math

print("Math module attributes and methods:")
print(dir(math))


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}!"

student = Student("Dhruvi", 21)
print("Student class attributes and methods:")
print(dir(student))
