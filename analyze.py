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
print("\nAdoptions by Year:\n", cats["Adoption_Clean"].dt.year.value_counts().sort_index())
print("\nMedian Length of Stay by Age Group:\n", cats.groupby("Age Group")["LOS_Days"].agg(["count", "median", "mean"]))

# 5. Chart 1: Demographics & Placement Overview
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

# 6. Chart 2: Adoption Timeline, Seasonality & Length of Stay by Age
fig, axes = plt.subplots(1, 3, figsize=(17, 5))

year_counts = cats["Adoption_Clean"].dropna().dt.year.astype(int).value_counts().sort_index()
sns.barplot(x=year_counts.index.astype(str), y=year_counts.values, ax=axes[0], color="#2b5c8f")
axes[0].set_title("Adoptions by Year (n = 538)")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Number of Adoptions")
axes[0].tick_params(axis="x", rotation=45)

month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_counts = cats["Adoption_Clean"].dropna().dt.month.value_counts().reindex(range(1, 13), fill_value=0)
sns.barplot(x=month_order, y=month_counts.values, ax=axes[1], color="#3b8ea5")
axes[1].set_title("Seasonality: Adoptions by Month")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Number of Adoptions")

los_age = (
    cats[cats["Age Group"].isin(["Kitten", "Juvenile", "Adult"])]
    .groupby("Age Group")["LOS_Days"]
    .median()
    .reindex(["Kitten", "Juvenile", "Adult"])
)
sns.barplot(x=los_age.index, y=los_age.values, ax=axes[2], palette=["#4c9f70", "#e08e45", "#c84b31"])
axes[2].set_title("Median Length of Stay by Age Group (n = 314)")
axes[2].set_xlabel("Age Group")
axes[2].set_ylabel("Median Days in Care")

plt.tight_layout()
plt.savefig("cat_adoption_timeline.png", dpi=150)
print("\nSaved charts to cat_overview_charts.png and cat_adoption_timeline.png")
