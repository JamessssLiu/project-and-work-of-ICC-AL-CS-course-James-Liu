
import numpy as np
a=np.array([[1,1,1],[24,24,24],[135,153,135]])
def imgflip(array):
    for i in range(len(array)):
        array[i].reverse()
    return array

print(imgflip(a))