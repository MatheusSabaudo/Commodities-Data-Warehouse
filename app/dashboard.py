# Dependencies
import yfinance as yf
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Streamlit page settings
st.set_page_config(
    page_title="Commodities Trading Dashboard",
    layout="wide"
)

st.title("📈 Commodities Trading Dashboard")

# Database config
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)


# Load data
@st.cache_data
def get_data():
    query = """
        SELECT *
        FROM public.dm_commodities;
    """
    df = pd.read_sql(query, engine)
    df['date'] = pd.to_datetime(df['date'])
    return df


df = get_data()


# Sidebar filters
st.sidebar.header("Filters")

commodities = df["commodity"].unique()

selected_commodity = st.sidebar.selectbox(
    "Select Commodity",
    commodities
)

filtered_df = df[df["commodity"] == selected_commodity]


# KPIs
latest_price = filtered_df.sort_values("date").iloc[-1]["closing_value"]
avg_price = filtered_df["closing_value"].mean()
max_price = filtered_df["closing_value"].max()

col1, col2, col3 = st.columns(3)

col1.metric("Latest Price", f"${latest_price:.2f}")
col2.metric("Average Price", f"${avg_price:.2f}")
col3.metric("Max Price", f"${max_price:.2f}")


# Price chart
st.subheader(f"{selected_commodity} Price Trend")

chart_data = filtered_df.set_index("date")["closing_value"]

st.line_chart(chart_data)


# Moving averages
st.subheader("Moving Averages")

filtered_df["MA_20"] = filtered_df["closing_value"].rolling(20).mean()
filtered_df["MA_50"] = filtered_df["closing_value"].rolling(50).mean()

ma_chart = filtered_df.set_index("date")[["closing_value", "MA_20", "MA_50"]]

st.line_chart(ma_chart)


# Quantity traded
if "quantity" in filtered_df.columns:
    st.subheader("Trading Volume")

    volume_chart = filtered_df.set_index("date")["quantity"]
    st.bar_chart(volume_chart)


# Data table
st.subheader("Dataset Preview")

st.dataframe(filtered_df.sort_values("date", ascending=False))