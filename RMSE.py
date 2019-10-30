# -*- coding: utf-8 -*-
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt

List_of_rmse = []
def rmse(predictions, targets):

    differences = predictions - targets                       #the DIFFERENCEs.

    differences_squared = differences ** 2                    #the SQUAREs of ^

    mean_of_differences_squared = differences_squared.mean()  #the MEAN of ^

    rmse_val = np.sqrt(mean_of_differences_squared)           #ROOT of ^

    return rmse_val

def writing_csv(file_path, NAME,AGE, GPA,MAJOR):
    fieldnames = ['name','age', 'gpa', ',major']

    with open(file_path, "a",newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,)
        # writer.writeheader("NAME","Age","GPA","MAJOR")
        writer.writerow({
			"name": NAME,
			"age": AGE,
            "gpa": GPA,
			"major": MAJOR,
})

for i in range(9): #task 1 and 2
    print("New Student")
    NAME  = input("Please input your name: ")
    AGE   = input("Please input your age: ")
    GPA   = input("Please input your GPA out of 4: ")
    MAJOR = input("Please input your MAJOR : ")
    printing_statement = "My name starts with the letter: {} and I am  years old {}. I study {} and my GPA is: ({}).".format(NAME[0],AGE,GPA,MAJOR)
    writing_csv("students.csv",str(NAME),AGE,GPA,(MAJOR)) #task 3

#task 4
data = pd.read_csv('students.csv',names=["NAME", "AGE", "GPA", "MAJOR"])
print(data)
sns.set(style='whitegrid')
ax = sns.barplot(x=data['MAJOR'].value_counts().index, y=data['MAJOR'].value_counts().values, palette='Blues_d')
plt.legend(loc=8)
plt.xlabel("MAJOR")
plt.ylabel('Frequency')
plt.title('shw of Major bar plot')
plt.savefig("Major.png")
# plt.show()

labels = data["AGE"].value_counts().index
values = data["AGE"].value_counts().values
# colors = ["red","blue","green","yellow","brown"]
explode = [0,0,0.1,0,0]

plt.figure(figsize=(7,7))
plt.pie(values, labels=labels,  explode=explode, autopct="%1.1f%%")
plt.title("AGE analysis")
plt.savefig("Age.png")
# plt.show()


sns.kdeplot(data["GPA"])
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("GPA score kde plot")
plt.savefig("GPA.png")
# plt.show()

sns.pairplot(data)
plt.savefig("pairplot.png")
# plt.show()


sns.set(style='whitegrid')
ax = sns.barplot(x=data['NAME'], y=data['AGE'], palette='Blues_d')
plt.legend(loc=8)
plt.xlabel("MAJOR")
plt.ylabel('Frequency')
plt.title('shw of Major bar plot')
plt.savefig("name.png")
# plt.show()


#task 5,6,7
for i in data["GPA"]:
    rmse_ret = rmse(data['GPA'],i)
    # rmse_ret = sqrt(mean_squared_error(10,predicted_value, i)) #attempting fail
    List_of_rmse.append(rmse_ret)

data['RMSE'] = List_of_rmse
print(data)

#task 8
data.to_csv('students.csv',index=False)

