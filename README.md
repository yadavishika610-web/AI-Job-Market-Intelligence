# 📊 AI Job Market Intelligence Platform

An interactive data analytics dashboard for exploring job listings, AI-related employment opportunities, salary patterns, and job-market trends across countries.

## 🚀 Project Overview

The **AI Job Market Intelligence Platform** transforms raw job-listing data into useful insights through Python-based data cleaning, exploratory analysis, visualization, and an interactive Streamlit dashboard.

The current dataset contains **1,696 job listings** across India, the United Kingdom, and the United States.

## ✨ Key Features

- **Interactive dashboard:** Explore job-market data through a professional interface.
- **KPI cards:** View total job listings, AI-related jobs, AI job share, and countries covered.
- **Country filters:** Focus on selected countries.
- **Category filters:** Explore specific job categories.
- **AI job filtering:** Separate AI-related listings from non-AI listings.
- **Market visualizations:** Analyze country-level listings, popular job categories, AI-related listings, and salary distributions.
- **Job search:** Search listings by job title or company.
- **Data cleaning:** Handle missing values, inconsistent text, dates, and salary data.
- **Exploratory analysis:** Examine dataset characteristics and identify patterns.

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Pandas** — Data cleaning and analysis
- **Matplotlib** — Data visualization
- **Streamlit** — Interactive dashboard
- **Git and GitHub** — Version control and project hosting

## 📁 Project Structure

```text
AI-Job-Market-Intelligence/
├── data/
│   └── ai_job_market_dataset.csv
├── output/
│   ├── cleaned_jobs.csv
│   └── charts/
├── app.py
├── app_backup.py
├── inspect_data.py
├── clean_data.py
├── analyze_data.py
├── visualize_data.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Job-Market-Intelligence
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the environment's Python executable directly without activating it.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Prepare the dataset

Make sure the original dataset is available at:

```text
data/ai_job_market_dataset.csv
```

Run the cleaning script:

```bash
python clean_data.py
```

This should generate `output/cleaned_jobs.csv`.

### 5. Launch the dashboard

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, typically `http://localhost:8501`.

## 📈 Dashboard Insights

The dashboard helps users explore:

- How job listings are distributed across countries.
- Which job categories have the most listings.
- The proportion of AI-related job listings in the selected data.
- Median listed salary patterns by country.
- Individual job listings matching selected filters and search terms.

## 📊 Visualizations

The analysis scripts generate charts covering:

1. Job listings by country.
2. AI-related versus non-AI job listings.
3. Top job categories.
4. AI-related job percentage by country.
5. Salary distribution by country.
6. Job listings over time.

## ⚠️ Data Limitations

- Findings reflect the available dataset, not the entire job market.
- AI-related job percentages describe this dataset and should not be interpreted as national hiring rates.
- Salary values may use different currencies and pay periods, so cross-country comparisons require caution.
- Missing values and dataset-specific collection methods can affect the results.

## 🔮 Future Improvements

- Integrate SQL or PostgreSQL for structured data storage and querying.
- Add more advanced salary and job-trend analytics.
- Deploy the dashboard online.
- Automate data updates from a reliable job-data source.
- Add further interactive filters and analytical features.

## 👩‍💻 Author

**Ishika Yadav**

B.Tech — Artificial Intelligence and Data Science

---

*Built as a practical data analytics project to explore job-market patterns and AI-related employment opportunities.*