print("Welcome to the student Data organizer!")
print()

students = []
while True:
    print("Select an option:")
    print("1. Add Student\n2. Display All Students\n3. Update students Infomation\n4. Delete Student\n5. Display Subjects Offered\n6. Exit")

    choice=input("Enter your choice: ")   

    if choice=='1':
        print("Enter Student details:")
        sid=int(input("Student ID: "))
        name=input("Name: ")
        age=int(input("Age: "))
        Grade=input("Grade: ")
        dob=input("Date of Birth (YYYY-MM-DD): ")
        Sub= set(input("Enter subjects (comma-separated): ").split(","))


        student = {
            "ID": sid,
            "Name": name,
            "Age": age,
            "Grade": Grade,
            "Subjects": Sub,
            "DOB": dob
        }
        students.append(student)
        print("Student added successfully!")

    if choice=='2':
        if not students:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, "
                      f"Grade: {student['Grade']}, Subjects: {', '.join(student['Subjects'])}")

    if choice=='3':
        print("Update Students")
        sid=int(input("Student ID: "))
        age=int(input("Age: "))
        Sub=input("Subjects (comma-separated): ")
        print(Sub.split(", "))

    if choice=='4':
        print("delete Student ID: ")
        sid=int(input("Student ID:"))
        del(sid)
        print("Student deleted successfully!")

    if choice=='5':
        unique_subjects = set()
        for student in students:
            unique_subjects.update(student["Subjects"])
        print("Subjects Offered:", ", ".join(unique_subjects))

    if choice=='6':
        print("Thank you...")
        break

