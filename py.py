import pandas as pd

file_path = "./housing.csv"
data = pd.read_csv(file_path)

print("Estadísticas descriptivas:")
print(data.describe())