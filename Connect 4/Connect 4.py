
#Set up board
Blank="■"
Board=[["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
for row in range(6):
    for column in range(7):
        Board[row][column]=Blank

#Set up game
global ThisPlayer
global WinnerFound
WinnerFound=False
ThisPlayer="○"
GameFinished=False

#Swap Players
def SwapPlayer():
    global ThisPlayer
    if ThisPlayer=="○":
        ThisPlayer="×"
    else:
        ThisPlayer="○"

#Output Board
def DisplayBoard():
    for row in range(5,-1,-1):
        for column in range(7):
            print(Board[row][column],end=" ")
        print("\n",end="")

#A Player choose a column
def ChooseColumn():
    print("Player {}'s turn".format(ThisPlayer))
    while 1:
        ColumnNumber=int(input("Please enter a valid column number"))-1
    #Check if the column number the player input is valid
        if 0<=ColumnNumber<=6 and Board[5][ColumnNumber]==Blank:
            break
    return ColumnNumber

#Find the free position in the column selected
def FindPositionInColumn(column):
    ThisRow=0
    while Board[ThisRow][column]!=Blank:
        ThisRow+=1
    return ThisRow

#A player makes a move
def ThisPlayerMakesAMove():
    ValidColumn=ChooseColumn()
    ValidRow=FindPositionInColumn(ValidColumn)
    Board[ValidRow][ValidColumn]=ThisPlayer
    return [ValidRow,ValidColumn]

#Check horizontal line
def CheckValidRow(currentrow):
    global WinnerFound
    for i in range(4):
        if Board[currentrow][i]==ThisPlayer and Board[currentrow][i+1]==ThisPlayer and Board[currentrow][i+2]==ThisPlayer and Board[currentrow][i+3]==ThisPlayer:
            WinnerFound=True

#Check vertical line
def CheckValidColumn(currentcolumn):
    global WinnerFound
    for i in range(3):
        if Board[i][currentcolumn]==ThisPlayer and Board[i+1][currentcolumn]==ThisPlayer and Board[i+2][currentcolumn]==ThisPlayer and Board[i+3][currentcolumn]==ThisPlayer:
            WinnerFound=True

#Check diagonal line
def CheckAllDiagnoalLine():
    global WinnerFound
    for row in range(3,6):
        for column in range(4):
            if Board[row][column]==ThisPlayer and Board[row-1][column+1]==ThisPlayer and Board[row-2][column+2]==ThisPlayer and Board[row-3][column+3]==ThisPlayer:
                WinnerFound=True
    for row in range(3,6):
        for column in range(3,7):
            if Board[row][column]==ThisPlayer and Board[row-1][column-1]==ThisPlayer and Board[row-2][column-2]==ThisPlayer and Board[row-3][column-3]==ThisPlayer:
                WinnerFound=True

#Check if any player has won or draw
def CheckFullBoard():
    global GameFinished
    BlankFound=False
    for row in range(6):
        for column in range(7):
            if Board[row][column]==Blank:
                BlankFound=True
                break
        if BlankFound==True:
            break
    if BlankFound==False:
        GameFinished=True
        print("It's a draw")
    
#START GAME
print("Game start")
DisplayBoard()
while not GameFinished:
    move=ThisPlayerMakesAMove()
    DisplayBoard()
    CheckValidRow(move[0])
    CheckValidColumn(move[1])
    CheckAllDiagnoalLine()
    CheckFullBoard()
    if WinnerFound==True:
        print("Game finished.\nPlayer {} is the winner".format(ThisPlayer))
        GameFinished=True
    elif GameFinished==False:
        SwapPlayer()
        
