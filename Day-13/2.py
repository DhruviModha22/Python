class Teacher:
    def teach(self):
        print("Teaching students")

class Administrator:
    def manage(self):
        print("Managing school administration")

class Headmaster(Teacher, Administrator):
    def lead(self):
        print("Leading the school")

h = Headmaster()
h.teach()
h.manage()
h.lead()
