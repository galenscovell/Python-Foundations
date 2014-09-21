
# Plays Rock, Paper, Scissors versus an AI

import random

# Determines player move
def moveChoice():
    playerChoice = input('Rock, paper or scissors? > ').lower()
    if playerChoice.startswith('r'):
        return 'rock'
    elif playerChoice.startswith('p'):
        return 'paper'
    elif playerChoice.startswith('s'):
        return 'scissors'

# Determines the AI's move
def AIchoice():
    options = random.randint(1,3)
    if options == 1:
        AImove = 'rock'
    elif options == 2:
        AImove = 'paper'
    else:
        AImove = 'scissors'
    return AImove

# Determines if another round begins
def playAgain():
    if not input('Another round? > ').lower().startswith('y'):
        quit()

WINS = 0
LOSSES = 0
DRAWS = 0
print('[ Rock | Paper | Scissors ]\n')

# Main game loop
while True:
    scoreBoard = 'Scoreboard\nWins: %d\nLosses: %d\nDraws: %d\n' % (WINS, LOSSES, DRAWS)
    print(scoreBoard)
    playerChoice = moveChoice()
    pcChoice = AIchoice()
    if pcChoice == playerChoice:
        print('The computer chose %s as well, draw!\n' % pcChoice)
        DRAWS += 1
        playAgain()
    elif playerChoice == 'rock' and pcChoice == 'scissors' or playerChoice == 'paper' and pcChoice == 'rock':
        print('The computer chose %s. You win!\n' % pcChoice)
        WINS += 1
        playAgain()
    else:
        print('The computer chose %s. You lost!\n' % pcChoice)
        LOSSES += 1
        playAgain()