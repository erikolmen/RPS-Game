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

Tests also run automatically on GitHub (using GitHub Actions) whenever code is pushed to, or a pull request is opened against, the `main` branch. See `.github/workflows/python-app.yml`.
