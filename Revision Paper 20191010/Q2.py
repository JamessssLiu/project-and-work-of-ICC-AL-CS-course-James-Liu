
import random
LowTemp=25
HighTemp=75

def GetTemp():
    Temp=random.uniform(1,100)
    return Temp

def Alarm():
    print("*ALARM*")

def CheckSensor():
    while 1:
        SensorID=eval(input("Please input the sensor ID"))
        if 1<=SensorID<=10 and isinstance(SensorID,int):
            break
    Temp=GetTemp()
    if Temp<LowTemp:
        print("Cold")
    elif LowTemp<=Temp<=HighTemp:
        print("Normal")
    else:
        Alarm()

CheckSensor()