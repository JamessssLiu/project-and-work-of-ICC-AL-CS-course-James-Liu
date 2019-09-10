
from PIL import Image
import numpy as n
a=n.array([[1,1,100],[24,24,42],[135,153,231]])

def imgflip(array):
    for i in range(len(array)):
        list(array[i]).reverse()
    return array

a=n.repeat(imgflip(a),100,axis=1)
a=n.repeat(imgflip(a),100,axis=0)

image1=Image.fromarray(n.uint8(imgflip(a)))
image1.show()