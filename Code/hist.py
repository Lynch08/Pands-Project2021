#Output a summary of the data as histograms
#Author: Enda Lynch 

import pandas as pd 
import matplotlib.pyplot as plt
#headings = ['sepal length in cm',  'sepal width in cm',  'petal length in cm', 'petal width in cm', 'species']

irisCsv = pd.read_csv('IrisdataCSV.csv')        #Read file

irisCsv.hist(figsize = (8, 6))
plt.show()