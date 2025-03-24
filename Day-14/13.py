class Base:
    def display(self):
        print("Base class method")

class Derived(Base):
    def display(self):
        super().display()
        print("Derived class method")

d = Derived()
d.display()
