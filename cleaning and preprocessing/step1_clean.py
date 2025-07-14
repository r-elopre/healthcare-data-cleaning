import pandas as pd

# 1. Load the dataset
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_messy_data.csv"
df = pd.read_csv(file_path)

# 2. Inspect structure
print("=== Shape ===")
print(df.shape)

print("\n=== Columns ===")
print(df.columns.tolist())

print("\n=== Missing Values ===")
print(df.isnull().sum())

print("\n=== Data Types ===")
print(df.dtypes)

print("\n=== Sample Data ===")
print(df.head())
