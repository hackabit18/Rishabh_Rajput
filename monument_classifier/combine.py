import pandas as pd

df1 = pd.read_csv('train_data1.csv')
with open('train_data.csv', 'a') as f:
	df1.to_csv(f, index=False, header=None)
print('CSV created!')
