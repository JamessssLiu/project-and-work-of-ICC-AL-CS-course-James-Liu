#
'''
def binsearch(testlist,element):
    found=False
    upper=0
    lower=len(testlist)-1
    while upper<lower and not found:
        m=int((lower+upper)/2)
        if testlist[m]==element:
            found=True
        else:
            if testlist[m]<element:
                lower=m+1
            else:
                upper=m-1
    return found

#
'''
def binsearch2(testlist,element):
    testlist.sort()
    m=len(testlist)//2
    if len(testlist)==0:
        return False
    else:
        if testlist[m]==element:
            return True
        else:
            if testlist[m]>element:
                return binsearch2(testlist[:m],element)
            else:
                return binsearch2(testlist[m:],element)

#