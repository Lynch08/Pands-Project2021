#Histogram for 4 variables

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = pd.read_csv('IrisdataCSV.csv')
irisCsv.columns = ['sepal length in cm', 'sepal width in cm', 'petal length in cm','petal width in cm', 'species']
rawlist = list(irisCsv.species)
rawlistNoDup = list(dict.fromkeys(rawlist))

print(rawlistNoDup)
#col = [ 'sepal length in cm',  'sepal width in cm',  'petal length in cm', 'petal width in cm', 'class']
#print(iris.columns[0])

fig = plt.figure(figsize = (10,8))
ax = fig.gca()
iris.hist(ax=ax)
plt.show()


