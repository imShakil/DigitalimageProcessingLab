# File     : ImageResizing.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 10:19 PM, 9/30/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

import cv2
from UserDefinedFunction import display

img = cv2.imread('res/NASAView.jpg')

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resizing the size of the image to 3/4 of it's original size

img_scaled = cv2.resize(img, None, fx=.75, fy=.75)

cv2.imshow('3/4 Size image', img_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resizing the size of the image to double of its original size

img_double = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Doubled Image', img_double)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resizing the size of the image by setting exact dimension

img_custom = cv2.resize(img, (320, 320), interpolation=cv2.INTER_AREA)
width, height = img_custom.shape[:2]

cv2.imshow('Custom dimension Image', img_custom)
cv2.waitKey(0)
cv2.destroyAllWindows()