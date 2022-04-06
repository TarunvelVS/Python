import random

def play():
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return 'tie'
    if if_win(user, computer):
        return 'You won!'
    
    return 'You lost!'


def if_win(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p')  or (player1 == 'p' and player2 == 'r'):
        return True

print(play())