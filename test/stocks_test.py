
# this is the "test/stocks_test.py" file...

import os

import pytest
from pandas import DataFrame

from app.stocks import format_usd, fetch_stocks_data, get_latest_close, make_chart

# some example data shaped like the AlphaVantage response (most recent day first)
SAMPLE_DATA = DataFrame({
    "timestamp": ["2026-11-12", "2026-11-11", "2026-11-10"],
    "adjusted_close": [105.50, 103.25, 101.00],
})


def test_format_usd():
    assert format_usd(3.5) == "$3.50"
    assert format_usd(1234.567) == "$1,234.57"


def test_get_latest_close():
    assert get_latest_close(SAMPLE_DATA) == 105.50


def test_make_chart():
    fig = make_chart(SAMPLE_DATA, "NFLX")
    assert fig.layout.title.text == "Stock Prices over Time (NFLX)"


# this test calls the real API, so it needs a premium API key
# (from the ".env" file locally, or the repository secret on GitHub Actions)
@pytest.mark.skipif(not os.getenv("ALPHAVANTAGE_API_KEY"), reason="no ALPHAVANTAGE_API_KEY set")
def test_fetch_data():
    df = fetch_stocks_data("NFLX")
    assert isinstance(df, DataFrame)
    assert "adjusted_close" in df.columns
    assert "timestamp" in df.columns
