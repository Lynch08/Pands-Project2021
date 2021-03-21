import pandas as pd
irisCsv = pd.read_csv('irisdataCSV.csv')

classl = irisCsv.columns.species

print(classl)
#column1 = [row[4] for row in irisCsv]
#print(column1)