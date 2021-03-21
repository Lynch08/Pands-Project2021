#Histogram for 4 variables

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = pd.read_csv('IrisdataCSV.csv')

col = [ 'sepal length in cm',  'sepal width in cm',  'petal length in cm', 'petal width in cm', 'species']
#print(iris.head())

iris_setosa=iris.loc[iris["species"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["species"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["species"]=="Iris-versicolor"]

sns.FacetGrid(iris,hue="species",height=5).map(sns.histplot, "petal length in cm").add_legend()
#sns.FacetGrid(iris,hue="species",height=3).map(sns.histplot,"petal width in cm ").add_legend()
#sns.FacetGrid(iris,hue="species",height=3).map(sns.histplot,"sepal length in cm").add_legend()
#sns.FacetGrid(iris,hue="species",height=3).map(sns.histplot,"sepal width in cm").add_legend()
plt.show()