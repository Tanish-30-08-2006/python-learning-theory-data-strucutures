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



print(" Deleting s1")
del s1
print(f"References to Alice after deleting s1: {sys.getrefcount(s2) - 1}")

# here memory address of s1 which contained dictionary self.__dict__['name']="alice" is still alive as s2 points to it
# so destructor checks ref count of that address every time we call s1,use s1,del s1 ...or every student poinitng to alice it checks 
# the the ref count of alice when we did del s1 it checks the ref count of self i.e where alice was stored
# still ref count will be 1 so no destructor called

print("deleting s2")
del s2
# here destructor is called ref count is 0 as no student pointer or variable s1 or s2 or s3 pointing to alice no destructor is called


#----------------deleting objects (del s1)----------------------#

