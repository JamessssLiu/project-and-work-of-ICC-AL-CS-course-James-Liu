
data=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\File processing test\\qbdata.txt","r+")
datalst=[]
character=input("Please input a single character")
while len(data.readline())>0:
    line=data.readline()
    splitlst=[]
    for j in range(len(line)):
        splitlst.append(line[j])
        if splitlst[j]==" ":
            splitlst[j]=character
    newline="".join(splitlst)
    datalst.append(newline)

newdata=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\File processing test\\qbdata.txt","w+")
i=0
while len(data.readline())>0:
    newdata.write(datalst[i])
    i+=1
newdata.close()
