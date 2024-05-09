import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from kneed import KneeLocator

file_path = "clasesemanatec/housing.csv"
df = pd.read_csv(file_path)

print("Estadísticas descriptivas:")
print(df.describe())