
ClassList=[]
StudentCont=open("StudentContact.txt","r")
ClassCont=open("ClasContact.txt","w")

#Search File
def CreateArray(List,File):
    List=[]
    while len(File.readline())!=0:
        List.append(File.readline())

def SearchFile(Name,File):
    found=False
    while not found:
        text=File.readline()
        for i in range(len(text)):
            if text[i]=="*" and text[:i]==Name:
                found=True
                return text
                break
    if found==False:
        return ""

#Process Array
def ProcessArray():
    for i in range(len(ClassList)):
        StudentName=ClassList[i]
        if StudentName!="":
            Contact=SearchFile(StudentName,StudentCont)
            if Contact!="":
                ClassCont.append(Contact)

CreateArray(ClassList,ClassCont)
ProcessArray()

