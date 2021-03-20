# This is the code to research the data set and code (in Python [1]) to investigate it.
# Author:Enda Lynch

import numpy as np
import matplotlib.pyplot as plt

filename = np.loadtxt('irisdata.txt', delimiter = ',')

seplelenght = filename[:, 0]
print (str(seplelenght))
