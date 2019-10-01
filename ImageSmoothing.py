# File     : ImageSmoothing.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 10:51 AM, 10/1/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh


import cv2

img = cv2.imread('res/NASAView.jpg')

cv2.imshow('Original Image', img)
cv2.waitKey(0)

# Using box filter
blur = cv2.blur(img, (3, 3))
cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)

# Instead of box filter using Gaussian Kernel
Gauss_img = cv2.GaussianBlur(img, (7, 7), 0)

cv2.imshow('Gaussian Filter Image', Gauss_img)
cv2.waitKey(0)

# Using Median Blur method
Median_img = cv2.medianBlur(img, 5)
cv2.imshow('Median Image Blur', Median_img)
cv2.waitKey(0)

# Very effective method to remove noise from image
Bilateral_img = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('Bilateral filter image', Bilateral_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
