from mysqlboilerplate import run_query
import pandas as pd
df=pd.read_excel("C:/Users/palak/OneDrive/Desktop/stocks/stock_analysis_results.xlsx")
for row in df.itertuples(index=False):
    date_str=pd.to_datetime(row.Date).strftime("%Y-%m-%d")
    query=f"""
INSERT INTO stock_data (stock_key,open,high,low,close,volume,sma20,sma50,trade_signal)
VALUES('{date_str}',{row.Open_AAPL},{row.High_AAPL},{row.Low_AAPL},{row.Close_AAPL},{row.Volume_AAPL},{row.SMA20 if pd.notna(row.SMA20)else "NULL"},{row.SMA50 if pd.notna(row.SMA50)else "NULL"},'{row.Signal}')"""
    run_query(query)
print("inserted")
