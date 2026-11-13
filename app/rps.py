# Rock Paper Scissors Game (Command Line)

# ORGANIZATIONAL STRUCTURE OF OUR PYTHON FILE

# 1. IMPORTS AT THE TOP
import random

# 2. FOLLOWED BY ANY CONSTANTS
VALID_OPTIONS = ["rock", "paper", "scissors"]

# each option and the option it beats
WINS_AGAINST = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# 3. FUNCTIONS OR CLASSES


def determine_winner(u, c):
    """
    Determines the winner of a game of rock paper scissors.

    Params:
        u (str): the user's choice ("rock", "paper", or "scissors")
        c (str): the computer's choice ("rock", "paper", or "scissors")

    Returns "TIE GAME", "USER WINS", or "COMPUTER WINS".
    """
    if u not in VALID_OPTIONS or c not in VALID_OPTIONS:
        raise ValueError("Invalid choice")

    if u == c:
        return "TIE GAME"
    elif WINS_AGAINST[u] == c:
        return "USER WINS"
    else:
        return "COMPUTER WINS"


# 4. MAIN CONDITIONAL

if __name__ == "__main__":
    # ONLY RUN THE CODE BELOW
    # IF WE EXECUTE THIS FILE FROM THE COMMAND LINE
    # BUT NOT IF WE IMPORT FROM THIS FILE

    # ASK USER FOR AN INPUT (R/P/S)

    user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
    user_choice = user_choice.lower().strip()
    print("USER:", user_choice)

    # VALIDATIONS

    if user_choice not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        quit()

    # GENERATE RANDOM COMPUTER CHOICE

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMP:", computer_choice)

    # DETERMINE THE WINNER

    winner = determine_winner(u=user_choice, c=computer_choice)
    print(winner)
