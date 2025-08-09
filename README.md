# Healthcare Data Cleaning and Preprocessing

<p align="center">
  <a href="https://youtu.be/9nqpTcP0RZ0">
    <img src="https://img.youtube.com/vi/9nqpTcP0RZ0/maxresdefault.jpg" alt="Healthcare Data Cleaning & Preprocessing Video">
  </a>
  <br/>
  <em>Click the thumbnail to watch on YouTube</em>
</p>

## 🧹 Step 1: Data Cleaning and Preprocessing

### 🔍 Inspection Summary
- **Dataset**: 1000 rows, 10 columns (Patient Name, Age, Gender, Condition, etc.)
- **Issues**:
  - Missing values: Age (159), Condition (206), Blood Pressure (166), Cholesterol (231), Email (384), Phone Number (179)
  - Data type issues: Age, Blood Pressure, Visit Date, Phone Number stored as objects
  - Inconsistent date formats in Visit Date (e.g., `01/15/2020`, `April 5, 2018`)
  - Duplicate entries for `David Lee`

### ✅ Step 1.2: Handling Missing Values
- **Age**: Converted to numeric, filled with median
- **Condition**: Filled with "Unknown"
- **Blood Pressure**: Filled with "Unknown" (parsed later)
- **Cholesterol**: Filled with mean
- **Email & Phone Number**: Dropped rows missing both; remaining missing: Email (315), Phone Number (110)
- **Result**: All medical fields complete; contact fields partially missing but handled.

### ✅ Step 1.3: Fixing Inconsistencies
| Task                     | Status | Notes                                              |
|--------------------------|--------|----------------------------------------------------|
| Capitalization           | ✅     | Normalized Patient Name, Gender, Condition          |
| Date Formatting          | ✅     | Visit Date to datetime, invalid values → NaT       |
| Blood Pressure Split     | ✅     | Split into Systolic/Diastolic columns              |
| Email & Phone Cleaning   | ✅     | Stripped spaces, lowercased                        |
| Removed Duplicates       | ✅     | Based on Patient Name, Age, Visit Date             |

- **Note**: NaT in Visit Date for unparseable formats.

### ✅ Step 1.4: Save Cleaned Data
- **Output**: `data/healthcare_cleaned.csv`
- **Includes**:
  - Handled missing values
  - Standardized text fields
  - Normalized Visit Date to datetime
  - Split Blood Pressure into Systolic/Diastolic
  - Removed duplicates
- **Ready for**: EDA, machine learning, or visualization

## 🔎 Step 1.5: Exploratory Data Analysis (EDA)
- **Key Insights**:
  - **Age**: Clustered at 25, 35, 60, 70 (pseudo-categorical)
  - **Cholesterol**: Clusters at 160–220 mg/dL, slight right skew
  - **Blood Pressure**: Binned at 110/70, 120/80, 130/85, 140/90
- **Actions**:
  - Checked dataset structure, types, nulls
  - Analyzed categorical value counts (Gender, Condition, etc.)
  - Plotted histograms and boxplots for numeric features
- **Why it matters**: Informs encoding/scaling choices, identifies outliers, and flags data quirks.

## ✅ Step 2: Categorical Encoding
- **Actions**:
  - Dropped identifiers (Patient Name) and mostly empty fields (Visit Date, Email, Phone Number)
  - One-hot encoded nominal features: Gender, developmental disabilities, Medication
  - Preserved numeric columns: Age, Cholesterol, Systolic, Diastolic
  - Saved to `data/healthcare_encoded.csv`
- **Why it matters**: Ensures numeric inputs for ML, avoids artificial category ordering, and enhances pipeline robustness.

## ✅ Step 3: Feature Scaling
- **Actions**:
  - Loaded `data/healthcare_encoded.csv` (76 rows, 17 columns)
  - Standardized numeric columns (Age, Cholesterol, Systolic, Diastolic) using StandardScaler
  - Left one-hot encoded columns unchanged
  - Saved to `Feature Scaling/healthcare_scaled.csv`
- **Why it matters**: Standardizes feature scales for ML algorithms like SVM or k-NN, ensuring equal contribution.
- **Output**: Fully numeric, scaled dataset ready for modeling or further analysis.