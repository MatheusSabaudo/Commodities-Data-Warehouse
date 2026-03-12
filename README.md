---

# 📊 Commodities Data Warehouse

A complete **Commodities Data Warehouse** built with dbt, PostgreSQL, and a **Streamlit analytical dashboard** — designed for time-series market data ingestion, transformation, modeling, and visualization.

Project extracts raw financial data (commodity prices and trading activity), transforms it into analytical structures using dbt, and serves business metrics through an interactive dashboard created with AI-assisted development.

---

## 🚀 Features

### 📌 Data Engineering & Modeling

* Modular dbt project with **staging** and **mart** layers
* Source tables for commodities pricing and trading activity
* Cleaned, standardized staging models
* Analytical fact & dimension models for reporting

### 📈 AI-Powered Streamlit Dashboard

* Located in the `app/` folder
* Interactive commodity selector
* Real-time KPIs: latest, average, and max prices
* Price trend charts with moving averages (20 & 50 days)
* Trading volume charts
* Data table preview
* Built using **Streamlit** and assisted by AI for code generation and visualization

### 🛠 Stack

| Component       | Technology                     |
| --------------- | ------------------------------ |
| Data Warehouse  | PostgreSQL                     |
| Transformations | dbt                            |
| Dashboard       | Streamlit                      |
| Data Ingestion  | Python (yfinance + SQLAlchemy) |
| Deployment      | Docker (optional)              |

---

## 📁 Repository Structure

```
├── app/                        # Streamlit dashboard
├── dbt/                        # dbt project folder
│   ├── models/
│   │   ├── staging/           # staging models for raw source
│   │   └── marts/             # business logic models
│   └── schema.yml             # model documentation & tests
├── src/                        # Python ETL / ingestion scripts
├── profiles.yml                # dbt profiles config
├── docker-compose.yml          # for local stack orchestration
├── .env.example                # environment variables template
├── README.md                  # this file
└── LICENSE                    # MIT
```

---

## 🧱 Architecture Overview

1. **Source Data**

   * Commodity prices and trading data pulled from financial APIs
   * Raw data landed into Postgres source schemas

2. **dbt Transformations**

   * *Staging*: Clean & standardize raw tables
   * *Business Models*: Create analytics-ready structures

3. **AI-Powered Streamlit Dashboard**

   * Interactive analytical dashboard located in `app/`
   * Visualizes prices, trends, and trade volumes
   * Built using AI-assisted code generation and the Streamlit library

*(dbt ensures transformations follow best practices for Test, Document, & Lineage)*

---

## 🚀 Quickstart

### 🔧 Requirements

* Python 3.8+
* pip
* PostgreSQL running (or your dbt/warehouse connection working)
* Streamlit

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 💻 Local Setup

1. **Clone repository**

```bash
git clone https://github.com/MatheusSabaudo/Commodities-Data-Warehouse.git
cd Commodities-Data-Warehouse
```

2. **Copy env file**

```bash
cp .env.example .env
```

Fill in your DB credentials.

3. **Run dbt models**

```bash
cd dbt
dbt deps
dbt run
dbt test
```

4. **Run the Streamlit dashboard**

```bash
streamlit run app/dashboard.py
```

Open browser at `http://localhost:8501` (or your network URL).

---

## 📘 Documentation

All dbt models are documented in `schema.yml`.
Generate browsable documentation with:

```bash
dbt docs generate
dbt docs serve
```

---

## 🤝 Contribute

Contributions are welcome!
Open an issue or submit a pull request with improvements.

---

## 📝 License

This project is licensed under the MIT License — free and open source.

---