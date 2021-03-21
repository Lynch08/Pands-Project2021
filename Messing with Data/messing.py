import pandas as pd
irisCsv = pd.read_csv('irisdataCSV.csv')

irisCsv.columns = ['sepal length in cm', 'sepal width in cm', 'petal length in cm','petal width in cm', 'species']
rawlist = list(irisCsv.species)
rawlistNoDup = list(dict.fromkeys(rawlist))

print(rawlistNoDup)
#column1 = [row[4] for row in irisCsv]
#print(column1)