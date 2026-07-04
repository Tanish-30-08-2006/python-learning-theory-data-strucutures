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

for s in students:
    # Python doesn't care what 'type' s is. 
    # It just follows the MRO for EACH object to find the 'study' method.
    s.study()
