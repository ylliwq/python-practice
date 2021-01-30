import cv2
import numpy as np
import matplotlib.pyplot as plt

image= cv2.imread('IMG_8561.JPG')

cv2.putText(image, text='Arnold', org=(1090,1737),
            fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=10, color=(255,255,255),
            thickness=10, lineType=cv2.LINE_AA)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()