import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

date1 = (2014, 12, 1)
date2 = (2016, 12, 1)

quotes = mpf.quotes_historical_yahoo_ohlc('601558.ss',date1,date2)
fig, ax = plt.subplots(facecolor=(0.5, 0.5, 0.5))
fig.subplots_adjust(bottom=0.2)
ax.xaxis_date()
ax.xaxis_date()
plt.xticks(rotation=45)
plt.title("股票代码:601558两年K线图")
plt.xlabel("时间")
plt.ylabel("股价(元)")
mpf.candlestick_ohlc(ax,quotes,width=1.2,colorup='r',colordown='green')
plt.grid(True)
