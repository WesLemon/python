theBoard = {
    '1': '1', '4': '4', '7': '7',
    '2': '2', '5': '5', '8': '8',
    '3': '3', '6': '6', '9': '9',
}


def drawBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def checkWin(board):
    if board['1'] == board['2'] and board['2'] == board['3'] \
            or \
            board['4'] == board['5'] and board['5'] == board['6'] \
            or \
            board['7'] == board['8'] and board['8'] == board['9'] \
            or \
            board['1'] == board['4'] and board['4'] == board['7'] \
            or \
            board['2'] == board['5'] and board['5'] == board['8'] \
            or \
            board['3'] == board['6'] and board['6'] == board['9'] \
            or \
            board['1'] == board['5'] and board['5'] == board['9'] \
            or \
            board['3'] == board['5'] and board['5'] == board['7']:
        return True
    else:
        return False


gameWin = False
playerX = 'X'
playerO = '0'
current_player = -1
game_round = 1

while not gameWin and game_round < 10:
    drawBoard(theBoard)
    current_player *= -1
    if current_player == 1:
        print('Player 1: Where do you want to go?')
        move = str(input())
        theBoard[move] = playerX
    else:
        print('Player 2: Where do you want to go?')
        move = str(input())
        theBoard[move] = playerO
    gameWin = checkWin(theBoard)
    game_round += 1

if current_player == -1:
    current_player = 2

drawBoard(theBoard)
if gameWin:
    print('Congratulations Player ' + str(current_player) + '! You won!')
else:
    print('It was a draw.')
