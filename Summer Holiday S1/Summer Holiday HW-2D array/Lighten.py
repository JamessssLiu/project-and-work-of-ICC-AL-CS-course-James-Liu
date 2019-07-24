
import numpy as np
a=np.array([[1,1,1],[24,24,24],[135,153,135]])
def imglighten(array,n): #n represents the presentage of brightness rises
    limit=255/n
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j]*=1+0.01*n
            if array[i][j]>limit:
                array[i][j]=255
    return array

print(imglighten(a,10))
