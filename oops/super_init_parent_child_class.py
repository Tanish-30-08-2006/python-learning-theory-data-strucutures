#PARENT CLASS

class student:

    def __init__(self,name,marks):

        self.name = name
        self.marks = marks #dictionary initialised in address which s1 is pointing i.e self.__dict__['marks'] = marks
        print(f"parent init calld by super() for :{self.name}")

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
    

#CHILD CLASS(derived class)
class scholarshipstudent(student):
