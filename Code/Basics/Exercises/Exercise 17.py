# Exercise 17: Rock, Paper, Scissors Game
import random

options = ("Rock", "Paper", "Scissors")
running = True

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Pick either (Rock, Paper, Scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You win!")
    elif player == "Paper" and computer == "Rock":
        print("You win!")
    elif player == "Scissors" and computer == "Paper":
        print("You win!")
    else:
        print("You lose!")
        
    running = input("Play again? (Y/N)").lower() == "y"

print("Thanks for playing!")