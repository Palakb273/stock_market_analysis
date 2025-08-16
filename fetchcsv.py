import yfinance as yf
data=yf.download("AAPL",start="2015-01-01",end="2025-08-08")
data.to_csv("aapl.csv")
print("downloaded")
