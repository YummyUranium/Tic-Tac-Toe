import pandas as pd

file = pd.read_csv("./Artefact/ttt-data.csv")

print(file.describe([.5], "all"))