import pandas as pd
import pandas_datareader as pdr
import yfinance as yf

input = input("Choose your stock symbol: ")

data = yf.Ticker(input).history(period='5y')

print(data.info())

#Make a function for 20-day, 50-day, 100-day, 200-day moving averages, using the above to change the timeframe