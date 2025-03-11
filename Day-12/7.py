class Employee:
    def __init__(self):
        self.name = "Default"
        self.age = 0
        print("Employee created")

    def __del__(self):
        print("Employee deleted")

e = Employee()
del e
