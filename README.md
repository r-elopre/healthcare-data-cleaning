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
