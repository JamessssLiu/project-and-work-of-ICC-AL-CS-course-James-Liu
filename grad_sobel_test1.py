#https://www.jianshu.com/p/e94a45038292 

import cv2
from matplotlib import pyplot as plt
## 运行程序报错，检查： 1. 图片格式，是jpg还是png或者是bmp，
## 2. 检查文件路径，是否正确，程序能找到，可以放在与程序同一个文件夹下
## 3. 

#img = cv2.imread("box.png",0)  #第二个参数1表示读入为灰度图像
img = cv2.imread("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\image processing opencv\\airplane.jpg",1)  #第二个参数1表示读入为彩色图像
h,w = img.shape[:2]
x=cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=3)  #第3,4个参数为1,0表示求水平方向梯度
y=cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=3)  #第3,4个参数为0,1表示求竖直方向梯度

absX=cv2.convertScaleAbs(x)   # 在经过处理后，需要用convertScaleAbs()函数将其转回原来的uint8形式，否则将无法显示图像，而只是一副灰色的窗口。
absY=cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX,0.5,absY,0.5,0)  #由于Sobel算子是在两个方向计算的，最后还需要用cv2.addWeighted(...)函数将其组合起来

laplacian=cv2.Laplacian(img,cv2.CV_16S, ksize =3)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])2
plt.subplot(2,2,2),plt.imshow(absX,cmap = 'gray')
plt.title('gradX'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(absY,cmap = 'gray')
plt.title('gradY'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(laplacian,cmap = 'gray')
plt.title('laplacian'), plt.xticks([]), plt.yticks([])

plt.imsave('laplacian.png', laplacian)
plt.imsave('gradY.png', absY)
plt.imsave('gradX.png', absX)

