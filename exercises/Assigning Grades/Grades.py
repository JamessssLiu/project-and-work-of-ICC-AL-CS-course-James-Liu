
#Generating random grades
import random
alist=[]
namelst=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\Assigning Grades\\Name List.txt","r")
number=len(namelst.readlines())
gradelst=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\Assigning Grades\\Grade List.txt","w")

def generatelst(emptylist:list,quant:int,average:int):
    for i in range(quant):
        emptylist.append(0)
    count=0
    while count!=quant*average:
        index=random.randint(0,quant-1)
        if emptylist[index]==100:
            continue
        else:
            emptylist[index]+=1
            count+=1
    return emptylist

mathgrade=generatelst(alist,number,90)
csgrade=generatelst(alist,number,95)
phygrade=generatelst(alist,number,88)

gradelst.write("English name","Chinese last name","Math grade","CS grade","Phy grade")
gradelst.write("English name      ")
for i in range(number):
    fullname=namelst.readline()
    for i in fullname:
        if fullname[i]==" ":
            gradelst.write(fullname[:i])
gradelst.write("\n"+"Chinese Last name ")
for i in range(number):
    fullname=namelst.readline()
    for i in fullname:
        if fullname[i]==" ":
            gradelst.write(fullname[(i+1):])
gradelst.write("\n"+"Math grade        ")
for i in range(number):   
    gradelst.write(str(mathgrade[i]))
gradelst.write("\n"+"CS grade          ")
for i in range(number):
    gradelst.write(str(csgrade[i]))
gradelst.write("\n"+"Phy grade         ")
for i in range(number):
    gradelst.write(str(phygrade[i]))
gradelst.close()         

#Adding the ID column
gradelst=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\Assigning Grades\\Grade List.txt","a+")
firstrow=gradelst.readline()
gradelst.write("ID "+firstrow)
for i in range(number):
    row=gradelst.readline()
    gradelst.write("     "+row)
gradelst.close()

#Adding the average score
gradelst=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\Assigning Grades\\Grade List.txt","a+")
for i in range(number):
    row=gradelst.readline()
    averagescore=(int(row[-1,-3])+int(row[-4,-6])+int(row[-7,-9]))/3
    gradelst.write(" "+str(averagescore))

#Modifying score
gradelst=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\exercises\\Assigning Grades\\Grade List.txt","a+")
for i in range(number):
    row=gradelst.readline()
    Newscore=1.1*(int(row[-7,-9]))
    if row[0,5]=="Daniel":
        row.translate(str.maketrans(row[-7,-9],Newscore))

#
