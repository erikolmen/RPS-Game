
# this is the "test/stocks_test.py" file...

from pandas import DataFrame

import app.stocks

from app.stocks import format_usd, fetch_stocks_data, get_latest_close, get_summary_stats, make_chart

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


def test_summary_stats():
    stats = get_summary_stats(df)
    assert stats["latest_close"] == df["adjusted_close"][0]
    assert round(stats["change"], 4) == round(df["adjusted_close"][0] - df["adjusted_close"][1], 4)
    assert stats["low_52wk"] <= stats["latest_close"] <= stats["high_52wk"]


def test_fetch_retries_when_rate_limited(monkeypatch):
    # pretend the API says "slow down" twice, then sends real data
    rate_limited = DataFrame({"{": ['"Information": "Please consider spreading out your free API requests"']})
    responses = [rate_limited, rate_limited, df]
    calls = []

    def fake_read_csv(url):
        calls.append(url)
        return responses[len(calls) - 1]

    monkeypatch.setattr(app.stocks, "read_csv", fake_read_csv)
    monkeypatch.setattr(app.stocks.time, "sleep", lambda seconds: None)  # don't actually wait in tests

    result = fetch_stocks_data("NFLX")
    assert len(calls) == 3
    assert "adjusted_close" in result.columns
