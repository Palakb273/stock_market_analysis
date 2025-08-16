import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
file_path="C:/Users/palak/OneDrive/Desktop/stocks/stock_analysis_results.xlsx"
output_dir="C:/Users/palak/OneDrive/Desktop/stocks/visuals"
os.makedirs(output_dir,exist_ok=True)
df=pd.read_excel(file_path,parse_dates=["Date"])
df.set_index("Date",inplace=True)
buy_price=[]
sell_price=[]
position=False
for i in range(len(df)):
    if df["SMA20"].iloc[i]>df["SMA50"].iloc[i]:
        if position==False:
            buy_price.append(df["Close_AAPL"].iloc[i])
            sell_price.append(None)
            position=True
        else:
            buy_price.append(None)
            sell_price.append(None)
    elif df["SMA20"].iloc[i]<df["SMA50"].iloc[i]:
        if position==True:
            buy_price.append(None)
            sell_price.append(df["Close_AAPL"].iloc[i])
            position=False
        else:
            buy_price.append(None)
            sell_price.append(None)
    else:
        buy_price.append(None)
        sell_price.append(None)
df["Buy_signal"]=buy_price
df["Sell_signal"]=sell_price
plt.figure(figsize=(14,7))
sns.set_style("whitegrid")
plt.plot(df.index,df["Close_AAPL"],label="Close Price",color="blue",alpha=0.6)
plt.plot(df.index,df["SMA20"],label="SMA20",color="red",linewidth=1.5)
plt.plot(df.index,df["SMA50"],label="SMA50",color="green",linewidth=1.5)
plt.scatter(df.index,df["Buy_signal"],label="Buy Signal",marker="^",color="green",s=150,edgecolors="black",alpha=0.9)
plt.scatter(df.index,df["Sell_signal"],label="Sell Signal",marker="v",color="green",s=150,edgecolors="black",alpha=0.9)
plt.title("AAPL Price with SMA20 & SMA50 and Buy/Sell Signals",fontsize=16)
plt.xlabel("Date")
plt.ylabel("Price(USD)")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir,"aapl_chart.png"),dpi=300)
plt.show()

