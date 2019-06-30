#

def seqsearch(testlist,element):
    num=0
    found = False
    while num<len(testlist) and not found:
        if testlist[num]==element:
            found=True
        else:
            num+=1
    return found

#
    
def seqsearch2(testlist,element):
    num=0
    found=False
    for i in testlist:
        if testlist[num]==element:
            found=True
            break
        else:
            num+=1
    return found

#
    
def seqsearchadv(testlist,element):
    num=0
    found=False
    stop=False
    testlist.sort()
    while num<len(testlist) and not found and not stop:
        if testlist[num]==element:
            found=True
        else:
            if testlist[num]>element:
                stop=True
            else:
                num+=1
    return found
            