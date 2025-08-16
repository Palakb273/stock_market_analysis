# 📊 Stock Market Analysis & Alert System

A beginner-friendly data science project that analyzes stock price data, calculates moving averages, stores results in a MySQL database, and visualizes trends with charts.

---

## 🚀 Features
- Fetch stock data (Yahoo Finance or CSV input).
- Store historical data in **MySQL**.
- Calculate **SMA20** and **SMA50** (Simple Moving Averages).
- Generate basic **trading signals** (BUY / SELL).
- Visualize stock price with SMA lines.
- Query the latest analysis from the database using Python.

---

## 🗂 Project Structure
stock-market-analysis/
│── fetch_data.py # Fetch stock data
│── process_data.py # Calculate SMAs & signals
│── store_sql.py # Save results to MySQL
│── visualize.py # Generate charts
│── main.py # Run analysis for a stock
│── stock_chart.png # Example chart output
│── README.md # Project documentation


---

## ⚙️ Requirements
Install dependencies:
```bash
pip install yfinance pandas matplotlib mysql-connector-python



## ▶️ How to Run

Clone the repo:

git clone https://github.com/YOUR_USERNAME/stock-market-analysis.git
cd stock-market-analysis


Run scripts in order:

python fetch_data.py
python process_data.py
python store_sql.py
python visualize.py
python main.py


Example output:

Enter stock ticker: AAPL
Stock Analysis for AAPL on 2025-08-16
Last Closing Price: 215.32
SMA20: 210.45
SMA50: 198.72
Last Signal: BUY

📸 Example Visualization

Stock chart with SMA20 & SMA50 (saved as stock_chart.png):

🎯 Resume Value

Beginner Data Science Project

Shows knowledge of:

Python (Pandas, Matplotlib)

SQL integration

Financial indicators (Moving Averages)

Clean repo + README
