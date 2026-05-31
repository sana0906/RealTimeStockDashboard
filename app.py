import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(
    page_title="Stock Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Real-Time Stock Market Dashboard")

stocks = ["AAPL", "MSFT", "GOOG", "TSLA", "NVDA", "AMZN"]

ticker = st.selectbox(
    "Select Stock",
    stocks
)

period = st.selectbox(
    "Select Time Period",
    ["1mo", "3mo", "6mo", "1y"]
)

stock = yf.Ticker(ticker)

data = stock.history(period=period)

# Moving Average
data["MA20"] = data["Close"].rolling(20).mean()

# Current Price Card
current_price = round(data["Close"].iloc[-1], 2)

st.metric(
    label="Current Price",
    value=f"${current_price}"
)

# Closing Price + MA20 Chart
st.subheader("Closing Price vs Moving Average")

st.line_chart(
    data[["Close", "MA20"]]
)

# Candlestick Chart
st.subheader("Candlestick Chart")

fig = go.Figure(data=[
    go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"]
    )
])

fig.update_layout(
    xaxis_rangeslider_visible=False
)

st.plotly_chart(fig, use_container_width=True)

# Volume Analysis
st.subheader("Volume Analysis")

st.bar_chart(data["Volume"])

# Raw Data
with st.expander("View Raw Data"):
    st.write(data)