import matplotlib.pyplot as plt 
import os

base_dir = os.path.dirname(__file__)
chart_image_path = os.path.join(base_dir,"..","data","grade_distribution_chart_image.png")  

x=["AA", "AB", "BB", "BC" ,"CC" ,"CD" , "DD"]
y=[2,5,7,6,5,4,1]



plt.figure(figsize=(4,4))
plt.bar(x,y, color= "green", edgecolor = "navy" , alpha=1) 


plt.title("class perfomance analysis",fontsize=14)
plt.xlabel("Grade Level" , fontsize=12)
plt.ylabel("Number of Students" , fontsize=12)
plt.grid(axis='y' , alpha = 0.3)

plt.savefig(chart_image_path)
plt.show()
plt.close()





