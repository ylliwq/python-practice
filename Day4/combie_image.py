import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread("IMG_8561.JPG")
img2 = cv2.imread("IMG_8591.JPG")
imgc= cv2.addWeighted(img1,0.2,img2,0.8,0)
imgd= cv2.cvtColor(imgc,cv2.COLOR_BGR2RGB)
plt.imshow(imgd) 
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis plt.show()
plt.show()
# cv2.imshow("test",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()