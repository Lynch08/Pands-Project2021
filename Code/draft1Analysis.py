#This is the first draft of my analysis.py file which will include comments
#Author: Enda Lynch


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

irisCsv = pd.read_csv('IrisdataCSV.csv')

#Give a count of the type of data
irisSize = irisCsv.groupby('species').size()
with open ('summary.txt', 'w' ) as f:
    f.write('This is a basic summary of the data set - a count of the 3 Species of Iris and a consise summary of the overall dataset using the pandas liberary \n \n')
    f.write(str(irisSize))
    f.write('\n\n\n')

#Breakdown of the overall data
irisSum = irisCsv.describe()
with open ('summary.txt', 'a') as f:
    f.write(str(irisSum))

#Histogram of the each of the variables
irisCsv.hist(figsize = (8, 6))
plt.show()

#Pairplot of the each of the variables using seaborn - this allows you to visualise the measurements between each variable
#Allow you to spot if patterns emerge - breaks down by species
sns.pairplot(irisCsv, hue = 'species') 
plt.show()

irisCsv.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()