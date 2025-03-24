class Parent:
    def displayO(self):
        print("This is the Parent class method.")

class Child(Parent):
    pass  # Inherits displayO from Parent

# Creating object of Child class
child_obj = Child()
child_obj.displayO()
