# This is the code to research the data set and code (in Python [1]) to investigate it.
# Author:Enda Lynch

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

irisCsv = pd.read_csv('irisdataCSV.csv')

classCount = irisCsv['species'].value_counts()

for n in range (0, 150):
    if irisCsv['species'][n] == 'Iris-setosa':
        plt.scatter(irisCsv['petal length in cm'][n], irisCsv['petal width in cm'][n], color = 'red')
        plt.xlabel('Petal Lenghth CM')
        plt.ylabel('Petal Width CM')
    elif irisCsv['species'][n] == 'Iris-virginica':
        plt.scatter(irisCsv['petal length in cm'][n], irisCsv['petal width in cm'][n], color = 'green')
    else:
        plt.scatter(irisCsv['petal length in cm'][n], irisCsv['petal width in cm'][n], color = 'blue')
plt.legend()
plt.savefig('ScatterPlot - Sepal Length and Width.png')
plt.show()