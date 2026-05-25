#Student Lifestyle & Performance Analysis System

import pandas as pd
data = pd.read_csv("students.csv")
print(data.head())
print("AVERAGE MARKS: ",data["MARKS"].mean())
print("HIGHEST MARKS: ",data["MARKS"].max())
print("LOWEST MARKS: ",data["MARKS"].min())

import matplotlib.pyplot as plt
#scatter plot shows relationshp bw study hours-x and marks-y
plt.scatter(data["STUDY_HOURS"],data["MARKS"])
plt.xlabel("STUDY HOURS")
plt.ylabel("MARKS")
plt.title("STUDY HOURS VS MARKS")
plt.show()

average_marks=data["MARKS"].mean()
if average_marks>=75:
    print("OVERALL STUDENT PERFORMANCE IS EXCELLENT")
elif average_marks>=50:
    print("OVERALL STUDENT PERFORMANCE IS AVERAGE")
else:
    print("OVERALL STUDENT PERFORMANCE NEEDS IMPROVEMENT")
          
high_study=data[data["STUDY_HOURS"]>5]
print("\n STUDENTS STUDYING MORE THAN 5 HOURS:")
print(high_study[["NAME", "MARKS"]])

          
#bar graph comparision analysis of student marks  plt.bar(x,y)
plt.figure(figsize=(8, 5))
plt.bar(data["NAME"],data["MARKS"])
plt.xlabel("STUDENTS")
plt.ylabel("MARKS")
plt.title("STUDENT MARKS COMPARISION")
plt.show()
