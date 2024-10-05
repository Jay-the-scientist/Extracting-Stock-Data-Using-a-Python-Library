# Extracting-Stock-Data-Using-a-Python-Library

## Project Overview

This project focuses on extracting stock data using the `yfinance` library in Python. The goal is to analyze stock share prices and dividends to identify any suspicious stock activity, which is crucial for data scientists working in hedge funds.

## Table of Contents
- Installation
- Usage
- Data Extraction
- Exercises
- License

## Installation

To get started, install the required libraries using pip:

```
pip install yfinance pandas matplotlib
```

## Usage

In your Python scripts or Jupyter notebooks, you can use the following import statements:

```
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
```

## Data Extraction
Using yfinance to Extract Stock Info
You can extract stock information by creating a Ticker object. For example, to extract data for Apple Inc. (AAPL):

```
apple = yf.Ticker("AAPL")
```

## Stock Info
To get detailed information about the stock:

```
apple_info = apple.info
print("Country:", apple_info['country'])
```

## Extracting Share Price Data
To get historical share price data:

```
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
```
![Apple Share Price](images/1-appleshareprice.png)

Then to reset the index of the table:
```
apple_share_price_data.reset_index(inplace=True)
print(apple_share_price_data.head())
```
![Apple Share Price with a reset index](images/2-appleshareprice.png)

## Plotting Share Prices
You can visualize the Open prices using:

```
apple_share_price_data.plot(x="Date", y="Open")
plt.show()
```
![Apple Share Price Plot](images/3-applesharepriceplot.png)


## Extracting Dividends
To get dividend data:

```
apple_dividends = apple.dividends
print(apple_dividends)
```
![Apple Dividends](images/4-appledividends.png)

## Plotting Dividends
Visualize dividends over time:

```
apple.dividends.plot()
plt.show()
```
![Apple Dividends Plot](images/5-appledividendsplot.png)

## Exercises
### Create a Ticker object for AMD (Advanced Micro Devices):

```
amd = yf.Ticker("AMD")
```

### Extract the country and sector for AMD:

```
amd_info = amd.info
print("Country:", amd_info['country'])  # 'United States'
print("Sector:", amd_info['sector'])    # 'Technology'
```

### Retrieve the historical stock data and find the volume traded on the first day:
You could run this code to show you the row that shows the 1st day of trading
```
x=amd.history(period = "max")
x.head(1)
```
![Amd 1st row of Trading History](images/6-amdhistory.png)

Alternatively, you could run this code to show you the 1st ten rows of trading
```
x=amd.history(period = "max")
x.head(1)
```
![Amd 10 rows of Trading History](images/7-amdhistory.png)

Also, you could specifcally determine the volume of the 1st day by calling it directly
```
x=amd.history(period = "max")
first_day_volume = x.head(1)['Volume']
print("Volume on first day:", first_day_volume)
```

![Amd calling the volume directly](images/8-amdhistory.png)

