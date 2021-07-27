#Tic-Tac-Toe Games
#Author: Md. Imran Hossain Emu
#Date: 27.07.2021
#Time: 23:30

#Declare the list to check who Won the games.
board = [ ' ' for x in range(10)]

#Print the check board
def printTheBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#Check if anyone Win or Not
def isWin(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

#Insert the Value 'X' or 'O' by Player or Computer Move
def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

#Insert my move with Friend and Computer
def yourMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

#Computer moves
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWin(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
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

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

#Check the board os Full or Not
def isFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

#Main function when play with Computer
def computer():
    printTheBoard(board)

    while not(isFull(board)):
        if not(isWin(board, '0')):
            yourMove()
            printTheBoard(board)
        else:
            print("Computer Wins!")
            break
        
        if not(isWin(board, 'X')):
            move = compMove()
            if move == 0:
                print("No one Won! It's Tie!")
            else:
                insertLetter('O', move)
                print("Computer take 'O' at position: ", move)
                printTheBoard(board)
        else:
            print("Hurray! You Won the match.")
            break

#To insert Friends move
def friendMove():
    run = True
    while run:
        move = input('Please select a position to place an \'O\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

#Main function when play with Friend
def friend():
    printTheBoard(board)

    while not(isFull(board)):
        if not(isWin(board, 'O')):
            yourMove()
            printTheBoard(board)
        else:
            print("Friends Win the match!")
            break;
        if(isFull(board)):
            print("No one Won! It's Tie!")
            break;

        if not(isWin(board, 'X')):
            friendMove()
            printTheBoard(board)
        else:
            print("Hurray! You Won the match.")
            break;
            
        if(isFull(board)):
            print("No one Won! It's Tie!")
            break;

#Main Function where the games start
while True:
    answer = input('Do you want to play again? (Y/N): ')
    if answer.upper() == 'Y' or answer.upper == 'YES':
        print('-----------------------------------')
        board = [' ' for x in range(10)]
        ask = input("Want to play with Computer or Friend! (C/F): ")
        print('-----------------------------------')
        if ask.upper() == 'C':
            print('Welcome to play with Computer!')
            computer()
        else:
            print("Welcome to You & Your friend to play the Tic-Tac-Toe Games!")
            friend()
    else:
        break

#End
#Enjoy the Game!