#Histogram for Petal Length
#credit: https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('IrisdataCSV.csv')

plt.figure(figsize = (10,7))
sepLenHis = data['petal length in cm']
plt.hist(sepLenHis, bins = 20, color = 'red')
plt.title("Petal Length in cm") 
plt.xlabel("Petal_Length_cm") 
plt.ylabel("Count")

plt.savefig('Petal Length Hist.png')
#plt.show()