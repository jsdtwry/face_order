import cv2
import sys
import os
import numpy as np


#capture = cv2.VideoCapture(0)
#print (capture)
#size = (int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
#        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

#print (capture.isOpened())


imagepath=(sys.argv[1])
image = cv2.imread(imagepath)

face_cascade = cv2.CascadeClassifier(r'third_lib/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#'''
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor = 1.15,
    minNeighbors = 1,
    minSize = (3,3),
#    flags = cv2.CV_HAAR_SCALE_IMAGE
)
#'''
print (faces)


for(x,y,w,h) in faces:
    #x, y, w, h = np.float(x), numpy
    #cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    cv2.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2)
    #print ((x+x+w)/2, (y+y+h)/2, w/2, h)

cv2.imshow("Image Title",image)
cv2.waitKey(0)

#input()

