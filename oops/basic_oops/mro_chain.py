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
s1 = GradStudent("Bob", 80)

#python finds we havent used any method like s1.getgrade or something so it means we are calling init as method 
#---------1
# so here we havent called any method so it just means init is called so python searches '__init__' in s1 but currently s1 has 
# no attributes not even ['name'] and ['marks'] ,in instances dictionary there are never methods ..

#----------2
# so we move to next link in method resolution order chain(mro chain)
# type of s1 is gradstudent
# class of s1 is gradstudent so gradstudent.__dict__['__init__'] is searched : result : FAIL

#----------3
# type of gradstudent now i.e parent class is student so we search student.__dict__['init'] : result : PASS
# execute it like student.__init__(s1,"bob",80)  



s1.display() 

#----------1
# searches in s1.__dict__['display'] FAIL
# searches in type(s1) i.e class gradstudents.__dict__['display'] FAIL
# searchesn in type (gradstudent) i.e class student so student.__dict__['display'] PASS
# if not even in parent class it is searched in root class object as in python everything is an object


#-------------------MRO PATH----------------
print(GradStudent.mro())

# OUTPUT: [<class '__main__.GradStudent'>, <class '__main__.Student'>, <class 'object'>]

# WHY object is at last what does it mean ?

# In Python, everything is an object—integers, strings, functions, and even the classes you create.
# Because of this, Python needs a "Master Blueprint" 
# that provides the basic functionality every single thing in the language must have.

# What you write:
