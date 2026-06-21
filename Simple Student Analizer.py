import pandas as pd
import numpy as np

# To Get Students Grade
def Grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"



df = pd.read_csv("Students.csv", index_col = "ID")

Columns = [ "Math","Physics","Programming","Database"]

# Deleting irrelevant columns
df = df.drop(columns = ["Attendance"])
df = df.drop_duplicates()
df = df.dropna()

# Deleting invalid rows
invalid_rows = (df[Columns] > 100) | (df[Columns] < 0)
deleted_index = df[invalid_rows.any(axis = 1)].index
df = df.drop(index = deleted_index)

# Adding new columns
df["Average"] = df[Columns].mean(axis = 1)

status = df["Average"] >= 60
df["Status"] = status

grades = df["Average"].apply(Grade)
df["Grade"] = grades

# Get Ranking with numpy
average = df["Average"].to_list()
average = np.array(average)
position = np.argsort(average)[::-1]
rank = np.argsort(position)
df["Rank"] = rank + 1

# Best/Worst Students
best_5 = df.nlargest(5, "Average")
worst_5 = df.nsmallest(5, "Average")
best_1 = df.nlargest(1, "Average")
worst_1 = df.nsmallest(1, "Average")

subjects = df[Columns].mean().round(2).to_list()

# Grouping
grouped_grades = df.groupby("Grade")
grouped_status = df.groupby("Status")

# Filtering
A_Grade_Students = df[df["Average"] >= 90]
Failed_Students = df[df["Status"] == False]
Excellent_In_Programing = df[df["Programming"] >= 90]
Bad_At_Math = df[df["Math"] <= 50]






print("===================================================================================================")
print("Total Number Of Students: ", df.shape[0])
print("===================================================================================================")
print("Top Students\n-------------------------------------------------------------------------------------------")
print(best_1)
print("===================================================================================================")
print("Worst Students\n-------------------------------------------------------------------------------------------")
print(worst_1)
print("===================================================================================================")
print("Subjects average\n-------------------")
for i in range(len(subjects)):
    print(Columns[i] ,":", subjects[i])
print("===================================================================================================")
print("Grades Count\n------------------------------")
print(grouped_grades["Grade"].count())
print("===================================================================================================")
print("Status Count\n------------------------------")
print(grouped_status["Status"].count())
print("===================================================================================================")
print("Students with A Grade\n-------------------------------------------------------------------------------------------")
print(A_Grade_Students)
print("===================================================================================================")
print("Failed Students\n-------------------------------------------------------------------------------------------")
print(Failed_Students)
print("===================================================================================================")
print("Excellent Students in Programming\n-------------------------------------------------------------------------------------------")
print(Excellent_In_Programing)
print("===================================================================================================")
print("Students Bad At Math\n-------------------------------------------------------------------------------------------")
print(Bad_At_Math)
print("===================================================================================================")
print("Rank\n------------------------------")
print(df.sort_values(by = "Rank", ascending = True))
