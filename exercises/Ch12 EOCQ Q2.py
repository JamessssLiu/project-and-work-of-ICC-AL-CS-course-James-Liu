import random
Point=[]
Grid=[]
global GameEnd
GameEnd=False

def SetUpGrid():
    for i in range(8):
        Grid.append([])
        for j in range(8):
            Grid[i].append(0)

def GetRandomEmptyPosition():
    while 1:
        global xrand,yrand
        xrand=random.randint(0,7)
        yrand=random.randint(0,7)
        if Grid[xrand][yrand]==0:
            break

def RandomlyDistributeCards():
    for n in range(1,33):
        GetRandomEmptyPosition()
        Grid[xrand][yrand]=n
        GetRandomEmptyPosition()
        Grid[xrand][yrand]=n

def SetUpPlayer():
    global ThisPlayer
    ThisPlayer=1
    Point.append(0)
    Point.append(0)
    

def SwapPlayer():
    if ThisPlayer==1:
        ThisPlayer=2
    else:
        ThisPlayer=1

def DisplayGrid():
    for i in range(8):
        for j in range(8):
            if (i,j)==(x,y):
                print(Grid[i][j],end="")
            elif Grid[i][j]==0:
                print(" ",end="")
            else:
                print("?",end="")
        print("")

def InputCoordinates():
    global x,y
    while 1:    
        x=int(input("Please input the x coordinate of the card"))
        y=int(input("Please input the y coordinate of the card"))
        if Grid[x][y]!=0:
            break
    DisplayGrid()
    global x2,y2
    while 1:
        x2=int(input("Please input another x coordinate of the card"))
        y2=int(input("Please input another y coordinate of the card"))
        if Grid[x2][y2]!=0 and x!=x2 and y!=y2:
            break 
        
def TestForMatch():
    if Grid[x][y]==Grid[x2][y2]:
        Grid[x][y]=0
        Grid[x1][y1]=0
        Point[ThisPlayer]+=1
    else:
        SwapPlayer()

def TestForEndGame():
    if sum(Point)==32:
        GameEnd=True

def OutputResult():
    if Point[0]>Point[1]:
        print("Player 1 wins")
    elif Point[0]<Point[1]:
        print("Player 2 wins")
    else:
        print("It's a draw")

SetUpGrid()
SetUpPlayer()
RandomlyDistributeCards()
while 1:
    InputCoordinates()
    DisplayGrid()
    TestForMatch()
    TestForEndGame()
    if GameEnd==True:
        break
OutputResult()


