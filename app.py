
import streamlit as st
import pandas as pd
from pathlib import Path

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="AI Job Market Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- PROFESSIONAL LIGHT THEME ----------------
st.markdown("""
<style>
    .stApp {
        background-color: #F5F7FB;
        color: #172B4D;
    }

    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E4E9F2;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }

    h1, h2, h3 {
        color: #172B4D !important;
    }

    .hero {
        background: linear-gradient(115deg, #173B70, #2463A6);
        padding: 28px 30px;
        border-radius: 16px;
        margin-bottom: 24px;
        color: white;
    }

    .hero h1 {
        color: white !important;
        font-size: 30px;
        margin: 0 0 8px 0;
    }

    .hero p {
        color: #E4EEFF;
        margin: 0;
        font-size: 15px;
    }

    .section-label {
        color: #64748B;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }

    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E4E9F2;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(23, 43, 77, 0.04);
    }

    div[data-testid="stMetricLabel"] {
        color: #64748B;
        font-size: 14px;
    }

    div[data-testid="stMetricValue"] {
        color: #173B70;
        font-weight: 700;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #E4E9F2;
        border-radius: 10px;
        overflow: hidden;
    }

    .info-note {
        color: #64748B;
        font-size: 12px;
    }

    div[data-testid="stVerticalBlock"] > div:has(> div > .section-label) {
        margin-bottom: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
DATA_PATH = Path(__file__).parent / "output" / "cleaned_jobs.csv"

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)

    data["is_ai_related"] = (
        data["is_ai_related"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({"true": True, "false": False})
    )

    for column in ["country_name", "category", "title", "company"]:
        if column in data.columns:
            data[column] = data[column].fillna("Unknown").astype(str)

    if "salary_avg" in data.columns:
        data["salary_avg"] = pd.to_numeric(
            data["salary_avg"], errors="coerce"
        )

    return data

try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "Cleaned dataset not found. Please check that "
        "'output/cleaned_jobs.csv' exists in your project folder."
    )
    st.stop()

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>AI Job Market Intelligence</h1>
    <p>
        Explore job opportunities, AI hiring patterns, salary distributions,
        and job-market trends across countries.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.markdown("## Market Filters")
st.sidebar.caption("Customize the job listings shown on your dashboard.")
st.sidebar.divider()

countries = sorted(
    df["country_name"].dropna().unique().tolist()
)
categories = sorted(
    df["category"].dropna().unique().tolist()
)

selected_countries = st.sidebar.multiselect(
    "Countries",
    options=countries,
    default=countries
)

selected_categories = st.sidebar.multiselect(
    "Job categories",
    options=categories,
    default=categories
)

ai_filter = st.sidebar.selectbox(
    "AI-related status",
    ["All jobs", "AI-related only", "Non-AI only"]
)

if st.sidebar.button("Reset filters", use_container_width=True):
    st.rerun()

st.sidebar.divider()
st.sidebar.caption("AI Job Market Intelligence | Portfolio Project")

# ---------------- APPLY FILTERS ----------------
filtered_df = df[
    df["country_name"].isin(selected_countries)
    & df["category"].isin(selected_categories)
].copy()

if ai_filter == "AI-related only":
    filtered_df = filtered_df[
        filtered_df["is_ai_related"] == True
    ]
elif ai_filter == "Non-AI only":
    filtered_df = filtered_df[
        filtered_df["is_ai_related"] == False
    ]

# ---------------- KPI CARDS ----------------
st.markdown('<p class="section-label">Market Overview</p>',
            unsafe_allow_html=True)

total_jobs = len(filtered_df)
ai_jobs = int((filtered_df["is_ai_related"] == True).sum())
ai_share = (ai_jobs / total_jobs * 100) if total_jobs else 0
country_count = filtered_df["country_name"].nunique()

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Job Listings", f"{total_jobs:,}")
k2.metric("AI-Related Jobs", f"{ai_jobs:,}")
k3.metric("AI Job Share", f"{ai_share:.1f}%")
k4.metric("Countries Covered", f"{country_count:,}")

st.caption(
    "All metrics reflect your current country, category, and AI-status filters."
)

st.divider()

# ---------------- CHARTS ----------------
st.markdown('<p class="section-label">Market Insights</p>',
            unsafe_allow_html=True)

left, right = st.columns(2, gap="large")

with left:
    st.subheader("Job Listings by Country")
    country_counts = (
        filtered_df["country_name"]
        .value_counts()
        .sort_values(ascending=True)
    )

    if not country_counts.empty:
        st.bar_chart(country_counts, color="#3478C8")
    else:
        st.info("No listings match the selected filters.")

with right:
    st.subheader("Top 10 Job Categories")
    category_counts = (
        filtered_df["category"]
        .value_counts()
        .head(10)
        .sort_values(ascending=True)
    )

    if not category_counts.empty:
        st.bar_chart(category_counts, color="#16A6A1")
    else:
        st.info("No category data available.")

left, right = st.columns(2, gap="large")

with left:
    st.subheader("AI vs Non-AI Listings")
    ai_labels = filtered_df["is_ai_related"].map({
        True: "AI-related",
        False: "Non-AI"
    }).fillna("Unknown")

    ai_counts = ai_labels.value_counts().reindex(
        ["AI-related", "Non-AI", "Unknown"],
        fill_value=0
    )
    ai_counts = ai_counts[ai_counts > 0]

    if not ai_counts.empty:
        st.bar_chart(ai_counts, color="#7C6DD8")
    else:
        st.info("No AI-status data available.")

with right:
    st.subheader("Median Listed Salary by Country")

    if "salary_avg" in filtered_df.columns:
        salary_df = filtered_df[
            filtered_df["salary_avg"].notna()
            & (filtered_df["salary_avg"] > 0)
        ].copy()

        if not salary_df.empty:
            salary_by_country = (
                salary_df.groupby("country_name")["salary_avg"]
                .median()
                .sort_values(ascending=True)
            )
            st.bar_chart(salary_by_country, color="#E69A36")
            st.caption(
                "Values use local currencies (INR, GBP, USD). "
                "They are not directly comparable across countries."
            )
        else:
            st.info("No salary data available for these filters.")
    else:
        st.info("Salary data is not available.")

st.divider()

# ---------------- JOB LISTINGS EXPLORER ----------------
st.markdown('<p class="section-label">Explore Opportunities</p>',
            unsafe_allow_html=True)
st.header("Job Listings Explorer")
st.write(
    "Search job titles or companies and inspect the matching listings."
)

search_text = st.text_input(
    "Search jobs",
    placeholder="e.g. Machine Learning Engineer or company name"
)

display_df = filtered_df.copy()

if search_text.strip():
    search_mask = (
        display_df["title"].str.contains(
            search_text.strip(), case=False, regex=False, na=False
        )
        | display_df["company"].str.contains(
            search_text.strip(), case=False, regex=False, na=False
        )
    )
    display_df = display_df[search_mask]

display_columns = [
    column for column in [
        "title",
        "company",
        "location",
        "country_name",
        "category",
        "contract_time",
        "salary_avg",
        "currency",
        "is_ai_related"
    ]
    if column in display_df.columns
]

st.caption(
    f"Showing {len(display_df):,} listings "
    f"out of {len(filtered_df):,} filtered listings."
)

st.dataframe(
    display_df[display_columns],
    width="stretch",
    hide_index=True
)

# ---------------- FOOTER ----------------
st.divider()
st.caption(
    "AI Job Market Intelligence Platform | "
    "Built with Python, Pandas, and Streamlit"
)
