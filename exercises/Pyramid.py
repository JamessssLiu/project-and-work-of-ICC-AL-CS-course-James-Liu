'''
#Solid Pyramid
#DECLARE symbol:STRING
#DECLARE MaxNumberOfSymbols:INTEGER
#DECLARE NumberOfSpaces:INTEGER
#DECLARE NumberOfSymbols:INTEGER
symbol=input("Please input the symbol")
while 1:
    MaxNumberOfSymbols=int(input("Please input the number of symbols in the last row"))
    if MaxNumberOfSymbols%2==1 and MaxNumberOfSymbols>0:
        break
NumberOfSpaces=int((MaxNumberOfSymbols-1)/2)
NumberOfSymbols=1
while 1:
    for i in range(NumberOfSpaces):
        print(" ",end="")
    for i in range(NumberOfSymbols):
        print(symbol,end="")
    print("\n",end="")
    NumberOfSpaces-=1
    NumberOfSymbols+=2
    if NumberOfSymbols>MaxNumberOfSymbols:
        break
'''
'''
#Hollow Pyramid
#DECLARE symbol:STRING
#DECLARE MaxNumberOfSymbols:INTEGER
#DECLARE NumberOfSpaces:INTEGER
#DECLARE NumberOfSymbols:INTEGER
#DECLARE NumberOfSpacesInMiddle:INTEGER
symbol=input("Please input the symbol")
while 1:
    MaxNumberOfSymbols=int(input("Please input the number of symbols in the last row"))
    if MaxNumberOfSymbols%2==1 and MaxNumberOfSymbols>0:
        break
NumberOfSpaces=int((MaxNumberOfSymbols-1)/2)
NumberOfSymbols=1
NumberOfSpacesInMiddle=0
while 1:
    if NumberOfSymbols==1:
        for i in range(NumberOfSpaces):
            print(" ",end="")
        print(symbol,end="")
    elif 1<NumberOfSymbols<MaxNumberOfSymbols:
        for i in range(NumberOfSpaces):
            print(" ",end="")
        print(symbol,end="")
        for i in range(NumberOfSpacesInMiddle-1):
            print(" ",end="")
        print(symbol,end="")
    elif NumberOfSymbols==MaxNumberOfSymbols:
        for i in range(MaxNumberOfSymbols):
            print(symbol,end="")
    print("\n",end="")
    NumberOfSpaces-=1
    NumberOfSymbols+=2
    NumberOfSpacesInMiddle+=2
    if NumberOfSymbols>MaxNumberOfSymbols:
        break
'''
#Revised version
global Space
Space=" "
def InputMaxNumberOfSymbols():
    Number=0
    while Number%2==0:
        print("Please input a valid integer")
        Number=int(input("Input an odd number"))
    return Number

def OutPut(Number,Symbol):
    for i in range(Number):
        print(Symbol,end="")

def GetSymbol():
    Symbol=input("Please input the character")
    return Symbol

def AdjustValues(Spaces,Symbols):
    Spaces-=1
    Symbols+=2
    return Spaces,Symbols

def PrintPyramid():
    Max=InputMaxNumberOfSymbols()
    NumberOfSpaces=(Max+1)/2
    NumberOfSymbols=1
    Symbol=GetSymbol()
    while NumberOfSymbols>=Max:
        OutPut(NumberOfSpaces,Space)
        OutPut(NumberOfSymbols,Symbol)
        NumberOfSpaces,NumberOfSymbols=AdjustValues(NumberOfSpaces,NumberOfSymbols)
        print()

PrintPyramid()
