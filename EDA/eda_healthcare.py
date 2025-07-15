# eda_healthcare.py
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load cleaned data
df = pd.read_csv(
    r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_cleaned.csv"
)

# 2. Quick overview
print("=== Shape ===")
print(df.shape, "\n")

print("=== Columns & dtypes ===")
print(df.dtypes, "\n")

print("=== Null counts ===")
print(df.isna().sum(), "\n")

print("=== Statistical summary (numeric) ===")
print(df.describe().T, "\n")

# 3. Value counts for categoricals
cat_cols = df.select_dtypes(include=['object', 'category']).columns
for col in cat_cols:
    print(f"--- {col} value counts ---")
    print(df[col].value_counts(dropna=False).head(10), "\n")

# 4. Histograms for numeric features
num_cols = df.select_dtypes(include=['int64','float64']).columns
df[num_cols].hist(bins=20, figsize=(12,8))
plt.tight_layout()
plt.show()

# 5. Boxplots to check outliers (optional per column)
for col in num_cols:
    plt.figure(figsize=(4,2))
    plt.boxplot(df[col].dropna(), vert=False)
    plt.title(col)
    plt.tight_layout()
    plt.show()
