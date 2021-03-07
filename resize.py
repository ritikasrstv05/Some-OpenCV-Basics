import cv2
import numpy as np

img = cv2.imread('aaa.jpg')
print(img.shape)
imgResize = cv2.resize(img,(662,623))

imgCropped = img[0:60,60:75]

cv2.imshow("resized image ",imgResize)
cv2.imshow("cropped image",imgCropped)
cv2.waitKey(0)
