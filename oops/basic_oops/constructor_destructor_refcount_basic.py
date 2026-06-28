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
    
