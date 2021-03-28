#my first attempt at outputing multiple plots in one go
#Author Enda Lynch

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

irisCsv = pd.read_csv('IrisdataCSV.csv')
dataSum = irisCsv.describe()

with open ('summary.txt', 'w') as f:
    f.write(str(dataSum))