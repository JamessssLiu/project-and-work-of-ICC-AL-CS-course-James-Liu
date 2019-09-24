
NameLst=[]
LateTimeLst=[]
swapped=True
while swapped:
    swapped=False
    for i in range(len(LateTimeLst)-1):
        if LateTimeLst[i]>LateTimeLst[i+1]:
            temp1=LateTimeLst[i]
            LateTimeLst[i]=LateTimeLst[i+1]
            LateTimeLst[i+1]=temp1
            temp2=NameLst[i]
            NameLst[i]=NameLst[i+1]
            NameLst[i+1]=temp2
            swapped=True

for i in range(len(NameLst)):
    print(NameLst[i],str(LateTimeLst[i]),"times")