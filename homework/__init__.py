import pandas as pd

df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")
print(df["sexo"].astype(str).str.lower().value_counts())
print(len(df))
