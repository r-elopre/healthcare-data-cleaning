## 🧹 Step 1: Data Cleaning and Preprocessing
<img width="410" height="614" alt="010a4c53-fa2c-4c21-a12c-a47d27cec606 (1)" src="https://github.com/user-attachments/assets/221a9471-abfe-42b8-8442-666555c0dbbb" />

### 🔍 Inspection Summary

✅ **Shape**: 1000 rows × 10 columns  
✅ **Columns**: Patient-related data (name, age, gender, condition, etc.)

⚠️ **Missing Values (notable):**
- `Age`: 159 missing  
- `Condition`: 206 missing  
- `Blood Pressure`: 166 missing  
- `Cholesterol`: 231 missing  
- `Email`: 384 missing  
- `Phone Number`: 179 missing  

⚠️ **Data Type Issues:**
- `Age`, `Blood Pressure`, `Visit Date`, and `Phone Number` are stored as `object` — should be numeric or datetime

⚠️ **Date Inconsistency:**
- Mixed formats found in `Visit Date`: `01/15/2020`, `April 5, 2018`, `2019.12.01`, `2020/02/20`

⚠️ **Duplicate Name**:  
- `David Lee` appears more than once

---

### ✅ Step 1.2: Handling Missing Values — Summary

We analyzed each column with missing data and handled them appropriately:

- 🔹 **`Age` (159 missing)**  
  → Converted to numeric (`int`) and filled with **median**  
  ✅ Now complete

- 🔹 **`Condition` (206 missing)**  
  → Filled with `"Unknown"`  
  ✅ Fully filled

- 🔹 **`Blood Pressure` (166 missing)**  
  → Temporarily filled with `"Unknown"` (parsed later)  
  ✅ Fully filled

- 🔹 **`Cholesterol` (231 missing)**  
  → Filled with **mean** value  
  ✅ Fully filled

- 🔹 **`Email` & `Phone Number`**  
  → Did **not** fill individually  
  → Dropped rows where **both were missing**  
  ✅ Reduced missing to:
    - `Email`: 315 remaining
    - `Phone Number`: 110 remaining

✅ **Result**: All key medical fields are complete and reliable. Contact fields are still partially missing but intelligently handled.

---

### ✅ Step 1.3: Fixing Inconsistencies — Summary

| Task                    | Status | Notes                                                  |
|-------------------------|--------|---------------------------------------------------------|
| ✔ Capitalization        | ✅     | `Patient Name`, `Gender`, `Condition` normalized        |
| ✔ Date Formatting       | ✅     | `Visit Date` converted to `datetime`, bad values → `NaT`|
| ✔ Blood Pressure Split  | ✅     | Extracted `Systolic` and `Diastolic` columns            |
| ✔ Email & Phone Cleaned | ✅     | Stripped, lowercased                                    |
| ✔ Removed Duplicates    | ✅     | Based on `Patient Name`, `Age`, and `Visit Date`        |

⚠️ Note: `NaT` in `Visit Date` indicates invalid or unparseable formats — expected with dirty data.

---

### ✅ Final Overview

| Substep | Description                                      | Status   |
|---------|--------------------------------------------------|----------|
| **1.1** | Inspect structure, types, nulls                  | ✅ Done  |
| **1.2** | Handle missing values                            | ✅ Done  |
| **1.3** | Fix inconsistencies (formatting, parsing, etc.)  | ✅ Done  |

### ✅ Step 1.4: Save the Cleaned Data — Summary

After completing all data cleaning steps (handling missing values and fixing inconsistencies), we finalized the process by exporting the cleaned dataset to a new CSV file.

**📁 Output Path:**  
`data/healthcare_cleaned.csv`

**📋 Export Includes:**
- Missing values in `Age`, `Condition`, `Blood Pressure`, and `Cholesterol` were handled
- Text fields like `Patient Name`, `Gender`, `Condition`, `Email`, and `Phone Number` were cleaned and standardized
- `Visit Date` values were normalized into a consistent `datetime` format
- `Blood Pressure` values were split into numeric `Systolic` and `Diastolic` columns
- Duplicate rows based on `Patient Name`, `Age`, and `Visit Date` were removed

✅ The cleaned CSV file is now ready to be used in:
- **Step 2: Exploratory Data Analysis (EDA)**
- or any machine learning, statistical modeling, or visualization steps

## 🔎 Step 1.5: Exploratory Data Analysis (EDA)
<img width="1903" height="959" alt="image" src="https://github.com/user-attachments/assets/09901f88-f7c7-4c1c-b7f2-c06314d21f30" />

### Key Distribution Insights

1. **Discrete, cluster‑style distributions**  
   - **Age** only takes on a handful of values—25, 35, 60, 70—with roughly equal counts at each.  
   - **Cholesterol** clusters around common measurements (160, 180, 190, 200, 220 mg/dL), with the highest frequency at 220.  
   - **Systolic** and **Diastolic** pressures fall into “textbook” bins (110/70, 120/80, 130/85, 140/90), with most readings at the low and high ends.  
   This suggests the data were rounded or binned at collection time (e.g. standard BP cuffs), making these numerics almost pseudo‑categorical.

2. **Symmetry and skew**  
   - **Age** is fairly symmetric between its minimum (25) and maximum (70).  
   - **Cholesterol** shows slight right skew (longer tail toward higher readings).  
   - **Blood pressure** readings appear roughly uniform across their four bins, with no heavy tails.

