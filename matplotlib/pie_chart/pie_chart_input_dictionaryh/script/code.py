import matplotlib.pyplot as plt
import os




base_dir = os.path.dirname(__file__)
sample_data_path = os.path.join(base_dir, ".." ,"data","sample_data.txt")
practice_pie_chart_path = os.path.join(base_dir, "..","data","practice_pie_chart.png")

lines =[]
prog_dict ={}

def generate_pie_chart(prog_dict , practice_pie_chart_path):

    keys_or_labels = list(prog_dict.keys())
    values = list(prog_dict.values())

    plt.figure(figsize=(7,7))
    

    #DIFFERENT WAYS TO PLOT PIE GRAPH........

    #plt.pie(values , labels = keys_or_labels )

    #plt.pie( values , labels= keys_or_labels ,startangle=90,colors=['darkred', 'darkblue', 'darkgreen', 'darkorange', 'salmon']) 
    # start angle 
    #DegreesClock Position
    # 0 °  3 o'clock (Default)
    # 90° 12 o'clock
    # 180° 9 o'clock
    # 270° 6 o'clock


    #plt.pie(values, labels= keys_or_labels , autopct='%1.2f%%',startangle=90)
    # 'autopct' uses a special string format: '%1.3f%%'
    # This means: 1 digit before decimal, 1 digit after, and show the % sign.
    
    # set_explode = [0.1, 0.1, 0.1, 0.1, 0.1]
    # plt.pie(values , labels= keys_or_labels ,autopct='%1.1f%%',explode= set_explode ,startangle=90,shadow=True)
    #You pass a list of numbers. 0 means the slice stays in the pie, and a small decimal like 0.1 means it pops out.
    #shadow=True: This adds a 3D drop-shadow effect to the pie chart.

    plt.title("Programming language popularity",fontsize=13)

    plt.savefig(practice_pie_chart_path)
    plt.show()
    plt.close()

with open(sample_data_path,"r") as sdp:
    lines = sdp.readlines()

for currline in lines:
    
    parts = currline.split()
    if len(parts)==2:
        key = parts[0]
        value = int(parts[1])
        prog_dict[key] =value
    
     
generate_pie_chart(prog_dict,practice_pie_chart_path)
