#cant change an element of tuple as immutable
#a[0]=5 will give error
a=(1,2,3,4,5,6,7,8,9)
# for i in a:
#     print(i)

for i in range(0,len(a),2):
    print(a[i])
print("tuple functions now")
#basic functions
print(a.count(4))
print(a.index(1))#index of first occurance of element
#in string name.find(element) and tuples name.index(element)


#finding element in tuple
print(f" is 2 there {2 in a}")
print(f" is 100 there {100 in a}")
print(f" is 3 there {3 in a}")

#concanted tuple
tuple1=(1,2,3)
tuple2=(1,2,3)
concanted_tuple = tuple1 + tuple2
for i in range(0,len(concanted_tuple)):
    print(concanted_tuple[i])
print(concanted_tuple)

#unpacking tuple 
tuple3=(4,7,9)
a,b,c= tuple3
print(f"{a} {b} {c}")

#slicing tuple
sliced= tuple3[1:3]
print(sliced)









