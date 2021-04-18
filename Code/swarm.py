

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

irisCsv = pd.read_csv('IrisdataCSV.csv')
petldata = irisCsv.groupby('petal length')
print(petldata)


petwdata = irisCsv.groupby('petal width')
sepldata = irisCsv.groupby('sepal length')
sepwdata = irisCsv.groupby('sepal width')

df = pd.DataFrame('IrisdataCSV.csv')
df['sepal length'] = sepldata
df['sepal width'] = sepwdata 
df['petal width'] = petwdata 
df['petal length'] = petldata 

fig, ax =plt.subplots(1,2,3,4)
sns.set(style="whitegrid")
fig=plt.gcf()
fig.set_size_inches(10,7)
fig = sns.swarmplot(x="species", y="petal length", data=irisCsv)


sns.set(style="whitegrid")
fig=plt.gcf()
fig.set_size_inches(10,7)
fig = sns.swarmplot(x="species", y="petal width", data=irisCsv)


sns.set(style="whitegrid")
fig=plt.gcf()
fig.set_size_inches(10,7)
fig = sns.swarmplot(x="species", y="sepal length", data=irisCsv)


sns.set(style="whitegrid")
fig=plt.gcf()
fig.set_size_inches(10,7)
fig = sns.swarmplot(x="species", y="sepal width", data=irisCsv)

plt.show()