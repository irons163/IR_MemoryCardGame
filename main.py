import random
import copy
import os
import string


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


cardsBoardRows = 6
cardsBoardCols = 6


def createCards():
    # listCard = 'ABCDEF'
    listCard = string.ascii_uppercase[:int(cardsBoardRows*cardsBoardCols/2)]
    listCard += listCard
    listCardList = list(listCard)
    random.shuffle(listCardList)

    return [[listCardList[x*cardsBoardRows+y] for y in range(cardsBoardRows)] for x in range(cardsBoardCols)]


def createBoard():
    return [['_' for x in range(cardsBoardRows)] for x in range(cardsBoardCols)]


def showBoard(board):
    cardsInRow = ''
    for row in board:
        for card in row:
            cardsInRow += card + ' '
        print(cardsInRow)
        cardsInRow = ''
    print('')


def isWin(board):
    for row_position, row in enumerate(board):
        for col_position, card in enumerate(row):
            if (card == '_'):
                return False

    return True


def selectCard(board, cards, count):
    tmpBoard = copy.deepcopy(board)
    selectCards = []

    while(True):
        while(True):
            try:
                col_position = int(
                    input('Please input 1 number of position(col nubmer 1-{0})'.format(cardsBoardCols))) - 1
                if col_position >= cardsBoardCols:
                    print('Col nubmer too large. Please try another one. \n')
                    continue
                if col_position < 0:
                    print('Col nubmer too small. Please try another one. \n')
                    continue

                row_position = int(
                    input('Please input 1 number of position(row number 1-{0})'.format(cardsBoardRows))) - 1
                if row_position >= cardsBoardRows:
                    print('Row nubmer too large. Please try another one. \n')
                    continue
                if row_position < 0:
                    print('Row nubmer too small. Please try another one. \n')

                break
            except:
                continue
        if(isFreeSpace(board, row_position, col_position)):
            selectCard = cards[row_position][col_position]
            openCard(tmpBoard, selectCard,
                     row_position, col_position)
            showBoard(tmpBoard)
            selectCards.append(selectCard)
            if len(selectCards) == 2:
                if selectCards[0] == selectCards[1]:
                    print('The two selected cards are match. \n')
                    return tmpBoard
                else:
                    # clear the screen
                    print('The two selected cards are not match. \n')
                    try:
                        input('Press Enter to continue...')
                    except:
                        pass
                    clear()
                    showBoard(board)
                    return board
        else:
            print('This card is opened. Please try another one. \n')


def isFreeSpace(board, row_position, col_position):
    return board[row_position][col_position] == '_'


def openCard(board, selectCard, row_position, col_position):
    board[row_position][col_position] = selectCard


while True:
    cards = createCards()
    board = createBoard()
    showBoard(board)
    while(not isWin(board)):
        didSelecteBoard = selectCard(board, cards, 2)
        board = didSelecteBoard
    print('You win. \n')
    try:
        letter = input('Play again? (Y/else)')
        if letter == 'Y' or letter == 'y':
            continue
        else:
            break
    except:
        break
