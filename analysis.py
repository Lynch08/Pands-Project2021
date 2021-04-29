#This is the fifth draft of my analysis.py file which will include comments, funtions and loops
#Author: Enda Lynch
#See README.md for Citations

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

irisCsv = pd.read_csv('IrisdataCSV.csv')


irisCsv.columns = ['sepal length', 'sepal width', 'petal length' , 'petal width', 'species']
grouped = irisCsv.groupby('species')
#test print (grouped.first())

irisCsv_set = grouped.get_group('Iris-setosa')
irisCsv_ver = grouped.get_group('Iris-versicolor')
irisCsv_vir = grouped.get_group('Iris-virginica')

######################## Summary Data - This data is being written to a file called summary.txt #############################
#Summary.txt will be created if it does not exist 
#If summary.txt exists, file will overwrite and save every time the program is run

#Give a count of each species in dataset
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

#Breakdown of the data by Species in one table
specSum = irisCsv.groupby('species').describe()
with open ('summary.txt', 'a' ) as f:
    f.write('This is a summary of the data set - broken down by the variables and species to for easier comparison \n')
    f.write(str(specSum))
    f.write('\n\n\n')

#Breakdown of the data by individual species  
sumSet = irisCsv_set.describe()
sumVer = irisCsv_ver.describe()
sumVir = irisCsv_vir.describe()
with open ('summary.txt', 'a' ) as f:
    f.write('\n\nThis is a summary of the data set - broken down by individual species\n')
    f.write('Iris-setosa\n')
    f.write(str(sumSet))
    f.write('\n\n\nIris-versicolor\n')
    f.write(str(sumVer))
    f.write('\n\n\nIris-virginica\n')
    f.write(str(sumVir))

#Breakdown of the correlation of the data by individual species 
corSet = irisCsv_set.corr()
corVer = irisCsv_ver.corr()
corVir = irisCsv_vir.corr()
with open ('summary.txt', 'a' ) as f:
    f.write('\n\nThis is a summary of the correlations in the data set - broken down by individual species \n')
    f.write('Iris-setosa\n')
    f.write(str(corSet))
    f.write('\n\n\nIris-versicolor\n')
    f.write(str(corVer))
    f.write('\n\n\nIris-virginica\n')
    f.write(str(corVir))



############################# Functions for each plot #############################################

#Histogram of the each of the variables
def hist():
    irisCsv.hist(figsize = (8, 6))
    
# Displays barplot          
def bar():        
    y = irisCsv.species  
    X = irisCsv.drop('species',axis=1)                                                           # "drop" returns a new object with labels in the requested axis removed.
    dataset = pd.melt(irisCsv, "species", var_name="Variables and Measurment")                   # "melt" unpivots the Pandas Dataframe from wide to long format.
    sns.catplot(x="Variables and Measurment", y="value", hue="species", data=dataset, height=7, kind="bar",palette="bright") 
    
#Pairplot of the each of the variables using seaborn - this allows you to visualise the measurements between each variable
#Allow you to spot if patterns emerge - breaks down by species
def pair():
    sns.pairplot(irisCsv, hue = 'species') 
    
#Box Plots-This gives us a much clearer idea of the distribution of the input attributes
def box():
    irisCsv.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    
#Heatmap to show corrolatons between variables
def heat():
    plt.figure(figsize=(7,5)) 
    sns.heatmap(irisCsv.corr(),annot=True,cmap='rainbow', linewidths=.5) 

#Swarmplots to show distribution between variables for each species
def swarm():
    sns.set(style="whitegrid")
    fig=plt.gcf()
    fig.set_size_inches(10,7)
    fig = sns.swarmplot(x="species", y="petal length", data=irisCsv)
    plt.title('Petal Length')
    plt.show()

    sns.set(style="whitegrid")
    fig=plt.gcf()
    fig.set_size_inches(10,7)
    fig = sns.swarmplot(x="species", y="petal width", data=irisCsv)
    plt.title('Petal Width')
    plt.show()

    sns.set(style="whitegrid")
    fig=plt.gcf()
    fig.set_size_inches(10,7)
    fig = sns.swarmplot(x="species", y="sepal length", data=irisCsv)
    plt.title('Sepal Length')
    plt.show()

    sns.set(style="whitegrid")
    fig=plt.gcf()
    fig.set_size_inches(10,7)
    fig = sns.swarmplot(x="species", y="sepal width", data=irisCsv)
    plt.title('Sepal Width')
    plt.show()

