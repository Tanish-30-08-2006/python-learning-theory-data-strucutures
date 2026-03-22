str=input("enter your comment: ")
str1="tanish is is a very very daiict daiict "
print("is" in str1)
print("Tanish" in str1)# case sensitive so false

str1.replace("is","")#NOT POSSIBLE AS STR1 IS IMMUTANT
str2=str1.replace("is","")#strings are immutant , you cant append remove add replace any element in string str.replace will create a new string 
print(str2)

lst=[]#empty list
size=int(input("enter no of names in list :"))
lst=input("enter name separated by space : ").split()#-------->map is ued only to convert strings(lists of numbers) to integers if direct strings are input no need to use map
#for input list via map-----> lst=input("enter name separated by space : ").split()
if("tanish" in lst):
    print("present")
else:
    print("not present")
    
