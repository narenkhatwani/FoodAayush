import pandas as pd

import os

directory = r'C:/Users/potda/Desktop/CSV_changes/assets/'
directory1 = r'C:/Users/potda/Desktop/CSV_changes/assests_modified/'

list1 = []
list2 = []
for filename in os.listdir(directory):
	if filename.endswith(".csv"):
		list1.append(os.path.join(directory, filename))
		list2.append(os.path.join(directory1, filename))
		continue
	else:
		continue

for i,j in zip(list1,list2):
	df = pd.read_csv(i)

	columns = list(df)

	df[columns] = df[columns].fillna(0)

	for col in columns:
	  df[col] = df[col].replace(to_replace = '±[\S]*', value = "", regex = True)

	df.to_csv(j)
