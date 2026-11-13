
# this is the "test/stocks_test.py" file...

from pandas import DataFrame

from app.stocks import format_usd, fetch_stocks_data, get_latest_close, make_chart

# fetch the data once, and re-use it in each test below
# (to avoid calling the API too many times in a row)
df = fetch_stocks_data("NFLX")


def test_format_usd():
    assert format_usd(3.5) == "$3.50"
    assert format_usd(1234.567) == "$1,234.57"


def test_fetch_data():
    assert isinstance(df, DataFrame)
    assert "adjusted_close" in df.columns
    assert "timestamp" in df.columns


def test_latest_close():
    latest_close = get_latest_close(df)
    assert latest_close == df["adjusted_close"][0]
    assert latest_close > 0


def test_make_chart():
    fig = make_chart(df, "NFLX")
    assert fig.layout.title.text == "Stock Prices over Time (NFLX)"
