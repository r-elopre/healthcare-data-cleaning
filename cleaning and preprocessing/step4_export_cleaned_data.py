import pandas as pd

# Load the raw data
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_messy_data.csv"
df = pd.read_csv(file_path)

# === Step 1.2: Handle missing values ===
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Condition'] = df['Condition'].fillna('Unknown')
df['Blood Pressure'] = df['Blood Pressure'].fillna('Unknown')
df['Cholesterol'] = df['Cholesterol'].fillna(df['Cholesterol'].mean())
df.dropna(subset=['Email', 'Phone Number'], how='all', inplace=True)

# === Step 1.3: Fix inconsistencies ===
df['Patient Name'] = df['Patient Name'].str.strip().str.title()
df['Gender'] = df['Gender'].str.strip().str.lower()
df['Condition'] = df['Condition'].str.strip().str.title()
df['Visit Date'] = pd.to_datetime(df['Visit Date'], errors='coerce')

bp_split = df['Blood Pressure'].str.extract(r'(?P<Systolic>\d{2,3})/(?P<Diastolic>\d{2,3})')
df['Systolic'] = pd.to_numeric(bp_split['Systolic'], errors='coerce')
df['Diastolic'] = pd.to_numeric(bp_split['Diastolic'], errors='coerce')

df['Email'] = df['Email'].str.strip().str.lower()
df['Phone Number'] = df['Phone Number'].str.strip()
df.drop_duplicates(subset=['Patient Name', 'Age', 'Visit Date'], inplace=True)

# === Step 1.4: Save cleaned dataset ===
output_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_cleaned.csv"
df.to_csv(output_path, index=False)

print(f"✅ Cleaned dataset saved to:\n{output_path}")
  