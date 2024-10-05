pip install yfinance pandas matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#Using yfinance to Extract Stock Info You can extract stock information by creating a Ticker object. For example, to extract data for Apple Inc. (AAPL):
apple = yf.Ticker("AAPL")

#To get detailed information about the stock:
apple_info = apple.info
print("Country:", apple_info['country'])

#To get historical share price data:
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()

#Then to reset the index of the table:
apple_share_price_data.reset_index(inplace=True)
print(apple_share_price_data.head())

#You can visualize the Open prices using:
apple_share_price_data.plot(x="Date", y="Open")
plt.show()

#To get dividend data:
apple_dividends = apple.dividends
print(apple_dividends)

Visualize dividends over time:
apple.dividends.plot()
plt.show()

#Create a Ticker object for AMD (Advanced Micro Devices):
amd = yf.Ticker("AMD")

#Extract the country and sector for AMD:
amd_info = amd.info
print("Country:", amd_info['country'])  # 'United States'
print("Sector:", amd_info['sector'])    # 'Technology'

#Retrieve the historical stock data and find the volume traded on the first day:

#You could run this code to show you the row that shows the 1st day of trading
x=amd.history(period = "max")
x.head(1)

#Alternatively, you could run this code to show you the 1st ten rows of trading
x=amd.history(period = "max")
x.head(1)

#Also, you could specifcally determine the volume of the 1st day by calling it directly
x=amd.history(period = "max")
first_day_volume = x.head(1)['Volume']
print("Volume on first day:", first_day_volume)




