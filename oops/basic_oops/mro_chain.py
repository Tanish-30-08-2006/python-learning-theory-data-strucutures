class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Parent Init usedc! without even calling by mro chain link")

    def display(self):
        print(self.name,self.marks)

class GradStudent(Student):
    pass # This means 'do nothing/empty'

# This WORKS because Python finds __init__ in the Parent
