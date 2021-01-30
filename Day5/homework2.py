import cv2
import numpy as np
def nothing(x):
     pass

img = cv2.imread('IMG_per.JPG', 0)
cv2.imshow('image1', img)
edges = cv2.Canny(img, 50, 100)
cv2.namedWindow('image')
cv2.createTrackbar('minval', 'image', 0, 255, nothing)
cv2.createTrackbar('maxval', 'image', 0, 255, nothing)
while(1):
     cv2.imshow('image', edges)
     k = cv2.waitKey(500)
     if k == 27:
         break
     minval = cv2.getTrackbarPos('minval', 'image')
     maxval = cv2.getTrackbarPos('maxval', 'image')
     edges = cv2.Canny(img, minval, maxval)
     cv2.putText(img,str(minval), org=(1090,3000),
            fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=10, color=(255,255,255),
            thickness=10, lineType=cv2.LINE_AA)
     
cv2.destroyAllWindows()