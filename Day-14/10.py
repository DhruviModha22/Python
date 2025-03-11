class Person:
    pass

class Student(Person):
    pass

print(issubclass(Student, Person))  # True
print(issubclass(Person, Student))  # False
