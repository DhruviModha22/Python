class Grandparent:
    def show(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def show(self):
        super().show()
        print("I am Parent")

class Teacher:
    def teach(self):
        print("I am a Teacher")

class Child(Parent, Teacher):
    def show(self):
        super().show()
        print("I am Child")

c = Child()
c.show()
c.teach()
