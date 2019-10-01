# File     : ImageCropping.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 10:32 AM, 10/1/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh


import cv2

img = cv2.imread('res/NASAView.jpg')
height, width = img.shape[:2]

# Fixing starting position of image
start_row, start_col = int(height*.25), int(width*.25)

# Fixing ending position of image
end_row, end_col = int(height*.75), int(width*.75)

# Cropping the image
Cropped_img = img[start_row:end_row, start_col:end_col]

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.imshow('Cropped Image', Cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
