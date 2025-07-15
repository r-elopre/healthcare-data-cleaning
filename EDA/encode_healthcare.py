import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# 1. Load cleaned data
df = pd.read_csv(
    r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_cleaned.csv"
)

# 2. Drop unused columns
df = df.drop(columns=[
    'Patient Name', 'Visit Date', 'Email', 'Phone Number', 'Blood Pressure'
])

# 3. Define categorical features
cat_cols = ['Gender', 'Condition', 'Medication']

# 4. Build the encoder transformer
encoder = ColumnTransformer(
    transformers=[
        ('onehot',
            OneHotEncoder(sparse_output=False, handle_unknown='ignore'),
            cat_cols
        )
    ],
    remainder='passthrough'
)

# 5. Fit & transform
encoded_array = encoder.fit_transform(df)

# 6. Reconstruct DataFrame
encoded_cols = encoder.named_transformers_['onehot'].get_feature_names_out(cat_cols)
numeric_cols = ['Age', 'Cholesterol', 'Systolic', 'Diastolic']
all_cols = list(encoded_cols) + numeric_cols
df_encoded = pd.DataFrame(encoded_array, columns=all_cols)

# 7. Save
df_encoded.to_csv(
    r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_encoded.csv",
    index=False
)
print("Encoded data saved to healthcare_encoded.csv")
