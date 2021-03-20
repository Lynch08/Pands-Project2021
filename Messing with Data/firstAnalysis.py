# This is the code to research the data set and code (in Python [1]) to investigate it.
# Author:Enda Lynch

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

filename = 'irisdataCSV.csv'

def readtxt():
    with open (filename) as f:
        txt = f.read()
        return txt

rtxt = readtxt()
print(rtxt)

