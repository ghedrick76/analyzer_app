#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd # for dataframes
import numpy as np # for NaN
import yfinance as yf
import matplotlib.pyplot as plt # for visualization
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

# Creates the dropdown box for the user to select tickers
dropdown = st.multiselect('Select equities to chart', tickers)

dropdown2 = st.multiselect('Calculate volatility ', tickers)


# Sets the start and end dates
start = st.date_input('Start', value = pd.to_datetime('2012-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))


# In[3]:


# def relativeret(df):
#     rel = df.pct_change()
#     cumret = (1+rel).cumprod() - 1
#     cumret = cumret.fillna(0)
#     return cumret

def returns(df):
    returns = df
    return returns

def calc_vol(df):
    df = df.pct_change()
    volatility = df.std()*252**.5
    return volatility

if len(dropdown) > 0:
    df = returns(yf.download(dropdown,start,end)['Close'])
    st.header('Graph of {}'.format(dropdown))
    st.line_chart(df)
    
if len(dropdown2) > 0:
    df = calc_vol(yf.download(dropdown2,start,end)['Close'])
    st.header('Volatility of {}'.format(dropdown2))
    df
    


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




