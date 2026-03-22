name ="tanish sanghavi"

nameshort=name[0:5]
print(nameshort)
nameshort=name[0:10]
print(nameshort) 
print(name[1]) 

print(name[0:])# 0: means 0 to size -1
print(name[1:])
print("negative slicing")

'''
negative slicing=start from end with index -1;
print[name[-4:-1]]
 0  1  2  3  4 = h a r r y
-5 -4 -3 -2 -1 = h a r r y
'''
name ='harry'

print(name[-4:-1])
print(name[1:4])

#skipping indices[slicing]
a='123456789'
print(a[1:4:1])




