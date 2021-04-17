import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

irisCsv = pd.read_csv('IrisdataCSV.csv')
petldata = irisCsv.groupby('petal length').show()
print(petldata)