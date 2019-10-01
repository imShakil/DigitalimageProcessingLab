# File     : ImageBlurringOperation.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 7:29 PM, 10/1/2019
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

# Creating 3x3 kernel
Kernel_3x3 = np.ones((3, 3), np.float32)/9
# We are using cv2.filter2D to convolve the kernel with an image
blurred = cv2.filter2D(img, -1, Kernel_3x3)
cv2.imshow('Kernel_3x3 blurred image', blurred)
cv2.waitKey(0)

# Creating 7x7 kernel
Kernel_7x7 = np.ones((7, 7), np.float32)/49
blurred = cv2.filter2D(img, -1, Kernel_7x7)
cv2.imshow('Kernel_7x7 blurred image', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
