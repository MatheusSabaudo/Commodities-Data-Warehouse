---

# 📊 Commodities Data Warehouse

A complete **Commodities Data Warehouse** built with dbt, PostgreSQL, and a Streamlit analytical dashboard — designed for time‑series market data ingestion, transformation, modeling, and visualization.

Project extracts raw financial data (e.g., commodity prices and trading activity), transforms it into analytical structures using dbt, and serves business metrics through an interactive dashboard.

---

## 🚀 Features

### 📌 Data Engineering & Modeling

* Modular dbt project with staging and mart layers
* Source tables for commodities pricing and trading activity
* Cleaned, standardized staging models
* Analytical fact & dimension models for reporting

### 📈 Streamlit Dashboard

* Commodity selector and performance KPIs
* Time‑series price charts and moving averages
* Volume & trading analytics
* Table viewer for raw and transformed data

### 🛠 Stack

| Component       | Technology                     |
| --------------- | ------------------------------ |
| Data Warehouse  | PostgreSQL                     |
| Transformations | dbt                            |
| Dashboard       | Streamlit                      |
| Data Ingestion  | Python (yfinance + SQLAlchemy) |
| Deployment      | Docker                         |

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
├── docker‑compose.yml          # for local stack orchestration
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
   * *Business Models*: Create analytics‑ready structures

3. **Dashboard**

   * Interactive analytical dashboard with Streamlit
   * Visualize prices, trends, and trade volumes

*(dbt ensures transformations follow best practices for Test, Document, & Lineage)*

---

## 🚀 Quickstart

### 🔧 Requirements

Make sure you have installed:

* Docker & Docker Compose
* dbt CLI
* Python 3.8+

### 💻 Local Setup

1. **Clone repository**

   ```sh
   git clone https://github.com/MatheusSabaudo/Commodities-Data-Warehouse.git
   cd Commodities-Data-Warehouse
   ```

2. **Copy env file**

   ```sh
   cp .env.example .env
   ```

   Fill in your DB and API credentials.

3. **Run with Docker**

   ```sh
   docker-compose up -d
   ```

4. **Initialize dbt**

   ```sh
   dbt deps
   dbt seed
   dbt run
   dbt test
   ```

5. **Start dashboard**

   ```sh
   streamlit run app/main.py
   ```

---

## 📊 Dashboard Features

* Select commodities to analyze trends 📉
* Real‑time moving average overlays
* Primary KPIs: latest, average, max prices
* Daily or historical filtering
* Volume charts from trading activity

---

## 📘 Documentation

All dbt models are documented in `schema.yml`.
Add model descriptions and column definitions to build a rich data catalog.

You can generate browsable documentation with:

```sh
dbt docs generate
dbt docs serve
```

---

## 🤝 Contribute

Contributions are welcome!
To contribute, open an issue or submit a pull request with improvements.

---

## 📝 License

This project is licensed under the MIT License — free and open source.

---