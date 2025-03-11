class Animal:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Animal Name: {self.name}")

a = Animal("Tiger")
a.display_name()
