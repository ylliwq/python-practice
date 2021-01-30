from cv2 import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('IMG_per.JPG')
# markpoint = np.float32([0,0],[0,0],[0,0],[0,0])
# i=0
# def savexy(event,x,y,flags,param):
#     global markpoint
#     global i
#     if event==cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,((x,y)),3, (255,0,0),1)
#         markpoint[i]=[x,y]
#         i+=1
# 设置标记点和目标点
markpoint = [[890, 1066], [3153, 1091], [314, 2523], [3975, 2420]]
dstpoint = [[0, 0], [1000, 0], [0, 500], [1000, 500]]

# 强调标记点
for i in markpoint:
    cv2.circle(img, tuple(i), 10, (0, 255, 0), -1)

# 转换点的格式
pts1 = np.float32(markpoint)
pts2 = np.float32(dstpoint)

# 生成透视矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)

# 转换
dst = cv2.warpPerspective(img, M, (1000, 500))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
