# File     : ImagePyramid.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 11:05 PM, 9/30/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh


import cv2

img = cv2.imread('res/NASAView.jpg')
choto = cv2.pyrDown(img)
boro = cv2.pyrUp(img)

cv2.imshow('Original', img)
cv2.imshow('Smaller', choto)
cv2.imshow('Bigger', boro)
cv2.waitKey(0)
cv2.destroyAllWindows()
