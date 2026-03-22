size = int(input("enter no of elements: "))
z=0
lst=[]
for i in range(0,size,1):
   lst.append(int(input(f"enter element {i+1}")))

max1=float('-inf')
for i in range(0,size,1):
   if lst[i]>max1 :
      max1=lst[i]

print(max) 
print(max(lst))

