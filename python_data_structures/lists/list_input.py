list=[] #tuple.append doesnt work as tuples are imutant..
size=int (input("enter size of list: "))
for i in range(0,size,1):
    list.append(input(f"enter {i+1}nth element : "))
    
print(list)

list_marks=[]
size1=int(input("enter no of students : "))
for i in range(0,size1,1):
    list_marks.append(input(f"enter student {i+1} marks : "))


print(list_marks)
list_marks.sort()
print(list_marks)



