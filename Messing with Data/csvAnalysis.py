# This is the code to research the data set and code (in Python [1]) to investigate it.
# Author:Enda Lynch

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

filename = 'irisdataCSV.csv'

with open(filename, 'rt') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    firstLine = True
    for line in csvReader:
        if firstLine:
            firstline = False
            continue
        print(line[1])
