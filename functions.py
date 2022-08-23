import pandas as pd
import pandas_datareader as pdr
import yfinance as yf

input = input("Choose your stock symbol: ")

data = yf.Ticker(input).history(period='5y')

print(data.info())

def dow_jones():

    data = yf.Ticker("DJI").history(period='10y')

    return data.info()

dow_jones()

def nasdaq():
    
    data = yf.Ticker("IXIC").history(period='10y')

    return data.info()

nasdaq()

def sp500():
    
    data = yf.Ticker("GSPC").history(period='10y')

    return data.info()

sp500()


#Make a function for 20-day, 50-day, 100-day, 200-day moving averages, using the above to change the timeframe