# ✈️ Flight Data Analysis Pipeline (ETL & Analytics)

End-to-end data engineering pipeline for extracting, transforming, and analyzing real-world flight data from European airports using the AeroDataBox API.

This project demonstrates production-style ETL design, relational data modeling, and analytical processing using Python.

---

## 🏗 Architecture

API (AeroDataBox)
   ↓
Extraction (requests + validation)
   ↓
Transformation (cleaning + normalization + time parsing)
   ↓
SQLite (relational storage, indexed)
   ↓
Pandas (analytics)
   ↓
Matplotlib (visualization)

---

## 🚀 Key Features

### 🔄 ETL Pipeline (Core System)
Extract
- REST API integration (AeroDataBox via RapidAPI)
- Multi-airport data ingestion (BER, STR, CDG, etc.)
- Config-driven execution (JSON-based pipeline configuration)
- Robust error handling for API/network failures

Transform

- JSON normalization into structured relational format
  - Timestamp decomposition into components:
    - year, month, day, hour, minute, second
- Airline and airport data normalization via reference tables
- Data validation and cleaning (null handling, type enforcement)

Load

- SQLite relational database
- Idempotent inserts (INSERT OR IGNORE)
- Referential integrity via foreign keys
- Indexed schema for query performance
- WAL mode enabled for concurrent-safe writes


### 🗄 Data Model
#### Tables:
airports
- airport_id (PK)
- iata_code (unique)
- name
- country

airlines
- airline_id (PK)
- name (unique)

flights
- flight_id (PK)
- airport_id (FK)
- airline_id (FK)
- departure/arrival timestamps
- decomposed time fields (Y/M/D/H/M/S)

Indexes on airport_id, airline_id for query performance
Foreign key constraints enforce referential integrity

---

### 📊 Analytics Capabilities
Using Pandas:
- Flight volume distribution by hour (traffic peaks)
- Airport activity ranking
- Airline frequency analysis
- Country-level traffic aggregation
---

### 📈 Data Visualization
- Hourly traffic histograms
- Airline activity comparison charts
- Airport throughput comparison

Built with Matplotlib.

---

### ⚙️ Engineering Practices
- Modular project structure (separation of ETL layers)
- Structured logging (file + console)
- Centralized configuration management
- Environment variable handling (.env)
- Defensive programming for API and parsing failures
- Reproducible pipeline execution
---

## 📁 Project Structure

project/
│
├── data/
│   ├── etl_rapid.db          # SQLite database
│   └── result_*.json         # Raw API responses
│
├── config/
│   ├── etl_config.json       # Pipeline configuration
│   └── logging_config.ini    # Logging setup
│
├── src/
│   ├── config_loader.py      # Config management
│   ├── db.py                 # DB connection & schema
│   ├── extract.py            # API extraction layer
│   ├── transform.py          # Data transformation logic
│   ├── load.py               # DB loading logic
│   ├── pipeline.py           # ETL orchestration
│   └── main.py               # Entry point
│
├── notebooks/
│   └── analysis.ipynb        # Exploratory data analysis
│
├── logs/
│   └── process.log           # Structured logs
│
├── .env.example              # Environment template
├── requirements.txt
└── README.md
---

## ⚙️ Installation

### 1. Clone repository
```bash
git clone https://github.com/vladsheben/air-traffic-pipeline.git
cd flight-data-pipeline
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
---

## 🔐 Environment Configuration

Create a .env file in the root directory:
```bash
RAPIDAPI_KEY=your_api_key_here
```
---

## ▶️ Run the ETL pipeline:
```bash
python src/main.py
```

Pipeline steps:

1. Load configuration
2. Fetch flight data from API
3. Transform and normalize dataset
4. Load into SQLite database
---

## 📊 Running Analysis

Launch Jupyter Notebook::
```bash
jupyter notebook notebooks/analysis.ipynb
```

Example insights:

- Peak flight activity hours
- Most active airports
- Airline dominance distribution
- Geographic traffic patterns
---

## 📈 Key Insights
- Flight activity peaks during morning and midday hours
- Major airports dominate traffic distribution
- Airline traffic follows a highly skewed distribution
- Strong temporal patterns in air traffic flow
---

## 🛠 Tech Stack
- Python 3.x
- Requests (API integration)
- SQLite (relational storage)
- Pandas (data processing)
- Matplotlib (visualization)
- python-dotenv (environment management)
- logging (observability)
---

## ⚠️ Limitations
- Fixed time window for API extraction
- No real-time streaming ingestion
- Limited historical dataset due to API constraints
---

## 🚀 Future Improvements
- Dynamic time-window ingestion (rolling ETL)
- Migration to PostgreSQL (production-grade DB)
- Orchestration with Airflow / Prefect
- Dashboard layer (Streamlit / Power BI)
- Incremental loading strategy (CDC-style approach)
- Containerization (Docker deployment)
---

## 📌 Project Purpose

This project demonstrates:

- End-to-end ETL pipeline design
- API-driven data ingestion
- Relational data modeling
- Data transformation engineering
- Analytical processing in Python
- Production-style code structure
---
