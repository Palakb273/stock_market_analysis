import pandas as pd
import os
file_path=r"C:/Users/palak/OneDrive/Desktop/stocks/aapl_final.xlsx"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"CS not fount at{file_path}")
df=pd.read_excel(file_path,header=[0,1],index_col=0)
df.columns=['_'.join(col).strip()for col in df.columns.values]
df.index = pd.to_datetime(df.index,format="%d-%m-%Y",errors="coerce")
df.dropna(inplace=True)
close_col="Close_AAPL"
df["SMA20"]=df[close_col].rolling(window=20).mean()
df["SMA50"]=df[close_col].rolling(window=50).mean()
df["Daily_returns"]=df[close_col].pct_change()*100
df["volatility"]=df["Daily_returns"].rolling(window=20).std()
processed_path="C:/Users/palak/OneDrive/Desktop/stocks/aapl_processed.csv"
df.to_csv("processed_path")
print("data processed")
print(df.head(10))
#print(df.columns)
