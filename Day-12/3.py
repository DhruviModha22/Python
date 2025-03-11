# Write a program that creates multiple objects of a class and deletes them using the del
# keyword.
# - Observe the behavior.

class Sample:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} deleted")

# Creating multiple objects
s1 = Sample("A")
s2 = Sample("B")

# Deleting an object
del s1
del s2
