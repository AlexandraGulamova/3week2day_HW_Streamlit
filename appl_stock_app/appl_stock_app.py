import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf


tickerSymbol='AAPL'
tickerData=yf.Ticker(tickerSymbol)
start='2014-10-08'
end='2024-10-08'
tickerDf=tickerData.history(period='1d',start=start, end=end)

mean_value=round(tickerDf.Close.mean(),2)
median_value=round(tickerDf.Close.median(),2)
std_value=round(tickerDf.Close.std(),2)
period=f"{start} - {end}"

st.write (f"""
# Simple Stock Price App (APPLE)


| Metrics      |      {period}      | 
| ------------- |:-------------:| 
| median     | {median_value} |
| mean      | {mean_value}     |
| std | {std_value}      |
                    
Shown are the stock **closing price** and **volume** of Apple!
          
""")



st.line_chart(data=tickerDf.Close,width=80, height=200)
st.line_chart(data=tickerDf.Volume,width=80, height=200)