import pandas as pd

# Load the raw dataset
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_messy_data.csv"
df = pd.read_csv(file_path)

# 1. Convert Age to numeric and fill with median
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'].fillna(df['Age'].median(), inplace=True)

# 2. Fill missing 'Condition' with 'Unknown'
df['Condition'].fillna('Unknown', inplace=True)

# 3. Fill missing 'Blood Pressure' with 'Unknown'
df['Blood Pressure'].fillna('Unknown', inplace=True)

# 4. Fill missing 'Cholesterol' with mean
df['Cholesterol'].fillna(df['Cholesterol'].mean(), inplace=True)

# 5. Drop rows where BOTH Email and Phone Number are missing
df.dropna(subset=['Email', 'Phone Number'], how='all', inplace=True)

# 6. Summary after cleaning
print("=== After Handling Missing Values ===")
print(df.isnull().sum())
