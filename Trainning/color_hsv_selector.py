

import cv2
import numpy as np
#定义窗口名称
imgName='Image Part'
trackbarName = 'Trackbar Part'

#定义滑动条回调函数，此处pass用作占位语句保持程序结构的完整性
def nothing(x):
    pass
img_original=cv2.imread('E:\\ProgrammingLanguage\\git\\Intelligence-Closet\\Trainning\\real_case_picture\\4_T-Shirt.jpg')
#颜色空间的转换
img_hsv=cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)

# #新建窗口
cv2.namedWindow(imgName, 0)
cv2.namedWindow(trackbarName, 0)


# #新建6个滑动条，表示颜色范围的上下边界，这里滑动条的初始化位置即为黄色的颜色范围
cv2.createTrackbar('LowerbH',trackbarName, 0, 255, nothing)
cv2.createTrackbar('LowerbS',trackbarName, 0, 255, nothing)
cv2.createTrackbar('LowerbV',trackbarName, 0, 255, nothing)
cv2.createTrackbar('UpperbH',trackbarName, 0, 255, nothing)
cv2.createTrackbar('UpperbS',trackbarName, 0, 255, nothing)
cv2.createTrackbar('UpperbV',trackbarName, 0, 255, nothing)

while(1):
    #函数cv2.getTrackbarPos()范围当前滑块对应的值
    lowerbH=cv2.getTrackbarPos('LowerbH', trackbarName)
    lowerbS=cv2.getTrackbarPos('LowerbS', trackbarName)
    lowerbV=cv2.getTrackbarPos('LowerbV', trackbarName)
    upperbH=cv2.getTrackbarPos('UpperbH', trackbarName)
    upperbS=cv2.getTrackbarPos('UpperbS', trackbarName)
    upperbV=cv2.getTrackbarPos('UpperbV', trackbarName)
    #得到目标颜色的二值图像，用作cv2.bitwise_and()的掩模
    img_target=cv2.inRange(img_original,(lowerbH,lowerbS,lowerbV),(upperbH,upperbS,upperbV))
    #输入图像与输入图像在掩模条件下按位与，得到掩模范围内的原图像
    img_specifiedColor=cv2.bitwise_and(img_original,img_original,mask=img_target)
    cv2.imshow(imgName,img_specifiedColor)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows() 