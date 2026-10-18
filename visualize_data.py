
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("output/cleaned_jobs.csv")

# Create a folder to store charts
chart_folder = Path("output/charts")
chart_folder.mkdir(parents=True, exist_ok=True)

# Chart 1: Job listings by country
country_counts = df["country_name"].value_counts()

plt.figure(figsize=(8, 5))
country_counts.plot(kind="bar")
plt.title("Job Listings by Country")
plt.xlabel("Country")
plt.ylabel("Number of Job Listings")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(chart_folder / "jobs_by_country.png", dpi=300)
plt.show()
plt.close()

# Chart 2: AI-related vs non-AI-related jobs
ai_counts = df["is_ai_related"].map({
    True: "AI-related",
    False: "Non-AI-related"
}).value_counts()

plt.figure(figsize=(7, 5))
ai_counts.plot(kind="bar")
plt.title("AI-Related vs Non-AI-Related Jobs")
plt.xlabel("Job Type")
plt.ylabel("Number of Job Listings")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(chart_folder / "ai_job_comparison.png", dpi=300)
plt.show()
plt.close()

# Chart 3: Top 10 job categories
category_counts = df["category"].value_counts().head(10)

plt.figure(figsize=(10, 6))
category_counts.sort_values().plot(kind="barh")
plt.title("Top 10 Job Categories")
plt.xlabel("Number of Job Listings")
plt.ylabel("Job Category")
plt.tight_layout()
plt.savefig(chart_folder / "top_job_categories.png", dpi=300)
plt.show()
plt.close()

print("All three charts created successfully!")
print("Charts saved in:", chart_folder)


# Chart 4: AI-related job percentage by country

ai_country = df.groupby("country_name").agg(
    total_jobs=("id", "count"),
    ai_jobs=("is_ai_related", "sum")
)

ai_country["ai_percentage"] = (
    ai_country["ai_jobs"] / ai_country["total_jobs"] * 100
)

ai_country = ai_country.sort_values("ai_percentage")

plt.figure(figsize=(8, 5))

bars = plt.barh(
    ai_country.index,
    ai_country["ai_percentage"]
)

plt.bar_label(bars, fmt="%.1f%%", padding=4)
plt.title("Percentage of AI-Related Job Listings by Country")
plt.xlabel("AI-Related Listings (%)")
plt.ylabel("Country")
plt.xlim(0, 100)
plt.tight_layout()

plt.savefig(
    chart_folder / "ai_jobs_by_country.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()

print("AI country comparison chart saved successfully!")

# Chart 5: Salary Distribution by Country
plt.figure(figsize=(9, 5))

countries = df["country_name"].dropna().unique()

salary_data = [
    df.loc[
        (df["country_name"] == country) & (df["salary_avg"] > 0),
        "salary_avg"
    ].dropna()
    for country in countries
]

plt.boxplot(salary_data, tick_labels=countries)

plt.title("Salary Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Average Salary (Local Currency)")
plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig(
    chart_folder / "salary_distribution_by_country.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()

print("Salary distribution chart saved successfully!")

# Chart 6: Job Listings Over Time

df["created_date"] = pd.to_datetime(
    df["created_date"], errors="coerce"
)

monthly_jobs = (
    df.dropna(subset=["created_date"])
    .groupby(df["created_date"].dt.to_period("M"))
    .size()
)

monthly_jobs.index = monthly_jobs.index.astype(str)

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_jobs.index,
    monthly_jobs.values,
    marker="o"
)

plt.title("Job Listings Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Job Listings")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    chart_folder / "job_listings_over_time.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()

print("Job listings over time chart saved successfully!")