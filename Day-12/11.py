class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def calculate_average(self):
        return sum(self.__marks) / len(self.__marks)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

s = Student("Alice", [85, 90, 88])
print("Average:", s.calculate_average())
print("Grade:", s.calculate_grade())
