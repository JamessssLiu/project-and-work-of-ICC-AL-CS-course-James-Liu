
import numpy as np
a=np.array([[1,1,1],[24,24,42],[135,153,531]])

def imgflip(array):
    for i in range(len(array)):
        list(array[i]).reverse()
    return array

print(imgflip(a))
