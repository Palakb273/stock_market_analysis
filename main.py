from mysqlboilerplate import run_query
ticker=input("enter stock ticker:").upper()
latest_date_result=run_query(f"""SELECT MAX(STOCK_KEY) FROM stock_data""")
if not latest_date_result or latest_date_result[0][0] is None:
    print("No data found in database")
    exit()
latest_date=latest_date_result[0][0]
data_result=run_query(f"""SELECT close,sma20,sma50,trade_signal FROM stock_data WHERE stock_key='{latest_date}'""")
if not data_result:
    print(f"No detailed data found for {ticker} on {latest_date}")
    exit()
last_close,sma20,sma50,signal=data_result[0]
print(f"stock analysis for {ticker} on {latest_date}")
print(f"last closing price: {last_close}")
print(f"""SMA20:{sma20 if sma20 is not None else "N/A"}""")
print(f"""SMA50:{sma50 if sma50 is not None else "N/A"}""")
print(f"Last signal:{signal}")
