import numpy as np
import imutils
import cv2
from matplotlib import pyplot as plt
import re
import argparse

def getC(img):
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cruxCnts = []
    k = []

    a = 0
    for c in cnts:
        M = cv2.moments(c)
        if cv2.contourArea(c) > 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)

            if w >= 0 and h >= 0:# and ar >= 0 and ar <= 11:
                cruxCnts.append(c)
                #break

    cv2.drawContours(img, cruxCnts, -1, (0, 255, 0), 2)
    cv2.imshow('Ok', img)
    cv2.waitKey(0)


def main():
    img = cv2.imread("c.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (1, 1), 0)
    getC(gray)

if __name__ == "__main__":
   main()