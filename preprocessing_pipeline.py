import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
import os

# Custom transformer for handling missing values
class MissingValueHandler(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.age_median_ = X['Age'].median()
        self.cholesterol_mean_ = X[X['Cholesterol'] != 189.23276983094928]['Cholesterol'].mean()
        return self
    
    def transform(self, X):
        X = X.copy()
        X['Age'] = pd.to_numeric(X['Age'], errors='coerce').fillna(self.age_median_)
        X['Condition'] = X['Condition'].fillna('Unknown')
        X['Blood Pressure'] = X['Blood Pressure'].fillna('Unknown')
        X['Cholesterol'] = X['Cholesterol'].fillna(self.cholesterol_mean_)
        X = X.dropna(subset=['Email', 'Phone Number'], how='all')
        return X

# Custom transformer for fixing inconsistencies
class InconsistencyFixer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X['Patient Name'] = X['Patient Name'].str.strip().str.title()
        X['Gender'] = X['Gender'].str.strip().str.lower()
        X['Condition'] = X['Condition'].str.strip().str.title()
        X['Visit Date'] = pd.to_datetime(X['Visit Date'], errors='coerce')
        bp_split = X['Blood Pressure'].str.extract(r'(?P<Systolic>\d{2,3})/(?P<Diastolic>\d{2,3})')
        X['Systolic'] = pd.to_numeric(bp_split['Systolic'], errors='coerce')
        X['Diastolic'] = pd.to_numeric(bp_split['Diastolic'], errors='coerce')
        X['Email'] = X['Email'].str.strip().str.lower()
        X['Phone Number'] = X['Phone Number'].str.strip()
        X = X.drop_duplicates(subset=['Patient Name', 'Age', 'Visit Date'])
        return X

# Custom transformer for condition-specific imputation and cholesterol replacement
class CustomImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.condition_medians_ = {}
        for condition in X['Condition'].unique():
            mask = (X['Condition'] == condition) & (X['Systolic'].notna()) & (X['Diastolic'].notna())
            self.condition_medians_[condition] = {
                'Systolic': X[mask]['Systolic'].median(),
                'Diastolic': X[mask]['Diastolic'].median()
            }
        self.cholesterol_median_ = X[X['Cholesterol'] != 189.23276983094928]['Cholesterol'].median()
        return self
    
    def transform(self, X):
        X = X.copy()
        for condition in X['Condition'].unique():
            X.loc[(X['Condition'] == condition) & (X['Systolic'].isna()), 'Systolic'] = self.condition_medians_[condition]['Systolic']
            X.loc[(X['Condition'] == condition) & (X['Diastolic'].isna()), 'Diastolic'] = self.condition_medians_[condition]['Diastolic']
        X['Cholesterol'] = X['Cholesterol'].replace(189.23276983094928, self.cholesterol_median_)
        return X

# Load data
input_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data\healthcare_cleaned.csv"
try:
    df = pd.read_csv(input_path)
except FileNotFoundError:
    print(f"Error: Input file {input_path} not found.")
    exit(1)

# Define columns
numeric_cols = ['Age', 'Cholesterol', 'Systolic', 'Diastolic']
categorical_cols = ['Gender', 'Condition', 'Medication']
drop_cols = ['Patient Name', 'Visit Date', 'Email', 'Phone Number', 'Blood Pressure']

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_cols),
        ('cat', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), categorical_cols),
        ('drop', 'drop', drop_cols)
    ])

# Full pipeline
pipeline = Pipeline(steps=[
    ('missing_values', MissingValueHandler()),
    ('fix_inconsistencies', InconsistencyFixer()),
    ('custom_imputer', CustomImputer()),
    ('preprocessor', preprocessor)
])

# Fit and transform
try:
    X_transformed = pipeline.fit_transform(df)
except Exception as e:
    print(f"Error in pipeline transformation: {e}")
    exit(1)

# Reconstruct DataFrame
encoded_cols = pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(categorical_cols)
all_cols = list(encoded_cols) + numeric_cols
df_transformed = pd.DataFrame(X_transformed, columns=all_cols)

# Save transformed data
output_dir = r"C:\Users\ri\OneDrive\ai project\data cleaning\healthcare\data"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'healthcare_encoded_scaled.csv')
try:
    df_transformed.to_csv(output_path, index=False)
    print(f"Transformed data saved to {output_path}")
except Exception as e:
    print(f"Error saving file: {e}")

# Save Cholesterol data for visualization
cholesterol_unscaled = df['Cholesterol'].replace(189.23276983094928, df[df['Cholesterol'] != 189.23276983094928]['Cholesterol'].median())
cholesterol_scaled = df_transformed['Cholesterol']
pd.DataFrame({
    'Unscaled': cholesterol_unscaled,
    'Scaled': cholesterol_scaled
}).to_csv(os.path.join(output_dir, 'cholesterol_for_viz.csv'), index=False)