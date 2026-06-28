class Student: 
    school_name  = "Global tech university"

    def __init__(self,name,marks): #init runs automatically

        self.name = name     #self.__dict__['name'] = name 
        self.marks = marks   #self.__dict__['marks'] = marks

s1 = Student("Alice", 85)
s2 = Student("Bob", 32)  #objects are created i.e instances of class

print(s1.school_name)



#--------------class and instance variables-------------
'''
