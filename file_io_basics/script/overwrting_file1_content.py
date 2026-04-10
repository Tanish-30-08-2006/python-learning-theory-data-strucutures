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
