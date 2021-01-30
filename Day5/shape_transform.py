import cv2 
import numpy as np
img=cv2.imread('test1.jpg',1)
res=cv2.resize(img,None,fx=3,fy=3,interpolation=cv2.INTER_NEAREST_EXACT)
while(1):
    cv2.imshow('res',res)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break 
cv2.destroyAllWindows()