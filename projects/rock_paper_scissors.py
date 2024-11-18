# Code a game of rock paper scissors.
# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner

import random

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    if hand == 0:
        return "scissor"
    elif hand == 1:
        return "rock"
    elif hand == 2:
        return "paper"
    else:
        return "unknown"
    
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif player == "rock" and computer == "scissor":
        return "Player wins!"
    elif player == "scissor" and computer == "paper":
        return "Player wins!"
    elif player == "paper" and computer == "rock":
        return "Player wins!"
    else:
        return "Computer wins!" 
    
player = int(input("Enter a number (0 = scissor, 1 = rock, 2 = paper): "))
computer = random.randint(0, 2)

player_hand = get_hand(player)
computer_hand = get_hand(computer)
winner = determine_winner(player_hand, computer_hand)
print(f"Player: {player_hand}")
print(f"Computer: {computer_hand}")
print(winner)

