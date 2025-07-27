import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the encoded dataset
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_encoded.csv"
df = pd.read_csv(file_path)

# Separate numeric columns (excluding one-hot encoded binary columns)
numeric_columns = ['Age', 'Cholesterol', 'Systolic', 'Diastolic']
X_numeric = df[numeric_columns]

# Initialize the scaler
scaler = StandardScaler()

# Fit and transform the numeric data
X_scaled = scaler.fit_transform(X_numeric)

# Convert the scaled data back to a DataFrame
X_scaled_df = pd.DataFrame(X_scaled, columns=numeric_columns)

# Combine with the one-hot encoded columns (which don't need scaling)
df_scaled = pd.concat([X_scaled_df, df.drop(columns=numeric_columns)], axis=1)

# Save the scaled dataset
output_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_scaled.csv"
df_scaled.to_csv(output_path, index=False)

print(f"Scaled dataset saved to {output_path}")