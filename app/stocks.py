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
    """Formats a number as a dollar amount, like "$1,234.57"."""
    return f"${price:,.2f}"


def fetch_stocks_data(symbol, api_key=ALPHAVANTAGE_API_KEY):
    """
    Fetches daily stock prices for the given symbol from the AlphaVantage API.

    Returns a pandas DataFrame with the most recent day first.
    """
    request_url = (
        "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"
        f"&symbol={symbol}&apikey={api_key}&outputsize=full&datatype=csv"
    )
    df = read_csv(request_url)

    # if the request fails (bad symbol, missing / invalid API key),
    # AlphaVantage sends back an error message instead of the data
    if "timestamp" not in df.columns:
        raise ValueError(f"Could not fetch data for '{symbol}'. Check the symbol and your API key.")

    return df


def get_latest_close(df):
    """Returns the most recent adjusted closing price from the data."""
    return df["adjusted_close"].iloc[0]


def make_chart(df, symbol):
    """Returns a line chart of the stock's adjusted closing price over time."""
    title = f"Stock Prices over Time ({symbol})"
    return px.line(df, x="timestamp", y="adjusted_close", title=title, height=400)


# 4. MAIN CONDITIONAL

if __name__ == "__main__":

    selected_symbol = input("Please input a stock symbol (e.g. 'GOOGL'): ") or "GOOGL"
    selected_symbol = selected_symbol.upper().strip()

    df = fetch_stocks_data(selected_symbol)
    print(df.head())

    latest_close = get_latest_close(df)
    print("LATEST CLOSE:", format_usd(latest_close))

    fig = make_chart(df, selected_symbol)
    fig.show()
