# app/dashboard.py

# -------------------------
# Dependencies
# -------------------------
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv
import os

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# -------------------------
# Robust data loader
# -------------------------
@st.cache_data
def get_data(table_name="dm_commodities", schema="public"):
    """
    Retrieves data from a table or view in PostgreSQL, automatically handling 
    table vs view and validating schema existence.
    """
    inspector = inspect(engine)
    
    # List all tables and views in the schema
    all_tables = inspector.get_table_names(schema=schema)
    all_views = inspector.get_view_names(schema=schema)
    
    if table_name in all_tables or table_name in all_views:
        query = f'SELECT * FROM "{schema}"."{table_name}"'
        df = pd.read_sql(query, engine)
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
        return df
    else:
        raise ValueError(
            f'"{table_name}" does not exist in schema "{schema}". '
            f'Available tables: {all_tables}, views: {all_views}'
        )

# -------------------------
# Streamlit page config
# -------------------------
st.set_page_config(
    page_title="Commodities Trading Dashboard",
    layout="wide"
)

st.title("📈 Commodities Trading Dashboard")

# -------------------------
# Load data
# -------------------------
try:
    df = get_data(table_name="dm_commodities", schema="public")
except ValueError as e:
    st.error(str(e))
    st.stop()

# -------------------------
# Sidebar filters
# -------------------------
st.sidebar.header("Filters")

commodities = df["commodity"].unique()
selected_commodity = st.sidebar.selectbox("Select Commodity", commodities)
filtered_df = df[df["commodity"] == selected_commodity]

# -------------------------
# KPIs
# -------------------------
latest_price = filtered_df.sort_values("date").iloc[-1]["closing_value"]
avg_price = filtered_df["closing_value"].mean()
max_price = filtered_df["closing_value"].max()

col1, col2, col3 = st.columns(3)
col1.metric("Latest Price", f"${latest_price:.2f}")
col2.metric("Average Price", f"${avg_price:.2f}")
col3.metric("Max Price", f"${max_price:.2f}")

# -------------------------
# Price chart
# -------------------------
st.subheader(f"{selected_commodity} Price Trend")
chart_data = filtered_df.set_index("date")["closing_value"]
st.line_chart(chart_data)

# -------------------------
# Moving averages
# -------------------------
st.subheader("Moving Averages")
filtered_df["MA_20"] = filtered_df["closing_value"].rolling(20).mean()
filtered_df["MA_50"] = filtered_df["closing_value"].rolling(50).mean()
ma_chart = filtered_df.set_index("date")[["closing_value", "MA_20", "MA_50"]]
st.line_chart(ma_chart)

# -------------------------
# Trading volume
# -------------------------
if "quantity" in filtered_df.columns:
    st.subheader("Trading Volume")
    volume_chart = filtered_df.set_index("date")["quantity"]
    st.bar_chart(volume_chart)

# -------------------------
# Data table
# -------------------------
st.subheader("Dataset Preview")
st.dataframe(filtered_df.sort_values("date", ascending=False))