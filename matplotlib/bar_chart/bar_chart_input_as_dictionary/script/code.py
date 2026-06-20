import matplotlib.pyplot as plt
import os

#function to break dictionary into two lists and plot a bar chart
def generate_bar_chart (dict , bar_chart_path):

    x_labels = list(dict.keys())
    y_labels = list(dict.values())
     
    # 1 --> set the figure size
    plt.figure(figsize=(5,5))

    # 2 --> plot the graph with no title and titles initially 
    plt.bar(x_labels, y_labels ,color ="skyblue",edgecolor = "salmon",alpha = 0.3)

    # 3 --> now title graph , x , y axis
    plt.xlabel("Programming language", fontsize = 10)
    plt.ylabel("Popularity " , fontsize = 10)
    plt.title("Programming language popularity", fontsize =12)

    #now add grid
    plt.grid(axis='y' , alpha = 0.5)


    #save the graph first then show it 
    plt.savefig(bar_chart_path)

    #now show the graph
    plt.show()

    #close the image as multiple runs would overwrite the graph
    plt.close()




#first read the sample_data_.txt

base_dir = os.path.dirname(__file__)
sample_data_path = os.path.join(base_dir, "..", "data","sample_data_.txt")
bar_chart_path = os.path.join(base_dir, "..", "data", "sample_data_bar_chart.png")

lines=[]
sample_dict = {} #dict is a reserved keyword , dict = {} is wrong 
if os.path.exists(sample_data_path):
    with open(sample_data_path,"r") as sdp:
       lines = sdp.readlines() #breaks every line into a string untill \n comes 
else:
    print("NO SAMPLE DATA FOUND")

for currline in lines:
    parts = currline.split() #breaks again a string into two strings...
    key = parts[0]        #key is a string 
    value = int(parts[1]) #value is a integer (eg python 45)
    sample_dict[key] = value

generate_bar_chart(sample_dict,bar_chart_path)
