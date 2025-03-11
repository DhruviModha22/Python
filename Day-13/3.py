class Grandparent:
    def role(self):
        print("I am the Grandparent")

class Parent(Grandparent):
    def role(self):
        super().role()
        print("I am the Parent")

class Child(Parent):
    def role(self):
        super().role()
        print("I am the Child")

c = Child()
c.role()
