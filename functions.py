import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# input = input("Choose your stock symbol: ")

# data = yf.Ticker(input).history(period='5y')

# print(data.info())


# Create the indices
def dow_jones():
    data = pdr.get_data_yahoo("DJI", start="2011-01-01", end="2012-08-20")
    return data

def nasdaq():
    data = yf.Ticker("IXIC").history(period='10y')

    return data.info()

def sp500():
    data = yf.Ticker("GSPC").history(period='10y')

    return data.info()



#Make a function for 20-day, 50-day, 100-day, 200-day moving averages, using the above to change the timeframe