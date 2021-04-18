#heat maps - same maps as above but function will save to .png
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

irisCsv = pd.read_csv('IrisdataCSV.csv')

irisCsv.columns = ['sepal length', 'sepal width', 'petal length' , 'petal width', 'species']
grouped = irisCsv.groupby('species')

irisCsv_set = grouped.get_group('Iris-setosa')
irisCsv_ver = grouped.get_group('Iris-versicolor')
irisCsv_vir = grouped.get_group('Iris-virginica')


def heatmulsave():
    plt.figure()
    sns.heatmap(irisCsv_set.corr(), annot=True, cmap='rainbow') 
    plt.title('Iris-Setsosa')
    plt.savefig('HeatMap Setsosa.png')

    plt.figure()
    sns.heatmap(irisCsv_ver.corr(), annot=True, cmap='rainbow') 
    plt.title('Iris-Versicolor')
    plt.savefig('HeatMap Versicolor.png')
    
    plt.figure()
    sns.heatmap(irisCsv_vir.corr(), annot=True, cmap='rainbow') 
    plt.title('Iris-Virginica')
    plt.savefig('HeatMap Virginica.png')
    

heatmulsave()