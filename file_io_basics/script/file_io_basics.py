'''''''''''''''''
all temp data in code(variables , function names arrays lists tuples) are stored in random access memory .(ram)
all the data in ram is volatile(temp) once the code is over it exits all the data is lost 
to persist the data we use files , persist meaning save the data we use txt files or file i/o to save the data

why we use ram (then) , we can use sdd or hdd i.e physical memory actual but its too slow we need execution of our program to be fast 

'''''''''''''''
###DONT RUN ANY CODE AS FILE PATHS WERE CHANGED............................

#reading a file in python
f=open("file1.txt","r") #opening a file 
data=f.read() #read its contents..
print(data) #--> reads one full line at a time 
f.close()

#writing to a file 
str="writing into a file\n"
f=open("file2.txt","w") #ERASES THE OLD CONTENT AND REWRITES IT EVERY TIME I RUN THIS FILE IS 
f.write(str)            #CLEARED AND WRITTEN AGAIN
f.close() 

f=open("file2.txt","a")
f.write(str)
f.close()

