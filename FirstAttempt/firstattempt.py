#my first attempt at outputing multiple plots in one go
#Author Enda Lynch

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

irisCsv = pd.read_csv('IrisdataCSV.csv')

plt.figure(figsize = (10,7))
sepLenHis = irisCsv['petal length in cm']
plt.hist(sepLenHis, bins = 20, color = 'red')
plt.title("Petal Length in cm") 
plt.xlabel("Petal_Length_cm") 
plt.ylabel("Count")

plt.savefig('Petal Length Hist.png')

plt.figure(figsize = (10,7))
sepLenHis = irisCsv['petal width in cm']
plt.hist(sepLenHis, bins = 20, color = 'red')
plt.title("Petal Width in cm") 
plt.xlabel("Petal_Width_cm") 
plt.ylabel("Count")

plt.savefig('Petal Width Hist.png')

plt.figure(figsize = (10,7))
sepLenHis = irisCsv['sepal length in cm']
plt.hist(sepLenHis, bins = 20, color = 'green')
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count")

plt.savefig('Sepal Length Hist.png')

plt.figure(figsize = (10,7))
sepLenHis = irisCsv['sepal width in cm']
plt.hist(sepLenHis, bins = 20, color = 'green')
plt.title("Sepal Width in cm") 
plt.xlabel("Sepal_Width_cm") 
plt.ylabel("Count")

plt.savefig('Sepal Width Hist.png')

classCount = irisCsv['species'].value_counts()

for n in range (0, 150):
    if irisCsv['species'][n] == 'Iris-setosa':
        plt.scatter(irisCsv['petal length in cm'][n], irisCsv['petal width in cm'][n], color = 'red')
        plt.xlabel('Petal Length CM')
        plt.ylabel('Petal Width CM')
    elif irisCsv['species'][n] == 'Iris-virginica':
        plt.scatter(irisCsv['petal length in cm'][n], irisCsv['petal width in cm'][n], color = 'green')
    else:
        plt.scatter(irisCsv['petal length in cm'][n], irisCsv['petal width in cm'][n], color = 'blue')
plt.legend()
plt.savefig('ScatterPlot - Petal Length and Width.png')

for n in range (0, 150):
    if irisCsv['species'][n] == 'Iris-setosa':
        plt.scatter(irisCsv['sepal length in cm'][n], irisCsv['sepal width in cm'][n], color = 'red')
        plt.xlabel('Sepal Lenghth CM')
        plt.ylabel('Serpal Width CM')
    elif irisCsv['species'][n] == 'Iris-virginica':
        plt.scatter(irisCsv['sepal length in cm'][n], irisCsv['sepal width in cm'][n], color = 'green')
    else:
        plt.scatter(irisCsv['sepal length in cm'][n], irisCsv['sepal width in cm'][n], color = 'blue')
plt.legend()
plt.savefig('ScatterPlot - Sepal Length and Width.png')

