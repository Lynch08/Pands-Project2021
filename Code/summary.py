#Output a summary of the data to a text file
#Author: Enda Lynch 

import pandas as pd 

#headings = ['sepal length in cm',  'sepal width in cm',  'petal length in cm', 'petal width in cm', 'species']

irisCsv = pd.read_csv('IrisdataCSV.csv')        #Read file
irisInfo = irisCsv.info() 
irisSum = irisCsv.describe() 
irisSize = irisCsv.groupby('species').size()
#dataSum = irisCsv.describe()                    #Use .describe() to give summary of data

with open ('summary.txt', 'w') as f:            #Create a write to file called summary.txt
    f.write(str(irisSize))  
    f.write(str(irisInfo))
    f.write(str(irisSum))
                          #Write summary data to file