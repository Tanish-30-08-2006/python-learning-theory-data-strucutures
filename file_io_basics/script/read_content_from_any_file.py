
import os

base_dir=os.path.dirname(__file__)

filename=input("Enter the filename from python->file_IO->data (example : file1.txt )  ")

file_path=os.path.join(base_dir,"..","data",filename)

if os.path.exists(file_path):
    with open(file_path,"r") as f:
        data =f.read()
        print(f"\nFILE [ {filename} ] CONTENT: \n{data}")
else:
    print("FILE NOT FOUND")


