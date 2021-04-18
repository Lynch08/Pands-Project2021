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

setSet = irisCsv_set.corr()
setVer = irisCsv_ver.corr()
setVir = irisCsv_vir.corr()
with open ('summary.txt', 'w' ) as f:
    f.write('\n\nThis is a summary of the data set - broken down by species alone \n')
    f.write('Iris-setosa\n')
    f.write(str(setSet))
    f.write('\n\n\nIris-versicolor\n')
    f.write(str(setVer))
    f.write('\n\n\nIris-virginica\n')
    f.write(str(setVir))