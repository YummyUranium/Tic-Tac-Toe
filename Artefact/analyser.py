import pandas as pd

file = pd.read_csv("ttt-data.csv")

print(file.describe([.5], "all"))