#Output a summary of the data to a text file
#Author: Enda Lynch 

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

irisCsv = pd.read_csv('IrisdataCSV.csv')

#Give a count of the type of data
specSum = irisCsv.groupby('species').describe()
with open ('summary.txt', 'w' ) as f:
    f.write(str(specSum ))
    f.write('\n\n\n')