# RPS-Game

A command-line game of Rock, Paper, Scissors written in Python.

## Setup

Create a virtual environment (first time only):

```sh
conda create -n rps-env python=3.11
```

Activate the environment (every time you open a new terminal):

```sh
conda activate rps-env
```

Install packages:

```sh
pip install -r requirements.txt
```

## Usage

Play the game:

```sh
python -m app.rps
```

## Testing

Run the automated tests:

```sh
python -m pytest
```

Tests also run automatically on every push and pull request using GitHub Actions (see `.github/workflows/python-app.yml`).
