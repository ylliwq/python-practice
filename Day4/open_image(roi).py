import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("Day4/test.jpg", 1)
px=img[100,100]
print(px)
print(img.shape)
print(img.dtype)
img[100,100]=(0,0,0)
camera=img[100:146,505:541]
img[108:154,690:726]=camera
img1= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img1) 
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis plt.show()
plt.show()
# cv2.imshow("test",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()