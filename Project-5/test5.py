class Employee():  #Employee class 
    def __init__(self, eid, name, age,salary): #employee class constructor 
        self.__eid = eid
        self.name = name
        self.age = age
        self.__salary = salary

    def get_id(self):  
        return self.__eid 
    def set_id(self,new_id):
        self.__eid = new_id
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        self.__salary = new_salary

    def display(self):
        print(f"ID: {self.__eid}, name:{self.name}, age: {self.age}, salary: {self.__salary}")

    def __eq__(self, other):
        return self.__salary==other.__salary

    def __lt__(self, other):
        return self.__salary<other.__salary

    def __gt__(self, other):
        return self.__salary> other.__salary
    
class Manager(Employee):
    def __init__(self, eid, name, age, salary, department):
        super().__init__(eid, name, age, salary)
        self.department = department
    def display(self):
        super().display()
        print(f"Department: {self.department}")

def main():
    employees=[]

    while True:
        print("Choose an operation: ")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Compare Salaries")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice==1:
            name=input("Enter Name: ")
            age=int(input("Enter Age:"))
            print(f"Person created with name:{name} and age:{age}")

        elif choice==2:
            eid=int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            employees.append(Employee(eid, name, age, salary))
            print(f"Employee created with name: {name}, age:{age}, ID:{eid}, and salary: ${salary}")

        elif choice==3:
            name=(input("Enter name: "))
            age=int(input("Enter Age:"))
            eid=int(input("Enter Employee ID: "))
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")
            employees.append(Manager(eid, name, age, salary, department))
            print(f"Manager created with name: {name}, age:{age}, ID:{eid}, and salary: ${salary}, department:{department}")

        elif choice==4:
            while True:
                print("Choose details to show: ")
                print("1. Person")
                print("2. Employee")
                print("3. Manager")
                choice2 = int(input("Enter your choice for details: "))
                if choice2==1:
                    print("Person Details")
                    for emp in employees:
                        emp.display()
                elif choice2==2:
                    print("Employee Details")
                    for emp in employees:
                        emp.display()
                        print(f"Salary: ${emp.get_salary()}")
                        print(f"ID: {emp.get_id()}")
                        print(f"Name: {emp.name}, Age: {emp.age}")
                elif choice2==3:
                    pass
                else:
                    print("Invalid choice. Try again.")
                    break

        elif choice==5: 
            print("choose two employees to compare salaries.")
            eid1 = int(input("Enter Employee ID 1: "))
            eid2 = int(input("Enter Employee ID 2: "))
            for emp in employees:
                if emp.get_id() == eid1:
                    emp1 = emp
                elif emp.get_id() == eid2:
                    emp2 = emp

            if emp1 > emp2:
                print(f"Employee with ID {eid1} has higher salary than Employee with ID {eid2}")
            elif emp1 < emp2:
                print(f"Employee with ID {eid2} has higher salary than Employee with ID {eid1}")
            else:
                print(f"Employees with ID {eid1} and ID {eid2} have the same salary.")

        elif choice==6:
            print("Exiting the system. All resources have been freed.")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()