import pandas as pd

# === Step 1: Load the messy dataset ===
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_messy_data.csv"
df = pd.read_csv(file_path)

# === Step 2: Basic Dataset Inspection ===

print("🟩 Dataset Shape (Rows, Columns):")
print(df.shape, "\n")

print("🟩 Column Names:")
print(df.columns.tolist(), "\n")

print("🟩 Missing Values per Column:")
print(df.isnull().sum(), "\n")

print("🟩 Data Types:")
print(df.dtypes, "\n")

print("🟩 First 5 Rows (Sample Data):")
print(df.head())
