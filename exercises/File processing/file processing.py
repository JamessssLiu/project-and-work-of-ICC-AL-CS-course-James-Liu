qbdata=open("qbdata.txt","r")
ratings=[]
names=[]

while len(qbdata.readline())>0:
    l=qbdata.readline()
    for i in range(len(l)):
        spacecount=0
        if l[i]==" ":
            spacecount+=1
        if spacecount==2:
            names.append(l[:i])
        if spacecount==19:
            ratings.append(l[i:])

newlist=open("above60.txt","w")
for i in ratings:
    if ratings[i]>=60:
        newlist.write(names[i],ratings[i])   

'''
while len(qbdata.readline())>0:
    l=qbdata.readline().split
    ratings.append(l[11])
'''
