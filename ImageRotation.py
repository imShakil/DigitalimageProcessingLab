# File     : ImageRotation.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 10:17 PM, 9/30/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh


import cv2

img = cv2.imread('res/arya_stark.jpg')

height, width = img.shape[:2]
center = (height/2, width/2)

# Performing the counter clockwise rotating from holding center point

# 90 degree
Mat = cv2.getRotationMatrix2D(center, angle=90, scale=1.0)
rotated90 = cv2.warpAffine(img, Mat, (height, width))

# 180 degree
Mat = cv2.getRotationMatrix2D(center, angle=180, scale=1.0)
rotated180 = cv2.warpAffine(img, Mat, (height, width))

# 270 degree
Mat = cv2.getRotationMatrix2D(center, angle=270, scale=1.0)
rotated270 = cv2.warpAffine(img, Mat, (height, width))

cv2.imshow('Original Image', img)
cv2.waitKey(0)

cv2.imshow('90 degree rotation', rotated90)
cv2.waitKey(0)
cv2.imshow('180 degree rotation', rotated180)
cv2.waitKey(0)
cv2.imshow('270 degree rotation', rotated270)
cv2.waitKey(0)
cv2.destroyAllWindows()
