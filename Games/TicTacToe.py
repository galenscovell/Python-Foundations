
# TicTacToe as learned from 'Invent Your Own Games with Python' (Al Sweigart)

import random

def drawBoard(board):
    # Prints out the board, a list of 10 strings (ignoring index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |\n')

def inputPlayerLetter():
    # Let's the player pick their letter, returns list with player letter as first item, computer's second
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Would you like to lose as X\'s or O\'s?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
        
def whoGoesFirst():
    # Randomly choose the player who goes first
    if random.randint(0, 1) == 0:
        print('The first move is mine.')
        return 'computer'
    else:
        print('Hmph, you first then.')
        return 'player'

def playAgain():
    # Returns True if the player wants to play again
    print('Give it another go? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, function returns True if that player has won
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top)
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make duplicate board list and return duplicate
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What\'s the word? (1-9)')
        move = input(' > ')
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns valid move from passed list on passed board, returns none if none valid
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given board and computer's letter, determine where to move and return it
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Algorithm for AI:
    # 1 Check if we can win in next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    # 2 Check if players could win next move, block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    # 3 Try to take one of the corners if free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # 4 Try to take center if free
    if isSpaceFree(board, 5):
        return 5
    # 5 Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return true if every space on board is full
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('This is Tice Tac Toe, son.')
print('The game of pure skill.\n')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.\n')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            # Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('What\'s that? You actually won?\n')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('A draw defaults to my victory.\n')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Victory is mine, as expected.\n')
                gameIsPLaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('A draw defaults to my victory.\n')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break