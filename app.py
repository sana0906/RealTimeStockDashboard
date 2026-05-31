import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.title("📈 Real-Time Stock Market Dashboard")

ticker = st.text_input("Enter Stock Symbol", "AAPL")

stock = yf.Ticker(ticker)

data = stock.history(period="1mo")

st.subheader("Stock Data")
st.write(data.tail())

fig = px.line(
    data,
    x=data.index,
    y="Close",
    title=f"{ticker} Closing Price"
)

st.plotly_chart(fig)

current_price = round(data['Close'].iloc[-1], 2)

st.metric(
    label="Current Price",
    value=f"${current_price}"
)