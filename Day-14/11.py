class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

m = Manager("Dhruvi", 80000, "HR")
print(f"Manager Name: {m.name}, Salary: {m.salary}, Department: {m.department}")
