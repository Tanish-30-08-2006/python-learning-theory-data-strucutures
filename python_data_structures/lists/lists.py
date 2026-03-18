#str="tanish"
#cant change str[2]=k
# str[2]="k" str will remain "tanish" cant change an
#  all str functions will create a new string

list=[1,4,False,"tanish", "sanghavi",54.5]

for i in list:
    print(type(i))

for ch in "HELLO": 
    print(ch)

#lists are mutable
list[2]=True
for i in list: 
    print(i)

for i in range(2,10,3):
    print(i)    



