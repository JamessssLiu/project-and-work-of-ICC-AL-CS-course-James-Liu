
import numpy as n
a=n.array([[1,1,100],[24,24,24],[135,153,231]])
def imglighten(array): #n represents the presentage of brightness rises
    limit=255/1.1
    burnout=False
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]>limit:
                array[i][j]=255
                burnout=True
            array[i][j]*=1.1
    return burnout

print(imglighten(a))
