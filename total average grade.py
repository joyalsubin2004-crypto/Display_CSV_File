import pandas as pd

data=pd.read_csv("student.csv")

data["total"] = data["mark1"]+data["mark2"]+data["mark3"]

data["average"] = data["total"]/3

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

data["grade"]=data["average"].apply(assign_grade)
print(data)

top_student=data.loc[data["average"].idxmax()]
print(top_student)

