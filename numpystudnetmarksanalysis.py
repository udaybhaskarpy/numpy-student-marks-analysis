import numpy as np

print("    ---STUDENT REPORT---   ")

marks = np.array([
    [78, 85, 90],   # Student 1
    [92, 88, 95],   # Student 2
    [65, 70, 72],   # Student 3
    [88, 90, 84],   # Student 4
])
Student_average=np.round(marks.mean(axis=1),2)

for i in range(len(marks)):
    print("Marks for student ",i+1,":",marks[i])
print()

for i in range(len(Student_average)):
    print("Average marks in all subjects ","(",i+1,")",Student_average[i])

print()

Subject_average=np.round(marks.mean(axis=0),2)
Subjects=["Maths","Science","English"]
for i in range(len(Subject_average)):
    print("Average marks of students in",Subjects[i],":",Subject_average[i])
    print()

Total_marks_of_students=marks.sum(axis=1)
Highest_marks=Total_marks_of_students.max()
    
    
for i in range(len(Total_marks_of_students)):
    print("Total marks of student ",i+1,":",Total_marks_of_students[i])
print("Highest marks :",Highest_marks )
    

print("Marks greater than 85 :",marks[marks>85])
