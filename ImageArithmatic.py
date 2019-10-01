# File     : ImageArithmatic.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 4:32 PM, 10/1/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

import cv2
import numpy as np

img = cv2.imread('res/NASAView.jpg')
cv2.imshow('Original Image', img)
cv2.waitKey(0)

Mat = np.ones(img.shape, dtype='uint8')*150

added_img = cv2.add(img, Mat)

cv2.imshow('Added Image', added_img)
cv2.waitKey(0)

subtracted_img = cv2.subtract(img, Mat)
cv2.imshow('Subtracted Image', subtracted_img)
cv2.waitKey(0)

mul_img = cv2.multiply(img, Mat)
cv2.imshow('Multiply Opreation', mul_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

