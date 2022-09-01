#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import required libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Import CSV files for all tickers
nyse = pd.read_csv("nyse.csv")['ACT Symbol']
nasdaq = pd.read_csv("nasdaq.csv")['Symbol']

# Combine the two datasets
tickers = pd.concat([nyse,nasdaq]).drop_duplicates().reset_index(drop=True)


# In[2]:


# Create the Streamlit instance
st.title('Finance Dashboard')
st.header('Stock Analyzer')


# Creates the dropdown boxes for the user to select their tickers and desired functions
dropdown = st.multiselect('Select equities to chart', tickers)

dropdown2 = st.multiselect('Calculate volatility ', tickers)

dropdown3 = st.multiselect('Calculate the beta of any two tickers', tickers)

dropdown4 = st.multiselect("Plot Moving Averages", tickers)
window_size = [20, 50, 100, 200]


# Sets the start and end dates
start = st.date_input('Start', value = pd.to_datetime('2012-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))


# In[3]:


# Build functions for user actions

# Graphs the ticker
def returns(df):
    returns = df
    return returns

# Calculates volatility of a ticker
def calc_vol(df):
    df = df.pct_change()
    volatility = df.std()*252**.5
    return volatility

# Calculates beta of a ticker against whatever ticker is in the first position
def calc_beta(df):
    covariance = df.cov()
    variance = df[dropdown3[1]].var()
    covariance = covariance.loc[dropdown3[0], dropdown3[1]]/variance
    return covariance

# Calculates the moving averages of each ticker, based on user's choice of timeframe
def sma20(df):
    rolling = df.rolling(window=20).mean()
    return rolling
def sma50(df):
    rolling = df.rolling(window=50).mean()
    return rolling
def sma100(df):
    rolling = df.rolling(window=100).mean()
    return rolling
def sma200(df):
    rolling = df.rolling(window=200).mean()
    return rolling



# Conditionals for each desired function
if len(dropdown) > 0:
    df = returns(yf.download(dropdown,start,end)['Close'])
    st.header('Graph of {}'.format(dropdown))
    st.line_chart(df)
    
if len(dropdown2) > 0:
    df = calc_vol(yf.download(dropdown2,start,end)['Close'])
    st.header('Volatility of {}'.format(dropdown2))
    df
    
if len(dropdown3) > 1:
    df = calc_beta(yf.download(dropdown3,start,end)['Close'])
    st.header("The beta of {} compared against {} is".format(dropdown3[1], dropdown3[0]))
    st.header(df)
    
    
if len(dropdown4) > 0:
    window_size = st.multiselect("Choose your window size", window_size)
    if 20 in window_size:
            df = sma20(yf.download(dropdown4,start,end)['Close'])
            st.header('20-day Moving Average of {}'.format(dropdown4))
            st.line_chart(df)
    if 50 in window_size:
            df = sma50(yf.download(dropdown4,start,end)['Close'])
            st.header('50 day Moving Average of {}'.format(dropdown4))
            st.line_chart(df)
    if 100 in window_size:
            df = sma100(yf.download(dropdown4,start,end)['Close'])
            st.header('100 day Moving Average of {}'.format(dropdown4))
            st.line_chart(df)
    if 200 in window_size:
            df = sma200(yf.download(dropdown4,start,end)['Close'])
            st.header('200 day Moving Average of {}'.format(dropdown4))
            st.line_chart(df)


# In[4]:


# Start of stock Balance Sheet Form
with st.form(key = "form2", clear_on_submit=True):
    st.header("Company Financial Performance")
    #Creates user input field for stock ticker
    user_input = st.text_input("Enter stock ticker i.e. AMZN, TSLA, AAPL, etc.")
    
    # Takes user input and gets stock ticker
    ticker_choice = yf.Ticker(user_input)
    
    filter_options = ['Annual','Quarterly']
    
    result_filter = st.multiselect("Report Type",filter_options)
    
    # Shows stock quarterly balance sheet
    def quarterly_data():
        st.subheader(user_input + """ Quarterly Balance Sheet""")
        stock_qtrly_balance = (ticker_choice.quarterly_balance_sheet)
        stock_qtrly_balance
    
    # Shows stock annual balance sheet
    def annual_data():
        st.subheader(user_input + """ Annual Balance Sheet""")
        stock_annual_balance = (ticker_choice.balance_sheet)
        stock_annual_balance

    # Generates button that executes 'quarterly_data()' and 'annual_data()' on user click 
    user_submit = st.form_submit_button(label = "Submit")
    
    if user_submit:
        if 'Annual' in result_filter:
            annual_data()
    
    if user_submit:
        if "Quarterly" in result_filter:
            quarterly_data()


# # Change the notebook to a .py file to run streamlit
# 

# In[ ]:


# Converts notebook to .py


# Runs the local streamlit app


# In[ ]:




