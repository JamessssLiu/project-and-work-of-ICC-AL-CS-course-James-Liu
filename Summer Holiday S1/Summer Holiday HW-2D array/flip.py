
from PIL import Image
import numpy as n
a=np.array([[1,1,1],[24,24,42],[135,153,531]])

def imgflip(array):
    for i in range(len(array)):
        list(array[i]).reverse()
    return array

print(imgflip(a))

a=n.repeat(imgclip(a,120),100,axis=1)
a=n.repeat(imgclip(a,120),100,axis=0)

image1=Image.fromarray(n.uint8(imgclip(a,120)))
image1.show()