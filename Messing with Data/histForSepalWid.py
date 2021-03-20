#Histogram for Sepal Width
#credit: https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('IrisdataCSV.csv')

plt.figure(figsize = (10,7))
sepLenHis = data['sepal width in cm']
plt.hist(sepLenHis, bins = 20, color = 'green')
plt.title("Sepal Width in cm") 
plt.xlabel("Sepal_Width_cm") 
plt.ylabel("Count")

plt.savefig('Sepal Width Hist.png')
#plt.show()