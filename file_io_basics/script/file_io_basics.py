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

f=open("file2.txt","a") 
f.write(str)           
f.close() 

#output:
# writing into a file
# writing into a file
# writing into a file


#when we do fopen and fwrite it sewrches for file in that directory here current diretory id daiict so
# METHOD 1 : cd TanishVSCODE\python\file_IO python file_io_basics.py [GO TO THAT FILE WHERE FILE1 EXISTS
#            as by default curretn directory is daiict..
# METHOD 2: import os 
f=open("file2.txt","a")
f.write("writing is over now \ni have written it 3 times ...")
f.close()

f=open("file2.txt","r")
data=f.read()
print(data)




