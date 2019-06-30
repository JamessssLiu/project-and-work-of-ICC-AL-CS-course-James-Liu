#Text Organization
import re
text=input("Please input the text needed for checking")
wd_lst=['a','aback','abacus','abandon','abandoned','abandonment','abashed','abate']
#An example as a vocabulary list
notexpectedwords=[]
punctuation = '!,;:?.()-*&/"\''
def removepunc(t):
    t = re.sub(r'[{}]+'.format(punctuation),'',t)
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
print(notexpectedwords)
