a="harry"
print(type(a))

b=1
print(type(b))

c="56" #inside double quotes is always a string 
print(type(c))

# c as 56 but type should be int not string
c=int(c) #typecasting
print(type(c))


#Input
a=input("enter number 1")
b=input("enter number 2")#every Input without typecast is taken as string
print(f"sum is  {a+b}")


#converting to int 
a=int(input("enter number 1"))
b=int (input("enter number 2"))#every Input without typecast is taken as string
print(f"sum is {a+b}")#taking input by f string method


d=input("enter your name: ")
print(f"good morning {d} ")















