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

tickers = pd.concat([nyse,nasdaq]).drop_duplicates().reset_index(drop=True)


# In[2]:


# Create the Streamlit instance
st.title('Finance Dashboard')

# Creates the dropdown box for the user to select tickers
dropdown = st.multiselect('Pick your assets', tickers)

# Sets the start and end dates
start = st.date_input('Start', value = pd.to_datetime('2012-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))


# In[3]:


# def relativeret(df):
#     rel = df.pct_change()
#     cumret = (1+rel).cumprod() - 1
#     cumret = cumret.fillna(0)
#     return cumret

def relativeret(df):
    rel = df
    return rel

if len(dropdown) > 0:
    df = relativeret(yf.download(dropdown,start,end)['Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)
    


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




