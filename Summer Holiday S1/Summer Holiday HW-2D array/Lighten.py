
import numpy as np
a=np.array([[1,1,1],[24,24,24],[135,153,135]])
burnout=False
def imglighten(array): #n represents the presentage of brightness rises
    limit=255/1.1
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j]*=1.1
            if array[i][j]>limit:
                array[i][j]=255
                burnout=True
    return burnout

print(burnout)