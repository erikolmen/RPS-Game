# Stocks Dashboard (Command Line)

# 1. IMPORTS AT THE TOP
import os
import random
import time

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


def is_rate_limited(df):
    # the API allows about 1 request per second, and sends back an "Information" message
    # instead of stock data when we go faster than that
    return "adjusted_close" not in df.columns and "Information" in df.to_string()


def fetch_stocks_data(symbol, retries=5):
    # gets the daily stock prices for the given symbol (most recent day first)
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&outputsize=full&datatype=csv"
    for attempt in range(1, retries + 1):
        df = read_csv(request_url)
        if not is_rate_limited(df) or attempt == retries:
            break
        # wait a little longer after each try (plus a bit of randomness,
        # so test runs that start at the same time spread out), then try again
        time.sleep(attempt * 1.5 + random.uniform(0, 1))
    return df


def get_latest_close(df):
    # the first row is the most recent day
    return df["adjusted_close"][0]


def get_summary_stats(df):
    # summary numbers for the dashboard (rows are most recent day first)
    latest_close = float(df["adjusted_close"].iloc[0])
    previous_close = float(df["adjusted_close"].iloc[1])
    change = latest_close - previous_close
    last_year = df["adjusted_close"].iloc[:252]  # about 252 trading days in a year
    return {
        "latest_close": latest_close,
        "change": change,
        "change_pct": change / previous_close * 100,
        "high_52wk": float(last_year.max()),
        "low_52wk": float(last_year.min()),
    }


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
