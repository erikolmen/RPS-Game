import pytest
from app.rps import determine_winner


def test_ties():
    assert determine_winner("rock", "rock") == "tie"
    assert determine_winner("paper", "paper") == "tie"
    assert determine_winner("scissors", "scissors") == "tie"


def test_user_wins():
    assert determine_winner("rock", "scissors") == "user"
    assert determine_winner("paper", "rock") == "user"
    assert determine_winner("scissors", "paper") == "user"


def test_computer_wins():
    assert determine_winner("scissors", "rock") == "computer"
    assert determine_winner("rock", "paper") == "computer"
    assert determine_winner("paper", "scissors") == "computer"


def test_invalid_choice():
    with pytest.raises(ValueError):
        determine_winner("banana", "rock")
