import time
from collections import Counter


def countdown():
    for word in ["Rock...", "Paper...", "Scissors...", "SHOOT!"]:
        print(word)
        time.sleep(0.5)


def get_player_choice():
    choices = ["rock", "paper", "scissors"]
    choice = input("Choose your move NOW! (rock, paper, scissors): ").lower()
    while choice not in choices:
        choice = input(
            "Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice


def get_computer_move(player_history):
    if not player_history:
        # If we have no history, pick randomly
        return random.choice(["rock", "paper", "scissors"])

    # Count most common player moves
    counts = Counter(player_history)
    most_common_move = counts.most_common(1)[0][0]

    # Pick the move that beats the predicted move
    counter = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }
    return counter[most_common_move]


def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "You win! (Nice one!)"
    else:
        return "Computer wins. 😈"


def play():
    print("Welcome to Rock-Paper-Scissors (Smart Edition)!")
    player_history = []

    while True:
        countdown()

        player_move = get_player_choice()
        player_history.append(player_move)

        computer_move = get_computer_move(player_history)

        print(f"You chose: {player_move}")
        print(f"Computer chose: {computer_move}")

        result = decide_winner(player_move, computer_move)
        print(result)

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break


play()
