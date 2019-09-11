#a
Tally=[]
for i in range(5):
    Tally.append("")

#b
while 1:
    choice=int(input("Please input the choice"))
    Tally[choice-1]+=1
    if choice==0:
        break

for i in range(len(Tally)):
    print(Tally[i])

#c
title=["Reading books","Playing computer games","Sport","Programming","Watching TV"]
#revised version of b
for i in range(len(Tally)):
    print(title[i]+":",Tally[i])

#d
file=open("text.txt","w")
for i in range(len(Tally)):
    file.write(Tally[i])
file.close()

#e
NewTally=[]
file=open("text.txt","r")
for i in range(len(Tally)):
    data=file.readline()
    NewTally.append(data)
file.close()
