
DigitDic={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}

def InputBase(prompt):
    while 1:
        n=int(input(prompt))
        if type(n)==type(1) and 1<n<=16:
            break
    return n

def ValidateBase(num,base):
    Valid=True
    for digit in str(num):
        if DigitDic[digit]>=base:
            Valid=False
            break

    return Valid

def ConvertToDenary(num,InBase):
    DenaryValue=0
    for digit in str(num):
        DenaryValue=DenaryValue*InBase+DigitDic[digit]
    return DenaryValue

def ConvertToBase(num,InBase):
    DigitList=[]
    while 1:
        DigitList.append(str(num%InBase))
        num=int(num/InBase)
        if num<InBase:
            DigitList.append(str(num))
            break
    DigitList.reverse()
    NewNum="".join(DigitList)
    return int(NewNum)

def ConvertBetweenBases():
    NumBase=InputBase("Please input the base of the number")
    ConvBase=InputBase("Please input the base you want the number be converted into")
    while 1:
        obj=input("Please input the number you wanted to convert (in the base of {})".format(NumBase))
        if ValidateBase(obj,NumBase)==True:
            break
    return ConvertToBase(ConvertToDenary(obj,NumBase),ConvBase)

print(ConvertBetweenBases())
