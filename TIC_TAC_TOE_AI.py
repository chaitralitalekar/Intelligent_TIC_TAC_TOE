#TIC TAC TOE game in python

board = [' ' for i in range(10)]

def insLetter(letter, pos):
    board[pos] = letter

def printBoard(board):
    print('   |   |')
    print('  '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('----------')
    print('   |   |')
    print('  '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print('  '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
def spaceIsFree(pos):
    return board[pos] == ' '
def isWinner(brd, ltr):
    return (brd[7] == ltr  and brd[8] == ltr and brd[9] == ltr) or (brd[4] == ltr  and brd[5] == ltr and brd[6] == ltr) or (brd[1] == ltr  and brd[2] == ltr and brd[3] == ltr) or (brd[1] == ltr  and brd[5] == ltr and brd[9] == ltr) or (brd[3] == ltr  and brd[5] == ltr and brd[7] == ltr) or (brd[1] == ltr  and brd[4] == ltr and brd[7] == ltr) or (brd[2] == ltr  and brd[5] == ltr and brd[8] == ltr) or (brd[3] == ltr  and brd[6] == ltr and brd[9] == ltr)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9)')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insLetter('X' , move)
                else:
                    print('Sorry this place is already occupied!')
            else:
                print('Please take the number within range!')
        except:
            print('Please type a number ')

def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x!=0]
    move = 0
    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move= selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
def selectRandom(board):
    import random
    lng = len(li)
    r = random.randrange(0 , lng)
    return li[r]
def main():
    print("Welcome to TIC TAC TOE!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('sorry!! O\'s won this time')
            break

        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print('Tie Game!')
            else:
                insLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print(' X\'s won this time! Good Job!')
            break


    if isBoardFull(board):
        print("Tie Game!")
while True:
    main()
