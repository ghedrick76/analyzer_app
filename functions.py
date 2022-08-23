import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# input = input("Choose your stock symbol: ")

# data = yf.Ticker(input).history(period='5y')

# print(data.info())


# Create the indices
def dow_jones():
    data = pdr.get_data_yahoo("DJI", period="10y")
    return data

def nasdaq():
    data = pdr.get_data_yahoo("IXIC", period="10y")
    return data

def sp500():
    data = pdr.get_data_yahoo("GSPC", period="10y")
    return data



#Make a function for 20-day, 50-day, 100-day, 200-day moving averages, using the above to change the timeframe