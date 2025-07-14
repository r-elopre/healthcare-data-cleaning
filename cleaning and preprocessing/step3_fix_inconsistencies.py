import pandas as pd

file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_messy_data.csv"
df = pd.read_csv(file_path)

# Fix Age column again (for safety)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'].fillna(df['Age'].median(), inplace=True)

# Normalize patient name, gender, condition
df['Patient Name'] = df['Patient Name'].str.strip().str.title()
df['Gender'] = df['Gender'].str.strip().str.lower()
df['Condition'] = df['Condition'].str.strip().str.title()

# Standardize visit date format
df['Visit Date'] = pd.to_datetime(df['Visit Date'], errors='coerce')

# Parse blood pressure
bp_split = df['Blood Pressure'].str.extract(r'(?P<Systolic>\d{2,3})/(?P<Diastolic>\d{2,3})')
df['Systolic'] = pd.to_numeric(bp_split['Systolic'], errors='coerce')
df['Diastolic'] = pd.to_numeric(bp_split['Diastolic'], errors='coerce')

# Clean email and phone number
df['Email'] = df['Email'].str.strip().str.lower()
df['Phone Number'] = df['Phone Number'].str.strip()

# Drop duplicates based on name, age, visit date
df.drop_duplicates(subset=['Patient Name', 'Age', 'Visit Date'], inplace=True)

# Final structure check
print("=== Data After Fixing Inconsistencies ===")
print(df.head())
