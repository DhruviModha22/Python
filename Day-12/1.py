# Create a class Person with attributes such as name and age.
# -Write a method to display the details.
# -Create multiple object and call the method for each.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
# Example usage
person1 = Person("Dhruvi", 25)
person1.display_details()
person2 = Person("Vansh", 30)
person2.display_details()
    