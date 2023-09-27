import sys
import random

# string for blank space
BLANK = " "

# getting new board
def getNewBoard():
    board = [
        [1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,BLANK]
    ]

    return board

# display the board to screen
def drawBoard(board):
    lables = [board[0][0],board[1][0],board[2][0],board[3][0],
              board[0][1],board[1][1],board[2][1],board[3][1],
              board[0][2],board[1][2],board[2][2],board[3][2],
              board[0][3],board[1][3],board[2][3],board[3][3]]
    boardToDraw = """
+-------+-------+-------+-------+
|       |       |       |       |
| {:^5} | {:^5} | {:^5} | {:^5} |
|       |       |       |       |
+-------+-------+-------+-------+
|       |       |       |       |
| {:^5} | {:^5} | {:^5} | {:^5} |
|       |       |       |       |
+-------+-------+-------+-------+
|       |       |       |       |
| {:^5} | {:^5} | {:^5} | {:^5} |
|       |       |       |       |
+-------+-------+-------+-------+
|       |       |       |       |
| {:^5} | {:^5} | {:^5} | {:^5} |
|       |       |       |       |
+-------+-------+-------+-------+
""".format(*lables)
    print(boardToDraw)

# finding the blank space position
def findBlankSpace(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] is BLANK:
                return (i, j)

# asking player for moves
def askForPlayerMove(board):
    bx, by = findBlankSpace(board)
    w = "W" if by != 3 else  " "
    a = "A" if bx != 3 else " "
    s = "S" if by != 0 else " "
    d = "D" if bx != 0 else " "
    # loop until the user give input
    while True:
        print(f"                                 ({w})")
        print(f"press key to move (q to Quit)({a})({s})({d})")
        usr_move = input(">").upper()
        if usr_move == "QUIT":
            sys.exit()
        if usr_move in (w+a+s+d).replace(" ","") :
            return usr_move

# function to make moves
def makeMove(board, response):     
    bx, by = findBlankSpace(board)
    # swaping the position of the blank space and neighboor numbers
    if response == "W":
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif response == "A":
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif response == "S":
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by] 
    elif response == "D":
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]

# make a random  move
def makeRandomMove(board):
    bx, by = findBlankSpace(board)
    validMoves = []
    if by != 3:
        validMoves.append("W")
    if bx != 3:
        validMoves.append("A")
    if bx != 0:
        validMoves.append("D")
    if by != 0:
        validMoves.append("S")
    makeMove(board, random.choice(validMoves))

# creating new puzzle
def getNewPuzzle(move=200):
    board = getNewBoard()
    # random moves to make puzzle tricky
    for i in range(move):
        makeRandomMove(board)
    return board

# main function start here
def main():
    print("""
        Slide the puzzle in correct order :-
        (press Ctr+c to quit)
          back to the original order
           1  2  3  4
           5  6  7  8
           9  10 11 12
           13 14 15
    """)
    input("Press enter to start...")
    # while True:
    board = getNewPuzzle()
    # loop to check the user win
    while True:
        drawBoard(board)
        playerMove = askForPlayerMove(board)
        makeMove(board, playerMove)
        if board == getNewBoard():
            print("YOU WON!")
            sys.exit

if __name__ == "__main__":
    main()