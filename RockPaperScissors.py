import random

choices = ['rock', 'paper', 'scissors']
player = input('rock paper scissors ')
computer = random.choice(choices)

print(player, 'vs', computer)

if player == computer:
    print('Draw')
elif player == 'rock' and computer == 'paper':
    print('Computer Wins!')
elif player == 'scissors' and computer == 'paper':
    print('Player Wins!')
elif player == 'paper' and computer == 'rock':
    print('Player Wins!')
elif player == 'paper' and computer == 'scissors':
    print('Computer Wins!')
elif player == 'rock' and computer == 'scissors':
    print('Player Wins!')
elif player == 'scissors' and computer == 'rock':
    print('Computer Wins!')
elif player == 'scissors' and computer == 'paper':
    print('Player Wins!')
elif player == 'done':
    print('Thank you, come again!')

while player != 'done':
    player = input('rock paper scissors ')
    computer = random.choice(choices)
    print(player, 'vs', computer)
    
    if player == computer:
        print('Draw')
    elif player == 'rock' and computer == 'paper':
        print('Computer Wins!')
    elif player == 'scissors' and computer == 'paper':
        print('Player Wins!')
    elif player == 'paper' and computer == 'rock':
        print('Player Wins!')
    elif player == 'paper' and computer == 'scissors':
        print('Computer Wins!')
    elif player == 'rock' and computer == 'scissors':
        print('Player Wins!')
    elif player == 'scissors' and computer == 'rock':
        print('Computer Wins!')
    elif player == 'scissors' and computer == 'paper':
        print('Player Wins!')
    elif player == 'done':
        print('Thank you, come again!')