import re
text=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\word frequency count\\hamlet.txt","r")

def removepunc(t):
    punctuation = '!,;:?.()-*&/"\'-_~%#'
    t = re.sub(r'[{}]+'.format(punctuation),'',t.read())
    return t.strip().lower()

txtsplt=removepunc(text).split()
txtsplt.sort()

words=[txtsplt[0]]
count=[]
for i in range(len(txtsplt)-1):
    if txtsplt[i+1]!=txtsplt[i]:
        words.append(txtsplt[i+1])
        n=1
    else:
        n+=1
    count.append(n)

outputfile=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\word frequency count\\Result of Hamlet word count.txt","w")
for i in range(len(words)):
    outputfile.write(str(words[i])+"  "+str(count[i])+"\n")
