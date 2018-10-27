import pandas as pd

data = pd.read_csv("test_data.csv", header=None, index_col=False) 
# Preview the first 5 lines of the loaded data 
data = data.sample(frac=1).reset_index(drop=True)
print(data)
