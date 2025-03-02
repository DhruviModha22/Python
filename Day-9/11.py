# Develop a program that allows users to pass any combination of attributes for an employee (e.g., name, department, salary) using **kwargs.
#     - check if any required fields are missing and print a message accordingly.

def create_employee(**kwargs):
    required_fields = ['name', 'department', 'salary']
    missing_fields = [field for field in required_fields if field not in kwargs]
    
    if missing_fields:
        print(f"Missing required fields: {', '.join(missing_fields)}")
    else:
        print("Employee created successfully:", kwargs)

# Test the function

create_employee(name="Dhruvi", department="HR", salary=50000)
create_employee(name="Vansh", salary=60000)
create_employee(department="IT", salary=70000)

