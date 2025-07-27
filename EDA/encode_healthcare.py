import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import os

# Ensure output directory exists
output_dir = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data"
os.makedirs(output_dir, exist_ok=True)

# 1. Load cleaned data
input_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_cleaned.csv"
try:
    df = pd.read_csv(input_path)
except FileNotFoundError:
    print(f"Error: Input file {input_path} not found.")
    exit(1)

# 2. Impute missing Systolic and Diastolic with condition-specific medians
for condition in df['Condition'].unique():
    condition_mask = (df['Condition'] == condition) & (df['Systolic'].notna()) & (df['Diastolic'].notna())
    systolic_median = df[condition_mask]['Systolic'].median()
    diastolic_median = df[condition_mask]['Diastolic'].median()
    df.loc[(df['Condition'] == condition) & (df['Systolic'].isna()), 'Systolic'] = systolic_median
    df.loc[(df['Condition'] == condition) & (df['Diastolic'].isna()), 'Diastolic'] = diastolic_median

# 3. Replace suspicious Cholesterol value
valid_cholesterol = df[df['Cholesterol'] != 189.23276983094928]['Cholesterol']
cholesterol_median = valid_cholesterol.median()
df['Cholesterol'] = df['Cholesterol'].replace(189.23276983094928, cholesterol_median)

# 4. Drop unused columns
df = df.drop(columns=['Patient Name', 'Visit Date', 'Email', 'Phone Number', 'Blood Pressure'])

# 5. Define categorical features
cat_cols = ['Gender', 'Condition', 'Medication']

# 6. Build the encoder transformer
encoder = ColumnTransformer(
    transformers=[
        ('onehot',
         OneHotEncoder(sparse_output=False, handle_unknown='ignore'),
         cat_cols)
    ],
    remainder='passthrough'
)

# 7. Fit & transform
encoded_array = encoder.fit_transform(df)

# 8. Reconstruct DataFrame
encoded_cols = encoder.named_transformers_['onehot'].get_feature_names_out(cat_cols)
numeric_cols = ['Age', 'Cholesterol', 'Systolic', 'Diastolic']
all_cols = list(encoded_cols) + numeric_cols
df_encoded = pd.DataFrame(encoded_array, columns=all_cols)

# 9. Save
output_path = os.path.join(output_dir, 'healthcare_encoded.csv')
try:
    df_encoded.to_csv(output_path, index=False)
    print(f"Encoded data saved to {output_path}")
except Exception as e:
    print(f"Error saving file: {e}")