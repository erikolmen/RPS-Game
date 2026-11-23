# this is the "test/web_app_test.py" file...

# testing a flask app. see:
# ... https://flask.palletsprojects.com/en/3.0.x/testing/

import pytest
from bs4 import BeautifulSoup

from web_app import create_app


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()


def test_home(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Welcome Home</h1>" in response.data


def test_about(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"<h1>About Me</h1>" in response.data


def test_hello(test_client):
    response = test_client.get("/hello")
    assert response.status_code == 200
    assert b"<h1>Hello, World!</h1>" in response.data

    # ... with url params
    response = test_client.get("/hello?name=Erik")
    assert response.status_code == 200
    assert b"<h1>Hello, Erik!</h1>" in response.data


def test_rps_form(test_client):
    response = test_client.get("/rps/form")
    assert response.status_code == 200
    assert b"<h2>Rock, Paper, Scissors</h2>" in response.data
    soup = BeautifulSoup(response.data, features="html.parser")
    options = [opt["value"] for opt in soup.find("select").find_all("option")]
    assert options == ["rock", "paper", "scissors"]


def test_rps_results(test_client):
    response = test_client.post("/rps/results", data={"user_choice": "rock"})
    assert response.status_code == 200
    assert b"<h2>Game Results</h2>" in response.data
    assert b"You chose: <strong>rock</strong>" in response.data


def test_rps_invalid_choice(test_client):
    response = test_client.post("/rps/results", data={"user_choice": "lizard"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"<h2>Rock, Paper, Scissors</h2>" in response.data
    assert b"Invalid choice" in response.data


def test_stocks_form(test_client):
    response = test_client.get("/stocks/form")
    assert response.status_code == 200
    assert b"<h2>Stocks Form</h2>" in response.data


def test_stocks_dash(test_client):
    #
    # DEFAULT SYMBOL
    #
    response = test_client.get("/stocks/dashboard")
    assert response.status_code == 200
    assert b"<h2>Stocks Dashboard (NFLX)</h2>" in response.data
    assert b"Latest Close: " in response.data
    soup = BeautifulSoup(response.data, features="html.parser")
    rows = soup.find("tbody").find_all("tr")
    assert len(rows) == 30

    #
    # CUSTOMIZED SYMBOL VIA FORM SUBMISSION
    #
    response = test_client.post("/stocks/dashboard", data={"symbol": "GOOGL"})
    assert response.status_code == 200
    assert b"<h2>Stocks Dashboard (GOOGL)</h2>" in response.data


def test_stocks_invalid_symbol(test_client):
    response = test_client.post("/stocks/dashboard", data={"symbol": "OOPS123"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"<h2>Stocks Form</h2>" in response.data
    assert b"Market Data Error" in response.data
