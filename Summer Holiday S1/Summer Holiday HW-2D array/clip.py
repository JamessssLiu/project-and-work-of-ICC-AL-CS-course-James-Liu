
from PIL import Image
import numpy as n
a=n.array([[1,1,100],[24,24,24],[135,153,231]])
def imgclip(array,n):#n for the maximum value of brightness
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]>n:
                array[i][j]=n
    return array

a=n.repeat(imgclip(a,120),100,axis=1)
a=n.repeat(imgclip(a,120),100,axis=0)

image1=Image.fromarray(n.uint8(imgclip(a,120)))
image1.show()