#Swarm plots - same maps as above but function will save to .png
def swarmsave():
    plt.figure()
    sns.set(style="whitegrid")
    fig=plt.gcf()
    fig.set_size_inches(10,7)
    fig = sns.swarmplot(x="species", y="petal length", data=irisCsv)
    plt.title('Petal Length')
    plt.savefig('Swarm Plot Petal Len.png')

    plt.figure()
    sns.set(style="whitegrid")
    fig=plt.gcf()
    fig.set_size_inches(10,7)
    fig = sns.swarmplot(x="species", y="petal width", data=irisCsv)
    plt.title('Petal width')
    plt.savefig('Swarm Plot Petal Wid.png')

    plt.figure()
    sns.set(style="whitegrid")
    fig=plt.gcf()
    fig.set_size_inches(10,7)
    fig = sns.swarmplot(x="species", y="sepal length", data=irisCsv)
    plt.title('Sepal Length')
    plt.savefig('Swarm Plot Sepal Len.png')

    plt.figure()    
    sns.set(style="whitegrid")
    fig=plt.gcf()
    fig.set_size_inches(10,7)
    fig = sns.swarmplot(x="species", y="sepal width", data=irisCsv)
    plt.title('Sepal Width')
    plt.savefig('Swarm Plot Sepal Wid.png')

#heat maps - help show correlation between variables for individual species
def heatmul():
    sns.heatmap(irisCsv_set.corr(), annot=True, cmap='rainbow') 
    plt.title('Iris-Setsosa')
    plt.show()

    sns.heatmap(irisCsv_ver.corr(), annot=True, cmap='rainbow') 
    plt.title('Iris-Versicolor')
    plt.show()

    sns.heatmap(irisCsv_vir.corr(), annot=True, cmap='rainbow') 
    plt.title('Iris-Virginica')
    plt.show()

#heat maps - same maps as above but function will save to .png
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

#################### Display Menu for user to decide what plots they want to see and save if neccessary############################
i = "input"
def displayMenu():
    i = (input('''\nSummary data has been saved to the file Summary.txt\n\n\nPlotting Options (The program will continue to run until 0 is entered):\n
    0 - Exit without plotting
    1 - Histograms of all 4 variables
    2 - Bargraph of Variables
    3 - PairPlot - All variables plotted againest all other variables as scatter plots
    4 - Box plot - Distribution of variable data
    5 - HeatMap - Correlation between variables
    6 - Swarmplots - 4 Plots, one for each variable (Close plot to see the next)
    7 - HeatMaps - 3 Maps, shows variable correlation for each species (Close Map to see the next)
    8 - Show all above plots in sequence (Close plot to see the next)
    9 - Save all plots as .png
    Please enter the number of an option listed above (invalid inputs will not be accepted): '''))
    return i

# Loop to call the relavent choice from the display menu function
# Program will not exit until user selects exit option (0)
# Error handling will not allow user to input invalid value

i = displayMenu()
while (i):
    try:
    # Try to convert 'i' to an integer type
        i = int(i)          
        if i >= 0:                             # If 'i' is an non-zero positive integer (not one of the choices below)                   
            if i == 0:                         # Exit program
                print('\n\nYou Have Exited The Program\n\n')  # Inform user that the program is finished

            elif i == 1:                            
                hist()                         
                plt.show()
                i = displayMenu()

            elif i == 2:
                bar()
                plt.show()
                i = displayMenu()

            elif i == 3:
                pair()
                plt.show()
                i = displayMenu()

            elif i == 4:
                box()
                plt.show()
                i = displayMenu()

            elif i == 5:
                heat()
                plt.show()
                i = displayMenu()

            elif i == 6:
                swarm()
                i = displayMenu()

            elif i == 7:
                heatmul()
                i = displayMenu()

            # Show all plots in sequence
            elif i == 8:
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
                swarm()
                heatmul()
                i = displayMenu()

            # Save all plots
            elif i == 9:
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
                swarmsave()
                heatmulsave()
                i = displayMenu()

            else:
                i = displayMenu()   #loop back to display if anything other than valid option is entered
        else:
            i = displayMenu()       #loop back to display if anything other than valid option is entered
    except:
        i = displayMenu()           #loop back to display if anything other than valid option is entered