# How rock, paper scissors works
  # r > s, s > p, p > r

import random

#Ask for input
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
#Tie logic
    if user == computer:
        return 'It\'s a tie'
#Selecting the winner
    if is_win(user,computer):
       return 'You won!'
    return 'You lost!'

# Logic for the game
def is_win(player, opponent):
    # return true if player wins
     # r > s, s > p, p > r
  if (player == 'r' and opponent = 's') or (player == 's' and opponent == 'p') \
  or (player == 'p' and opponent == 'r'):
     return True
     
print(play())

    