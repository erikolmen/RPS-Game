import random

VALID_OPTIONS = ["rock", "paper", "scissors"]
WINS_AGAINST = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def determine_winner(user_choice, computer_choice):
    """Returns "user", "computer", or "tie"."""
    if user_choice not in VALID_OPTIONS or computer_choice not in VALID_OPTIONS:
        raise ValueError("Invalid choice")
    if user_choice == computer_choice:
        return "tie"
    if WINS_AGAINST[user_choice] == computer_choice:
        return "user"
    return "computer"


def play():
    user_choice = input("Choose rock, paper, or scissors: ").lower().strip()
    if user_choice not in VALID_OPTIONS:
        print("Oops, invalid choice. Please try again.")
        return

    computer_choice = random.choice(VALID_OPTIONS)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    play()
