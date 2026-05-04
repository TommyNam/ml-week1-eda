import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
# If you downloaded it: df = pd.read_csv('iris.csv')
df = pd.read_csv('valorant-stats.csv')

# Always check the first 5 rows to make sure it loaded correctly
print(df.head())