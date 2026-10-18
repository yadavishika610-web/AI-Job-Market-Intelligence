
from pathlib import Path
import pandas as pd

# Load cleaned dataset
file_path = Path("output") / "cleaned_jobs.csv"
df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)

# 1. Job listings by country
print("\n--- Jobs by Country ---")
print(df["country_name"].value_counts())

# 2. AI-related vs non-AI-related jobs
print("\n--- AI-Related Jobs ---")
print(df["is_ai_related"].value_counts())

# 3. Most common job categories
print("\n--- Top 10 Job Categories ---")
print(df["category"].value_counts().head(10))

# 4. Most common job titles
print("\n--- Top 10 Job Titles ---")
print(df["title"].value_counts().head(10))

# 5. Average salary by country and currency
print("\n--- Median Salary by Country and Currency ---")
print(
    df.groupby(["country_name", "currency"])["salary_avg"]
    .median()
    .round(2)
)

# 6. Contract time distribution
print("\n--- Contract Time ---")
print(df["contract_time"].value_counts(dropna=False))

print("\nAnalysis complete!")


# AI-related job demand by country

ai_country = df.groupby("country_name").agg(
    total_jobs=("id", "count"),
    ai_jobs=("is_ai_related", "sum")
)

ai_country["non_ai_jobs"] = (
    ai_country["total_jobs"] - ai_country["ai_jobs"]
)

ai_country["ai_percentage"] = (
    ai_country["ai_jobs"] / ai_country["total_jobs"] * 100
).round(2)

print("\n--- AI Job Demand by Country ---")
print(ai_country.sort_values("ai_percentage", ascending=False))
