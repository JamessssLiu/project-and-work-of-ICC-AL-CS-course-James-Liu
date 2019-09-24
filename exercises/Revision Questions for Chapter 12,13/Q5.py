
data=open("HealthCare.txt","w+")
data.write("Name          Height   Weight   Vital capacity")
while 1:
    Name=input("Please enter the patient's name")
    Height=input("Please enter the patient's height")
    Weight=input("Please enter the patient's weight")
    VitalCapacity=input("Please enter the patient's vital capacity")
    data.write(Name.ljust(14)+Height.ljust(9)+Weight.ljust(9)+VitalCapacity.ljust(14))
    if VitalCapacity[-1]=="!":
        break