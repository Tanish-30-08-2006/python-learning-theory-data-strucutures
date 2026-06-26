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
