import pandas as pd
file_path="C:/Users/palak/OneDrive/Desktop/stocks/aapl_processedfinal.xlsx"
df=pd.read_excel(file_path)
df["Date"]=pd.to_datetime(df["Date"]).dt.date
df["Signal"]=0
df.loc[df["SMA20"]>df["SMA50"],"Signal"]=1
df.loc[df["SMA20"]<df["SMA50"],"Signal"]=-1
up_days=(df["Daily_returns"]>0).sum()
down_days=(df["Daily_returns"]<0).sum()
print(f"UP days:{up_days}")
print(f"DOWn days:{down_days}")
highest_price=df["Close_AAPL"].max()
lowest_price=df["Close_AAPL"].min()
print(f"Highest price:{highest_price}")
print(f"Lowest price: {lowest_price}")
df["cumulative_Max"]=df["Close_AAPL"].cummax()
df["Drawdown"]=(df["Close_AAPL"]-df["cumulative_Max"])/df["cumulative_Max"]
max_drawdown=df["Drawdown"].min()
print(f"Max Drawdown: {max_drawdown:.2%}")
df.to_excel("C:/Users/palak/OneDrive/Desktop/stocks/stock_analysis_results.xlsx")
print("saved")
