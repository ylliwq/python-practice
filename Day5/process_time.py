import numpy as np
import cv2
img1 = cv2.imread("IMG_8561.JPG")
img2 = cv2.imread("IMG_8591.JPG")
t1 =cv2.getTickCount()
imgc= cv2.addWeighted(img1,0.2,img2,0.8,0)
t2 =cv2.getTickCount()
t=(t2-t1)/cv2.getTickFrequency()
print(t)
cv2.namedWindow("test",cv2.WINDOW_NORMAL)
cv2.imshow("test",imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()