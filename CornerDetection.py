# File     : CornerDetection.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 7:40 PM, 10/1/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

import cv2
import numpy as np

img = cv2.imread('res/rubics.jpg')
img2 = img
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)


# Using Corner Harris method to detect corner
CornerHarris = cv2.cornerHarris(gray_img, 2, 3, 0.04)
CornerHarris = cv2.dilate(CornerHarris, None)
img2[CornerHarris>0.01*CornerHarris.max()] = [0, 0, 255]

# Using Shi-Tomasi Corner Detector & Good Features to Track
GFT_corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10)
GFT_corners = np.int0(GFT_corners)

for corner in GFT_corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corners detection using GFT', img)
cv2.waitKey(0)

cv2.imshow('Corners Harris method', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
