
import os

base_dir=os.path.dirname(__file__)

filename=input("Enter the filename from python->file_IO->data (example : file1.txt )  ")

file_path=os.path.join(base_dir,"..","data",filename)

