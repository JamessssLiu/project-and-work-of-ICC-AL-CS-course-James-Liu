#Text Organization
import matplotlib.pyplot as plt
import re
text=open('D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\Sequential search\\alice in wonderland.txt')
wd_lst=list(open('D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\Sequential search\\vocab list.txt'))
#An example as a vocabulary list
notexpectedwords=[]
punctuation = '!,;:?.()-*&/"\'-_'
def removepunc(t):
    t = re.sub(r'[{}]+'.format(punctuation),'',t.read())
    return t.strip().lower()
txtsplt=removepunc(text).split()
txtsplt.sort()
check_lst=[txtsplt[0]]

for i in range(len(txtsplt)-1):
    if txtsplt[i+1]!=txtsplt[i]:
        check_lst.append(txtsplt[i+1])

#-------------------------------------------------------------------------------------------
'''
#The inefficient sequential search
for i in range(len(check_lst)):
    found=False
    for j in range(len(wd_lst)):
        if check_lst[i]==wd_lst[j]:
            found=True
            break
        elif check_lst[i]<wd_lst[j]:
            break
    if found==False:
        notexpectedwords.append(check_lst[i])
'''
#-------------------------------------------------------------------------------------------

#A more efficient alternative: binary search
found=False
lower_elmt=0
upper_elmt=len(wd_lst)-1
for i in range(len(check_lst)):
    while not found and lower_elmt<upper_elmt:
        m=int((lower_elmt+upper_elmt)/2)
        if wd_lst[m]==check_lst[i]:
            found=True
        else:
            if wd_lst[m]<check_lst[i]:
                lower_elmt=m
            else:
                upper_elmt=m
    if found==False:
        notexpectedwords.append(check_lst[i])

#------------------------------------------------------------------------------------------

#Output
unfamiliarwords=len(notexpectedwords)
knownwords=len(check_lst)-len(notexpectedwords)

labels = 'known words', 'unfamiliar words'
sizes = [knownwords,unfamiliarwords]
explode = (0,0)  
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()