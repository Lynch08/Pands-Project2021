#heat maps - same maps as above but function will save to .png
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

irisCsv = pd.read_csv('IrisdataCSV.csv')
grouped = irisCsv.groupby('species')
#print (grouped.first())

irisCsv_set = grouped.get_group('Iris-setosa')
irisCsv_ver = grouped.get_group('Iris-versicolor')
irisCsv_vir = grouped.get_group('Iris-virginica')
#irisCsv.columns = ['sepal length', 'sepal width', 'petal length' , 'petal width', 'species']
#grouped = irisCsv.groupby('species')
fig, axes = plt.subplots(nrows= 2, ncols=2)
colors= ['blue', 'red', 'green']

for i, ax in enumerate(axes.flat):
    for label, color in zip(range(irisCsv.groupby), colors):
        ax.hist(iris.data[irisCsv.target==label, i], label=             
                            irisCsv.grouped[label], color=color)
        ax.set_xlabel(irisCsv.feature_names[i])  
        ax.legend(loc='upper right')