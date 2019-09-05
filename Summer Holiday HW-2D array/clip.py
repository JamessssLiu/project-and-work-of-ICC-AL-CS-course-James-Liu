
import numpy as np
a=np.array([[1,1,1],[24,24,24],[135,153,135]])
def imgclip(array,n):#n for the maximum value of brightness
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]>n:
                array[i][j]=n
    return array

print(imgclip(a,100))