#heat maps - same maps as above but function will save to .png
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

irisCsv = pd.read_csv('IrisdataCSV.csv')

#irisCsv.columns = ['sepal length', 'sepal width', 'petal length' , 'petal width', 'species']
#grouped = irisCsv.groupby('species')
fig, axes = plt.subplots(2,2, figsize = (10,10))
sns.histplot(irisCsv['petal length'], ax=axes[0,0]).legend('species')


sns.histplot(irisCsv['petal width'], ax=axes[0,1]).legend('species')


sns.histplot(irisCsv['sepal length'], ax=axes[1,0]).legend('species')


sns.histplot(irisCsv['sepal width'], ax=axes[1,1]).legend('species')

plt.show()