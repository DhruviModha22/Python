# Implement a function that takes a list od student names using *args and prints each name on a new line.
#    -Add functionality to check if the list is empty and display a suitable message.

def print_student_names(*names):
    if not names:
        print("The list is empty.")
    else:
        for name in names:
            print(name)
    
# Test the function
print_student_names("Dhruvi", "Vansh")
print_student_names()