n=int(input("enter number : "))
last=int(input("enter last table index: "))
for i in range(1,last+1,1):
    print(f"{n} X {i}= {n*i}")
i=1
while(i<=last):
    print(f"{n} X {i}= {n*i}")
    i=i+1

