'''
#Q1
def InputTicketType():
    while 1:
        TicketType=input("Please input the ticket type")
        if TicketType=="E" or TicketType=="S":
            break
    return TicketType

def InputBaggageWeight():
    while 1:
        BaggageWeight=int(input("Please input the weight of the baggage (in kg)"))
        if 0<BaggageWeight<50:
            break
    return BaggageWeight

def CalculatePrice(Type,Weight):
    if Type=="E":
        BaggageAllowance=16
        ChargeRate=3.5
    else:
        BaggageAllowance=20
        ChargeRate=5.75
    ExcessWeight=Weight-BaggageAllowance
    if ExcessWeight>0:
        Charge=ExcessWeight*ChargeRate
    else:
        Charge=0
    return "The charge is "+str(Charge)+"$"

print(CalculatePrice(InputTicketType(),InputBaggageWeight()))

#Q2
global PCode
PCode=[]
PDescription=[]
PRetailPrice=[]

def ReadProductFile():
    ProductFile=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\Summative Assignment Paper 19.10.31\\PRODUCTS.txt","r")
    while 1:
        ReadCode=ProductFile.readline()
        if len(ReadCode)==0:
            break
        PCode.append(ReadCode[:-1])
        PDescription.append(ProductFile.readline()[:-1])
        Price=ProductFile.readline()
        PRetailPrice.append(float(Price))
    ProductFile.close()

def SearchByProductCode():
    Code=str(input("Please input the product code"))
    Found=False
    for i in range(len(PCode)):
        if PCode[i]==Code:
            Found=True
            break
    if Found==True:
        return i+1
    else:
        return -1

ReadProductFile()
print(SearchByProductCode())
'''
#Q3
DailyHoursWorked=[5,10,10]
ProductionData=[[10,20,9],[11,16,11],[10,24,13],[14,20,17]]
WorkerTotal=[]
def SetupWorkerHoursList():
    for i in range(3):
        WorkerTotal.append(0)

def CheckWorkingHours():
    for Num in range(3):
        for Day in range(4):
            WorkerTotal[Num]+=ProductionData[Day][Num]
    for Num in range(3):
        WorkerAverage=WorkerTotal[Num]/(4*DailyHoursWorked[Num])
        if WorkerAverage<2:
            print("Investigate",Num+1)

SetupWorkerHoursList()
CheckWorkingHours()
