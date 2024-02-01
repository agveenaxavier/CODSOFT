import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    choice = input("Enter your choice (rock/paper/scissors): ")
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Enter your choice (rock/paper/scissors): ")
    return choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game():
    player_score = 0
    computer_score = 0
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Player chose {player_choice}, computer chose {computer_choice}.")
        winner = determine_winner(player_choice, computer_choice)
        print(winner)
        if winner == "Player wins!":
            player_score += 1
        elif winner == "Computer wins!":
            computer_score += 1
        print(f"Score: Player {player_score}, Computer {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'yes':
            continue
        else:
            break

play_game()