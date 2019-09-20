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

