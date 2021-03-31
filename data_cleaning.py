import pandas as pd

df = pd.read_csv("data/H1N1_Flu_Vaccines.csv")

df.to_pickle("data/data.pkl")
print('Successfully cleaned data')