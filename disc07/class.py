class Student:
    students = 0  # this is a class attribute

    def __init__(self, name, staff):
        self.name = name  # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


callahan = Professor("Callahan")
elle = Student("Elle", callahan)
elle.visit_office_hours(callahan)
elle.visit_office_hours(Professor("Paulette"))
elle.understanding
[name for name in callahan.students]
x = Student("Vivian", Professor("Stromwell")).name
x
[name for name in callahan.students]
