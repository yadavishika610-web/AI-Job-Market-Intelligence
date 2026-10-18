
from pathlib import Path
import pandas as pd

data_folder = Path("data")
csv_files = list(data_folder.glob("*.csv"))

if not csv_files:
    print("No CSV file found in the data folder.")
else:
    file_path = csv_files[0]
    print("Dataset found:", file_path.name)

    df = pd.read_csv(file_path)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset shape (rows, columns):")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nMissing values per column:")
    print(df.isnull().sum())

    print("\nData types:")
    print(df.dtypes)

    
    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nTop 10 job titles:")
    print(df["title"].value_counts().head(10))

    print("\nTop 10 countries:")
    print(df["country_name"].value_counts().head(10))

    print("\nAI-related job counts:")
    print(df["is_ai_related"].value_counts(dropna=False))

    print("\nSalary summary:")
    print(df[["salary_min", "salary_max", "salary_avg"]].describe())

    
    # 10. Check duplicate job IDs
    print("\nDuplicate job IDs:")
    print(df["id"].duplicated().sum())

    # 11. Salary ranges by country and currency
    print("\nSalary statistics by country and currency:")
    print(
        df.groupby(["country_name", "currency"])[
            ["salary_min", "salary_max", "salary_avg"]
        ].agg(["count", "min", "median", "max"]).round(2)
    )

    # 12. Check suspicious salary values
    print("\nJobs with unusually high average salaries:")
    print(
        df[df["salary_avg"] > 500000][
            ["title", "company", "country_name", "currency",
             "salary_min", "salary_max", "salary_avg"]
        ].to_string(index=False)
    )

    # 13. Check salary values that are zero or negative
    print("\nNon-positive salary values:")
    print(
        df[
            (df["salary_min"] <= 0) |
            (df["salary_max"] <= 0) |
            (df["salary_avg"] <= 0)
        ][["title", "country_name", "currency",
           "salary_min", "salary_max", "salary_avg"]]
        .to_string(index=False)
    )

    