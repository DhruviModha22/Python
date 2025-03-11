class Parent:
    def displayO(self):
        print("This is the Parent class method")

class Child(Parent):
    def show(self):
        print("This is the Child class method")

c = Child()
c.displayO()  # Calling parent class method
c.show()  # Calling child class method
