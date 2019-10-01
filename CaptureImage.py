# File     : CaptureImage.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 10:21 AM, 10/1/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh

import cv2
import matplotlib.pyplot as plt

capture = cv2.VideoCapture(0)

if capture.isOpened():
    ret, frame = capture.read()
    print(ret)
    print(frame)
else:
    ret = False

img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title('Camera Image')
plt.xticks([])
plt.yticks([])
plt.show()
capture.release()
