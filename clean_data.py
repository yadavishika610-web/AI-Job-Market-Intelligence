
from pathlib import Path
import pandas as pd

# Locate the dataset
data_folder = Path("data")
csv_files = list(data_folder.glob("*.csv"))

if not csv_files:
    print("No CSV file found in the data folder.")
else:
    file_path = csv_files[0]
    df = pd.read_csv(file_path)

    print("Original shape:", df.shape)

    # 1. Remove exact duplicate rows
    df = df.drop_duplicates()

    # 2. Clean whitespace in text columns
    text_columns = df.select_dtypes(
        include=["object", "str"]
    ).columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    # 3. Replace empty text with missing values
    df[text_columns] = df[text_columns].replace(
        "", pd.NA
    )

    # 4. Convert date columns
    df["created_date"] = pd.to_datetime(
        df["created_date"], errors="coerce"
    )

    # 5. Treat zero minimum salary as unknown
    # Preserve the original maximum and average salary.
    df.loc[df["salary_min"] <= 0, "salary_min"] = pd.NA

    # 6. Save the cleaned dataset
    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    output_path = output_folder / "cleaned_jobs.csv"
    df.to_csv(output_path, index=False)

    print("\nCleaning summary")
    print("Cleaned shape:", df.shape)
    print("Missing values after cleaning:")
    print(df.isnull().sum())

    print("\nCleaned dataset saved to:", output_path)
