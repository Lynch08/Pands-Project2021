#Histogram for 4 variables

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = pd.read_csv('IrisdataCSV.csv')

#col = [ 'sepal length in cm',  'sepal width in cm',  'petal length in cm', 'petal width in cm', 'class']
#print(iris.columns[0])

fig = plt.figure(figsize = (10,10))
ax = fig.gca()
iris.hist(ax=ax)
plt.show()


