# CLASS  IS A BLUEPRINT 
# OBJECT IS AN INSTANCE OF CLASS....

# you want to build 100 cars we design a blueprint of a car and then 100 cars are stamped out of it
# when we write class student we create our own custom datatype

class student:

    def __init__(self, name , marks ):
        self.name = name
        self.marks = marks 
        print(f"object student {self} has been created successfully")

    def check_pass_fail(self):
        if self.marks >= 40 :
            line = f"{self.name} has passed"
            print(self)
            return line
        else:
            line = f"{self.name} has failed"
            print(self)
            return line 

s1 = student("alice" , 80)
s2 = student("bob" ,30)

print(s1.check_pass_fail())
print(s2.check_pass_fail())

#if we create an object for student def __init__ runs automatically when new student is created 


'''
what is self :this is placeholder it stores the students name and marks for every student
(address of storage of attributes) for that student 
self says, "Whichever specific student is being created right now, give them this name.
self is essentially a pointer. When you create s1, Python allocates a chunk of memory to store Alice's data

# def pass fail is a method it a function inside a class   
'''
 


#------------attributes vs methods---------------------------
''' 
ATTRIBUTES VS METHODS 
attributes are parametres a student(object) HAS like self.name self.marks are attributes
methods are functions for things student DOES like gives exam pass or fails an exam etc 
'''


#--------actual logic of self-----------------------------
'''
when we call s1.checkpassorfail() , python tranforms the code it into student.checkpassorfail(s1) so object s1(address)
was passed as the arguement and def checkpassorfail(self) and that address here is named as self 
now inside the function when we call self.marks python goes into the address of self i.e address of s1 and accessses offset marks 

first python checks if any attribute s1.__dict__['checkpassorfail'] exists if not 
