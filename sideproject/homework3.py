import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('IMG_per.JPG')
img1 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(imgray, (7, 7), 0)
edges = cv2.Canny(blurred, 20, 170)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
draw = cv2.drawContours(img1, contours, -1, (0, 255, 0), 5)

plt.subplot(131), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(132), plt.imshow(edges,cmap='gray'), plt.title('Edge Image')
plt.subplot(133), plt.imshow(cv2.cvtColor(draw,cv2.COLOR_BGR2RGB)), plt.title('contour Image')

plt.show()