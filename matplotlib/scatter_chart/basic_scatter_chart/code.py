import matplotlib.pyplot as plt

# 1. INITIALIZE DATA (No external files needed)
# Each index represents one student
# Student 1: 2 hours study -> 45 marks, etc.
study_hours = [2, 3, 5, 1, 8, 7, 10, 4, 6, 9, 2, 8]
exam_scores = [45, 50, 65, 35, 88, 72, 95, 55, 70, 92, 80, 40] 

# Note: The last student (8 hours, 40 marks) is our "Outlier" 
# They studied a lot but likely had a bad day!

def generate_practice_scatter():
    plt.figure(figsize=(10, 6))

    # 2. CREATE THE SCATTER PLOT
    # s=100 sets the size of the dots
    # alpha=0.6 makes them slightly transparent (good for overlapping dots)
    # edgecolor adds a nice ring around the dot
    
    plt.scatter(study_hours , exam_scores ,color= 'royalblue', s=100,alpha =0.6,edgecolors='black')

