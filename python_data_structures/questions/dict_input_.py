subj=int(input(print("enter no of subjects: ")))

student={}#empty dictionary
for i in range(0,subj,1):
    subject, marks= input("enter subject name and marks separated by space:  ").split()
    student[subject] =int(marks)

print(student)
