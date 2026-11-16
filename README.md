# cat_adoption_analysis
Analysis of adoption data from AA

# 🐱 Cat Adoption & Shelter Outcomes Analysis

An exploratory data analysis (EDA) project examining intake, medical screening, foster-to-adopt workflows, and placement outcomes for **602 rescued cats** (spanning 2007–2025).

## 📊 Dataset Overview

* **Source File:** `data/Cat Spreadsheet for AA - Sheet1.csv`
* **Total Valid Cat Records:** 602 (after filtering out 158 blank spreadsheet template rows)
* **Adoption Date Range:** March 2011 – August 2025
* **Key Insights:**
  * **Kitten-Heavy Intake:** 69.6% of records are Kittens ($n=419$), followed by Juveniles ($n=111$) and Adults ($n=71$).
  * **High Pair Adoption Rate:** Nearly half of all placements (**48.5%**, $n=283$) were **Double Adoptions**, alongside 9 Triple adoptions.
  * **Shelter Stay:** Among records with valid intake and adoption dates ($n=338$), the median length of stay before adoption is **82.5 days**.

## 🗂️ Data Dictionary

| Column | Description |
| :--- | :--- |
| `Name` & `ID Number` | Cat name and unique shelter tracking ID (`YY-###` format) |
| `Color`, `Sex`, `Breed` | Physical traits and coat color/pattern |
| `Age Group` & `Estimated Age` | Life stage (`Kitten`, `Juvenile`, `Adult`, `Senior`) and estimated age in weeks/months |
| `Spayed/Nuetered` | Sterilization status (`Spayed`, `Nuetered`, `No`) |
| `Rabies`, `FVRCP 1`, `FVPCP 2` | Vaccination completion flags (`Yes` / `No`) |
| `FELV/FIV Screen` & `FIV Neg/Pos` | Viral screening completion and test result (`Negative`, `Positive`, `FELV positive`) |
| `Intake Date` & `Date of Adoption` | Dates of shelter entry and final placement |
| `Single or Double Adoption` | Whether the cat was adopted alone (`Single`) or with companions (`Double`, `Triple`) |
| `Adoption Site` & `Adoption Zipcode` | Partner retail location or foster home and adopter ZIP code |
| `Length of Stay` | Days between intake and adoption (cleaned in `analyze.py` to remove Excel serial date artifacts) |

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/cat-adoption-analysis.git
   cd cat-adoption-analysis
