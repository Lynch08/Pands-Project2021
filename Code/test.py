import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

irisCsv = pd.read_csv('IrisdataCSV.csv')
irisCsv.columns = ['sepal length', 'sepal width', 'petal length' , 'petal width', 'species']
grouped = irisCsv.groupby('species')
#print (grouped.first())

irisCsv_set = grouped.get_group('Iris-setosa')
irisCsv_ver = grouped.get_group('Iris-versicolor')
irisCsv_vir = grouped.get_group('Iris-virginica')

sns.heatmap(irisCsv_set.corr(), annot=True, cmap='rainbow') 
plt.title('Setsosa')
plt.show()

sns.heatmap(irisCsv_ver.corr(), annot=True, cmap='rainbow') 
plt.title('Versicolor')
plt.show()

sns.heatmap(irisCsv_vir.corr(), annot=True, cmap='rainbow') 
plt.title('Virginica')
plt.show()