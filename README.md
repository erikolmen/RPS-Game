# RPS-Game

A command-line game of Rock, Paper, Scissors, plus a stocks dashboard, written in Python.

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

I used Claude Code to help review my code, simplify in areas, and check that my tests and CI build pass.