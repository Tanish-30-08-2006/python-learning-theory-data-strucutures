class Student: 
    school_name  = "Global tech university"

    def __init__(self,name,marks): #init runs automatically

        self.name = name     #self.__dict__['name'] = name 
        self.marks = marks   #self.__dict__['marks'] = marks

