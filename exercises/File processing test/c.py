
data=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\File processing test\\qbdata.txt","r")
datalst=[]
code=input("Please input the four-digit code")
global found
found=False
while len(data.readline())>0:
    line=data.readline()
    for j in range(len(line)):
        if line[:4]==code:
            display=line
            found=True
if found==True:
    print(display)
else:
    print("The code is unfounded")


