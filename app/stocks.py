# Stocks Dashboard (Command Line)

# 1. IMPORTS AT THE TOP
import os

from dotenv import load_dotenv
from pandas import read_csv
import plotly.express as px

# 2. FOLLOWED BY ANY CONSTANTS

load_dotenv()  # read env vars from the ".env" file

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

# 3. FUNCTIONS


def format_usd(price):
    # formats a number as a dollar amount, like "$1,234.57"
    return f"${price:,.2f}"


def fetch_stocks_data(symbol):
    # gets the daily stock prices for the given symbol (most recent day first)
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&outputsize=full&datatype=csv"
    return read_csv(request_url)


def get_latest_close(df):
    # the first row is the most recent day
    return df["adjusted_close"][0]


def make_chart(df, symbol):
    # makes a line chart of the stock price over time
    title = f"Stock Prices over Time ({symbol})"
    fig = px.line(df, x="timestamp", y="adjusted_close", title=title, height=400)
    return fig


# 4. MAIN CONDITIONAL

if __name__ == "__main__":

    selected_symbol = input("Please input a stock symbol (e.g. 'GOOGL'): ") or "GOOGL"

    df = fetch_stocks_data(selected_symbol)
    print(df.head())

    latest_close = get_latest_close(df)
    print("LATEST CLOSE:", format_usd(latest_close))

    fig = make_chart(df, selected_symbol)
    fig.show()
