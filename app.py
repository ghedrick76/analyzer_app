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
nyse = pd.read_csv("untitled.csv")['ACT Symbol']
nasdaq = pd.read_csv("nasdaq.csv")['Symbol']

# Combine the two datasets
tickers = pd.concat([nyse,nasdaq]).drop_duplicates().reset_index(drop=True)


# In[2]:


# Create the Streamlit instance
st.title('Finance Dashboard')

# Creates the dropdown boxes for the user to select their tickers and desired functions
dropdown = st.multiselect('Select equities to chart', tickers)

dropdown2 = st.multiselect('Calculate volatility ', tickers)

dropdown3 = st.multiselect('Calculate the beta of any two tickers', tickers)


# Sets the start and end dates
start = st.date_input('Start', value = pd.to_datetime('2012-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))


# In[3]:


# def relativeret(df):
#     rel = df.pct_change()
#     cumret = (1+rel).cumprod() - 1
#     cumret = cumret.fillna(0)
#     return cumret

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
    


# # What does the script do? 
# 

# Converts NB to .py
# `jupyter nbconvert   --to script YOURNAME.ipynb`
# 
# 
# 
# 
# 
# Runs the local streamlit app
# `streamlit run app.py`

# In[ ]:




# In[ ]:




