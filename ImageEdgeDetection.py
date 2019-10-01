# File     : ImageEdgeDetection.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 11:08 AM, 10/1/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

import cv2

img = cv2.imread('res/rubics.jpg', 0)
height, width = img.shape

# Extract slope edges
Sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
Sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('Original Image', img)
cv2.waitKey(0)

cv2.imshow('Sobel_x image', Sobel_x)
cv2.waitKey(0)
cv2.imshow('Sobel_y image', Sobel_y)
cv2.waitKey(0)

Sobel_or = cv2.bitwise_or(Sobel_x, Sobel_y)
cv2.imshow('Sobel or', Sobel_or)
cv2.waitKey(0)

# Laplacian method

laplacian_img = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('Laplacian Image', laplacian_img)
cv2.waitKey(0)

# Canny Edge detection uses gradient values as thersholds
canny = cv2.Canny(img, 20, 170)
cv2.imshow('Canny Image', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

