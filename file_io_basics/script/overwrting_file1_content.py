import os
## OVERWRITE FILE1 CONTENT TO LINES(LIST)
base_dir =os.path.dirname(__file__)

file_path=os.path.join(base_dir,"..","data","file1.txt")

lines = [
    "Age: 18\n",
    "Semester: 2\n",
    "Favorite Subject: Programming\n",
    "Skills: C++, Python\n",
    "Goal: Software Engineer\n",
    "Favorite Sport: Cricket\n",
    "Email: tanish@example.com\n",
    "Phone: 9999999999\n",
    "Country: India\n",
    "Status: Learning Python File IO\n"
]

if os.path.exists(file_path):
    with open(file_path,"w") as f: #overwrites...
        f.writelines(lines) 
#f.write accepts only a single string and returns number of characters written 
#for list of strings or tuple we use f.writelines() which writes multiple string at once...
print("\nlines appended successfully")


