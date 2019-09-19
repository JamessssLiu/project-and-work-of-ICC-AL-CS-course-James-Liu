
data=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\File processing test\\qbdata.txt","r")
datalst=[]
name=input("Please input a name")
while len(data.readline())>0:
    line=data.readline()
    for i in range(len(line)):
        if line[i]==" " and line[:i]!=name:
                datalst.append(str(i*1000)+line)

newdata=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\File processing test\\newqbdata.txt","w+")
i=0
while len(data.readline())>0:
    newdata.write(datalst[i])
    i+=1
newdata.close()
