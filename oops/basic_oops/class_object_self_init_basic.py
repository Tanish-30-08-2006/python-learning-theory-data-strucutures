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
