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
