class Person:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0")

    def get_age(self):
        return self.__age

p = Person("John", 25)
print("Age:", p.get_age())

p.set_age(-5)  # Invalid
