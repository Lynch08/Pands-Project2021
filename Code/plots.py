
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

irisCsv = pd.read_csv('IrisdataCSV.csv')
y = irisCsv.species  
X = irisCsv.drop('species',axis=1) # "drop" returns a new object with labels in the requested axis removed.
dataset = pd.melt(irisCsv, "species", var_name="Variables and Measurment") # "melt" unpivots the Pandas Dataframe from wide to long format.
sns.catplot(x="Variables and Measurment", y="value", hue="species", data=dataset, height=7, kind="bar",palette="bright") # plot configuration
plt.show() # Displays barplot