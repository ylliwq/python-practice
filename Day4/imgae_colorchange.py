import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("Day4/test.jpg", 1)
b =cv2.imread("Day4/test.jpg", 1)
b[:,:,1]=0
b[:,:,2]=0
img1= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(b) 
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis plt.show()
plt.show()
# cv2.imshow("test",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()