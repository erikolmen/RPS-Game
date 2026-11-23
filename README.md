# RPS-Game

A game of Rock, Paper, Scissors, plus a stocks dashboard, written in Python. Both can be used from the command line or through a Flask web app.

## Prerequisites

Install python version 3.x (for example using Anaconda).

## Setup

1. Clone [the repo](https://github.com/erikolmen/RPS-Game) from GitHub, and put it somewhere (like your Desktop).
2. Navigate to the local repo from the command line (for example if on your desktop):

```sh
cd ~/Desktop/RPS-Game
```

3. Create a new Anaconda virtual environment called "rps-env" (first time only):

```sh
conda create -n rps-env python=3.11
```

4. Activate the virtual environment as necessary (every time you come back to the project):

```sh
conda activate rps-env
```

5. Install package dependencies:

```sh
pip install -r requirements.txt
```

### Secret Credentials

For the stocks dashboard, you will need to acquire a "premium" [AlphaVantage](https://www.alphavantage.co/) API key (from the prof) and supply it as an environment variable. Create a local ".env" file in the root directory of the repo and place inside contents like the following:

```sh
# this is the ".env" file...

# replace "demo" with your premium key:
ALPHAVANTAGE_API_KEY="demo"

# used by the web app for flash messaging (set to any random string):
SECRET_KEY="super secret"
```

The ".env" file is listed in the ".gitignore" file, so your key will NOT be uploaded to GitHub.

Also, for the stocks tests to work on GitHub Actions, you will need to set a repository secret named `ALPHAVANTAGE_API_KEY` via the repository's settings on GitHub (Settings > Secrets and variables > Actions > New repository secret).

## Usage

Play the rock paper scissors game:

```sh
python app/rps.py

# alternatively:
python -m app.rps
```

Run the stocks dashboard:

```sh
python -m app.stocks
```

Run the web app (then visit http://localhost:5000 in a browser):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
export FLASK_APP=web_app
flask run
```

The web app has these pages:

| Route | Description |
| --- | --- |
| `/`, `/about`, `/hello?name=Erik` | Basic home routes |
| `/rps/form` | Pick rock, paper, or scissors from a dropdown and play |
| `/rps/results` | Shows both choices and who won |
| `/stocks/form` | Enter a stock symbol |
| `/stocks/dashboard?symbol=MSFT` | Latest close, a chart of prices over time, and a table of recent prices |

All pages share a Bootstrap layout with a custom navbar. An invalid stock symbol shows a flash message and redirects back to the stocks form.

## Deployment

The web app is deployed to [Render](https://render.com) as a "Web Service":

1. In the [Render dashboard](https://dashboard.render.com), create a New "Web Service" from this GitHub repo.
2. Build command: `pip install -r requirements.txt`
3. Start command: `gunicorn "web_app:create_app()"`
4. Instance type: "Free".
5. Environment variables: `ALPHAVANTAGE_API_KEY` (your key, no quotes) and `SECRET_KEY` (any random string).

Each push to the `main` branch triggers a new deploy.

Production URL: _(add your onrender.com URL here)_

## Testing

To run tests:

```sh
pytest
```

## Continuous Integration

[![Python application](https://github.com/erikolmen/RPS-Game/actions/workflows/python-app.yml/badge.svg)](https://github.com/erikolmen/RPS-Game/actions/workflows/python-app.yml)

This repo uses GitHub Actions as an automatic check step. Whenever code is pushed to, or a pull request is opened against, the `main` branch, GitHub will:

1. Download the code and set up Python.
2. Install the packages listed in `requirements.txt`.
3. Run `flake8` to check for Python syntax errors.
4. Run `pytest` to run all of the automated tests (using the `ALPHAVANTAGE_API_KEY` repository secret for the stocks tests).

If any of these steps fail, the pull request shows a red X, and the code should be fixed before merging. If they all pass, it shows a green check. See `.github/workflows/python-app.yml` for the workflow configuration.

## AI Credit

I used Claude Code to help review my code, simplify in areas, and check that my tests and CI build pass. I also used it to help troubleshoot the Flask web app (routes, templates, Bootstrap layout, flash messaging, and web app tests) when I had trouble or needed help.