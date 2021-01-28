class Student:
    def __init__(self, name, major, gpa, studentId, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.studentId = studentId
        self.iis_on_probation = is_on_probation


def test_class_objs():
    name = input("Enter Student name:")
    major = input("Enter student major:")
    Student1 = Student("Jim", "Bussiness", 3.2, "s9011", False)
    print(Student1.name)
