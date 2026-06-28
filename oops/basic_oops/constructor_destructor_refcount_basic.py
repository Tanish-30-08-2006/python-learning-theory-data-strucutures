# ----------DIFFERENCE BETWEEN MALLOC AND FREE AND REFERENCE COUNT -------------
'''

In a lower-level language like C, if you malloc() memory and forget to free() it, you get a memory leak.
Python automates this using a "Reference Counter."

WHAT IS REFERENCE COUNT 

counter tracks how many variables are currently poiniting towards this address 

'''

import sys

class student:
    def __init__(self,name):
        print("constructor is called")
        self.name =name
    
    def __del__(self):
        print("destructor is called , ref count =0")
        print(f"--- {self.name}'s memory address is being WIPED! ---")
    


# create an object(instance of class)
s1 =student("alice") 
# init is automatically called so student.init(s1,name) is called if function with same attributes self , name is there
# then self.name = name is executed so s1 is a address of containng attributes ...

print(f"References to Alice: {sys.getrefcount(s1)-1}")
# s1 has memory address of attributes of s1 
# Note: getrefcount is always +1 because the function itself 'refers' to it momentarily.

#Create another pointer to the same address
s2 = s1
print(f"References to Alice after s2 = s1: {sys.getrefcount(s1) - 1}")
# now s2 also points to same memory address that contains dictionary with self.__dict__['name'] = "alice"
