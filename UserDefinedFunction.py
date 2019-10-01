# File     : UserDefinedFunction.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 10:28 PM, 9/30/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

import cv2


def display(img, tag):
    cv2.imshow(tag, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


