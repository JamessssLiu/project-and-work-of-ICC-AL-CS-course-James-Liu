import cv2
import numpy as np 
from matplotlib import pyplot as plt
src = cv2.imread("airplane-small.jpg")  ## 源图像A图
dst = cv2.imread("sky.jpg")   ##源图像B图
 
b,g,r = cv2.split(src)
src_show = cv2.merge([r,g,b])
b,g,r = cv2.split(dst)
dst_show = cv2.merge([r,g,b])
#src_mask = cv2.imread("")  mask方法1：直接读图像
#mask方法2： 给出坐标

plt.subplot(1,2,1),plt.imshow(src_show)
plt.subplot(1,2,2),plt.imshow(dst_show)
plt.show()
#src_mask = np.zeros(src.shape, src.dtype)
#poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
#cv2.fillPoly(src_mask, [poly], (255, 255, 255))

src_mask = 255 * np.ones(src.shape, src.dtype)

laplacian=cv2.Laplacian(src,cv2.CV_16S, ksize =3)

# 源图像放在目标图里的位置
center = (300,400)
# 无缝融合
output1 = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
output2 = cv2.seamlessClone(src, dst, src_mask, center, cv2.MIXED_CLONE)
b,g,r = cv2.split(output1)
output1_show = cv2.merge([r,g,b])
b,g,r = cv2.split(output2)
output2_show = cv2.merge([r,g,b])
plt.figure()
plt.subplot(2,2,1),plt.imshow(src_show)
plt.title('src'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(output1_show,cmap = 'gray')
plt.title('normalClone'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(output2_show,cmap = 'gray')
plt.title('mixedClone'), plt.xticks([]), plt.yticks([])

# Save result
cv2.imwrite("clone-plane.jpg", output1);
plt.show()