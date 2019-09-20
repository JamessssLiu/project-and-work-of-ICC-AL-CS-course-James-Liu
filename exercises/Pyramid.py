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
