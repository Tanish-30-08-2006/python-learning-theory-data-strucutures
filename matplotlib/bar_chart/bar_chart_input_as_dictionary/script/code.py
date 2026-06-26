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
