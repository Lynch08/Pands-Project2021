#This is the second draft of my analysis.py file which will include comments
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

# Functions for each plot
def hist():
    irisCsv.hist(figsize = (8, 6))
    
            
def bar():        
    y = irisCsv.species  
    X = irisCsv.drop('species',axis=1)                                                           # "drop" returns a new object with labels in the requested axis removed.
    dataset = pd.melt(irisCsv, "species", var_name="Variables and Measurment")                   # "melt" unpivots the Pandas Dataframe from wide to long format.
    sns.catplot(x="Variables and Measurment", y="value", hue="species", data=dataset, height=7, kind="bar",palette="bright") 
    

def pair():
    sns.pairplot(irisCsv, hue = 'species') 
    

def box():
    irisCsv.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    

def heat():
    plt.figure(figsize=(7,5)) 
    sns.heatmap(irisCsv.corr(),annot=True,cmap='rainbow', linewidths=.5) 
    
i = (input('''\nSummary data has been saved to the file Summary.txt\n\n\nTo See Plots Please Choose An Option from Below:\n
0 - Exit without plotting
1 - Histogram of all 4 variables
2 - Barplot of Variables
3 - PairPlot - All variables plotted againest all other variables
4 - Box plot
5 - HeatMap - Corrolation between variables
6 - Show all above plots in sequence (Close plot to see the next)
7 - Save all plots as .png
Please enter the number of an option listed above: '''))

try:
    # Try to convert 'i' to an integer type
    i = int(i)          
    if i >= 0:                             # If 'i' is an non-zero positive integer not one of the choices below                   
        if i == 0:                         # Exit program
            print('\nEnd of program\n\n')  # Inform user that the program is finished

        elif i == 1:
#Histogram of the each of the variables
            hist()
            plt.show()
        elif i == 2:
# Displays barplot
            bar()
            plt.show()
        elif i == 3:
#Pairplot of the each of the variables using seaborn - this allows you to visualise the measurements between each variable
#Allow you to spot if patterns emerge - breaks down by species
            pair()
            plt.show()
        elif i == 4:
#Box Plots-This gives us a much clearer idea of the distribution of the input attributes
            box()
            plt.show()

        elif i == 5:
            #Heatmap to show corrolatons between variables
            heat()
            plt.show()

            # Show all plots in sequence
        elif i == 6:
            hist()
            plt.show()
            bar()
            plt.show()
            pair()
            plt.show()
            box()
            plt.show()
            heat()
            plt.show()

        elif i == 7:
            hist()
            plt.savefig('Histograms.png')
            bar()
            plt.savefig('Barplot.png')
            pair()
            plt.savefig('Pairplot.png')
            box()
            plt.savefig('Boxplot.png')
            heat()
            plt.savefig('Heatmap.png')
        # Prints a VALUE error message if 'i' is not an integer > numbers in
        # list above.
        else:
            # Note to user that the program is finished
            print('\nInput Error:', i, 'is not a option listed above.\n',
                    '\nEnd of program\n\n')

    # Prints a VALUE error message if 'i' is not an integer > 0
    # Note to user that the program is finished
    else:
        print('\nError:', i, 'is not a option listed above.\n',
                '\nEnd of program\n\n')
# Prints a TYPE exception error if 'i' not an integer
# Note to user that the program is finished
except:
    print('\nError:', i, 'is not an number type listed above.\n',
            '\nEnd of program\n\n')