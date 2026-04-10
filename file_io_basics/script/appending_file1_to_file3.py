import os

#FETCH DATA FROM FILE1 (SOURCE)
source="file1.txt"
base_dir=os.path.dirname(__file__)
file_path=os.path.join(base_dir,"..","data",source)

if os.path.exists(file_path):
    with open(file_path,"r") as f:
        data=f.readlines() #list of strings from file1.txt


#MOVE TOWARDS DESTINATION
destination="file3.txt"
file_path=os.path.join(base_dir,"..","data",destination)

if os.path.exists(file_path):
    with open(file_path,"a") as f:
        f.writelines(data)


###-----------FILE3--------
# Name: Tanish
# College: DAIICT
# Branch: B.Tech IT
# Year: 1
# City: Ahmedabad
# Hobby: Coding
# Favorite Language: Python
# Age: 18
# Semester: 2
# Favorite Subject: Programming
# Skills: C++, Python
# Goal: Software Engineer
# Favorite Sport: Cricket
# Email: tanish@example.com
# Phone: 9999999999
# Country: India
# Status: Learning Python File IO


##------------FILE1----------
# Age: 18
# Semester: 2
# Favorite Subject: Programming
# Skills: C++, Python
# Goal: Software Engineer
# Favorite Sport: Cricket
# Email: tanish@example.com
# Phone: 9999999999
# Country: India
# Status: Learning Python File IO
