# ---------- TAKING TUPLE INPUT USING map ----------
# input().split() takes space separated values as integers
#map(int ,"input string") converts each number entered into int
#tuple converts mapped values as input separated by space into a tuple

t=tuple(map(int,input("enter each number in a tuple separated by space: ").split()))

for i in range(0,len(t),1):
    print(t[i])
    
print(t)    

s = {8, 7, 12, "Harry", (1,2,3)}
print("accessing tuple inside set")
#set are unordered (hashed) and unindexd so cant index and access
for item in s: #cant for i in range() and s[i] as set are mutant unordered unindexed
    if isinstance(item,tuple):
       for i in range(0,len(item),1):
           print(item[i])
        

   


          