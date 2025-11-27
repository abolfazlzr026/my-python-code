# chapter 15
# print("rock")
# print("paper")
# print("scissors")
# player_1= input("  player_1 , move :")
# player_2= input("player_2 , move :")
# print(player_1)
# if player_1 == "rock" and player_2 == "scissors":
#     print(" player_1 win")
# elif player_1 == "rock" and player_2 == "paper":
#     print("player_2 win")
# elif player_1 =="paper" and player_2 == "rock":
#     print("player _1 win")
# elif player_1 =="paper" and player_2 == "scissors":
#     print("player _2 win")
# elif player_1 == "scissors" and player_2 == "paper":
#     print("player _1 win")
# elif player_1 == "scissors" and player_2 == "rock":
#     print("player _2 win")
# elif player_1 == player_2 :
#     print(" thats tie")
# else:
#     print(" somthing went wrong!")






# or
# print("rock")
# print("paper")
# print("scissors")
# player_1= input("  player_1 , move :")
# player_2= input("player_2 , move :")

# if player_1 == player_2:
#     print("That's a tie!")
# elif player_1 == "rock":
#     if player_2 == "scissors":
#         print("Player 1 wins!")
#     elif player_2 == "paper":
#         print("Player 2 wins!")
# elif player_1 == "paper":
#     if player_2 == "rock":
#         print("Player 1 wins!")
#     elif player_2 == "scissors":
#         print("Player 2 wins!")
# elif player_1 == "scissors":
#     if player_2 == "paper":
#         print("Player 1 wins!")
#     elif player_2 == "rock":
#         print("Player 2 wins!")
# else:
#     print("Something went wrong!")
# or
import random
from random import randint
print("rock")
print("paper")
print("scissors")

randomNumber= randint(0, 2)
if randomNumber == 0:
    computermove ="rock"
elif  randomNumber == 1:
      computermove ="scissors"
elif randomNumber == 1:
     computermove ="paper"

player_1= input("  player_1 , move :")
player_2=computermove
print(f"player_2 , move :{computermove}")

if player_1 == player_2:
    print("That's a tie!")
elif player_1 == "rock":
    if player_2 == "scissors":
        print("Player 1 wins!")
    elif player_2 == "paper":
        print("Player 2 wins!")
elif player_1 == "paper":
    if player_2 == "rock":
        print("Player 1 wins!")
    elif player_2 == "scissors":
        print("Player 2 wins!")
elif player_1 == "scissors":
    if player_2 == "paper":
        print("Player 1 wins!")
    elif player_2 == "rock":
        print("Player 2 wins!")
else:
    print("Something went wrong!")
