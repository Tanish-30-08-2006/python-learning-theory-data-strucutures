class Student:
    def study(self):
        print("Reading basic textbooks...")

class CSE_Student(Student):
    def study(self):
        print("Writing C code and checking memory leaks...")

class Art_Student(Student):
    def study(self):
        print("Sketching in the studio...")

# THE DEEP LOGIC: A single loop handling different memory layouts
students = [CSE_Student(), Art_Student(), Student()]

