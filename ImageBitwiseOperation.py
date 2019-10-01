# File     : ImageBitwiseOperation.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 7:13 PM, 10/1/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

import cv2
import numpy as np

# Making an square
sqr = np.zeros((300, 300), np.uint8)
cv2.rectangle(sqr, (50, 50), (250, 250), 255, -1)
cv2.imshow('Square Image', sqr)
cv2.waitKey(0)

# Making an ellipse
ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow('Ellipse Image', ellipse)
cv2.waitKey(0)

And_img = cv2.bitwise_and(sqr, ellipse)
cv2.imshow('Bitwise and Image', And_img)
cv2.waitKey(0)

Or_img = cv2.bitwise_or(sqr, ellipse)
cv2.imshow('Bitwise or Image', Or_img)
cv2.waitKey(0)

Not_img = cv2.bitwise_not(sqr)
cv2.imshow('Bitwise not Image', Not_img)
cv2.waitKey(0)

Xor_img = cv2.bitwise_xor(sqr, ellipse)
cv2.imshow('Xor Image', Xor_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
