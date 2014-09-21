
# Plays a game of Bagels against the computer 
# AI creates random n-digit number with no repeating digits, and we try to guess it
# Picked up from 'Invent Your Own Games with Python' (Al Sweigart)

import random

# Generate secret number
def getNumber(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

# Generate clues
def getClues(guess, secretNumber):
    if guess == secretNumber:
        return ('You got it!')
    clue = []
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'
    clue.sort()
    return ' '.join(clue)

# Ensure that player inputs only digits
def isOnlyDigits(num):
    if num == '': # No input, asks again
        return False
    for i in num: # Input not a digit, asks again
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

# Player input determines whether to reset and play again
def playAgain():
    return input('Do you want to play again? > ').lower().startswith('y')

# Intro
print('Let\'s play Bagels.\n')
NUMDIGITS = int(input('How many digits long should the secret number be? > '))
MAXGUESSES = int(input('How many guesses should be allowed? > '))
print('\nI\'m thinking of a number %d digits long with no repeat numbers.' % NUMDIGITS)
print('You have %d guesses to figure it out.\n' % MAXGUESSES)
print('Here are some clues:')
print('When I say:          That means:')
print('   Pico              One digit is correct but in the wrong place.')
print('   Fermi             One digit is correct and in the right place.')
print('   Bagels            None of the digits are correct.')

# Main loop
while True:
    secretNum = getNumber(NUMDIGITS)
    numGuesses = 1
    while numGuesses <= MAXGUESSES:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print('\nGuess #%s: ' % numGuesses)
            guess = input(' > ')
        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1
        if guess == secretNum:
            break
        if numGuesses > MAXGUESSES:
            print('You ran out of guesses! Answer was %s.' % secretNum)

    if not playAgain():
        quit()

