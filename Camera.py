# File     : Camera.py
# Project  : DigitalimageProcessingLab
# Product  : PyCharm
# Created  : 11:19 PM, 9/30/2019
# Author   : Mobarak Hosen Shakil
# E-mail   : mh.ice.iu@gmail.com
# Blog     : http://codefighter.cf
# Information & Communication Technology
# Islamic University, Kushtia, Bangladesh


import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()

    if ret:
        cv2.imshow('Captured', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

capture.release()
cv2.destroyAllWindows()
