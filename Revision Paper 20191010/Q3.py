
import random
def GenerateArray():
    Array=[]
    for i in range(100):
        rancond=random.randint(1,100)
        if rancond>=30:
            Array.append(random.uniform(1,1000))
        else:
            Array.append(0)
    return Array

Result=GenerateArray()
def SearchArray(Array):
    TotalValue=0
    ZeroCount=0
    for i in range(len(Array)):
        TotalValue+=Array[i]
        if Array[i]==0:
            ZeroCount+=1
    Average=TotalValue/100
    print("The average value is",Average,"\n"+"The number of zeros are",ZeroCount)

SearchArray(Result)