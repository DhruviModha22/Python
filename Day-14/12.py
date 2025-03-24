class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))        # True
print(issubclass(Parent, Grandparent))  # True
print(issubclass(Child, Grandparent))   # True
