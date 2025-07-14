## 🧹 Step 1: Data Cleaning and Preprocessing

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
