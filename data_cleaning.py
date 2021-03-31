import sys


import pandas as pd

data_file = sys.argv[1]
df = pd.read_csv(data_file)

df.to_pickle("data/data.pkl")

print('Successfully cleaned data')