#Histogram for 4 variables

import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd

iris = pd.read_csv('IrisdataCSV.csv')
col = [ 'sepal length in cm',  'sepal width in cm',  'petal length in cm', 'petal width in cm', 'class']

fig, axes = plt.subplots(nrows= 2, ncols=2)
colors= ['blue', 'red', 'green']

for i, ax in enumerate(axes.flat):
    for label, color in zip(range(len(iris.target_names)), colors):
        ax.hist(iris.data[iris.target==label, i], label=             
                            iris.target_names[label], color=color)
        ax.set_xlabel(iris.feature_names[i])  
        ax.legend(loc='upper right')


plt.show()

