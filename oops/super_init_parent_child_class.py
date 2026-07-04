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
    
    def __init__(self , name , marks , stipend):
        #here we must initialize parent(__init__) first then we initialise child i.e run childs init function
        super().__init__(name , marks)
        self.stipend = stipend
        print(f"Child Init called for {self.name} with stipend {self.stipend}")
    
    def show_stipend(self):
        print("calling method i.e a function from child which is not init")
        print(f"stipend amount : {self.stipend}")

s1 = scholarshipstudent("alice",95,1000)
s1.display()      # Calling method from Parent
s1.show_stipend() # Calling method from Child

#-------------problem--------------------