**What we did:**  
1. **Overview & summaries**  
   - Checked the cleaned dataset’s shape, dtypes, and null counts.  
   - Viewed `.describe()` for numeric summaries.  
2. **Categorical counts**  
   - Printed value counts for each object/categorical column (e.g. `Gender`, `Condition`, `Medication`, `Blood Pressure`, `Email`, `Phone Number`).  
3. **Visual checks**  
   - Plotted histograms for all numeric features (`Age`, `Cholesterol`, `Systolic`, `Diastolic`) to see distributions.  
   - Boxplots to spot outliers and potential skew.  
4. **Key takeaways:**  
   - Dropped or ignored identifier‑like columns and mostly empty fields.  
   - Confirmed which numeric columns have outliers (→ later choice of `RobustScaler`).  
   - Noted category cardinalities and rare levels (→ informed encoding strategy).

**Why it matters:**  
- EDA ensures you understand data distributions, outliers, and category frequencies before encoding or scaling.  
- Helps choose the right encoding and scaling methods, and flags any remaining data quirks.

---

## ✅ Step 2: Categorical Encoding
<img width="660" height="440" alt="79dfa770-e1ff-43c9-8ba1-e2f23f8e8157 (1)" src="https://github.com/user-attachments/assets/bc5ce7ab-6cbb-42c4-9990-2aa36dc3b37e" />

**What we did:**  
1. **Dropped non‑informative or redundant columns**  
   - Removed identifiers (`Patient Name`), mostly‑empty fields (`Visit Date`, `Email`, `Phone Number`) and the original combined `Blood Pressure` (we split it into `Systolic`/`Diastolic`).  
2. **Identified categorical features**  
   - **Nominal** (no inherent order): `Gender`, `Condition`, `Medication`  
3. **Applied One‑Hot Encoding**  
   - Converted each category into its own binary column (e.g. `Gender_female`, `Condition_Diabetes`, `Medication_METFORMIN`, etc.)  
   - Used `handle_unknown='ignore'` so unseen categories won’t break the pipeline.  
4. **Preserved numeric columns**  
   - Left `Age`, `Cholesterol`, `Systolic`, and `Diastolic` unchanged.  
5. **Saved the result** to `data/healthcare_encoded.csv`, yielding a fully numeric dataset ready for scaling and modeling.

**Why it matters:**  
- ML algorithms require numeric inputs—text labels must be encoded.  
- One‑Hot Encoding prevents implying any artificial order among nominal categories.  
- Dropping identifiers and unused fields avoids privacy leaks and model overfitting.  
- Using a `ColumnTransformer` with `handle_unknown='ignore'` makes your pipeline robust and reusable.  

---

## ✅ Step 3: Feature Scaling
<img width="660" height="440" alt="feature_scaling_image" src="https://github.com/user-attachments/assets/placeholder-for-scaling-image" />

**What we did:**  
1. **Loaded the encoded dataset**  
   - Read `data/healthcare_encoded.csv`, which contains 76 records with 17 columns (13 one-hot encoded columns for `Gender`, `Condition`, `Medication`, and 4 numeric columns: `Age`, `Cholesterol`, `Systolic`, `Diastolic`).  
2. **Separated numeric columns**  
   - Identified `Age`, `Cholesterol`, `Systolic`, and `Diastolic` for scaling, as these have varying ranges (e.g., `Age`: 25–70, `Cholesterol`: 160–220).  
3. **Applied StandardScaler**  
   - Standardized the numeric columns to have a mean of 0 and a standard deviation of 1 using `StandardScaler` from scikit-learn.  
   - One-hot encoded columns (binary 0/1 values) were left unchanged, as scaling is unnecessary for binary features.  
4. **Combined scaled and non-scaled columns**  
   - Reconstructed the dataset by combining the scaled numeric columns with the original one-hot encoded columns.  
5. **Saved the result**  
   - Exported the scaled dataset to `Feature Scaling/healthcare_scaled.csv`, yielding a fully numeric, scaled dataset ready for machine learning.  

**Why it matters:**  
- Many machine learning algorithms (e.g., SVM, k-NN, neural networks) are sensitive to feature scales, as differing ranges can skew distance-based calculations or gradient updates.  
- `StandardScaler` ensures all numeric features contribute equally to the model by standardizing them to a common scale (mean = 0, std = 1).  
- Preserving one-hot encoded columns without scaling maintains their binary nature, which is appropriate for categorical features.  
- The scaled dataset is now optimized for a wide range of machine learning tasks, such as classification of medical conditions or regression on blood pressure values.

**📁 Output Path:**  
`Feature Scaling/healthcare_scaled.csv`

**📋 Output Includes:**  
- Standardized numeric columns (`Age`, `Cholesterol`, `Systolic`, `Diastolic`) with mean ≈ 0 and std ≈ 1.  
- Unchanged one-hot encoded columns (e.g., `Gender_female`, `Condition_Diabetes`, etc.).  
- No missing values, as imputation was handled in prior steps.  

✅ The scaled CSV file is now ready for:  
- **Machine Learning**: Training models like SVM, k-NN, or neural networks that require scaled features.  
- **Further Analysis**: Evaluating feature importance or correlations in a machine learning context.