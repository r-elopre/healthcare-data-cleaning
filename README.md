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


**📋 Export Includes:**
- Missing values in `Age`, `Condition`, `Blood Pressure`, and `Cholesterol` were handled
- Text fields like `Patient Name`, `Gender`, `Condition`, `Email`, and `Phone Number` were cleaned and standardized
- `Visit Date` values were normalized into a consistent `datetime` format
- `Blood Pressure` values were split into numeric `Systolic` and `Diastolic` columns
- Duplicate rows based on `Patient Name`, `Age`, and `Visit Date` were removed

✅ The cleaned CSV file is now ready to be used in:
- **Step 2: Exploratory Data Analysis (EDA)**
- or any machine learning, statistical modeling, or visualization steps


## 🔎 Step 1.5: Exploratory Data Analysis (EDA)

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

## ✅ Step 2: Categorical Encoding

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
