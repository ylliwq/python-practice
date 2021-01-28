import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
#Import only if not previously imported
# Coordinates must be a tuple - (x,y)
cv2.line(img,(0,0),(512,512),(34,64,34),3)                   #Color is by default black
pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img,[pts],True,(0,0,255),3)
cv2.ellipse(img,(256,256),(100,50),0,0,360,(0,76,99),1)
font=cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)
cv2.imshow("gogo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()