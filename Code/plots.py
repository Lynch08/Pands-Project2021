
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

irisCsv = pd.read_csv('IrisdataCSV.csv')
sns.pairplot(irisCsv, hue = 'species') 
plt.show()
#plt.savefig('save.png')