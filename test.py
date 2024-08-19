import streamlit as st
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import matplotlib.pyplot as plt


st.title("test 123")

# Fetch data for the last 5 years
def get_recent_data():
    ticker = yf.Ticker('AAPL')
    aapl_df = ticker.history(period="5y")
    return aapl_df.tail(5)  # Get the 5 most recent data points

# Streamlit app
def app():
    st.title("Apple Stock Price Analysis")

    st.write("### Displaying the 5 Most Recent Data Points for Apple (AAPL)")
    recent_data = get_recent_data()

    st.write("#### Most Recent Data:")
    st.dataframe(recent_data)

    st.write("### Closing Prices for the Most Recent 5 Days")
    fig, ax = plt.subplots()
    recent_data['Close'].plot(title="Apple's Stock Price - Last 5 Days", ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    app()