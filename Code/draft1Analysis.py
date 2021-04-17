#This is the first draft of my analysis.py file which will include comments
#Author: Enda Lynch


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
    f.write('\n\n\n')

#Breakdown of the data by Species
specSum = irisCsv.groupby('species').describe()
with open ('summary.txt', 'a' ) as f:
    f.write('This is a summary of the data set - broken down by the variables and species to for easier comparison \n')
    f.write(str(specSum))

#Histogram of the each of the variables
irisCsv.hist(figsize = (8, 6))
plt.show()
#plt.savefig('Histograms.png')

# Displays barplot
y = irisCsv.species  
X = irisCsv.drop('species',axis=1)                                                           # "drop" returns a new object with labels in the requested axis removed.
dataset = pd.melt(irisCsv, "species", var_name="Variables and Measurment")                   # "melt" unpivots the Pandas Dataframe from wide to long format.
sns.catplot(x="Variables and Measurment", y="value", hue="species", data=dataset, height=7, kind="bar",palette="bright") 
plt.show()
#plt.savefig('Barplot.png')

#Pairplot of the each of the variables using seaborn - this allows you to visualise the measurements between each variable
#Allow you to spot if patterns emerge - breaks down by species
sns.pairplot(irisCsv, hue = 'species') 
plt.show()
#plt.savefig('Pairplot.png')

#Box Plots-This gives us a much clearer idea of the distribution of the input attributes
irisCsv.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
#plt.savefig('Boxplot.png')

#Heatmap to show corrolatons between variables
plt.figure(figsize=(7,5)) 
sns.heatmap(irisCsv.corr(),annot=True,cmap='rainbow', linewidths=.5) 
plt.show()
#plt.savefig('Heatmap.png')