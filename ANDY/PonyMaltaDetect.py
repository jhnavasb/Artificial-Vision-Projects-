import cv2
import numpy as np
#import matplotlib.pyplot as plt
import imutils
from collections import deque
from imutils.video import VideoStream

bufferSize = 64
pts = deque(maxlen=bufferSize)
vs = VideoStream(src=0).start()

CascadeFile = './classifier/cascade1.xml'
PonyMaltaCascade = cv2.CascadeClassifier(CascadeFile)
while True:
    Img = vs.read()
    Img = cv2.flip( Img, 1 )
    Img = imutils.resize(Img, width = 600)
    ImgGray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
    PonyMaltas = PonyMaltaCascade.detectMultiScale(ImgGray, 1.3, 5)
    for (x,y,w,h) in PonyMaltas:
        cv2.rectangle(Img,(x,y),(x+w,y+h),(255,0,0),2)
        
    cv2.imshow("Frame", Img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.stop()
cv2.destroyAllWindows()
    
