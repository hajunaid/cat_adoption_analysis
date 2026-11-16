import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset and drop empty template rows
df = pd.read_csv("data/Cat Spreadsheet for AA - Sheet1.csv")
cats = df[df["Name"].notna() | df["ID Number"].notna()].copy()

# 2. Clean dates and recalculate valid Length of Stay (in days)
cats["Intake_Clean"] = pd.to_datetime(cats["Intake Date"], errors="coerce")
cats["Adoption_Clean"] = pd.to_datetime(cats["Date of Adoption"], errors="coerce")
cats["LOS_Days"] = (cats["Adoption_Clean"] - cats["Intake_Clean"]).dt.days
cats.loc[(cats["LOS_Days"] < 0) | (cats["LOS_Days"] > 3650), "LOS_Days"] = pd.NA

# 3. Standardize minor spelling inconsistencies
cats["Spayed/Nuetered"] = cats["Spayed/Nuetered"].replace({"Nuetered": "Neutered"})
cats["Adoption Site"] = cats["Adoption Site"].str.strip().str.replace(r"\s*-\s*", " - ", regex=True)

# 4. Print summary metrics
print(f"Total Valid Cat Records: {len(cats)}")
print("\nAge Group Breakdown:\n", cats["Age Group"].value_counts())
print("\nPlacement Type Breakdown:\n", cats["Single or Double Adoption"].value_counts())
print("\nValid Length of Stay Summary (Days):\n", cats["LOS_Days"].dropna().describe())

# 5. Generate summary visualizations
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

age_counts = cats["Age Group"].value_counts()
sns.barplot(x=age_counts.index, y=age_counts.values, ax=axes[0], palette="Blues_d")
axes[0].set_title("Cats by Age Group")
axes[0].set_ylabel("Count")

color_counts = cats["Color"].value_counts().head(8)
sns.barplot(y=color_counts.index, x=color_counts.values, ax=axes[1], palette="viridis")
axes[1].set_title("Top 8 Coat Colors")
axes[1].set_xlabel("Count")

adopt_type = cats["Single or Double Adoption"].dropna().value_counts()
sns.barplot(x=adopt_type.index, y=adopt_type.values, ax=axes[2], palette="Set2")
axes[2].set_title("Adoption Placement Type")
axes[2].set_ylabel("Count")

plt.tight_layout()
plt.savefig("cat_overview_charts.png", dpi=150)
print("\nSaved summary chart to cat_overview_charts.png")
