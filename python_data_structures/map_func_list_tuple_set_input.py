#map(function,iterable)

x= map(int , "1 2".split()) #int -> function and convets strings to integer  #.split() --> "1,"2" splits them to "1" and "2" and int converts them to integer
print(type(x)) # --->   <class map>
#MAP WILL NOT RETURN A FINAL LIST CONVERTED TO INTEGER ITS JUST AN OBJECT (MACHINE JUST LIKE A CONVERTER)

#to see the result store it in a list or tuple to see the results (map is object which just does conversion
list1=list(x)
print(list1)
print(list1[0])

#map converts input to integer but cant assign it to vaiable 
#it can assign to tuples list or sets as series of numbers..
#USE MAP WHEN MULTIPLE INPUTS IN A SINGLE LINE 

# size=map(int , input("enter size of list: "))
# print(size) #map object must be converted to list or tuple..

print("\nlist and tuple as an input with map without map \n")

#-----> LIST INPUT ---------------

#WITHOUT MAP
list1=[]
size = int(input("enter size: "))
for i in range(0,size,1):
    list1.append(int(input(f"enter element {i+1}")))
print(list1)
 
list1.clear()
#WITH MAP
x=map(int,input("enter elements separated by space" ).split() )
print(x) #list 1 is a map object #list1 has converted data only
list2=list(x) #list(x) ----> converts x into list
print(list2)

x=list(map(int,input("enter elements separated by space" ).split() ))
print(x)

#---------TUPLE INPUT --------------#
#tuple are immutant and indexed and ordered...
#cant add elements in tuple as size of initialized tuple is fix so convert list to tuple

#without map
t=()
lst=[]
size=int(input("enter size of tuple : "))
for i in range(0,size,1):
    lst.append(input(f"enter element {i+1}"))

t=tuple(lst) #t=tuple(x) converts x into a tuple(here x is list)
print(t)

#WITH MAP
# t.clear() t.append() t.remove functions will give attribute error
# to clear a tuple , INITIALIZE A TUPLE TO NULL (t=())

t=()   # t initialized to empty tuple again
t=tuple(map(int , input("enter elements separated with space for tuple with map: ").split()))
print(t)

#-------SET INPUT-----------#

#WITHOUT MAP
s=set()   #to initialise a tuple t=() to iniliase a set s=set()
size=int(input("enter size of set"))

for i in range(0,size,1):
    s.add(input(f" enter element {i+1}"))
print(s)

#WITH MAP
s=set(map(int,input(f"enter element separated by space for a set with map").split()))
print(s)


