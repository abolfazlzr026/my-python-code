# chapter 19
import random
from random import randint

print("rock")
print("paper")
print("scissors")

player_1_wins = 0
player_2_wins = 0
winning_score = 4

while player_1_wins < winning_score and player_2_wins < winning_score:
    print(f"player 1: {player_1_wins}   player 2: {player_2_wins}")

    player_1 = input("player_1 , move : ").lower()

    if player_1 == "q" or player_1 == "quit":
        print("Game ended.")
        break

    # تعیین حرکت کامپیوتر داخل حلقه
    randomNumber = randint(0, 2)
    if randomNumber == 0:
        computermove = "rock"
    elif randomNumber == 1:
        computermove = "paper"
    else:
        computermove = "scissors"

    player_2 = computermove
    print(f"player_2 , move : {player_2}")

    # منطق بازی
    if player_1 == player_2:
        print("That's a tie!")
    elif player_1 == "rock":
        if player_2 == "scissors":
            print("Player 1 wins!")
            player_1_wins += 1
        else:
            print("Player 2 wins!")
            player_2_wins += 1

    elif player_1 == "paper":
        if player_2 == "rock":
            print("Player 1 wins!")
            player_1_wins += 1
        else:
            print("Player 2 wins!")
            player_2_wins += 1

    elif player_1 == "scissors":
        if player_2 == "paper":
            print("Player 1 wins!")
            player_1_wins += 1
        else:
            print("Player 2 wins!")
            player_2_wins += 1

    else:
        print("Invalid move! (use rock/paper/scissors)")

print("Final result:")
print(f"Player 1: {player_1_wins}  |  Player 2: {player_2_wins}")
