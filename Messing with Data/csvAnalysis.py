# This is the code to research the data set and code (in Python [1]) to investigate it.
# Author:Enda Lynch

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

irisCsv = pd.read_csv('irisdataCSV.csv')

classCount = irisCsv['class'].value_counts()

for n in range (0, 150):
    if irisCsv['class'][n] == 'Iris-setosa':
        plt.scatter(irisCsv['sepal length in cm'][n], irisCsv['sepal width in cm'][n], color = 'red')
        plt.xlabel('Sepal Lenghth CM')
        plt.ylabel('Serpal Width CM')
    elif irisCsv['class'][n] == 'Iris-virginica':
        plt.scatter(irisCsv['sepal length in cm'][n], irisCsv['sepal width in cm'][n], color = 'green')
    else:
        plt.scatter(irisCsv['sepal length in cm'][n], irisCsv['sepal width in cm'][n], color = 'blue')
plt.legend()
plt.savefig('ScatterPlot - Sepal Length and Width.png')
#plt.show()